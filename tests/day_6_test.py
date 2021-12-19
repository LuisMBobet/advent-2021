import days.day_6 as day_6


def test_day_6_part_1_example():
    test_data = day_6.get_input_data("day_6_example.txt")
    assert day_6.part_1(test_data) == 5934


def test_day_6_part_1():
    test_data = day_6.get_input_data("day_6.txt")
    assert day_6.part_1(test_data) == 387413


def test_day_6_part_2_example():
    test_data = day_6.get_input_data("day_6_example.txt")
    assert day_6.part_2(test_data) == 26984457539


def test_day_6_part_2():
    test_data = day_6.get_input_data("day_6.txt")
    assert day_6.part_2(test_data) == 1738377086345
