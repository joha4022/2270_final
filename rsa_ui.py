import tkinter as tk
from tkinter import filedialog
import rsa

# Create the main window
root = tk.Tk()
root.title("Extract")

# browse input or ouput xml
def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text files", "*.xml*"),("All files", "*.*")))
    if(filename):
        label1.configure(text="File opened: " + filename)


# Function to handle the encode button click
def encode():
    # get n and e value
    n, e = rsa.mini_rsa.search_encrypt()
    # create a popup window to provide n and e value
    top = tk.Toplevel(root)
    n_label = tk.Label(top, text="n value = {}".format(n))
    n_label.grid(row = 0, column=0, padx=5, pady=0, sticky='w')
    e_label = tk.Label(top, text="e value = {}".format(e))
    e_label.grid(row = 1, column=0, padx=5, pady=0, sticky='w')
    

def decode():
    # id = entry1.get()
    rsa.mini_rsa.search_encrypt()


# Function to handle the quit button click
def quit():
    root.destroy()

# Create and place the labels and entry fields
top_frame = tk.Frame(root, width = 100, height=100)
top_frame.grid(row=0, column=0, padx=5, pady=0, sticky='w')

label0 = tk.Label(top_frame, text="Click browse and find the .xml file")
label0.grid(row=0, column=0, padx=5, pady=0, sticky='w')
button_explore = tk.Button(top_frame, text='Browse', command=browseFiles)
button_explore.grid(row=1, column=0, padx=5, pady=0, sticky='w')

# label1 = tk.Label(top_frame, text="n:")
# label1.grid(row=1, column=0, padx=5, pady=0)

# entry1 = tk.Entry(top_frame)
# entry1.grid(row=1, column=1, padx=0, pady=0, sticky="w")

# label2 = tk.Label(top_frame, text="e:")
# label2.grid(row=2, column=0, padx=5, pady=0)

# entry2 = tk.Entry(top_frame)
# entry2.grid(row=2, column=1, padx=0, pady=0, sticky="w")

# Status box
mid_frame = tk.Frame(root, width = 100, height=10)
mid_frame.grid(row=1, column=0, padx=5, pady=0)
label1 = tk.Label(mid_frame, text="")
label1.grid(row=0, column=1, padx=5, pady=0)

# Create and place the buttons
bottom_frame = tk.Frame(root, width = 100, height=10)
bottom_frame.grid(row=2, column=0, padx=5, pady=0)

encode_button = tk.Button(bottom_frame, text="Encode", command=encode)
encode_button.grid(row=0, column=0, padx=5, pady=5)

decode_button = tk.Button(bottom_frame, text="Decode", command=decode)
decode_button.grid(row=0, column=1, padx=5, pady=5)

quit_button = tk.Button(bottom_frame, text="Quit", command=quit)
quit_button.grid(row=0, column=2, padx=5, pady=5)

# Run the application
root.mainloop()
