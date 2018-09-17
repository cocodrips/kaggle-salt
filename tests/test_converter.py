import pytest
from utils import converter


def test_array_to_img():
    data = "1 1 9 93 109 94 210 94 310 95 411 95 511 96 612 96"
    target = converter.array_to_img(data)
    assert target[0, 0] == 1
    assert target[1, 1] == 0
    assert target[(411 - 1) // 101, (411 - 1) % 101] == 1


def test_count_array_mask():
    data = "9 93 109 94 210 94 310 95 411 95 511 96 612 96"
    target = converter.count_array_mask(data)
    assert target == 663
