from LDADictionary import LDADictionary
from LDADocument import LDADocument


class LDADataset:
    def __init__(self, M):
        self.dictionary = LDADictionary()
        self.M = M
        self.V = 0
        self.docs = [None] * M

    def set_doc(self, doc, index):
        if 0 <= index < self.M:
            self.docs[index] = doc

    def set_doc(self, raw_str, index):
        if 0 <= index < self.M:
            words = raw_str.lower().split()
            ids = []

            for word in words:
                if self.dictionary.contains_word(word):
                    word_id = self.dictionary.get_id(word)
                else:
                    word_id = self.dictionary.add_word(word)
                ids.append(word_id)

            doc = LDADocument(ids=ids, raw_str=raw_str)
            self.docs[index] = doc
            self.V = len(self.dictionary.word2id)
