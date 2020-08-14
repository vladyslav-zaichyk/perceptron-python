import random


def hex2rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rand_hex_color():
    random_number = random.randint(1118481, 16777215)
    hex_number = str(hex(random_number))
    hex_number = '#' + hex_number[2:]
    return hex_number
