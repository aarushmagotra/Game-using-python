import tkinter as tk

start_var = 0

def quitGame():
    exit()

def game(p1=1, p2=1):
    print(p1, p2)

def playerNames():
    player1_name = player1_Name.get()
    player2_name = player2_Name.get()
    name_screen.destroy()
    if len(player1_name) != 0 and len(player2_name) != 0:    
        game(player1_name, player2_name)
    elif len(player1_name) == 0 and len(player2_name) != 0:
        game(p2=player2_name)
    elif len(player2_name) == 0 and len(player1_name) != 0:
        game(p1=player1_name)

def names():
    global start_var

    if start_var == 0:
        start_var += 1
        start_screen.destroy()
    else:
        end_screen.destroy()

name_screen = tk.Tk()
name_screen.title("Enter Names:")
name_screen.configure(bg="grey")

name_screen.geometry("600x400")
name_screen.minsize(600, 400)
name_screen.maxsize(600, 400)


entry_text = tk.Label(text="Enter Names:", font=("Courier", 25), bg="grey")
entry_text.pack(pady=50, padx=150)

player1_var = tk.StringVar()
player2_var = tk.StringVar()

player_text1 = tk.Label(text="Enter player 1 name:", bg="grey", font=("Arial", 15, "italic"))
player_text1.pack()

player1_Name = tk.Entry(width=40, bd=6, relief="flat", textvariable=player1_var)
player1_Name.pack(pady=10)

player_text2 = tk.Label(text="Enter player 2 name:", bg="grey", font=("Arial", 15, "italic"))
player_text2.pack()

player2_Name = tk.Entry(width=40, bd=6, relief="flat", textvariable=player2_var)
player2_Name.pack(pady=10)

button_name = tk.Button(name_screen, text='Play', width=10, height=1, bg='white', fg='#000000', activebackground='#66ff66', font=("arial", 12, "bold italic"), relief="flat", command=playerNames)
button_name.pack(pady=7)

foot_name = tk.Label(name_screen, text="Made By ~ Muteen, Aarush & Arjun", font=("Courier", 12 , "italic underline"), bg="grey")
foot_name.pack(side="bottom", anchor="e")

name_screen.mainloop()




start_screen = tk.Tk(className=" PONG MENU")
start_screen.configure(bg="grey")
start_screen.geometry("600x400")
start_screen.minsize(600, 400)
start_screen.maxsize(600, 400)

head_start = tk.Label(start_screen, text = "PONG MENU", bg="grey", pady=50) 
head_start.config(font =("Courier", 35)) 
head_start.pack()

button1_start = tk.Button(start_screen, text='Play', width=40, height=2, bg='white', fg='#000000', activebackground='#66ff66', font=("arial", 12, "bold italic"), command = names, relief="flat")
button1_start.pack()

button2_start = tk.Button(start_screen, text='Difficulty', width=40, height=2, bg='white', fg='#000000', activebackground='#ff9933', font=("arial", 12, "bold italic"), relief="flat")
button2_start.pack(pady=10)

button3_start = tk.Button(start_screen, text='Exit', width=40, height=2, bg='white', fg='#000000', activebackground='#ff355e', font=("arial", 12, "bold italic"), command = quitGame, relief="flat")
button3_start.pack()

foot_start = tk.Label(start_screen, text="Made By ~ Muteen, Aarush & Arjun", font=("Courier", 12 , "italic underline"), bg="grey")
foot_start.pack(side="bottom", anchor="e")

start_screen.mainloop()


while True:
    end_screen = tk.Tk()
    end_screen.title("GAME OVER!!!")
    end_screen.configure(bg="grey")
    end_screen.geometry("600x400")
    end_screen.minsize(600, 400)
    end_screen.maxsize(600, 400)

    head_end = tk.Label(end_screen, text = "PONG MENU", bg="grey", pady=50) 
    head_end.config(font =("Courier", 35)) 
    head_end.pack()

    button1_end = tk.Button(end_screen, text='Play Again', width=40, height=2, bg='white', fg='#000000', activebackground='#66ff66', font=("arial", 12, "bold italic"), command = names, relief="flat")
    button1_end.pack()

    button2_end = tk.Button(end_screen, text='Difficulty', width=40, height=2, bg='white', fg='#000000', activebackground='#ff9933', font=("arial", 12, "bold italic"), relief="flat")
    button2_end.pack(pady=10)

    button3_end = tk.Button(end_screen, text='Exit', width=40, height=2, bg='white', fg='#000000', activebackground='#ff355e', font=("arial", 12, "bold italic"), command = quitGame, relief="flat")
    button3_end.pack()

    foot_end = tk.Label(end_screen, text="Made By ~ Muteen, Aarush & Arjun", font=("Courier", 12 , "italic underline"), bg="grey")
    foot_end.pack(side="bottom", anchor="e")

    end_screen.mainloop()