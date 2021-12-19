import days.day_5 as day_5


def test_day_5_part_1_example():
    test_data = day_5.get_input_data("day_5_example.txt")
    assert day_5.part_1(test_data) == 5


def test_day_5_part_1():
    test_data = day_5.get_input_data("day_5.txt")
    assert day_5.part_1(test_data) == 5167


def test_day_5_part_2_example():
    test_data = day_5.get_input_data("day_5_example.txt")
    assert day_5.part_2(test_data) == 12


def test_day_5_part_2():
    test_data = day_5.get_input_data("day_5.txt")
    assert day_5.part_2(test_data) == 17604
