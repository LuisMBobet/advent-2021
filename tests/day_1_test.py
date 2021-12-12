import days.day_1 as day_1


def test_day_1_part_1_example():
    test_data = day_1.get_input_data("day_1_test.txt")
    assert day_1.part_1(test_data) == 7


def test_day_1_part_1():
    test_data = day_1.get_input_data("day_1.txt")
    assert day_1.part_1(test_data) == 1529


def test_day_1_part_2_example():
    test_data = day_1.get_input_data("day_1_test.txt")
    assert day_1.part_2(test_data) == 5


def test_day_1_part_2():
    test_data = day_1.get_input_data("day_1.txt")
    assert day_1.part_2(test_data) == 1567
