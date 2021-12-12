import days.day_3 as day_3


def test_day_3_part_1_example():
    test_data = day_3.get_input_data("day_3_example.txt")
    assert day_3.part_1(test_data) == 198


def test_day_3_part_1():
    test_data = day_3.get_input_data("day_3.txt")
    assert day_3.part_1(test_data) == 1025636


def test_day_3_part_2_example():
    test_data = day_3.get_input_data("day_3_example.txt")
    assert day_3.part_2(test_data) == 230


def test_day_3_part_2():
    test_data = day_3.get_input_data("day_3.txt")
    assert day_3.part_2(test_data) == 793873
