from zad_1_itog import szd, szd_f
from zad_2_itog import rspd, rspd_f, analiz_textov_po_temam
import os.path
import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from ctypes import windll
import easygui
import os
import shutil


def on_closing():
    try:
        if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
            window.destroy()
    except Warning:
        return


def getDirectory():
    try:
        input_dir_name = easygui.diropenbox()
        return input_dir_name
    except (
            FileNotFoundError, FileExistsError, PermissionError, UnicodeDecodeError, TypeError, NameError,
            AttributeError) as e:
        print(f"Error! {e}")


def getFile():
    try:
        input_dir_name = easygui.fileopenbox()
        return input_dir_name
    except (
            FileNotFoundError, FileExistsError, PermissionError, UnicodeDecodeError, TypeError, NameError,
            AttributeError) as e:
        print(f"Error! {e}")


def openOut():
    os.startfile(os.path.relpath('output/'))


def clearOut():
    shutil.rmtree('output/txts')
    shutil.rmtree('output/thms')
    os.mkdir('output/txts')
    os.mkdir('output/thms')


def open_info():
    try:
        #showinfo(title="Инструкция", message=f'''''')
        os.startfile(os.path.relpath('README.txt'))
    except Exception as e:
        messagebox.showerror("Error!", str(e))


def my_app_id():
    try:
        myappid = "mycompany.myproduct.subproduct.version"
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass


# выполняем задание 1
def texts_from_dir():
    try:
        szd(getDirectory(), 'output/txts/', False)
    except (
            FileNotFoundError, FileExistsError, PermissionError, UnicodeDecodeError, TypeError, NameError,
            AttributeError) as e:
        print(f"Error! {e}")


def texts_from_file():
    try:
        szd_f(getFile(), 'output/txts/', False)
    except (
            FileNotFoundError, FileExistsError, PermissionError, UnicodeDecodeError, TypeError, NameError,
            AttributeError) as e:
        print(f"Error! {e}")


# выполняем задание 2
def thems_from_dir():
    try:
        rspd(getDirectory())
    except (
            FileNotFoundError, FileExistsError, PermissionError, UnicodeDecodeError, TypeError, NameError,
            AttributeError) as e:
        print(f"Error! {e}")


def thems_from_file():
    try:
        rspd_f(getFile())
    except (
            FileNotFoundError, FileExistsError, PermissionError, UnicodeDecodeError, TypeError, NameError,
            AttributeError) as e:
        print(f"Error! {e}")


if __name__ == "__main__":

    # тело приложения
    window = tk.Tk()
    window.protocol("WM_DELETE_WINDOW", on_closing)
    basedir = os.path.dirname(__file__)

    # иконка приложения
    window.iconbitmap(os.path.join(basedir, "NLP.ico"))
    window.title("natural language processing")
    window.resizable(width=False, height=False)
    window.wm_attributes("-topmost")
    window.geometry('700x400')
    window["bg"] = "#15161a"


    Text_Dir_Enter_Button = tk.Button(window, text="ДОБАВИТЬ ТЕКСТЫ ИЗ ПАПКИ", command=texts_from_dir, width="40",
                                      height="4",
                                      fg="white", bg="#15161a", borderwidth=3, relief='groove',
                                      activebackground='#3C3C44',
                                      activeforeground='white')
    Text_Dir_Enter_Button.place(x=49, y=105)

    Text_File_Enter_Button = tk.Button(window, text="добавить один текст", command=texts_from_file, width="40",
                                       height="2",
                                       fg="white", bg="#15161a", borderwidth=3, relief='groove',
                                       activebackground='#3C3C44',
                                       activeforeground='white')
    Text_File_Enter_Button.place(x=49, y=170)

    Theme_Dir_Enter_Button = tk.Button(window, text="ДОБАВИТЬ ТЕМЫ ИЗ ПАПКИ", command=thems_from_dir, width="40",
                                       height="4",
                                       fg="white", bg="#15161a", borderwidth=3, relief='groove',
                                       activebackground='#3C3C44',
                                       activeforeground='white')
    Theme_Dir_Enter_Button.place(x=365, y=105)

    Theme_File_Enter_Button = tk.Button(window, text="добавить одну тему", command=thems_from_file, width="40",
                                        height="2",
                                        fg="white", bg="#15161a", borderwidth=3, relief='groove',
                                        activebackground='#3C3C44',
                                        activeforeground='white')
    Theme_File_Enter_Button.place(x=365, y=170)

    Analyse_Button = tk.Button(window, text="АНАЛИЗ", command=analiz_textov_po_temam, width="30", height="2",
                               fg="#d42c32", bg="#15161a", borderwidth=3, relief='groove', activebackground='#3C3C44',
                               activeforeground='red')
    Analyse_Button.place(x=239, y=220)
    # кнопока для папки
    loadimage_dady = tk.PhotoImage(file='Dady.png')
    btn_dady = tk.Button(window, activebackground='#15161a', command=openOut,
                         activeforeground='white', image=loadimage_dady, bg="#15161a", relief='flat', width='50',
                         height='50')  # command=  добавь функцию
    btn_dady.place(x=540, y=20)
    # кнопока для корзины
    loadimage_trash = tk.PhotoImage(file='Trash_Bin.png')
    btn_trash = tk.Button(window, activebackground='#15161a', command=clearOut,
                          activeforeground='white', image=loadimage_trash, bg="#15161a", relief='flat', width='50',
                          height='50')  # command=  добавь функцию
    btn_trash.place(x=600, y=20)
    # кнопока инструкции
    loadimage = tk.PhotoImage(file='Instructions.png')
    btn_info = tk.Button(window, text="Инструкция", command=open_info, activebackground='#15161a',
                         activeforeground='white', image=loadimage, bg="#15161a", relief='flat', width='50',
                         height='50')
    btn_info.place(x=50, y=20)
    try:
        window.mainloop()
    except KeyboardInterrupt as e:
        print(e)
