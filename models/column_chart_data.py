import json
import pickle


class ColumnChart:
    def __init__(self, label, y):
        self.label = label
        self.y = y

    def serialize(self):
        return {
            'label': self.label,
            'y': self.y
        }
