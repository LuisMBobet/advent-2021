from utils.file_service import read_file_from_resources
from typing import List
import numpy


def part_1(data_set: List[str]) -> int:
    entries = [[[int(number) for number in vector.split(",")]
                for vector in line.split(" -> ")] for line in data_set]

    field = numpy.zeros((1000, 1000))

    for positions in entries:
        x_direction = get_direction(positions[1][0] - positions[0][0])
        y_direction = get_direction(positions[1][1] - positions[0][1])
        if (x_direction and y_direction):
            continue
        current_position = positions[0]
        final_position = positions[1]
        while current_position != final_position:
            field[current_position[1]][current_position[0]] += 1
            current_position[0] += x_direction
            current_position[1] += y_direction
        field[current_position[1]][current_position[0]] += 1
    return len(field[field > 1])


def part_2(data_set: List[str]) -> int:
    entries = [[[int(number) for number in vector.split(",")]
                for vector in line.split(" -> ")] for line in data_set]

    field = numpy.zeros((1000, 1000))

    for positions in entries:
        x_direction = get_direction(positions[1][0] - positions[0][0])
        y_direction = get_direction(positions[1][1] - positions[0][1])
        current_position = positions[0]
        final_position = positions[1]
        while current_position != final_position:
            field[current_position[1]][current_position[0]] += 1
            current_position[0] += x_direction
            current_position[1] += y_direction
        field[current_position[1]][current_position[0]] += 1
    return len(field[field > 1])


def get_direction(position_difference: int):
    if position_difference > 0:
        return 1
    if position_difference < 0:
        return -1
    return 0


def get_input_data(file_name: str) -> List[str]:
    return list(map(str,
                    read_file_from_resources(file_name).split("\n")[0:-1]))
