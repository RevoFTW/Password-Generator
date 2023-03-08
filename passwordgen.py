import random
import string
from tkinter import *
from tkinter import messagebox

def generate_password():
    # Get password length and website name from user
    length = int(entry_length.get())
    website = entry_website.get()

    # Generate a random password
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))

    # Display the password in a message box
    messagebox.showinfo("Password Generated", f"Your password for {website} is:\n\n{password}")

    # Save the password to a text file
    with open("passwords.txt", "a") as file:
        file.write(f"{website}: {password}\n")

# Create a GUI window
window = Tk()
window.geometry("400x200") # Set the window size
window.title("Password Generator")

# Create input fields for password length and website name
label_length = Label(window, text="Password Length:")
label_length.grid(row=0, column=0, padx=10, pady=10) # Add padx and pady options
entry_length = Entry(window)
entry_length.grid(row=0, column=1, padx=10, pady=10) # Add padx and pady options

label_website = Label(window, text="Website:")
label_website.grid(row=1, column=0, padx=10, pady=10) # Add padx and pady options
entry_website = Entry(window)
entry_website.grid(row=1, column=1, padx=10, pady=10) # Add padx and pady options

# Create a button to generate password
button_generate = Button(window, text="Generate Password", command=generate_password)
button_generate.grid(row=2, column=0, columnspan=2, padx=10, pady=10) # Add padx and pady options
button_generate.config(width=20) # Increase button width

# Run the window loop
window.mainloop()
