from utils.file_service import read_file_from_resources
from typing import List


def part_1(data_set: List[str]) -> int:
    lines = [line.split(" | ") for line in data_set]
    occurences = 0
    desired_unique_character_lengths = [2, 3, 4, 7]
    for line in lines:
        occurences += len([value for value in line[1].split(" ")
                          if len(value) in desired_unique_character_lengths])
    return occurences

def get_input_data(file_name: str) -> List[str]:
    return list(map(str,
                    read_file_from_resources(file_name).split("\n")[0: -1]))
