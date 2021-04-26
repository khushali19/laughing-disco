from tkinter import *
import pyjokes

bg = '#ebc634'  #background color
fg = '#2B2B2B'  #foreground color
root = Tk()
root.title('Python Joke Generator | Khushali Mehta')
root.geometry("550x400")
root.config(bg=bg)

def gen_joke(joke_label):
    joke_label.config(text=pyjokes.get_joke())

Label(root, text=" Jokes Generator ", font="Helvetica 25 bold",
      height=2, fg=fg, bg='#e8e6e0').pack()

joke_label = Label(root, text=pyjokes.get_joke(),
                   font="Helvetica 20 italic",
                   wraplength=300, fg=fg, bg=bg)

refresh = Button(root, text='Once More', fg=fg, bg='#9bf2db', font="Helvetica 20 normal",
                 command=lambda : gen_joke(joke_label))

# by_ = Label(root, text='By:Khushali Mehta', font='Helvetica 20 normal', fg=fg, bg=bg)

joke_label.pack()
# by_.pack(side='bottom')
refresh.pack(side='bottom')


root.mainloop()
