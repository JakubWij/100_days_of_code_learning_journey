from tkinter import *
import time

# def button_clicked():
#     print("I got clicked")
#     new_text = input.get()
#     my_label.config(text=new_text)

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km converter")
# window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

# Label
# my_label = Label(text="I Am a Label", font=("Arial", 24, "italic"))
# my_label = Label(text="")
# my_label.grid(column=0, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

def timing_with_time():
    start = time.perf_counter()
    time.sleep(1)
    end = time.perf_counter()
    print(end - start)

timing_with_time()












window.mainloop()
