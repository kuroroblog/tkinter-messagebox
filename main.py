import tkinter as tk
from tkinter import messagebox

# messageboxのaskyesnocancelのdialogを表示する。
def getAskYesNoCancel():
    # Yes, No, Cancelの質問を提供するmessagebox dialogになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    # 戻り値 : True (Yes), False (No), None (Cancel)
    res = messagebox.askyesnocancel("askyesnocancel", "askyesnocancelです。")
    # レスポンスの内容を表示する。
    print("askyesnocancel", res)

# messageboxのaskretrycancelのdialogを表示する。
def getAskRetryCancel():
    # Retry, Cancelの質問を提供するmessagebox dialogになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    # 戻り値 : True(Retry), False(Cancel)
    res = messagebox.askretrycancel("askretrycancel", "askretrycancelです。")
    # レスポンスの内容を表示する。
    print("askretrycancel", res)

# messageboxのaskyesnoのdialogを表示する。
def getAskYesNo():
    # Yes, Noの質問を提供するmessagebox dialogになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    # 戻り値 : True (Yes), False (No)
    res = messagebox.askyesno("askyesno", "askyesnoです。")
    # レスポンスの内容を表示する。
    print("askyesno", res)

# messageboxのaskokcancelのdialogを表示する。
def getAskOkCancel():
    # OK, Cancelの質問を提供するmessagebox dialogになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    # 戻り値 : True(OK), False(Cancel)
    res = messagebox.askokcancel("askokcancel", "askokcancelです。")
    # レスポンスの内容を表示する。
    print("askokcancel", res)

# messageboxのaskquestionのdialogを表示する。
def getAskQuestion():
    # Yes, Noの質問を提供するmessagebox dialogになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    # 戻り値 : yes(Yes), no(No)
    res = messagebox.askquestion("askquestion", "askquestionです。")
    # レスポンスの内容を表示する。
    print("askquestion", res)

# messageboxのshowerrorのdialogを表示する。
def getShowError():
    # エラーを提供するmessagebox dialogになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    # 戻り値 : OK
    res = messagebox.showerror("showerror", "showerrorです。")
    # レスポンスの内容を表示する。
    print("showerror", res)

# messageboxのshowwarningのdialogを表示する。
def getShowWarning():
    # 警告を提供するmessagebox dialogになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    # 戻り値 : OK
    res = messagebox.showwarning("showwarning", "showwarningです。")
    # レスポンスの内容を表示する。
    print("showwarning", res)

# messageboxのshowinfoのdialogを表示する。
def getShowInfo():
    # 情報を提供するmessagebox dialogになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    # 戻り値 : OK
    res = messagebox.showinfo("showinfo", "showinfoです。")
    # レスポンスの内容を表示する。
    print("showinfo", res)

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
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
    # getAskYesNoCancel()
