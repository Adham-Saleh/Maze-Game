import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import sys
import pygame

pygame.mixer.init()


def start():
    pygame.mixer.music.load('start.mp3')
    pygame.mixer.music.play(loops=1)


def win():
    pygame.mixer.music.load('Yay.mp3')
    pygame.mixer.music.play(loops=1)


def on_move():
    pygame.mixer.music.load('move.mp3')
    pygame.mixer.music.play(loops=1)


def lose():
    pygame.mixer.music.load('lose.mp3')
    pygame.mixer.music.play(loops=1)


def enemyinteracting():
    pygame.mixer.music.load('slap.mp3')
    pygame.mixer.music.play(loops=1)


def hoob(self):
    player_coords = self.canvas.coords(self.player)
    for i in range(len(self.maze)):
        for j in range(17):
            if self.maze[i][j] == 1:
                self.canvas.create_rectangle(
                    player_coords[0], player_coords[1], player_coords[2], player_coords[3], fill='white', outline='white')
                self.player = self.canvas.create_oval(
                    player_coords[0], player_coords[1], player_coords[2], player_coords[3], fill='yellow')


global c
c = 0
root = tk.Tk()


def signup():
    root = tk.Tk()

    def signup():
        username = userNameEntry.get()
        email = emailEntry.get() + '\n'
        password = passwordEntry.get()
        if username and email and password:
            cardinals = [email, password]
            print(cardinals)
            cf = open(
                r'fileB\{}.txt'.format(username), 'w')
            cf.writelines(cardinals)
            root.destroy()
        else:
            errorLabel.config(text='You must write something..')

    root.title('Maze Game - Create an account')
    root.geometry('250x300')
    root.resizable(0, 0)
    root.iconbitmap('icon.png')

    titleLabel = tk.Label(root, text='Create New Account')
    titleLabel.pack(pady=(5, 10))

    errorLabel = tk.Label(root, text='')
    errorLabel.pack()

    username = tk.Label(root, text='create username:')
    username.pack()
    userNameEntry = tk.Entry(root, width=25)
    userNameEntry.pack(pady=(0, 10), ipadx=2, ipady=2)

    email = tk.Label(root, text='create email:')
    email.pack()
    emailEntry = tk.Entry(root, width=25)
    emailEntry.pack(pady=(0, 10), ipadx=2, ipady=2)

    password = tk.Label(root, text='create password:')
    password.pack()
    passwordEntry = tk.Entry(root, width=25)
    passwordEntry.pack(pady=(0, 10), ipadx=2, ipady=2)

    signupBut = tk.Button(root, text='Sign Up', command=signup)
    signupBut.pack()

    root.mainloop()


