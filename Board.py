import sys #importing needed libaries
from tkinter import *

#set the canvas as a variable
board = Tk()
spacing = 60
#Front page of game and place to select options
def welcomeBoard(): 
    board.geometry("400x400+400+300") #setting size of window and where on the screen to open it
    board.title("Connect Four") #title of the window show on the bar
    gameTitle = Label(board, text="Connect Four", font=(None, 35)) # Title of the game as a label
    gameTitle.pack()
    play = Button(board,text="PLAY", height = 2 , width = 12,bg="#8dd1e8", command=gameBoard)#Play button ---using place instead of pack 
    play.place(x=155,y=290)#because it allows for a more precisie location

    #exit option to close game
    exitboard=Button(board,text="EXIT",height = 2 , width = 12,bg="#e2062b", command=board.destroy)
    exitboard.place(x=155,y=335)
    
    #player 1 and 2 labels
    player1 = Label(board,text="Player 1", font=(None,18))
    player1.place(x=2, y=100, anchor=W)
    player2 = Label(board,text="Player 2", font=(None,18))
    player2.place(x=300, y=100, anchor=W)

    #dropdown menus to select colors for PLAYER 2
    #making var1 a global so it can be used in another function
    global chipscolor1
    chipscolor1=StringVar(board)
    chipscolor1.set("Red")
    colors1=["Red","Black","Blue","Green","Yellow"]
    colors1 = OptionMenu(board,chipscolor1, *colors1,command=func1)
    colors1.place(x=300, y=180,anchor=W)
    colors1.config(textvariable=chipscolor1)
    
    #dropdown menus to select colors for PLAYER 1
    global chipscolor
    chipscolor=StringVar(board)
    chipscolor.set("Black")
    colors = ["Black","Red","Blue","Green","Yellow"]
    colors = OptionMenu(board,chipscolor, *colors,command=func)
    colors.place(x=5, y=180,anchor=W)
    
    #dropdown menu to select human or computer
    global playerOne
    playerOne=StringVar(board)
    playerOne.set("Human")
    firstplayer = ["Human","Computer"]
    firstplayer = OptionMenu(board,playerOne, *firstplayer)
    firstplayer.place(x=5,y=130)

    #dropdown menu to select human or computer
    global playerTwo
    playerTwo=StringVar(board)
    playerTwo.set("Human")
    secondplayer = ["Human","Computer"]
    secondplayer = OptionMenu(board,playerTwo, *secondplayer)
    secondplayer.place(x=300,y=130)
    
    #Making it clearer on selecting difficulty
    difficulty = Label(board,text="< - - - Select Difficulty - - - >",font=(None,12))
    difficulty.place(x=100,y=220)

    #dropdown menu for difficulty selection PLAYER 1
    difficultyMode=StringVar(board)
    difficultyMode.set("Easy")
    difficult=["Easy","Meduim","Advanced"]
    difficult=OptionMenu(board,difficultyMode,*difficult)
    difficult.place(x=5,y=215)

    #dropdown menu for difficulty selection PLAYER 2
    difficultyMode1=StringVar(board)
    difficultyMode1.set("Easy")
    difficult1=["Easy","Meduim","Advanced"]
    difficult1=OptionMenu(board,difficultyMode1,*difficult1)
    difficult1.place(x=300,y=215)

    #Label to explain instruction to start the game
    instructions = Label(board, text="Select game options then click PLAY",font=(None,12))
    instructions.place(x=80, y=380)

    gridoption=Label(board,text="Select grid size", font=(None,12))
    gridoption.place(x=140,y=130)

    global sizes
    sizes=StringVar(board)
    sizes.set("6x7")
    gridsize=["4x5","5x6","6x7","7x8","8x9"]
    gridsize=OptionMenu(board,sizes,*gridsize)
    gridsize.place(x=170,y=160)


#show chip color before game, while changing
#getting value from optionmenu and saving into a var
#then adding that to ".gif" to open the image and display
    
def func(ballcolor):
    
    ballcolor=(chipscolor.get())
    photos = PhotoImage(file=ballcolor + ".gif")
    gif = Label(board,image=photos)
    gif.image=photos
    gif.place(x=2,y=290)
    return
def func1(ballcolor1):
    global gif1
    
    ballcolor1=(chipscolor1.get())
    photos = PhotoImage(file=ballcolor1 + ".gif")
    gif1 = Label(board,image=photos)
    gif1.image=photos
    gif1.place(x=320,y=290)


