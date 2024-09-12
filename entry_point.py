from input import input_filename, get_data, choose_region, choose_column
from logic import process_data
from output import output_data

END_OF_PROGRAM = "Closed."


def entry_point():
    try:
        filename = input_filename()

        data, flag = get_data(filename)

        region = choose_region(data, flag)

        column = choose_column(data)

        calculation_data = process_data(data, region, column)

        output_data(calculation_data)

    except KeyboardInterrupt:
        print(END_OF_PROGRAM)