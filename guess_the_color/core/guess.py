import random


class GuessColor:
    COUNT = 100
    GREEN_RANGE = (6, 9)
    RED_RANGE = (2, 5)

    COLOR_BLUE = 1
    COLOR_GREEN = 2
    COLOR_RED = 3

    COLORS = {
        COLOR_BLUE: 'blue',
        COLOR_GREEN: 'green',
        COLOR_RED: 'red'
    }

    object = []

    def __init__(self, number):
        self.number = number
        self.__make_objects()

    def guess_the_color(self):
        return self.COLORS[self.objects[self.number]]

    def __make_objects(self):
        green_count = random.randint(*self.GREEN_RANGE)
        red_count = random.randint(*self.RED_RANGE)
        blue_count = self.COUNT - green_count - red_count

        self.objects = (
                [self.COLOR_BLUE] * blue_count +
                [self.COLOR_GREEN] * green_count +
                [self.COLOR_RED] * red_count)

        random.shuffle(self.objects)
