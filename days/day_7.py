from utils.file_service import read_file_from_resources
from typing import List
from math import floor, ceil
import numpy


def part_1(data_set: List[str]) -> int:
    positions = [int(position) for position in data_set[0].split(",")]
    positions.sort()
    baseline = positions[floor(len(positions)/2) - 1]
    return get_fuel_cost_for_position_part_1(positions, baseline)


def part_2(data_set: List[str]) -> int:
    positions = [int(position) for position in data_set[0].split(",")]
    baseline = ceil(sum(positions)/len(positions))
    return min(get_fuel_cost_for_position_part_2(positions, baseline), get_fuel_cost_for_position_part_2(positions, baseline-1))


def get_fuel_cost_for_position_part_1(positions: List[int], desired_position: int):
    numpy_positions = numpy.array(positions)
    numpy_positions -= desired_position
    return numpy.sum(numpy.absolute(numpy_positions))


def get_fuel_cost_for_position_part_2(positions: List[int], desired_position: int):
    numpy_positions = numpy.array(positions)
    numpy_positions -= desired_position
    numpy_positions = numpy.absolute(numpy_positions)
    fuel_cost = sum([sum(range(position+1)) for position in numpy_positions])
    return fuel_cost


def get_input_data(file_name: str) -> List[str]:
    return list(map(str,
                    read_file_from_resources(file_name).split("\n")[0: -1]))
