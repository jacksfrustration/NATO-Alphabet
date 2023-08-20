from tkinter import *
from tkinter import messagebox
def convert(_event):
    word=word_entry.get().upper()
    letter_dict={"A":"Alpha","B":"Bravo","C": "Charlie",
             "D":"Delta","E": "Echo","F": "Foxtrot","G": "Golf"
                ,"H": "Hotel","I": "India","J":"Juliett","K": "Kilo"
                ,"L":"Lima","M": "Mike","N": "November","O": "Oscar"
                ,"P": "Papa","Q":"Quebec","R": "Romeo",
             "S":"Sierra","T": "Tango","U": "Uniform","V":"Victor",
             "W":"Whiskey","X":" X-ray","Y": "Yankee","Z": "Zulu"," ": " "
             ,"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6",
             "7":"7","8":"8","9":"9","0":"0"}

    converted_word=[letter_dict[x] for x in word]
    for i in range(len(converted_word)-1,0,-1):
        if i ==len(converted_word)-1 and converted_word[i]==" ":
            converted_word.remove(" ")
    if converted_word:
        joined=",".join(converted_word)
        messagebox.showinfo(title="Your words",message=joined)
    else:
        messagebox.showerror(title="Oops",message="You haven't typed anything.\nTry again!!")

window=Tk()
window.title("NATO Alphabet")
eawe_lbl=Label(text="Enter a word")
eawe_lbl.grid(row=2,column=0)
word_entry=Entry()
word_entry.grid(row=2,column=1)
window.bind("<Return>",convert)
go_btn=Button(text="Convert",command=convert)
go_btn.grid(row=2,column=2)
window.mainloop()