from scripts.common.paths import files
from typing import List

def create_label_map(label_names: List[str]):
    labels = []

    for idx, name in enumerate(label_names):
        labels.append({'name':name, 'id':idx+1})

    true_labels = [{'name':'ThumbsUp', 'id':1}, {'name':'ThumbsDown', 'id':2}, {'name':'ThankYou', 'id':3}, {'name':'LiveLong', 'id':4}]
    # label_names = ThumbsUp ThumbsDown ThankYou LiveLong

    print(labels)
    print(true_labels)
    print(labels == true_labels)


    with open(files['LABEL_MAP'], 'w') as f:
        for label in labels:
            f.write('item { \n')
            f.write('\tname:\'{}\'\n'.format(label['name']))
            f.write('\tid:{}\n'.format(label['id']))
            f.write('}\n')