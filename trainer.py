from util.color_util import hex2rgb

# keys: hex colors, values: perceptron target
# -1 stands for white color, 1 stands for black color
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


def train_perceptron(perceptron, train_data):
    """Feeds train data to a perceptron"""
    for key, value in train_data.items():
        perceptron.learn(hex2rgb(key), value)
