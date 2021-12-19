import days.day_7 as day_7


def test_day_7_part_1_example():
    test_data = day_7.get_input_data("day_7_example.txt")
    assert day_7.part_1(test_data) == 37


def test_day_7_part_1():
    test_data = day_7.get_input_data("day_7.txt")
    assert day_7.part_1(test_data) == 355521


def test_day_7_part_2_example():
    test_data = day_7.get_input_data("day_7_example.txt")
    assert day_7.part_2(test_data) == 168


def test_day_7_part_2():
    test_data = day_7.get_input_data("day_7.txt")
    assert day_7.part_2(test_data) == 100148777
