PERCENTILES = '\nPercentiles:'


def print_table(data):
    fields_max_len = {key: len(key) for key in data[0].keys()}
    for row in data:
        for key in row:
            linelen = len(row[key])
            if linelen > fields_max_len[key]:
                fields_max_len[key] = linelen

    max_row_len = sum(fields_max_len.values()) + 30
    print('_' * max_row_len)

    print('| ', end='')
    for key in fields_max_len:
        linelen = len(key)
        spaces_num = fields_max_len[key] - linelen
        print(' ' * ((spaces_num + 1) // 2), key, ' ' * (spaces_num - ((spaces_num + 1) // 2)), '|', end='')
    print()

    for row in data:
        print('| ', end='')
        for key in row:
            linelen = len(row[key])
            spaces_num = fields_max_len[key] - linelen
            print(' ' * ((spaces_num + 1) // 2), row[key], ' ' * (spaces_num - ((spaces_num + 1) // 2)), '|', end='')
        print()
    print('_' * max_row_len)


def print_perc(data):
    print(PERCENTILES)
    max_len_of_data = 0
    for row in data:
        row_len = len(str(row))
        if row_len > max_len_of_data:
            max_len_of_data = row_len

    for row in sorted(data):
        print(' '*(max_len_of_data - len(str(row))), row, ' ', int(data[row]), '%', sep='')


def output_data(data):
    print_table(data[0])

    print(f'\nMaximum: {data[1]}')
    print(f'Minimum: {data[2]}')
    print(f'Mediana: {data[3]}')
    print(f'Average: {data[4]}')

    print_perc(data[5])


def show_regions(regions):
    for num in regions:
        print(f'{num}. {regions[num]}')


def show_columns(columns):
    for i in range(1, len(columns) + 1):
        print(f'{i}. {columns[i]}')
