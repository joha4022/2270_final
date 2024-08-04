import tkinter as tk
from tkinter import filedialog
import rsa

# Create the main window
root = tk.Tk()
root.title("Extract")
xml_filename = ""

# browse input or ouput xml
def browseFiles():
    global xml_filename
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=((".xml files", "*.xml"),("All files", "*.*")))
    if(filename):
        label1.configure(text="File opened: " + filename)
        xml_filename = filename.split("/")[len(filename.split("/"))-1]


# Function to handle the encode button click
def encode():
    if(xml_filename):
        # get n and e value
        n, e, e_filename = rsa.search_encrypt(xml_filename)
        # create a popup window to provide n and e value
        top = tk.Toplevel(root)
        n_label = tk.Label(top, text="n value: {}".format(n))
        n_label.grid(row = 0, column=0, padx=(5,0), pady=0, sticky='w')
        e_label = tk.Label(top, text="e value: {}".format(e))
        e_label.grid(row = 1, column=0, padx=(5,0), pady=0, sticky='w')
        text_label = tk.Label(top, text="output file name: {}".format(e_filename))
        text_label.grid(row = 2, column=0, padx=(5,0), pady=0, sticky='w')
        popup_close = tk.Button(top, text='Close', command=lambda: quit(top))
        popup_close.grid(row = 3, column=0, padx=0, pady=(0,5))
        
    

def decode():
    if(xml_filename):
        top = tk.Toplevel(root)

        first_row = tk.Frame(top, width=100, height=100)
        first_row.grid(row=0, column=0, padx=5, pady=0)
        n_label = tk.Label(first_row, text="n value:")
        n_label.grid(row = 0, column=0, padx=0, pady=0)
        n_input = tk.Entry(first_row)
        n_input.grid(row = 0, column=1, padx=0, pady=0)

        e_label = tk.Label(first_row, text="e value:")
        e_label.grid(row = 1, column=0, padx=0, pady=0)
        e_input = tk.Entry(first_row)
        e_input.grid(row = 1, column=1, padx=0, pady=0)

        second_row = tk.Frame(top, width=100, height=100)
        second_row.grid(row=1, column=0, padx=0, pady=5)
        popup_decode = tk.Button(second_row, text='Decode', command=lambda: rsa.decode_and_build(xml_filename, n_input.get(), e_input.get()))
        popup_decode.grid(row = 0, column=0, padx=0, pady=0)
        popup_close = tk.Button(second_row, text='Close', command=lambda: quit(top))
        popup_close.grid(row = 0, column=1, padx=0, pady=0)



# Function to handle the quit button click
def quit(n):
    n.destroy()

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

quit_button = tk.Button(bottom_frame, text="Close", command=lambda: quit(root))
quit_button.grid(row=0, column=2, padx=5, pady=5)

# Run the application
root.mainloop()
