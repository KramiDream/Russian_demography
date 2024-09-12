HEADERS = ("year", "region", "npg", "birth_rate", "death_rate", "gdw", "urbanization")
REGION = 'region'
YEAR = 'year'
NPG = 'npg'
BIRTH_RATE = 'birth_rate'
DEATH_RATE = 'death_rate'
GDW = 'gdw'
URBANIZATION = 'urbanization'


def filter_region(data, region):
    result = list()
    for row in data:
        if row[REGION] == region:
            result.append(row)

    return result


def get_data_by_column(data, column):
    result = list()
    for row in data:
        result.append(row[column])

    return list(map(float, result))


def get_mediana(nums):
    length = len(nums)
    s_nums = sorted(nums)
    if length % 2 == 0:
        result = (s_nums[(length - 1) // 2] + s_nums[(length - 1) // 2 + 1]) / 2
    else:
        a = (length - 1) // 2
        result = s_nums[a]

    return result


def round_percs(percent):
    if round(percent % 5 / 10) == 0:
        percent = percent // 5 * 5
    else:
        percent = percent // 5 * 5 + 5

    return int(percent)


def get_percs(nums):
    percs = {}
    for num in nums:
        f_nums = list(filter(lambda x: x <= num, nums))
        percent = (len(f_nums) / len(nums)) * 100
        percs[num] = round_percs(percent)

    return percs


def process_data(data, region, column):
    output_data = filter_region(data, region)
    nums = get_data_by_column(output_data, column)
    minimum = min(nums)
    maximum = max(nums)
    mediana = get_mediana(nums)
    average = sum(nums) / len(nums)
    percs = get_percs(nums)

    return output_data, maximum, minimum, mediana, average, percs


def get_regions(data):
    regions = set()
    for row in data:
        regions.add(row[REGION])

    reg_dict = {}
    i = 1
    for region in sorted(regions):
        reg_dict[i] = region
        i += 1

    return reg_dict


def get_columns(data):
    columns = list(filter(lambda x: x != REGION, data[0].keys()))
    columns = {col: columns[col - 1] for col in range(1, len(columns) + 1)}

    return columns


def check_headers(headers):
    flag = True
    if len(headers) != len(HEADERS):
        flag = False
    if flag:
        for header in headers:
            if header not in HEADERS:
                flag = False

    return flag


def check_row(row):
    flag = True
    for key in row.keys():
        if row[key].isspace():
            flag = False

    if not (row[YEAR].replace(' ', '').isnumeric()
            and str.replace(row[NPG], '.', '').replace('-', '').replace(' ', '').isnumeric()
            and str.replace(row[BIRTH_RATE], '.', '').replace('-', '').replace(' ', '').isnumeric()
            and str.replace(row[DEATH_RATE], '.', '').replace('-', '').replace(' ', '').isnumeric()
            and str.replace(row[GDW], '.', '').replace('-', '').replace(' ', '').isnumeric()
            and str.replace(row[URBANIZATION], '.', '').replace('-', '').replace(' ', '').isnumeric()):

        flag = False

    elif not str.replace(row[REGION], '-', '').replace(' ', '').isalpha():
        flag = False

    return flag
