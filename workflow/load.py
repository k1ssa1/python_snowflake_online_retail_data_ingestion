import os
from dotenv import load_dotenv

import snowflake.connector

from workflow.extract import extract_data

load_dotenv()

snowflake.connector.paramstyle = "qmark"


def load_data():
    rows = list(extract_data())

    with snowflake.connector.connect(
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        account=os.getenv("ACCOUNT"),
        warehouse=os.getenv("WAREHOUSE"),
        database=os.getenv("DATABASE"),
        schema=os.getenv("SCHEMA"),
    ) as con:
        with con.cursor() as cursor:
            cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS invoices_raw_data(
                    InvoiceNo VARCHAR,
                    StockCode VARCHAR,
                    Description VARCHAR,
                    Quantity INTEGER,
                    InvoiceDate TIMESTAMP_NTZ,
                    UnitPrice NUMBER(10,2),
                    CustomerID VARCHAR,
                    COUNTRY VARCHAR
                    )
                """
            )

            batch_size = 10000

            for i in range(0, len(rows), batch_size):
                batch = rows[i : i + batch_size]

                cursor.executemany(
                    """
                    INSERT INTO invoices_raw_data (
                        InvoiceNo,
                        StockCode,
                        Description,
                        Quantity,
                        InvoiceDate,
                        UnitPrice,
                        CustomerID,
                        Country
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                    batch,
                )
