import tkinter

# Initiate tkinter 
root = tkinter.Tk()

# Set the display configurations
root.title("Calculator")
root.resizable(width = False, height = False)

w = 275 # width for the Tk root
h = 300 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# Output box
output_box = tkinter.Text(root, fg='grey', bg='white', height=4, width=35, borderwidth=5)
output_box.place(x=5, y=5)

def add(num):
	sequence = []
	sequence.append(num)

	for i in sequence:
		result += i
	return result

def sub(num):
	sequence = []
	sequence.append(num)

	if len(sequence) >= 2:
		for i in range(len(sequence)):
			if i == 0:
				continue
			else:
				sequence[0] -= sequence[i]
	return sequence[0]

def div(num):
	sequence = []
	sequence.append(num)

	if len(sequence) >= 2:
		for i in range(len(sequence)):
			if i == 0:
				continue
			else:
				sequence[0] /= sequence[i]
	return sequence[0]

def mult(nmu):
    sequence = []
    sequence.append(num)

    if len(sequence) >= 2:
        for i in range(len(sequence)):
            if i == 0:
                continue
            else:
                sequence[0] *= sequence[i]
    return sequence[0]


def calculate(box, text):

    if text == "=":

        input_string = box.get("1.0", tkinter.END)
        input_array = input_string.split("")

        num_array = []
        operator_array = []
        for i in calculation_array:
            try:
                i = int(i)  # Try to convert i to an integer
                num_array.append(i)
            except ValueError:
                pass
    else:
        box.insert(tkinter.END, text)

# Define buttons with delayed execution
add_button = tkinter.Button(root, text='+', command=lambda: calculate(output_box, "+"), height=2, width=2, foreground="red")
add_button.place(x=10, y=100)

sub_button = tkinter.Button(root, text='-', command=lambda: calculate(output_box, "-"), height=2, width=2, foreground="red")
sub_button.place(x=10, y=150)

div_button = tkinter.Button(root, text=':', command=lambda: calculate(output_box, "/"), height=2, width=2, foreground="red")
div_button.place(x=10, y=200)

mult_button = tkinter.Button(root, text='x', command=lambda: calculate(output_box, "*"), height=2, width=2, foreground="red")
mult_button.place(x=10, y=250)

# Number buttons
number_buttons = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '=']
cox = 100
coy = 100

for index, num_text in enumerate(number_buttons):
    num_button = tkinter.Button(
            root, text=num_text, command=lambda: output_box.insert(tkinter.END, num_text), height=2, width=2)
    num_button.place(x=cox, y=coy)
    cox += 50
    if (index + 1) % 3 == 0:
        cox = 100
        coy += 50

root.mainloop()