def login():
    openGame = False
    try:
        global username
        username = userNameEntry.get()
        email = emailEntry.get() + '\n'
        password = passEntry.get()
        checkcardinals = []
        check = open(
            r'fileB\{}.txt'.format(username), 'r')
        for lines in check:
            checkcardinals.append(lines)
        print(checkcardinals)
        if checkcardinals[0] == email and checkcardinals[1] == password:
            errorLabel.config(text='logged in successfully', bg='green')
            openGame = True
        else:
            errorLabel.config(text='wrong email or password', bg='red')
    except:
        errorLabel.config(text='username doesnt exist', bg='red')

    if openGame:
        start()

        def restartGame():
            python = sys.executable
            os.execl(python, python, *sys.argv)

        global healthi
        healthi = 3

        class MazeGame:
            def __init__(self, root):
                global healthi
                self.root = root
                self.root.title('Maze Game')
                self.root.geometry('505x600')
                self.canvas = tk.Canvas(
                    self.root, width=505, height=550, bg='white')
                self.canvas.pack()
                self.root.bind("<KeyPress>", self.move)
                self.health = tk.Label(
                    self.root, font=20, text="Health: {}".format(healthi), fg='green')
                self.health.pack(pady=(10, 0))

                self.maze()
                self.player()
                self.check_win()
                self.check_if_3green()
                self.check_if_2red()

            def maze(self):
                self.maze = [
                    [1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 0, 0, 1, 2, 0, 1, 0, 2, 1, 0, 3, 0, 1],
                    [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 'e'],
                    [1, 0, 2, 0, 1, 0, 0, 1, 0, 1, 3, 0, 0, 2, 1, 0, 'e'],
                    [1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 2, 1],
                    [1, 1, 0, 2, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
                    [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 3, 0, 1, 0, 1],
                    [1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 2, 1],
                    [1, 0, 1, 1, 2, 1, 2, 1, 0, 1, 0, 1, 2, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 3, 0, 1],
                    [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
                    [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 3, 1],
                    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 's', 0, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                ]

                for i in range(len(self.maze)):
                    for j in range(17):
                        if self.maze[i][j] == 1:
                            self.canvas.create_rectangle(
                                j*30, i*30, (j+1)*30, (i+1)*30, fill='black')  # (0*30, 0*30, 1*30, 1*30) (x1, y1, x2, y2)
                        elif self.maze[i][j] == 2:
                            global enemy
                            enemy = self.canvas.create_rectangle(
                                j*30, i*30, (j+1)*30, (i+1)*30, width=20, fill='red', outline='white')
                        elif self.maze[i][j] == 3:
                            self.canvas.create_rectangle(
                                j*30, i*30, (j+1)*30, (i+1)*30, width=20, fill='green', outline='white')

            def player(self):
                for i in range(len(self.maze)):
                    for j in range(17):
                        if self.maze[i][j] == 's':
                            self.player = self.canvas.create_oval(j*30, i*30, (j+1)*30,
                                                                  (i+1)*30, fill='yellow')

            def move(self, event):
                player_coords = self.canvas.coords(self.player)
                print(player_coords)
                player_row = int(player_coords[1] / 30)  # 15
                player_col = int(player_coords[0] / 30)  # 8

                if event.keysym == 'w' and player_row > 0 and self.maze[player_row - 1][player_col] != 1:
                    self.canvas.move(self.player, 0, -30)
                    on_move()

                if event.keysym == 's' and player_row < len(self.maze) - 1 and self.maze[player_row + 1][player_col] != 1:
                    self.canvas.move(self.player, 0, 30)
                    on_move()

                if event.keysym == 'a' and player_col > 0 and self.maze[player_row][player_col - 1] != 1:
                    self.canvas.move(self.player, -30, 0)
                    on_move()

                if event.keysym == 'd' and player_col < len(self.maze[0]) - 1 and self.maze[player_row][player_col + 1] != 1:
                    self.canvas.move(self.player, 30, 0)
                    on_move()

                self.check_win()
                self.check_if_3green()
                self.check_if_2red()

            def check_win(self):
                player_coords = self.canvas.coords(self.player)
                player_row = int(player_coords[1] / 30)
                player_col = int(player_coords[0] / 30)
                if self.maze[player_row][player_col] == 'e':
                    if c == 6:
                        win()
                        messagebox.showinfo(
                            'Congrants!', '{} Wins'.format(username))
                        root.destroy()

            def check_if_3green(self):
                global healthi
                player_coords = self.canvas.coords(self.player)
                player_row = int(player_coords[1] / 30)
                player_col = int(player_coords[0] / 30)
                if self.maze[player_row][player_col] == 3:
                    if healthi < 3:
                        healthi += 1
                        global c
                        c += 1
                        self.health.config(
                            text='Health: {}'.format(healthi))
                        self.maze[player_row][player_col] = 0
                        hoob(self)

            def check_if_2red(self):
                def res():
                    restartGame()
                global healthi
                player_coords = self.canvas.coords(self.player)
                player_row = int(player_coords[1] / 30)
                player_col = int(player_coords[0] / 30)
                if self.maze[player_row][player_col] == 2:
                    if healthi > 0:
                        enemyinteracting()
                        healthi -= 1
                        self.health.config(text='Health: {}'.format(healthi))
                        self.maze[player_row][player_col] = 0
                        hoob(self)
                    if healthi == 0:
                        lose()
                        self.health.config(
                            text='Health: {}'.format(healthi), fg='red')
                        self.canvas.delete('all')
                        loseLabel = tk.Label(
                            self.root, text='You have lost!', fg='red', font=50, bg='white')
                        loseLabel.place(x=200, y=275)
                        restartButton = tk.Button(
                            self.root, text='Restart', width=17, command=res)
                        restartButton.place(x=190, y=300)

        root = tk.Tk()
        game = MazeGame(root)
        root.mainloop()


root.title('Maze Game - Login page')
root.geometry('500x450')
img = tk.PhotoImage(file=r'icon.png')
root.iconphoto(False, img)
root.resizable(0, 0)

mazepng = tk.PhotoImage(file='Artboard 2.png')
imglab = tk.Label(root, image=mazepng)
imglab.pack(pady=(10, 0))

welcomeLabel = tk.Label(root, text='---Welcome to Maze Game---')
welcomeLabel.pack()

loginLabel = tk.Label(root, text='Login')
loginLabel.pack()

errorLabel = tk.Label(root, text='')
errorLabel.pack()

userNameLabel = tk.Label(root, text='username:')
userNameLabel.pack()
userNameEntry = tk.Entry(root, width=25)
userNameEntry.pack(pady=(0, 10), ipadx=2, ipady=2)

emailLabel = tk.Label(root, text='email:')
emailLabel.pack()
emailEntry = tk.Entry(root, width=25)
emailEntry.pack(ipadx=2, ipady=2)

passLabel = tk.Label(root, text='passwrod:')
passLabel.pack(pady=(10, 0))
passEntry = tk.Entry(root, width=25)
passEntry.pack(ipadx=2, ipady=2)

loginBut = tk.Button(root, text='Login', command=login)
loginBut.pack(pady=10)

askLabel = tk.Label(root, text='Dont have an account?')
askLabel.pack()

signUpBut = tk.Button(root, text='Sign up',  command=signup)
signUpBut.pack()

root.mainloop()
