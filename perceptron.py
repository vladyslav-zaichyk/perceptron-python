from numpy import random


class Perceptron:
    """Basic perceptron with randomly generated weights"""

    def __init__(self, sign_threshold, inputs_count, learning_rate):
        self.sign_threshold = sign_threshold
        self.inputs_count = inputs_count
        self.weights = random.rand(inputs_count)
        self.learning_rate = learning_rate

    def guess(self, inputs):
        assert len(inputs) == self.inputs_count, \
            "Wrong inputs count. This perceptron works with {} inputs, got {}" \
            .format(self.inputs_count, len(inputs))

        wi_sum = self.__calc_sum(inputs)
        output = self.__sign(wi_sum, self.sign_threshold)
        return output

    def __calc_sum(self, inputs):
        result = 0
        for i in range(self.inputs_count):
            result += inputs[i] * self.weights[i]
        return result

    # Activation function
    @staticmethod
    def __sign(n, threshold):
        return 1 if n >= threshold else -1

    def learn(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess

        # Tune all the weights
        for i in range(self.inputs_count):
            self.weights[i] += error * inputs[i] * self.learning_rate