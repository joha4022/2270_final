import tkinter as tk
import rsa

# Function to handle the start button click
def start():
    id = entry1.get()

    rsa.Mini_E.main(id)
    

# Function to handle the quit button click
def quit():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Extract")

# Create and place the labels and entry fields
top_frame = tk.Frame(root, width = 100, height=100)
top_frame.grid(row=0, column=0, padx=5, pady=0)

label1 = tk.Label(top_frame, text="ID:")
label1.grid(row=0, column=0, padx=5, pady=0)

entry1 = tk.Entry(top_frame)
entry1.grid(row=0, column=1, padx=0, pady=0)

# Status box
mid_frame = tk.Frame(root, width = 100, height=10)
mid_frame.grid(row=1, column=0, padx=5, pady=(10,0))
label3 = tk.Label(mid_frame, text="Fill in the ID and click 'Convert'")
label3.grid(row=0, column=0 )


# Create and place the buttons
bottom_frame = tk.Frame(root, width = 100, height=10)
bottom_frame.grid(row=2, column=0, padx=5, pady=5)

start_button = tk.Button(bottom_frame, text="Convert", command=start)
start_button.grid(row=0, column=0, padx=20, pady=5)

quit_button = tk.Button(bottom_frame, text="Quit", command=quit)
quit_button.grid(row=0, column=1, padx=20, pady=5)

# Run the application
root.mainloop()
