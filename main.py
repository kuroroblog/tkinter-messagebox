import tkinter as tk
from tkinter import messagebox

# messageboxのaskyesnocancelを表示する。
def getAskYesNoCancel():
    # Yes, No, Cancelの質問メッセージを伝える、messageboxになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    # 戻り値 : True, False, None
    res = messagebox.askyesnocancel("askyesnocancel", "askyesnocancelです。")
    # レスポンスの内容を表示する。
    print("askyesnocancel", res)

# messageboxのaskretrycancelを表示する。
def getAskRetryCancel():
    # Retry, Cancelの質問メッセージを伝える、messageboxになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    # 戻り値 : True, False
    res = messagebox.askretrycancel("askretrycancel", "askretrycancelです。")
    # レスポンスの内容を表示する。
    print("askretrycancel", res)

# messageboxのaskyesnoを表示する。
def getAskYesNo():
    # Yes, Noの質問メッセージを伝える、messageboxになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    # 戻り値 : True, False
    res = messagebox.askyesno("askyesno", "askyesnoです。")
    # レスポンスの内容を表示する。
    print("askyesno", res)

# messageboxのaskokcancelを表示する。
def getAskOkCancel():
    # OK, Cancelの質問メッセージを伝える、messageboxになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    # 戻り値 : True, False
    res = messagebox.askokcancel("askokcancel", "askokcancelです。")
    # レスポンスの内容を表示する。
    print("askokcancel", res)

# messageboxのaskquestionを表示する。
def getAskQuestion():
    # Yes, Noの質問メッセージを伝える、messageboxになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    # 第三引数以降(任意) : option
    # 戻り値 : yes, no
    res = messagebox.askquestion("askquestion", "askquestionです。")
    # レスポンスの内容を表示する。
    print("askquestion", res)

# messageboxのshowerrorを表示する。
def getShowError():
    # エラーメッセージを伝える、messageboxになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    # 第三引数以降(任意) : option
    # 戻り値 : ok
    res = messagebox.showerror("showerror", "showerrorです。")
    # レスポンスの内容を表示する。
    print("showerror", res)

# messageboxのshowwarningを表示する。
def getShowWarning():
    # 警告メッセージを伝える、messageboxになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    # 第三引数以降(任意) : option
    # 戻り値 : ok
    res = messagebox.showwarning("showwarning", "showwarningです。")
    # レスポンスの内容を表示する。
    print("showwarning", res)

# messageboxのshowinfoを表示する。
def getShowInfo():
    # お知らせメッセージを伝える、messageboxになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    # 第三引数以降(任意) : option
    # 戻り値 : ok
    res = messagebox.showinfo("showinfo", "showinfoです。")
    # レスポンスの内容を表示する。
    print("showinfo", res)

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    # Windowを生成する。
    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()
    # Windowの非表示
    root.withdraw()

    # getShowInfo()
    # getShowWarning()
    # getShowError()
    # getAskQuestion()
    # getAskOkCancel()
    # getAskYesNo()
    # getAskRetryCancel()
    getAskYesNoCancel()
