import numpy as np


def array_to_img(str_array: str) -> np.array:
    img = np.zeros(101 * 101)
    if str_array == 'nan':
        return img

    splited = list(map(int, str_array.split(' ')))
    for start, num in zip(splited[0::2], splited[1::2]):
        img[start - 1:start + num - 1] = 1

    return img.reshape(101, 101)


def count_array_mask(str_array: str) -> int:
    if str_array == 'nan':
        return 0

    splited = list(map(int, str_array.split(' ')))
    return sum(splited[1::2])


if __name__ == '__main__':
    test_data = "9 93 109 94 210 94 310 95 411 95 511 96 612 96"
    print(array_to_img(test_data))
    print(count_array_mask(test_data))
