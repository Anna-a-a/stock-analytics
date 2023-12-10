import pickle


class StackedColumnChart:
    def __init__(self, q1, q2, q3, q4):
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4

    def serialize(self):
        return {
            'q1': [item.serialize() for item in self.q1],
            'q2': [item.serialize() for item in self.q2],
            'q3': [item.serialize() for item in self.q3],
            'q4': [item.serialize() for item in self.q4],
        }
