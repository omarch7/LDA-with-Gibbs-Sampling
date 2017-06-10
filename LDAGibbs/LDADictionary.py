class LDADictionary:
    def __init__(self):
        self.word2id = dict()
        self.id2word = dict()
        self.stop_list = set('for a of the and to in'.split())

    def get_word(self, word_id):
        return self.id2word[word_id]

    def get_id(self, word):
        return self.word2id[word]

    def contains_word(self, word):
        return True if word in self.word2id else False

    def contains_id(self, word_id):
        return True if word_id in self.id2word else False

    def add_word(self, word):
        if not self.contains_word(word) and word not in self.stop_list:
            word_id = len(self.word2id)
            self.word2id[word] = word_id
            self.id2word[word_id] = word
            return word_id
        else:
            return self.get_id(word)
