import csv
from os import SEEK_END

from logic import check_headers, check_row

FILE_NOT_FOUND_ERROR = "No such file in chosen directory."
INVALID_HEADERS_ERROR = "Invalid headers in CSV file."
NO_DATA_ERROR = "File has no rows."


def load_data(filename):
    rows = None
    flag = False
    try:
        with open(filename, 'r', newline='') as file:
            data = csv.DictReader(file)

            if not ((data.fieldnames is not None) and check_headers(data.fieldnames)):
                raise ValueError

            rows = list()

            for row in data:
                if check_row(row):
                    rows.append(row)
                else:
                    flag = True

            if len(rows) == 0:
                rows = None
                raise EOFError
    except FileNotFoundError:
        print(FILE_NOT_FOUND_ERROR)
    except ValueError:
        print(INVALID_HEADERS_ERROR)
    except EOFError:
        print(NO_DATA_ERROR)

    return rows, flag
