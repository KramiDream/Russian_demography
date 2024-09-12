from file_work import load_data
from logic import get_regions, get_columns
from output import show_regions, show_columns

HELLO_INPUT_FILENAME_OUTPUT_STRING = "Please, enter filepath of the file you want to open.\n"
HELLO_INPUT_REGION_OUTPUT_STRING = "\nPlease, enter the number of the region.\n"
HELLO_INPUT_COLUMN_OUTPUT_STRING = "\nPlease, enter number of column.\n"
EMPTY_FIELDS_WARNING = "\nWARNING: some rows were removed because of invalid fields."
UNKNOWN_REGION_ERROR = 'Unknown region, please enter number of the region from the list above.'
UNKNOWN_REGION_NUMBER_FORM_ERROR = "Region number must be integer."
UNKNOWN_COLUMN_ERROR = 'Invalid number of column, please try again.'
UNKNOWN_COLUMN_NUMBER_FORM_ERROR = "Column number must be integer."


def input_filename():
    return input(HELLO_INPUT_FILENAME_OUTPUT_STRING)


def input_region():
    return int(input(HELLO_INPUT_REGION_OUTPUT_STRING))


def input_column():
    return int(input(HELLO_INPUT_COLUMN_OUTPUT_STRING))


def choose_region(data, flag):
    regions = get_regions(data)
    show_regions(regions)

    if flag:
        print(EMPTY_FIELDS_WARNING)

    flag = True
    region = None
    while flag:
        try:
            region = input_region()
            while region not in regions.keys():
                print(UNKNOWN_REGION_ERROR)
                region = input_region()
            flag = False
        except ValueError:
            print(UNKNOWN_REGION_NUMBER_FORM_ERROR)
    print(f'\nChosen region: {regions[region]}')

    return regions[region]


def choose_column(data):
    columns = get_columns(data)
    show_columns(columns)
    flag = True
    column = None
    while flag:
        try:
            column = input_column()
            while column not in columns.keys():
                print(UNKNOWN_COLUMN_ERROR)
                column = input_column()
            flag = False
        except ValueError:
            print(UNKNOWN_COLUMN_NUMBER_FORM_ERROR)
    print(f'Chosen column: {columns[column]}\n')

    return columns[column]


def get_data(filename):
    data, flag = load_data(filename)
    while data is None:
        filename = input_filename()
        data, flag = load_data(filename)

    return data, flag
