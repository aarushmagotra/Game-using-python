import tkinter as tk


def hi():
    name_screen.destroy()

name_screen = tk.Tk()
name_screen.title("Enter Names")
name_screen.configure(bg="grey")

name_screen.geometry("600x400")
name_screen.minsize(600, 400)
name_screen.maxsize(600, 400)

# text_frame = tk.Frame(name_screen)
# text_frame.grid(row=20, column=10)

entry_text = tk.Label(text="Enter Names:", font=("Courier", 25), bg="grey")
entry_text.pack(pady=50, padx=150)

player1_var = tk.StringVar()
player2_var = tk.StringVar()

player_text1 = tk.Label(text="Enter player 1 name:", bg="grey", font=("Arial", 15, "italic"))
player_text1.pack()

player1_Name = tk.Entry(text="enter",width=40, bd=6, relief="flat", textvariable=player1_var)
player1_Name.pack(pady=10)


player_text2 = tk.Label(text="Enter player 2 name:", bg="grey", font=("Arial", 15, "italic"))
player_text2.pack()

player2_Name = tk.Entry(text="enter",width=40, bd=6, relief="flat", textvariable=player2_var)
player2_Name.pack(pady=10)


button_name = tk.Button(name_screen, text='Play', width=10, height=1, bg='white', fg='#000000', activebackground='#66ff66', font=("arial", 12, "bold italic"), relief="flat", command=hi)
button_name.pack(pady=7)

foot_name = tk.Label(name_screen, text="Made By ~ Muteen, Aarush & Arjun", font=("Courier", 12 , "italic underline"), bg="grey")
foot_name.pack(side="bottom", anchor="e")

name_screen.mainloop()

def playerNames():
    player1_name = player1_Name.get()
    player2_name = player2_Name.get()
    
    return(player1_name, player2_name)
a = playerNames()
print(a)
