import days.day_8 as day_8


def test_day_8_part_1_example():
    test_data = day_8.get_input_data("day_8_example.txt")
    assert day_8.part_1(test_data) == 26


def test_day_8_part_1():
    test_data = day_8.get_input_data("day_8.txt")
    assert day_8.part_1(test_data) == 375


# def test_day_8_part_2_example():
#     test_data = day_8.get_input_data("day_8_example.txt")
#     assert day_8.part_2(test_data) == 61229
#
#
# def test_day_8_part_2():
#     test_data = day_8.get_input_data("day_8.txt")
#     assert day_8.part_2(test_data) == 100148777
