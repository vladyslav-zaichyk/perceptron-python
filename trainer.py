# 0 stands for white, 1 stands for black
color_set = {
    "#800000": -1,
    "#993333": -1,
    "#cc3300": -1,
    "#ff9900": 1,
    "#ffcc00": 1,
    "#ffcc66": 1,
    "#ffff66": 1,
    "#ccff33": 1,
    "#003300": -1,
    "#00ff00": 1,
    "#66ccff": 1,
    "#660066": -1,
    "#003399": -1,
    "#ffffff": 1,
    "#66ff66": 1,
    "#ff00ff": 1,
    "#ff6699": -1,
    "#00ffff": 1,
    "#99ffcc": 1,
    "#3333cc": -1
}


def hex2rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def train2pick_colours(perceptron, train_data):
    for key, value in train_data.items():
        perceptron.learn(hex2rgb(key), value)
