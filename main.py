from tkinter import *

isSwapped = False
FT_TO_CM = 30.48
window = Tk()
window.title("Height Convertor")
window.minsize(width=270, height=100)
window.config(padx=20, pady=20)


def calculate():
    error_label.config(text="")
    try:
        if not isSwapped:
            cm = round(float(text_box.get()) / FT_TO_CM, 2)
            label_result.config(text=cm)
        else:
            ft = round(float(text_box.get()) * FT_TO_CM, 2)
            label_result.config(text=ft)
    except:
        error_label.config(text="Please Fill the fields")


def clear_results():
    label_result.config(text="0")
    text_box.delete(0, 'end')


def swap():
    clear_results()
    global isSwapped
    if not isSwapped:
        first_measure.config(text="Ft")
        second_measure.config(text="Cm")
        isSwapped = True

    else:
        first_measure.config(text="Cm")
        second_measure.config(text="Ft")
        isSwapped = False


text_box = Entry()
text_box.config(width=7, )
text_box.insert(string="0", index=1)

text_box.grid(row=1, column=2, padx=5)

first_measure = Label(text="Cm")
first_measure.grid(row=1, column=3)

label_equal = Label(text="is equal to")
label_equal.grid(row=2, column=1)

label_result = Label(text="0")
label_result.config(font=("Montserrat", 15, "bold"))
label_result.grid(row=2, column=2)

second_measure = Label(text="Ft")
second_measure.grid(row=2, column=3)

swap_button = Button(text="Swap", command=swap)
swap_button.grid(row=4, column=2)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=5, column=2)

error_label = Label(text="")
error_label.grid(row=6, column=2)

window.mainloop()
