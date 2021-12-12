from utils.file_service import read_file_from_resources


def part_1(data_set: str):
    last_number = data_set[0]
    increased_number_count = 0
    for number in data_set[1::]:
        if number > last_number:
            increased_number_count += 1
        last_number = number
    return increased_number_count


def part_2(data_set: str):
    last_sum = sum(data_set[0:3])
    increased_sum_count = 0
    for index in range(2, len(data_set)):
        sum_of_numbers = sum(data_set[index-3:index])
        if sum_of_numbers > last_sum:
            increased_sum_count += 1
        last_sum = sum_of_numbers
    return increased_sum_count


def get_input_data(file_name: str) -> str:
    return list(map(int,
                    read_file_from_resources(file_name).split("\n")[0:-1]))
