from tkinter import *
from tkinter import ttk
from tkinter import font
from translate_data import translate_sentence as ts
import threading

win = Tk()
win.title("Translator")
win.maxsize(width=600, height=300)
win.minsize(width=600, height=300)


# function
def threading_translate():
    #calling translate_sentence method on other thread.
    t = threading.Thread(target=translate_sentence)
    t.start()
def translate_sentence():
    try:
        sentence = sentence_var.get()
        from_lan = from_lan_var.get()
        to_lan = to_lan_var.get()
        print(f"sentence is {sentence}, from is {from_lan} and to is {to_lan}")
        s = ts(from_lan, to_lan, sentence)
        translated_label.config(text=s)
    except Exception as e:
        translated_label.config(text="Something went wrong")
        print(e.message)

def reset_fields():
    translated_label.config(text="Translate : ")
    pick_from_language_box.current(0)
    pick_to_language_box.current(0)
    sentence_var.set("")


# label
title_label = Label(win, text="Welcome to PyTranslator", font=("Aerial", 15))
title_label.place(x=200, y=10)
translated_label = Label(win, text="Translate : ", font=("Aerial", 12))
translated_label.place(x=150, y=190)
# combobox
from_lan_var = StringVar()
pick_from_language_box = ttk.Combobox(win, textvariable=from_lan_var)
pick_from_language_box['state'] = 'readonly'
pick_from_language_box['values'] = (
    'From', 'Hindi', "English", "Spanish", "Japanese")
pick_from_language_box.current(0)
pick_from_language_box.place(x=150, y=60)

to_lan_var = StringVar()
pick_to_language_box = ttk.Combobox(win, textvariable=to_lan_var)
pick_to_language_box['state'] = 'readonly'
pick_to_language_box['values'] = (
    'To', 'Hindi', "English", "Spanish", "Japanese")
pick_to_language_box.current(0)
pick_to_language_box.place(x=300, y=60)

# Entry
sentence_var = StringVar()
sentence_entry = Entry(win, textvariable=sentence_var, bd=2)
sentence_entry.place(x=150, y=90, width=298, height=50)

# Button
translate_btn = Button(win, text="Translate", width=20,
                       bg="Green", fg="white", command=threading_translate)
translate_btn.place(x=148, y=150)

Reset_btn = Button(win, text="Reset", width=19, bg="Red",
                   fg="white", command=reset_fields)
Reset_btn.place(x=302, y=150)
win.mainloop()
