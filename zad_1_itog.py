import glob
import re
import pymorphy2
from stop_words_f import stop_words_m
import tkinter as tk
# from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
import time
import datetime

morph = pymorphy2.MorphAnalyzer()


# функция ремува стоп слов
def rmv_sw(a):
    return [w for w in a if w.lower() not in stop_words_m and len(w) > 1]


# функция получения названия файла
def get_file_name(a):
    c = a.split('\ '[0])
    n = c[-1].rsplit('.', 1)
    return n[0]


# функция получения начальной формы всех слов массива
def nf(a):
    return [str(morph.parse(x)[0].normal_form).upper() for x in a]


# функция, которая вызывается в main
# подаются сюда: путь к папке с изначальными файлами, и
# путь к папке в которую нам надо вывести файлы с отсортированными словами и циферками, и
# булевая переменная для реверсирования/нереверсирования
def szd(pth, adrs_out, srt_rv):
    print(pth)

    # ввод пути к папке с первыми файлами без расширения
    pth = pth + '/*'
    # print(pth)

    # o = []

    g = glob.iglob(pth)
    kg = 0
    lg = len(list(g))
    w = lg / 100

    # перебор по всем файлам в папке
    for fp in glob.iglob(pth):
        prc_r = '=' * (int(kg / w) // 5)
        prc_t = '-' * (20 - (int(kg / w) // 5))
        prc = f'{prc_r}{prc_t} | {int(kg // w)}%'

        print(prc)

        # открытие n-го файла
        with open(fp, encoding='UTF-8') as file:

            # читаем файл, убираем служебные символы и цифры, сплитуем, убираем стоп слова, берём начальную форму
            # получили массив со всеми словами в файле
            # знаете, что такое безумие? безумие - это двойная фильтраци по стоп словам
            tx = rmv_sw(nf(rmv_sw(re.sub('[^\w]+|[\d]+', ' ', file.read()).split())))

            # массив переделываем в сет, чтобы каждое слово шло по одному разу
            stx = set(tx)

            # создаём n-ый файл в папке аутпут, куда будем писать выходные данные
            n = adrs_out + get_file_name(fp) + '.txt'

            # создаём массив для сортирования, чтобы записать в ответы
            srttx = []

            # сортируем
            for x in stx:
                k = tx.count(x)
                srttx.append([k, x])

            # o.append(sorted(srttx, reverse=srt_rv))

            # открываем файл
            otv = open(n, 'w+')

            # перебираем слова в сете, чтобы посчитать их количество в файле(уже массиве)
            for x in sorted(srttx, reverse=srt_rv):
                # записываем в файл слово и его количество в одну строчку с переносом на слудующую
                v = x[1] + '\t' + str(x[0]) + '\n'
                otv.write(v)

            # закрываем n-ый файл
            otv.close()

        kg += 1
        print('\033[A', end='')

    print('=' * 20, ' | 100%', sep='')


def szd_f(fp, adrs_out, srt_rv):
    print(fp)

    # открытие n-го файла
    with open(fp, encoding='UTF-8') as file:

        # читаем файл, убираем служебные символы и цифры, сплитуем, убираем стоп слова, берём начальную форму
        # получили массив со всеми словами в файле
        # знаете, что такое безумие? безумие - это двойная фильтраци по стоп словам
        tx = rmv_sw(nf(rmv_sw(re.sub('[^\w]+|[\d]+', ' ', file.read()).split())))

        # массив переделываем в сет, чтобы каждое слово шло по одному разу
        stx = set(tx)

        # создаём n-ый файл в папке аутпут, куда будем писать выходные данные
        n = adrs_out + get_file_name(fp) + '.txt'

        # создаём массив для сортирования, чтобы записать в ответы
        srttx = []

        # сортируем
        for x in stx:
            k = tx.count(x)
            srttx.append([k, x])

        # o.append(sorted(srttx, reverse=srt_rv))

        # открываем файл
        otv = open(n, 'w+')

        # перебираем слова в сете, чтобы посчитать их количество в файле(уже массиве)
        for x in sorted(srttx, reverse=srt_rv):
            # записываем в файл слово и его количество в одну строчку с переносом на слудующую
            v = x[1] + '\t' + str(x[0]) + '\n'
            otv.write(v)

        # закрываем n-ый файл
        otv.close()
