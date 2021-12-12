from utils.file_service import read_file_from_resources
from typing import List


def part_1(data_set: List[str]) -> int:
    gamma = 0
    epsilon = 0
    size_of_binary_number = len(data_set[0])
    most_common_bits = [0] * size_of_binary_number
    for number in data_set:
        bits = list(number)
        for index in range(0, len(most_common_bits)):
            bit = int(bits[index])
            if bit == 1:
                most_common_bits[index] += bit
            else:
                most_common_bits[index] -= 1
    most_common_bits = ["0" if bit <= 0 else "1" for bit in most_common_bits]
    gamma = int(''.join(most_common_bits), 2)
    epsilon = (2**size_of_binary_number) - 1 - gamma
    return gamma * epsilon


def part_2(data_set: List[str]):
    oxygen_rating = 0
    oxygen_rating_dataset = data_set.copy()
    co2_rating = 0
    co2_rating_dataset = data_set
    size_of_binary_number = len(data_set[0])
    for position in range(0, size_of_binary_number):
        most_common_bit = get_most_common_bit_in_position(
            oxygen_rating_dataset, position)
        oxygen_rating_dataset = [binary_number
                                 for binary_number in oxygen_rating_dataset
                                 if binary_number[position] == most_common_bit]
        if (len(oxygen_rating_dataset) == 1):
            break
    oxygen_rating = int(oxygen_rating_dataset[0], 2)

    for position in range(0, size_of_binary_number):
        most_common_bit = get_most_common_bit_in_position(
            co2_rating_dataset, position)
        co2_rating_dataset = [binary_number
                              for binary_number in co2_rating_dataset
                              if binary_number[position] != most_common_bit]
        if (len(co2_rating_dataset) == 1):
            break
    co2_rating = int(co2_rating_dataset[0], 2)

    return oxygen_rating * co2_rating


def get_most_common_bit_in_position(data_set: List[str],
                                    position: int) -> str:
    bias = "1"
    most_common_bit = 0
    for number in data_set:
        bits = list(number)
        bit = int(bits[position])
        if bit == 1:
            most_common_bit += bit
        else:
            most_common_bit -= 1

    if most_common_bit < 0:
        return "0"
    elif most_common_bit == 0:
        return bias
    else:
        return "1"


def get_input_data(file_name: str) -> List[str]:
    return list(map(str,
                    read_file_from_resources(file_name).split("\n")[0:-1]))
