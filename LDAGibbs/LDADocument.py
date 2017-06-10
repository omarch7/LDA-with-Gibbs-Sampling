class LDADocument:
    def __init__(self, ids, raw_str):
        self.length = len(ids)
        self.raw_str = raw_str
        self.words = [0] * self.length

        for i in range(self.length):
            self.words[i] = ids[i]
