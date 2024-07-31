import tkinter as tk
from tkinter import filedialog
import rsa

# browse input or ouput xml
def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text files", "*.xml*"),("All files", "*.*")))
    if(filename):
        label1.configure(text="File opened: " + filename)


# Function to handle the start button click
def start():
    # id = entry1.get()
    rsa.mini_rsa.search_encrypt()


# Function to handle the quit button click
def quit():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Extract")

# Create and place the labels and entry fields
top_frame = tk.Frame(root, width = 100, height=100)
top_frame.grid(row=0, column=0, padx=5, pady=0, sticky='w')

label0 = tk.Label(top_frame, text="Click browse and find the .xml file")
label0.grid(row=0, column=0, padx=0, pady=0, sticky='w')
button_explore = tk.Button(top_frame, text='Browse', command=browseFiles)
button_explore.grid(row=1, column=0, padx=0, pady=0, sticky='w')

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
mid_frame.grid(row=1, column=0, padx=5, pady=(10,0))
label1 = tk.Label(mid_frame, text="", fg="blue")
label1.grid(row=0, column=1, padx=5, pady=0)

# Create and place the buttons
bottom_frame = tk.Frame(root, width = 100, height=10)
bottom_frame.grid(row=2, column=0, padx=5, pady=5)

encode_button = tk.Button(bottom_frame, text="Encode", command=start)
encode_button.grid(row=0, column=0, padx=20, pady=5)

decode_button = tk.Button(bottom_frame, text="Encode", command=start)
decode_button.grid(row=0, column=1, padx=20, pady=5)

quit_button = tk.Button(bottom_frame, text="Quit", command=quit)
quit_button.grid(row=0, column=2, padx=20, pady=5)

# Run the application
root.mainloop()
