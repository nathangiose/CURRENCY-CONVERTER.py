# Nathan John Giose
# First we will install everything from tkinter
# Then we will import requests


from tkinter import *
import requests
# Let's start with the design of the GUI


root = Tk()
root.title("Currency Converter")
root.geometry("500x400")
root.config(bg="Black")

value = StringVar()
StringVar = IntVar()
# Retrieving the information from an external JSON file as a source of reference


information = requests.get('https://v6.exchangerate-api.com/v6/3b6104d9c62069d198e73219/latest/USD')
information_json = information.json()

conversion_rate = information_json['conversion_rates']
print(conversion_rate)


# Creating a label and entry for the results


value_label = Label(root, text="Value", font=("Arial", 20))
value_label.pack()

value_entry = Entry(root, textvariable=value, width=40)
value_entry.pack()

# Creating the FROM (Standard value is USD)


from_label = Label(root, text="From: USD", font=("Arial", 20))
from_label.pack()

# Doing the Conversion of the data with its loop


convert = Label(root, text="TO:", font=("Arial", 20))
convert.pack()

convert_list = Listbox(root, width=20)
for i in conversion_rate.keys():
    convert_list.insert(END, str(i))
convert_list.pack()

convert_label = Label(root, text="Converted to: ", font=("Arial", 20))
convert_label.pack()


def convert_curr():
    num = float(value_entry.get())
    print(information_json['conversion_rates'][convert_list.get(ACTIVE)])
    ans = num * information_json['conversion_rates'][convert_list.get(ACTIVE)]
    convert_label['text'] = ans


convert_btn = Button(root, command=convert_curr, text="CONVERT", font=("Arial", 20), width=20)
convert_btn.pack()


root.mainloop()
