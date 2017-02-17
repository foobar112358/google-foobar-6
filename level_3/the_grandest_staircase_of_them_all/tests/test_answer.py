from solution import answer

from nose.tools import eq_
# 0 - 1
# 1 - 1
# 2 - 1
# 3 - 2
# 4 - 2
# 5 - 3
# 6 - 4
# 7 - 5
# 8 - 6
# 9 - 8
# 10 - 10
def test_answer():
    # define expected input / output values
    test_data = {
        0 : 0, 1 : 0, 2 : 0, 3 : 1, 4 : 1, 5 : 2,
        6 : 3, 7 : 4, 8 : 5, 9 : 7, 10 : 9, 11 : 11
    }

    for key, expected in test_data.items():
        eq_(expected, answer(key))

