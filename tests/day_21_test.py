import days.day_21 as day_21


def test_day_21_part_1_example():
    test_data = day_21.get_input_data("day_21_example.txt")
    assert day_21.part_1(test_data) == 739785


def test_day_21_part_1():
    test_data = day_21.get_input_data("day_21.txt")
    assert day_21.part_1(test_data) == 893700


# def test_day_21_part_2_example():
#     test_data = day_21.get_input_data("day_21_example.txt")
#     assert day_21.part_2(test_data) == 61229
#
#
# def test_day_21_part_2():
#     test_data = day_21.get_input_data("day_21.txt")
#     assert day_21.part_2(test_data) == 100148777
