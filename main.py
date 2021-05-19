import tkinter as tk
from tkinter import messagebox

# messageboxのaskyesnocancelのdialogを表示する。
def getAskYesNoCancel():
    # 質問を提供するmessagebox dialogになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    res = messagebox.askyesnocancel("askyesnocancel", "askyesnocancelです。")
    # レスポンスの内容を表示する。
    print("askyesnocancel", res)

# messageboxのaskretrycancelのdialogを表示する。
def getAskRetryCancel():
    # 質問を提供するmessagebox dialogになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    res = messagebox.askretrycancel("askretrycancel", "askretrycancelです。")
    # レスポンスの内容を表示する。
    print("askretrycancel", res)

# messageboxのaskyesnoのdialogを表示する。
def getAskYesNo():
    # 質問を提供するmessagebox dialogになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    res = messagebox.askyesno("askyesno", "askyesnoです。")
    # レスポンスの内容を表示する。
    print("askyesno", res)

# messageboxのaskokcancelのdialogを表示する。
def getAskOkCancel():
    # 質問を提供するmessagebox dialogになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    res = messagebox.askokcancel("askokcancel", "askokcancelです。")
    # レスポンスの内容を表示する。
    print("askokcancel", res)

# messageboxのaskquestionのdialogを表示する。
def getAskQuestion():
    # 質問を提供するmessagebox dialogになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    res = messagebox.askquestion("askquestion", "askquestionです。")
    # レスポンスの内容を表示する。
    print("askquestion", res)

# messageboxのshowerrorのdialogを表示する。
def getShowError():
    # 警告を提供するmessagebox dialogになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    res = messagebox.showerror("showerror", "showerrorです。")
    # レスポンスの内容を表示する。
    print("showerror", res)

# messageboxのshowwarningのdialogを表示する。
def getShowWarning():
    # 警告を提供するmessagebox dialogになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
    res = messagebox.showwarning("showwarning", "showwarningです。")
    # レスポンスの内容を表示する。
    print("showwarning", res)

# messageboxのshowinfoのdialogを表示する。
def getShowInfo():
    # 情報を提供するmessagebox dialogになります。
    # 第一引数 : タイトル文字列
    # 第二引数 : メッセージ内容
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
