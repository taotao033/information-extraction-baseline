from tqdm import tqdm
import json


def _is_valid_input_data(input_line):
    """is the input data valid"""
    try:
        dic = input_line.strip()
        dic = json.loads(dic)
    except:
        return False
    if "text" not in dic or "postag" not in dic or \
            type(dic["postag"]) is not list:
        return False
    for item in dic['postag']:
        if "word" not in item or "pos" not in item:
            return False
    return True


vocab_list = []
dataset_char_set = set()
with open("./checkpoint/vocab.txt", 'r+') as vocab:
    for i in vocab.readlines():
        vocab_list.append(str(i).replace('\n', ''))

    with open("../../data/train_data.json", 'r') as train_f:
        for li in tqdm(train_f.readlines()):
            if not _is_valid_input_data(li):
                print('Format is error')

            dic = li.strip()
            dic = json.loads(dic)
            sentence = dic['text']
            for c in sentence:
                dataset_char_set.add(c)

    with open("../../data/dev_data.json", 'r') as dev_f:
        for li in tqdm(dev_f.readlines()):
            if not _is_valid_input_data(li):
                print('Format is error')

            dic = li.strip()
            dic = json.loads(dic)
            sentence = dic['text']
            for c in sentence:
                dataset_char_set.add(c)

    with open("../../data/test1_data_postag.json", 'r') as test_f:
        for li in tqdm(test_f.readlines()):
            if not _is_valid_input_data(li):
                print('Format is error')

            dic = li.strip()
            dic = json.loads(dic)
            sentence = dic['text']
            for c in sentence:
                dataset_char_set.add(c)

    different_char_list = dataset_char_set.difference(set(vocab_list))

    for i in different_char_list:
        if i != ' ':
            vocab.write(i + '\n')
    vocab.close()
print("Bert vocabulary has been updated.")