import glob
from zad_1_itog import szd, get_file_name, szd_f
from gensim.similarities import MatrixSimilarity
from gensim.corpora import Dictionary
import os
import datetime
import chardet


# функция которая вернёт нам словарь
def ret_dict(a):
    d = {}
    with open(a) as f:
        for y in f.readlines():
            b = y.split()
            d[b[0]] = int(b[1])
    return dict(sorted(d.items(), key=lambda x: x[1]))


# функция, которая возвращает массив, где слова пишутся с только раз, сколько они встречаются в тексте
def ret_arr(a):
    d = []
    with open(a, 'rb') as file:
        data = file.read()
        encoding = chardet.detect(data)['encoding']
    with open(a, encoding=encoding) as f:
        for y in f.readlines():
            b = y.split()
            for i in range(int(b[1])):
                d.append(b[0])
    return d


def analiz_textov_po_temam():
    # массив из массивов, в которых все название и все слова для каждого из файлов задания 1
    o2 = [[get_file_name(fp), ret_arr(fp)] for fp in glob.iglob('output/txts/*.txt')]
    # print(len(o2))

    # массив из массивов, в которых все название и все слова для каждого из файлов в отсортированных темах
    th2 = [[get_file_name(fp), ret_arr(fp)] for fp in glob.iglob('output/thms/*.txt')]

    # открываем файл
    data = datetime.datetime.now().strftime('%d-%m-%y_%H-%M-%S')
    print(data)
    otv = open(f'output/classification_{data}.txt', 'w+')

    # проходимя по каждому элементу из массива текстов
    for x in o2:
        # print(f'сходства для файла {x[0]}.txt:')

        # массив для хранения массивов с схожестью и номером темы
        o = []

        # проходимя по каждому элементу из массива тем
        for y in th2:
            # сравниваем два массива на схожесть
            texts = [x[1], y[1]]
            dictionary = Dictionary(texts)
            corpus = [dictionary.doc2bow(text) for text in texts]
            similarity_matrix = MatrixSimilarity(corpus)
            similarity = similarity_matrix[corpus[0]]

            # добавляем схожесть с темой и её номер в массив о
            o.append([similarity[1], y[0]])

        # записываем в файл имя файла и тему
        v = x[0] + '\t' + max(o)[1] + '\n'
        otv.write(v)

    # закрываем файл
    otv.close()

    os.startfile(os.path.relpath('output/'))

    # print(f'{y[0]} тема - {similarity[1]}')
    # print(f'максимальное сходство файла {}.txt с темой {}')
    # print()


# функция, которая вызывается в main
# def rspd(tth=input('введите адрес папки с темами: ')):
def rspd(tth):
    # делаем те же действия(без удаления слов паразитов для текстов из папки с темами)
    szd(tth, 'output/thms/', True)


def rspd_f(tth):
    szd_f(tth, 'output/thms/', True)
