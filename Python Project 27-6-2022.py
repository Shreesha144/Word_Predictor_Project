from tkinter import *

root = Tk()
root.title('5Square - Word Predictor')
root.geometry("700x500")



# Create a Main company label
my_label = Label(root, text="5Square - Word Predictor",
	font=("Helvetica bold", 20), fg="red")

my_label.pack(pady=20)

# Create a label
my_label = Label(root, text="Start Typing...",
	font=("Helvetica bold", 18), fg="grey")

my_label.pack(pady=5)

# Create an entry box
my_entry = Entry(root, font=("Helvetica", 20),width=30)
my_entry.pack()

#Create frame and scrollbar
my_frame=Frame(root)
my_scrollbar=Scrollbar(my_frame,orient=VERTICAL)


# Create a listbox
my_list = Listbox(my_frame, width=70)



#Configuring scrollbar
my_scrollbar.config(width=15,command=my_list.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)
my_frame.pack()


my_list.pack(pady=15)


# Update the listbox
def update(data):
	# Clear the listbox
	my_list.delete(0,END)

	# Add toppings to listbox
	for item in data:
		my_list.insert(END,item)

# Update entry box with listbox clicked
def fillout(e):
	# Delete whatever is in the entry box
	my_entry.delete(0, END)

	# Add clicked list item to entry box
	my_entry.insert(0, my_list.get(ANCHOR))

# Create function to check entry vs listbox
def check(e):
	# grab what was typed
	typed = my_entry.get()

	if typed == '':
		data = toppings
	else:
		data = []
		for item in toppings:
			if typed.lower() in item.lower():
				data.append(item)

	# update our listbox with selected items
	update(data)				





# Create a list of 100 common words
toppings = ['a','about','all','also','and','as','at',
'be','because','but','by','can','come','could','day',
'do','even','find','first','for','from','get','give',
'go','have','he','her','here','him','his','how','I','if',
'in','into','it','its','just','know','like','look','make',
'man','many','me','more','my','new','no','not','now',
'of','on','one','only','or','other','our','out','people',
'say','see','she','so','some','take','tell','than','that',
'the','their','them','then','there','these','they','thing',
'think','this','those','time','to','two','up','use','very',
'want','way','we','well','what','when','which','who','will',
'with','would','year','you','your']

# Add the toppings to our list
update(toppings)

# Create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>", fillout)

# Create a binding on the entry box
my_entry.bind("<KeyRelease>", check)

root.mainloop()
