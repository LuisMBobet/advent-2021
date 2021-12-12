import days.day_2 as day_2


def test_day_2_part_1_example():
    test_data = day_2.get_input_data("day_2_example.txt")
    assert day_2.part_1(test_data) == 150


def test_day_2_part_1():
    test_data = day_2.get_input_data("day_2.txt")
    assert day_2.part_1(test_data) == 2039912


def test_day_2_part_2_example():
    test_data = day_2.get_input_data("day_2_example.txt")
    assert day_2.part_2(test_data) == 900


def test_day_2_part_2():
    test_data = day_2.get_input_data("day_2.txt")
    assert day_2.part_2(test_data) == 1942068080
