import math
import random


class LDAModel:
    def __init__(self, K, dataset):
        self.M = 0
        self.V = 0
        self.K = K
        self.alpha = 50.0 / K
        self.beta = 0.1
        self.niters = 2000
        self.z = None
        self.nw = None
        self.nd = None
        self.nwsum = None
        self.ndsum = None
        self.theta = None
        self.phi = None
        self.dataset = dataset
        self.p = [0.0 for x in range(self.K)]

    def init_model(self):
        self.M = self.dataset.M
        self.V = self.dataset.V

        self.nd = [[0 for x in range(self.K)] for y in range(self.M)]
        self.nw = [[0 for x in range(self.K)] for y in range(self.V)]
        self.nwsum = [0 for x in range(self.K)]
        self.ndsum = [0 for x in range(self.M)]

        self.z = [[] for x in range(self.M)]

        for m in range(self.M):
            N = self.dataset.docs[m].length
            for n in range(N):
                topic = int(math.floor(random.random() * self.K))
                self.z[m].append(topic)
                self.nw[self.dataset.docs[m].words[n]][topic] += 1
                self.nd[m][topic] += 1
                self.nwsum[topic] += 1
            self.ndsum[m] = N

        self.theta = [[0.0 for x in range(self.K)] for y in range(self.M)]
        self.phi = [[0.0 for x in range(self.V)] for y in range(self.K)]

