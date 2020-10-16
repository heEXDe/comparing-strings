from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
import string
root = Tk()


def compare():
    try:
        lblStatus.config(text="comparing ...")
        input1 = txtBox01.get('1.0', 'end-1c')
        input2 = txtBox02.get('1.0', 'end-1c')
        if input1 == input2:
            lblStatus.config(text="identical")
        else:
            lblStatus.config(text="different")
    except:
        messagebox.showinfo("Błąd", "Złe dane lub niepoprawna akcja.")


def wyczysc():
    lblStatus.config(text="")
    txtBox01.delete('1.0', END)
    txtBox02.delete('1.0', END)


lblStatus = Label(root, text="")
txtBox01 = Text(root, height=5, width=50)
txtBox02 = Text(root, height=5, width=50)
btnCompare = Button(root, text="Compare", command=lambda: compare())
btnWyczysc = Button(root, text="Wyczysc", command=lambda: wyczysc())
txtBox01.grid(row=0, columnspan=4, sticky=W+E)
txtBox02.grid(row=2, columnspan=4, sticky=W+E)
lblStatus.grid(row=1, column=0)
btnCompare.grid(row=1, column=2)
btnWyczysc.grid(row=1, column=3)

root.title("Szyfrator")
#root.geometry("500x300")
root.resizable(0, 0)
root.mainloop()
