def semantic_preprocess():
    semantic_dict = dict()
    line_num = 0

    for line in open('datasets/NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt'):
        if line_num > 2:
            words = line.split('\t')
            if words[0] not in semantic_dict.keys():
                semantic_dict[words[0]] = {'anger': 0, 'anticipation': 0, 'disgust': 0, 'fear': 0, 'joy': 0,
                                           'negative': 0, 'positive': 0, 'sadness': 0, 'surprise': 0, 'trust': 0}
            semantic_dict[words[0]][words[1]] = int(words[2])

        line_num += 1

    return semantic_dict


print(semantic_preprocess())