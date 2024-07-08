import random
import pandas as pd

class Cloudlet:
    def __init__(self, area, instructions, size, priority, bandwidth, delay, score):
        self.area = area
        self.instructions = instructions
        self.size = size
        self.priority = priority
        self.bandwidth = bandwidth
        self.delay = delay
        self.score = score

    def getAsDict(self):
        return {
            'Area': self.area,
            'Instructions': self.instructions,
            'Size': self.size,
            'Priority': self.priority,
            'Bandwidth': self.bandwidth,
            'Delay': self.delay,
            'Score': self.score
        }
    
    