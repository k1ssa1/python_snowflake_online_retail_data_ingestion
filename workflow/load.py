from workflow.extract import extract_data


def load_data():
    rows = extract_data()

    for row in rows:
        print(row)