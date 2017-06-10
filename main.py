from LDAGibbs.LDADataset import LDADataset
from LDAGibbs.LDAInferencer import LDAInferencer


def main():
    M = 0
    raw_docs = []
    with open('input/data.txt', 'r') as f:
        for index, line in enumerate(f):
            if index == 0:
                M = int(line)
            else:
                raw_docs.append(line)
    dataset = LDADataset(M)
    for index, raw_doc in enumerate(raw_docs):
        dataset.set_doc(raw_doc, index)
    inferencer = LDAInferencer(K=10, dataset=dataset, niters=50)
    model = inferencer.inference()

    output_str = ""
    for i in range(len(model.phi)):
        output_str += "----------------------------\nTopic " + str(i) + "\n"
        words = []
        for j in range(len(model.phi[i])):
            words.append([j, model.phi[i][j]])
        sorted_words = sorted(words, key=lambda word: word[1], reverse=True)
        for j in range(20):
            output_str += inferencer.dictionary.get_word(sorted_words[j][0]) + " : " + str(sorted_words[j][1]) + "\n"

    output_file = open('output/topic_word.txt', 'w')
    output_file.write(output_str)
    output_file.close()

    output_str = ""
    for i in range(len(model.theta)):
        output_str += str(i+1) + ": "
        topics = []
        for j in range(len(model.theta[i])):
            topics.append([j, model.theta[i][j]])
        sorted_topics = sorted(topics, key=lambda topic: topic[1], reverse=True)
        for j in range(5):
            output_str += str(sorted_topics[j][0]) + " " + str(sorted_topics[j][1]) + " "
        output_str += "\n"

    output_file = open('output/topic_doc.txt', 'w')
    output_file.write(output_str)
    output_file.close()

    output_str = ""
    for j in range(len(model.phi[0])):
        output_str += inferencer.dictionary.get_word(j)
        topics = []
        for i in range(len(model.phi)):
            topics.append([i, model.phi[i][j]])
        sorted_topics = sorted(topics, key=lambda topic: topic[1], reverse=True)
        for i in range(5):
            output_str += " " + str(sorted_topics[i][0]) + " " + str(sorted_topics[i][1])
        output_str += "\n"

    output_file = open('output/word_topic.txt', 'w')
    output_file.write(output_str)
    output_file.close()

if __name__ == '__main__':
    main()
