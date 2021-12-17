from utils.file_service import read_file_from_resources
from typing import List, Union


def part_1(data_set: List[str]) -> int:
    drawn_numbers = data_set[0].split(",")
    boards = [[]]
    winning_board = 0
    index = 0
    last_number = 0
    for line in data_set[2::]:
        if line != '':
            board_line = [number for number in line.split(" ") if number]
            boards[index].append(board_line)
        else:
            boards.append([])
            index += 1
    for number in drawn_numbers:
        winning_board = score_boards(boards, number)
        if winning_board:
            last_number = number
            break
    return calculate_score(winning_board, last_number)


def calculate_score(board: List[List[str]], last_number: str) -> int:
    sum_of_unused_numbers = 0
    for line in board:
        sum_of_unused_numbers += sum([int(number)
                                     for number in line if number != "x"])

    return int(last_number) * sum_of_unused_numbers


def score_boards(boards: List[List[List[str]]], number: int) -> Union[List[List[str]], None]:
    for board in boards:
        mark_board(board, number)
        if has_board_won(board):
            return board


def mark_board(board: List[List[str]], number: int) -> None:
    for line in board:
        if number in line:
            line[line.index(number)] = "x"


def has_board_won(board: List[List[str]]) -> bool:
    column_count = [0, 0, 0, 0, 0]
    row_count = 0
    for line in board:
        row_count = 0
        for position in range(0, 5):
            if line[position] == "x":
                row_count += 1
                column_count[position] += 1
        if row_count == 5 or column_count == 5:
            return True

    return False


def get_input_data(file_name: str) -> List[str]:
    return list(map(str,
                    read_file_from_resources(file_name).split("\n")[0:-1]))
