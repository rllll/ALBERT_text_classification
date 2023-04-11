from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split


def read_data_from_excel():
    # type_list = ['宝马1系', '宝马2系', '宝马3系（1）','宝马3系（2）', '宝马3系（3）', '宝马3系（4）','宝马3系（5）', '宝马3系（6）', '宝马3系（7）','宝马3系（8）', '宝马3系（9）', '宝马3系（10)','宝马3系（11）', '宝马3系（12）', '宝马4系','宝马5系','宝马X1（1）', '宝马X1（2）', '宝马X1(5)', '宝马X2', '宝马X3']
    type_list = ['宝马3系（3）']
    df = pd.read_excel('./data/bmw_all.xlsx', sheet_name=type_list, usecols=[2, 21], dtype=str)
    contents, labels = [], []
    for type in type_list:
        df_drop = df[type].dropna(subset=['总的来说'])
        contents += df_drop["具体评价"].tolist()
        labels += df_drop['总的来说'].tolist()
    train_words, test_words, train_labels, test_labels = train_test_split(contents, labels, test_size=0.2)
    return train_words, test_words, train_labels, test_labels

def save_data_to_text(mode, save_words, save_labels):
    for label, word in zip(save_labels, save_words):
        if label.strip() != '' and word.strip() != '':
            with Path('./data/{}.txt'.format(mode)).open('a', encoding='utf-8') as g:
                g.write('{} {}\n'.format(label, word))

if __name__ == '__main__':
    train_words, test_words, train_labels, test_labels = read_data_from_excel()
    print(len(train_words), len(train_labels))
    print(len(test_words), len(test_labels))
    save_data_to_text('train', train_words, train_labels)
    save_data_to_text('test', test_words, test_labels)
