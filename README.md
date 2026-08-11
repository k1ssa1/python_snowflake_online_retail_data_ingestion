# Online Retail Data Ingestion

Python application to extract the **Online Retail** dataset from a xlsx file and load it into **Snowflake**.

---

## Project Objective

The objective of this project is to use a transactional dataset to design a data warehouse for **educational purposes**.

This Python application is responsible only for:

* Extracting data from the downloaded `.xlsx` file
* Connecting to Snowflake
* Loading the extracted data into Snowflake

**Data transformation is not performed by this application.**

The transformation layer is handled by dbt, where the data will be transformed into a **star schema**.

Full details about the warehouse design and transformation process will be available in an upcoming article and in the related dbt repository.

---

## Dataset

### Online Retail

The dataset contains transactional data from a UK-based and registered non-store online retailer. The company mainly sells unique all-occasion gifts, and many of its customers are wholesalers.

The dataset contains transactions occurring between:

`01/12/2010` and `09/12/2011`

### Source

UCI Machine Learning Repository:

https://archive.ics.uci.edu/dataset/352/online+retail

### Data Attribution

#### Creator

Daqing Chen

School of Engineering
London South Bank University

#### DOI

`10.24432/C5BW33`

#### License

The dataset is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license:

https://creativecommons.org/licenses/by/4.0/legalcode

---

## Project Structure

```text
online_retail_ingestion/
│
├── data/
│   └── online_retail.xlsx
│
├── workflow/
│   ├── __init__.py
│   ├── extract.py
│   └── load.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Requirements

* Python 3.x
* Snowflake account
* Downloaded Online Retail `.xlsx` dataset

### Python Dependencies

```text
snowflake-connector-python
ruff
openpyxl
```

---

## Installation

Clone the repository and navigate to the project directory.

Create a Python virtual environment:

```bash
python -m venv .venv
```

### Windows

Activate the virtual environment using PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Or using Command Prompt:

```cmd
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Dataset Setup

Download the **Online Retail** dataset from the UCI Machine Learning Repository:

https://archive.ics.uci.edu/dataset/352/online+retail

Place the downloaded Excel file in the `data` directory.

The expected path is:

```text
data/online_retail.xlsx
```

---

## Running the Application

Activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

Run the application from the project root:

```bash
python main.py
```

The application will extract the data from the Excel file and load it into the configured Snowflake environment.