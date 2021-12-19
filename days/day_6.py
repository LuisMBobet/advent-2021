from utils.file_service import read_file_from_resources
from typing import List
import numpy


def part_1(data_set: List[str]) -> int:
    shoal = numpy.array([int(fish) for fish in data_set[0].split(",")])
    for day in range(0, 80):
        shoal = increment_day(shoal)
    return len(shoal)


def part_2(data_set: List[str]) -> int:
    shoal = [int(fish) for fish in data_set[0].split(",")]
    fish_count = [0] * 9
    for cycle in range(0, 9):
        fish_count[cycle] = shoal.count(cycle)
    for day in range(0, 256):
        fish_at_end_of_cycle = fish_count[0]
        fish_count = fish_count[1::]
        fish_count[6] += fish_at_end_of_cycle
        fish_count.append(fish_at_end_of_cycle)

    return sum(fish_count)


def increment_day(shoal) -> List[int]:
    shoal -= 1
    number_of_fish_to_add = len(shoal[shoal == -1])
    shoal[shoal == -1] += 7
    shoal = numpy.append(shoal, [8] * number_of_fish_to_add)
    return shoal


def get_input_data(file_name: str) -> List[str]:
    return list(map(str,
                    read_file_from_resources(file_name).split("\n")[0:-1]))
