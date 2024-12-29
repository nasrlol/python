import tkinter

class arithmatics: 
	def init(self,x):
		self.number_sequence = []
 

# LEFT TO DO:
# MAKE THE FUNCTIONS OF THE CLASS DISPLAY THE RESULT IN THE TEXTBOX 
# EVERYTHING WORKS EXECEPT FOR THE RESWULT 
# AND THEN WE WILL WORK ON THE TEXT FORMATTING OF THE CODE TO MAKE IT LOOK LIKE A REAL CALULCATOR AND ACTUALLY WORK


	def add(x,output_box):
		number_sequence = []  
		result = 0 
		number_sequence.append(x)  
		for i in number_sequence:  
			result += i 
		return result  

	def sub(x,output_box):
		number_sequence = []
		number_sequence_result = 0
		number_sequence.append(x)
		if len(number_sequence) > 2:
			for i in number_sequence:
				x = 0
				result = number_sequence[x] - number_sequence[x+1]
		return result

	def div(x,output_box):
		number_sequence = []
		number_sequence_result = 0
		number_sequence.append(x)
		if len(number_sequence) > 2:
			for i in number_sequence:
				x = 0
				result = number_sequence[x] / number_sequence[x+1]
		return result

	def mult(x,output_box):
		number_sequence = []
		number_sequence_result = 0
		number_sequence.append(x)
		if len(number_sequence) > 2:
			for i in number_sequence:
				x = 0
				result = number_sequence[x] * number_sequence[x+1]
		return result

	def div(x):
		number_sequence = []
		number_sequence_result = 0
		number_sequence.append(x)
		if len(number_sequence) > 2:
			for i in number_sequence:
				x = 0
				result = number_sequence[x] * number_sequence[x+1]
		return result

def display_text(x, output_text):
	if output_text == "=":
		calculation = x.get("1.0", tkinter.END)
		calculation_array = calculation.split("")
		for i in calculation_array: 
			try:
				i = int(i)  # Try to convert i to an integer
				numbers_array = []
				numbers_array.append(i)
			except ValueError:  # Catch only ValueError
				match i:
					case '+':
						i = arithmatics.add(numbers_array) # Assign a function for addition
					case '-':
						i = arithmatics.sub(numbers_array)  # Assign a function for subtraction
					case '*':
						i = arithmatics.mult(numbers_array)  # Assign a function for multiplication
					case '/':
						i = arithmatics.mult(numbers_array)  # Assign a function for division
					case _:
						raise ValueError(f"Unsupported operator or invalid input: {i}")
					

	else:
		x.insert(tkinter.END, output_text)
	root.mainloop

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

result = 0

# Output box
output_box = tkinter.Text(root, fg='grey', bg='white', height=4, width=35, borderwidth=5)
output_box.place(x=5, y=5)

# Define buttons with delayed execution
add_button = tkinter.Button(root, text='+', command=lambda: display_text(output_box, "+"), height=2, width=2, foreground="red")
add_button.place(x=10, y=100)

sub_button = tkinter.Button(root, text='-', command=lambda: display_text(output_box, "-"), height=2, width=2, foreground="red")
sub_button.place(x=10, y=150)

div_button = tkinter.Button(root, text=':', command=lambda: display_text(output_box, "/"), height=2, width=2, foreground="red")
div_button.place(x=10, y=200)

mult_button = tkinter.Button(root, text='x', command=lambda: display_text(output_box, "*"), height=2, width=2, foreground="red")
mult_button.place(x=10, y=250)

# Number buttons
number_buttons = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '=']
cox = 100
coy = 100

for index, num_text in enumerate(number_buttons):
    num_button = tkinter.Button(
        root, text=num_text, command=lambda num=num_text: display_text(output_box, num), height=2, width=2)
    num_button.place(x=cox, y=coy)
    cox += 50
    if (index + 1) % 3 == 0:
        cox = 100
        coy += 50

root.mainloop()