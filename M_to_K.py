from tkinter import *

# Define a window
window = Tk()
window.title("First Build")
window.minsize(width= 500, height= 500)
window.config(padx=30, pady=30)

#Entry
miles_input = Entry(width=10)
miles_input.insert(0,"1")
miles_input.grid(column=1, row=0 )


#Label
my_label = Label(text="Miles", font=("Arial", 24, "bold"))
my_label.grid(column=2, row=0)
my_label.config(padx=50, pady=50)

#Label
my_label0 = Label(text="is equal to", font=("Arial", 24, "bold"))
my_label0.grid(column=0, row=1)
my_label0.config(padx=50, pady=50)

#Label
my_label1 = Label(text="0", font=("Arial", 24, "bold"))
my_label1.grid(column=1, row=1)
my_label1.config(padx=50, pady=50)

#Label
my_label2 = Label(text="Km", font=("Arial", 24, "bold"))
my_label2.grid(column=2, row=1)
my_label2.config(padx=50, pady=50)




def button_clicked():
   miles = float(miles_input.get())
   km = miles*1.609
   my_label1.config(text=f"{km:.2f}")

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)











window.mainloop()