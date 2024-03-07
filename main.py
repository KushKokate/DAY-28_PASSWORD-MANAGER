from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    messagebox.showinfo(title = "Welcome to Password Manager", message = "Are you sure you want to save ?")
    with open("data.txt", "a") as f:
        f.write(f"{website} | {email} | {password}\n")
    clear_fields()

def clear_fields():
    entry_website.delete(0, 'end')
    entry_email.delete(0, 'end')
    entry_password.delete(0, 'end')
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# label and entry for website textfield

label_web = Label(window, text="website:  ", font=("Italic", 15, "bold"))
label_web.grid(row=1, column =0)

entry_website = Entry(window, width=35)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()

# label and entry for email/username textfield

label_email = Label(window, text="Email/Username", font=("Italic", 15, "bold"))
label_email.grid(row=2, column =0)

entry_email = Entry(window, width =35)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(END, "kokatekush@gmial.com")

# label and entry for Password textfield

label_password = Label(window, text="Password: ", font=("Italic", 15, "bold"))
label_password.grid(row=3, column =0)

entry_password = Entry(window, width=21)
entry_password.grid(row=3, column=1)

# button for generate Password

button = Button(window, text="Generate Password")
button.grid(row=3, column=2)

# button for Add

button_add = Button(window, text="Add", width=35, command=save_password)
button_add.grid(row=4, column=1, columnspan=2)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column = 1)













window.mainloop()