#Game board functions
def gameBoard():
    global top
    global top1
    top = Toplevel()
    top.title("Connect Four")     
    top.geometry("1000x800") #setting size of window and where on the screen to open it
    top1=Canvas (top, width=700, height=700)
    top1.pack()
    #get selected option from dropdown to create grid
    #convert the string to integer
    row_col=(sizes.get())
    row_s=row_col[0]
    col_s=row_col[2]
    l_rows=int(row_s)
    e_cols=int(col_s)

    #get the players into a label to display
    playertype = (playerOne.get())
    playertype1 = (playerTwo.get())
    players = Label(top, text=playertype + " VS " +playertype1, font=(None,12))
    players.place(x=340,y=520)


    #display chipcolors to show who is who
    ballcolor=(chipscolor.get())
    ballcolor1=(chipscolor1.get())
    photos = PhotoImage(file=ballcolor + ".gif")
    photos1=PhotoImage(file=ballcolor1+ ".gif")
    gif = Label(top,image=photos)
    gif.image=photos
    gif.place(x=360,y=545)

    gif1 = Label(top,image=photos1)
    gif1.image=photos1
    gif1.place(x=420,y=545)

    #simple label saying who is player 1 and 2
    playerLabel = Label(top, text="Player 1",font=(None,14))
    playerLabel1 = Label(top, text="Player 2",font=(None,14))
    playerLabel.place(x=330,y=485)
    playerLabel1.place(x=430,y=485)

    #actual grid being drawing, input also comes from selected drop down menu.
    for i in range(0,e_cols+1):
        top1.create_line((i+1)*spacing,spacing,(i+1)*spacing,(l_rows+1)*spacing)
        for i in range(0,l_rows+1):
            top1.create_line(spacing,(i+1)*spacing,\
                            spacing*(1+e_cols),(i+1)*spacing)

    #drop buttons
    drop = Button(top,text="DROP", command=playerTurn)
    drop.place(x=215,y=430)
    drop1 = Button(top,text="DROP", command=playerTurn)
    drop1.place(x=275,y=430)
    drop2 = Button(top,text="DROP", command=playerTurn)
    drop2.place(x=335,y=430)
    drop3 = Button(top,text="DROP", command=playerTurn)
    drop3.place(x=395,y=430)
    drop4 = Button(top,text="DROP", command=playerTurn)
    drop4.place(x=455,y=430)
    drop5 = Button(top,text="DROP", command=playerTurn)
    drop5.place(x=515,y=430)
    drop6 = Button(top,text="DROP", command=playerTurn)
    drop6.place(x=575,y=430)


    #restart option
    restart = Button(top, text="Restart", command=restartGame)   
    restart.place(x=365,y=2)
    
    #exit option
    exitgame=Button(top,text="Exit",command=top.destroy)
    exitgame.place(x=760,y=2)
    #save option into a txt format
    save=Button(top,text="Save",command=file_save)
    save.place(x=2,y=2)
    #save and exit
    saveandexit=Button(top,text="Save and Exit",command=save_exit)
    saveandexit.place(x=50,y=2)


#saving function, 'w' to write data to file  
def file_save():
    top.filename = filedialog.asksaveasfile(mode='w',defaultextension=".txt")
def save_exit():
    top.filename = filedialog.asksaveasfile(mode='w',defaultextension=".txt")
    top.destroy()
def restartGame():
    top.destroy()
    gameBoard()
#####swap between player 1 and player 2's turn but not work#######
def playerTurn():
    e=0
    if (e % 2 ==0):
        
        dropChip()
        e=e+1

    else:
        dropChip1()
        e=e+1


#drop the chip to grid
#by getting position of button clicked and places the chip where it was click + 130 of x and -85 of y
#save coordinate in coord_x and coord_y variable which are passed
def dropChip():
    global gif3
    x = top1.winfo_pointerx()
    y = top1.winfo_pointery()
    coord_x = top1.winfo_pointerx() - top1.winfo_rootx()
    coord_y = top1.winfo_pointery() - top1.winfo_rooty()
    #print(coord_x,coord_y)

    rounded_x=round(coord_x,-1)
    rounded_y=round(coord_y,-1)
    #print(rounded_x,rounded_y)
    
    ballcolor=(chipscolor.get())
    photos3 = PhotoImage(file=ballcolor + ".gif")
    gif3 = Label(top,image=photos3)
    gif3.image=photos3
    gif3.place(x=coord_x+130,y=coord_y-85)
    exi=gif3.winfo_exists()
    #print(exi)
def dropChip1():
    global gif4
    x = top1.winfo_pointerx()
    y = top1.winfo_pointery()
    coord_x = top1.winfo_pointerx() - top1.winfo_rootx()
    coord_y = top1.winfo_pointery() - top1.winfo_rooty()
    #print(coord_x,coord_y)

    #rounding the coordinate integers to try and give a more resonaable chip position
    rounded_x=round(coord_x,-1)
    rounded_y=round(coord_y,-1)
    #print(rounded_x,rounded_y)
        
    ballcolor1=(chipscolor1.get())
    photos4 = PhotoImage(file=ballcolor1 + ".gif")
    gif4 = Label(top,image=photos4)
    gif4.image=photos4
    gif4.place(x=coord_x+130,y=coord_y-85)
    exi=gif4.winfo_exists()
    #print(exi)

    


board.mainloop(welcomeBoard())
