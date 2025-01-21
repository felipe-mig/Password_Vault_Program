from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import choice, randint, shuffle

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    # Picks random letters, symbols and numbers from the dictionary
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    
    # copy the generated password into the clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    website = website_entry.get()
    email = email_entry.get()    
    password = password_entry.get()
    
    
    # case the inputs are blank
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oh no!", message="Please, fill all the fields")
    else:    
        # Message box set up
        is_ok = messagebox.askokcancel(title="Confirm", message=f"These are the details entered: \nEmail: {email}" f"\nPassword: {password} \nwould you like to save?")
        
        if is_ok:
            # open a text file using append
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                #remove previous parameters
                website_entry.delete(0, END) # <-- removes from the 0 character until the end of the entry
                password_entry.delete(0, END)
            
        
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Vault")

# padding around the main content of the window
window.config(padx=50, pady=10)


# window size
canvas = Canvas(height=200, width=200)

# logo image
logo_img = PhotoImage(file="vault-logo.png")
canvas.create_image(100, 100, image=logo_img)

# grid to display elements
canvas.grid(row=0, column=1)


#LABELS:
website_label = Label(text="Website:")
# position on grid
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
# position on grid
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
# position on grid
password_label.grid(row=3, column=0)

signature_label = Label(text="© Felipe Iglesias")
signature_label.grid(row=6, column=0)


#INPUTS:
website_entry = Entry(width=48) # <-- width is a property related with the Entry no with the grid
# position on grid
website_entry.grid(row=1, column=1, columnspan=2, pady=5)
# where does the cursor starts
website_entry.focus()

email_entry = Entry(width=48)
# position on grid
email_entry.grid(row=2, column=1, columnspan=2)
# default email
email_entry.insert(0, "felipeTest1@gmail.com")

password_entry = Entry(width=31)
# position on grid
password_entry.grid(row=3, column=1, sticky=E, pady=5)


#BUTTONS:
generate_password_button = Button(text="Generate Password", command=generate_password) # <-- triggers the  generate_password function when pressing the button 
# position on grid
generate_password_button.grid(row=3, column=2, sticky=E, pady=5)

add_button = Button(text="Add", width=41, command=save)
# position on grid
add_button.grid(row=4, column=1, columnspan=2, pady=20)









# Without this tkinter won't show results. It's basically looping through the program and every millisecond is checking to see: did
# something happen, did something happen, did something happen?
window.mainloop()
