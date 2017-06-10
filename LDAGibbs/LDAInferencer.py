import random
from LDAModel import LDAModel


class LDAInferencer:
    def __init__(self, K, dataset, niters):
        self.niters = niters
        self.model = LDAModel(K, dataset)
        self.model.init_model()
        self.dictionary = self.model.dataset.dictionary

        self.compute_theta()
        self.computer_phi()

    def inference(self):
        print "Sampling " + str(self.niters) + " iteration for inference!"
        for i in range(self.niters):
            for m in range(self.model.M):
                for n in range(self.model.dataset.docs[m].length):
                    topic = self.inf_sampling(m, n)
                    self.model.z[m][n] = topic
        self.compute_theta()
        self.computer_phi()
        return self.model

    def inf_sampling(self, m, n):
        topic = self.model.z[m][n]
        w = self.model.dataset.docs[m].words[n]

        self.model.nw[w][topic] -= 1
        self.model.nd[m][topic] -= 1
        self.model.nwsum[topic] -= 1
        self.model.ndsum[n] -= 1

        v_beta = float(self.model.V * self.model.beta)
        k_alpha = float(self.model.K * self.model.alpha)

        for k in range(self.model.K):
            try:
                self.model.p[k] = (self.model.nw[w][k] + self.model.beta) / (self.model.nwsum[k] + v_beta) * (self.model.nd[m][k] + self.model.alpha) / (self.model.ndsum[m] + k_alpha)
            except ZeroDivisionError:
                pass

        for k in range(1, self.model.K):
            self.model.p[k] += self.model.p[k - 1]

        u = float(random.random() * self.model.p[self.model.K - 1])

        for topic in range(self.model.K):
            if self.model.p[topic] > u:
                break

        self.model.nw[w][topic] += 1
        self.model.nd[m][topic] += 1
        self.model.nwsum[topic] += 1
        self.model.ndsum[m] += 1

        return topic

    def compute_theta(self):
        for m in range(self.model.M):
            for k in range(self.model.K):
                self.model.theta[m][k] = (self.model.nd[m][k] + self.model.alpha) / (self.model.ndsum[m] + self.model.K * self.model.alpha)

    def computer_phi(self):
        for k in range(self.model.K):
            for w in range(self.model.V):
                self.model.phi[k][w] = (self.model.nw[w][k] + self.model.beta) / (self.model.nwsum[k] + self.model.V * self.model.beta)