import tkinter as tk 



def savedata():
    dat1 = ent1.get()
    dat2 = ent2.get()
    dat3 = ent3.get() 


    


app = tk.Tk()

app.geometry("600x500")
app.title("This is my titile")

lbl0 = tk.Label(app, text = " ", font = ("sans-serif", 18, "bold"))
lbl1 = tk.Label(app, text = "Name ", font = ("sans-serif", 18, "bold"))
lbl2 = tk.Label(app, text = "Phone No.", font = ("sans-serif", 18, "bold"))
lbl3 = tk.Label(app, text = "Email ", font = ("sans-serif", 18, "bold"))
lbl4 = tk.Label(app, text = " : ", font = ("sans-serif", 18, "bold"))
lbl5 = tk.Label(app, text = " : ", font = ("sans-serif", 18, "bold"))
lbl6 = tk.Label(app, text = " : ", font = ("sans-serif", 18, "bold"))

# lbl6.grid(row = 0, column = 1)
lbl0.grid(row = 0, column = 0, padx = 55, ipady=10)
lbl1.grid(row = 1, column = 0, ipady=30 )
lbl2.grid(row = 2, column = 0, ipady=10)
lbl3.grid(row = 3, column = 0, ipady = 10)
lbl4.grid(row = 1, column = 1)
lbl5.grid(row = 2, column = 1)
lbl6.grid(row = 3, column = 1)

ent3 = tk.Entry(app, font = ("sans-serif", 18, "italic"))
ent1 = tk.Entry(app, font = ("sans-serif", 18, "italic"))
ent2 = tk.Entry(app, font = ("sans-serif", 18, "italic"))

ent3.grid(row = 3, column = 3)
ent1.grid(row = 1, column = 3)
ent2.grid(row = 2, column = 3)

btn = tk.Button(app, text = "submit", font = ("sans-serif", 18, "bold"), command = savedata)
btn.grid(row=4, column=1, pady = 20)



app.mainloop()
