from utils.file_service import read_file_from_resources
from typing import List


def part_1(data_set: str) -> int:
    horizontal_position = 0
    vertical_position = 0
    for instruction in data_set:
        direction, speed = split_instruction(instruction)
        speed = int(speed)
        if (direction == "forward"):
            horizontal_position += speed
        elif (direction == "down"):
            vertical_position += speed
        elif (direction == "up"):
            vertical_position -= speed
        else:
            raise LookupError("Unexpected direction")
    return horizontal_position * vertical_position


def part_2(data_set: str):
    horizontal_position = 0
    vertical_position = 0
    aim = 0
    for instruction in data_set:
        direction, speed = split_instruction(instruction)
        speed = int(speed)
        if (direction == "forward"):
            horizontal_position += speed
            vertical_position += aim * speed
        elif (direction == "down"):
            aim += speed
        elif (direction == "up"):
            aim -= speed
        else:
            raise LookupError("Unexpected direction")
    return horizontal_position * vertical_position


def split_instruction(instruction: str) -> List[str]:
    return instruction.split(" ")


def get_input_data(file_name: str) -> str:
    return list(map(str,
                    read_file_from_resources(file_name).split("\n")[0:-1]))
