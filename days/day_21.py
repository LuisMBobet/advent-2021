from utils.file_service import read_file_from_resources
from typing import List


def part_1(data_set: List[str]) -> int:
    player_positions = [int(line.split(":")[1]) for line in data_set]
    player_scores = [0, 0]
    die = 1
    index = 1
    while 1000 not in player_scores:
        index = (index + 1) % 2
        score = get_next_position(
            player_positions[index], die)
        player_scores[index] += score
        player_positions[index] = score
        die += 3
    player_scores.remove(1000)
    return player_scores[0] * (die - 1)


def get_next_position(initial_position: int, first_roll: int) -> int:
    relative_position = initial_position + (first_roll * 3) + 3
    mod_position = relative_position % 10
    if(mod_position == 0):
        return 10
    else:
        return mod_position


def get_input_data(file_name: str) -> List[str]:
    return list(map(str,
                    read_file_from_resources(file_name).split("\n")[0: -1]))
