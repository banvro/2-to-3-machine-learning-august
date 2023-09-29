# tkiner : 
import tkinter as tk 

app = tk.Tk()

app.geometry("700x400")
app.title("This is my titile")
app.configure(background = "blue")

lbl = tk.Label(app, text = "How are you", font = ("sans-serif", 30, "bold"), fg = "red", bg = "yellow")
lbl.pack(fill = "x", padx = 20, pady = 10, ipady=5)

entr = tk.Entry(app, font = ("sans-serif", 18, "italic"))
entr.pack()

btb = tk.Button(app, text = "Submit", font = ("sans-serif", 18, "bold"))
btb.pack(pady=20)

btb = tk.Radiobutton(app, text = "Submit", font = ("sans-serif", 18, "bold"))
# btb = tk.Checkbutton(app, text = "Submit", font = ("sans-serif", 18, "bold"))
btb.pack(pady=20)



app.mainloop()
