import tkinter as tk
from tkinter import messagebox

def yes_clicked(): 
    root.destroy() #steng windu

def no_clicked():
    root.destroy() # steng windu

def exit_clicked():
    root.destroy()  # Close the window

#  laget windu
root = tk.Tk()
root.title("Albanian Virus")
root.geometry("420x200")

# tekst for popup
label = tk.Label(root, text="Hi, I am an Albanian virus but because of poor technology in my country unfortunately I am not able to harm your computer. "
"Please be so kind to delete one of your important files yourself and then forward me other users. "
"Many thanks for your cooperation! Best regards, Albanian virus", font=("Arial", 12, "bold"), wraplength=400, justify="center")


label.pack(pady=20, padx=20)


# knapper for steng etc
exit_button = tk.Button(root, text="Close", command=exit_clicked, width=5,)
exit_button.pack(side="right", padx=10, pady=10)

no_button = tk.Button(root, text="No", command=no_clicked, width=5,)
no_button.pack(side="right", padx=10, pady=10)

yes_button = tk.Button(root, text="Yes", command=yes_clicked, width=5,)
yes_button.pack(side="right", padx=10, pady=10)


# Run the pop-up
root.mainloop()
