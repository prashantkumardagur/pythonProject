from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import json

#------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------

# First Game... Quiz .


# loading of  questions and answer choices from json file instead of the using lists
with open('./data.json', encoding="utf8") as f:
    data = json.load(f)

# convert the dictionary in lists of questions and answers
questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]

answers = [1,1,1,1,3,1,0,1,3,3] #list of all the correct answer index values

user_answer = []
indexes = []

ques = 1
lblQuestion=0
r1=0
r2=0
r3=0
r4=0

def theQuizGame():

    def gen():
        global indexes
        while(len(indexes) < 5):
            x = random.randint(0,9) # random function to give questions in a random order
            if x in indexes:
                continue
            else:
                indexes.append(x) 

    # RESULT PART******************************************************
    def showresult(score):
        lblQuestion.destroy()
        r1.destroy()
        r2.destroy()            # destroying the question and opts to show the result
        r3.destroy()
        r4.destroy()
        labelimage = Label(
            root,
            background = "#ffffff",
            border = 0,
        )
        labelimage.pack(pady=(50,30))
        labelresulttext = Label(
            root,
            font = ("Consolas",20),
            background = "#ffffff",
        )
        labelresulttext.pack()
        if score >= 20:         # using nested if else to give scoring according to the number of questions he answered correct
            img = PhotoImage(file="great.png")
            labelimage.configure(image=img)
            labelimage.image = img
            labelresulttext.configure(text="You Are Excellent !!")
        elif (score >= 10 and score < 20):
            img = PhotoImage(file="ok.png")
            labelimage.configure(image=img)
            labelimage.image = img
            labelresulttext.configure(text="You Can Be Better !!")
        else:
            img = PhotoImage(file="bad.png")
            labelimage.configure(image=img)
            labelimage.image = img
            labelresulttext.configure(text="You Should Work Hard !!")

    # calculation the marks he scored by giving each correct answer 5 marks 
    def calc():
        global indexes,user_answer,answers
        x = 0
        score = 0
        for i in indexes:
            if user_answer[x] == answers[i]:
                score = score + 5
            x += 1
        print("your score is :",score)
        showresult(score)


    #function to select and add all the options selected by user 
    def selected():
        global radiovar,user_answer
        global lblQuestion,r1,r2,r3,r4
        global ques
        x = radiovar.get()
        user_answer.append(x) #appending all the answers to the list
        radiovar.set(-1)
        if ques < 5:
            lblQuestion.config(text= questions[indexes[ques]])  #showing the next question 
            r1['text'] = answers_choice[indexes[ques]][0]
            r2['text'] = answers_choice[indexes[ques]][1]
            r3['text'] = answers_choice[indexes[ques]][2]
            r4['text'] = answers_choice[indexes[ques]][3]
            ques += 1
        else:
            
            calc() #when questions end then this statement will pass and the result will be calculated
        



    # function to start displaying all the questions when it is called after pressing the start button.
    def startquiz():
        global lblQuestion,r1,r2,r3,r4
        #lable to view the question
        lblQuestion = Label(
            root,
            text = questions[indexes[0]],
            font = ("Consolas", 16),
            width = 500,
            justify = "center",
            wraplength = 400,
            background = "#ffe6ea",
        )
        lblQuestion.pack(pady=(100,30))

        global radiovar
        radiovar = IntVar()
        radiovar.set(-1)
        #radio button for first option
        r1 = Radiobutton(
            root,
            text = answers_choice[indexes[0]][0],
            font = ("Times", 12),
            value = 0,
            variable = radiovar, 
            command = selected, # after selecting the option selected function is called and will show the next option
            background = "#ffe6ea",
        )
        r1.pack(pady=5)
        #radio button for second option
        r2 = Radiobutton(
            root,
            text = answers_choice[indexes[0]][1],
            font = ("Times", 12),
            value = 1,
            variable = radiovar,
            command = selected,  # after selecting the option selected function is called and will show the next option
            background = "#ffe6ea",
        )
        r2.pack(pady=5)
        #radio button for third option
        r3 = Radiobutton(
            root,
            text = answers_choice[indexes[0]][2],
            font = ("Times", 12),
            value = 2,
            variable = radiovar,
            command = selected,  # after selecting the option selected function is called and will show the next option
            background = "#ffe6ea",
        )
        r3.pack(pady=5)
        #radio button for fourth option
        r4 = Radiobutton(
            root,
            text = answers_choice[indexes[0]][3],
            font = ("Times", 12),
            value = 3,
            variable = radiovar,
            command = selected,  # after selecting the option selected function is called and will show the next option
            background = "#ffe6ea",
        )
        r4.pack(pady=5)
        
    #SINGLE WINDOW GUI
    #so i thought of making a function which destroys everything on the page when called and shows new content or the next question
    def startIspressed():
        labelimage.destroy()
        labeltext.destroy()
        lblInstruction.destroy()
        lblRules.destroy()
        btnStart.destroy()
        gen()
        startquiz() #start quiz function is called after everything is destroyed and questions will appear


    #home page allignments ************************************************************* 
    root = Tk()
    root.title("Quizmaster") # adding title
    root.geometry("700x600")
    root.config(background="#ffffff")
    root.resizable(0,0)

    bgImage= PhotoImage(file=r"nd.png") # adding bg image
    Label(root,image = bgImage).place(relwidth=1,relheight=1)


    img1 = PhotoImage(file="transparentGradHat.png") 
    # lable to view logo
    labelimage = Label(root,image = img1)
    labelimage.pack(pady=(40,0))

    # lable to view name of the quiz
    labeltext = Label(
        root,
        text = "Quiz Master", 
        font = ("Comic sans MS",28,"bold"),
        background="#ffffff"
        
    )
    labeltext.pack(pady=(0,50))

    img2 = PhotoImage(file="Frame.png")
    #start button
    btnStart = Button(
        root,
        image = img2,
        relief = FLAT,
        border = 0,
        command = startIspressed,
    )
    btnStart.pack()

    #lable to make the user view about the instructions
    lblInstruction = Label(
        root,
        text = "Read The Rules And\nClick Start Once You Are ready",
    
        font = ("Consolas",14,"bold"),
        justify = "center",
        background="#ffffff"
        
    )
    lblInstruction.pack(pady=(10,100))
    #lable to view the rules of the game
    lblRules = Label(
        root,
        text = " =>This quiz contains 10 questions\n =>You will get 20 seconds to solve a question\n =>Once you select a radio button that will be a final choice\nhence think before you select",
        width = 100,
        font = ("Times",14,"bold"),
        background = "#ffffff",
        foreground = "#DB7093",
    )
    lblRules.pack()
    root.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------

# Second game TIC TAC TOE

turn = 1 #For first person turn.
flag=1

def theTicTacToe():
    window=Tk()

    window.title("Welcome to The Gaming world TIC-Tac-Toe ")
    window.geometry("400x300")

    lbl=Label(window,text="Tic-tac-toe Game",font=('Helvetica','15'))
    lbl.grid(row=0,column=0)
    lbl=Label(window,text="Player 1: X",font=('Helvetica','10'))
    lbl.grid(row=1,column=0)
    lbl=Label(window,text="Player 2: O",font=('Helvetica','10'))
    lbl.grid(row=2,column=0)

    def clicked1():
        global turn
        if btn1["text"]==" ":   #For getting the text of a button
            if turn==1:
                turn =2
                btn1["text"]="X"
            elif turn==2:
                turn=1
                btn1["text"]="O"
            check()
    def clicked2():
        global turn
        if btn2["text"]==" ":
            if turn==1:
                turn =2
                btn2["text"]="X"
            elif turn==2:
                turn=1
                btn2["text"]="O"
            check()
    def clicked3():
        global turn
        if btn3["text"]==" ":
            if turn==1:
                turn =2
                btn3["text"]="X"
            elif turn==2:
                turn=1
                btn3["text"]="O"
            check()
    def clicked4():
        global turn
        if btn4["text"]==" ":
            if turn==1:
                turn =2
                btn4["text"]="X"
            elif turn==2:
                turn=1
                btn4["text"]="O"
            check()
    def clicked5():
        global turn
        if btn5["text"]==" ":
            if turn==1:
                turn =2
                btn5["text"]="X"
            elif turn==2:
                turn=1
                btn5["text"]="O"
            check()
    def clicked6():
        global turn
        if btn6["text"]==" ":
            if turn==1:
                turn =2
                btn6["text"]="X"
            elif turn==2:
                turn=1
                btn6["text"]="O"
            check()
    def clicked7():
        global turn
        if btn7["text"]==" ":
            if turn==1:
                turn =2
                btn7["text"]="X"
            elif turn==2:
                turn=1
                btn7["text"]="O"
            check()
    def clicked8():
        global turn
        if btn8["text"]==" ":
            if turn==1:
                turn =2
                btn8["text"]="X"
            elif turn==2:
                turn=1
                btn8["text"]="O"
            check()
    def clicked9():
        global turn
        if btn9["text"]==" ":
            if turn==1:
                turn =2
                btn9["text"]="X"
            elif turn==2:
                turn=1
                btn9["text"]="O"
            check()
    
    def check():
        global flag
        b1 = btn1["text"]
        b2 = btn2["text"]
        b3 = btn3["text"]
        b4 = btn4["text"]
        b5 = btn5["text"]
        b6 = btn6["text"]
        b7 = btn7["text"]
        b8 = btn8["text"]
        b9 = btn9["text"]
        flag=flag+1
        if b1==b2 and b1==b3 and b1=="O" or b1==b2 and b1==b3 and b1=="X":
            win(btn1["text"])
        if b4==b5 and b4==b6 and b4=="O" or b4==b5 and b4==b6 and b4=="X":
            win(btn4["text"])
        if b7==b8 and b7==b9 and b7=="O" or b7==b8 and b7==b9 and b7=="X":
            win(btn7["text"])
        if b1==b4 and b1==b7 and b1=="O" or b1==b4 and b1==b7 and b1=="X":
            win(btn1["text"])
        if b2==b5 and b2==b8 and b2=="O" or b2==b5 and b2==b8 and b2=="X":
            win(btn2["text"])
        if b3==b6 and b3==b9 and b3=="O" or b3==b6 and b3==b9 and b3=="X":
            win(btn3["text"])
        if b1==b5 and b1==b9 and b1=="O" or b1==b5 and b1==b9 and b1=="X":
            win(btn1["text"])
        if b7==b5 and b7==b3 and b7=="O" or b7==b5 and b7==b3 and b7=="X":
            win(btn7["text"])
        if flag ==10:
            messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
            window.destroy()

    def win(player):
        ans = "Game complete " +player + " wins "
        messagebox.showinfo("Congratulations", ans)
        window.destroy()  # is used to close the program


    btn1 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
    btn1.grid(column=1, row=1)
    btn2 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
    btn2.grid(column=2, row=1)
    btn3 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
    btn3.grid(column=3, row=1)
    btn4 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked4)
    btn4.grid(column=1, row=2)
    btn5 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked5)
    btn5.grid(column=2, row=2)
    btn6 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked6)
    btn6.grid(column=3, row=2)
    btn7 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked7)
    btn7.grid(column=1, row=3)
    btn8 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked8)
    btn8.grid(column=2, row=3)
    btn9 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked9)
    btn9.grid(column=3, row=3)

    window.mainloop()



#------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------

# Game 3: Jumbled words

# you can add more words as per your requirement
answersj = [
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
    "apple",
    "rainbow",
    "earth"
]

words = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
    "lppea",
    "wnbiroa",
    "raeht"
]

# I have improvised the code by using len(words)
num =  random.randrange(0, len(words), 1)


def jumbledWords():
    def default():
        global words,answersj,num
        lbl.config(text = words[num])

    def res():
        global words,answersj,num
        num = random.randrange(0, len(words), 1)
        lbl.config(text = words[num])
        e1.delete(0, END)


    def checkans():
        global words,answersj,num
        var = e1.get()
        if var == answersj[num]:
            promtLbl.configure(text="Correct... Continue Playing.", fg="#00dd00")
            res()
        else:
            promtLbl.configure(text="Wrong... Guess again.", fg="#ff0000")
            e1.delete(0, END)




    root1 = Tk()
    root1.geometry("350x400")
    root1.title("Jumbbled")
    root1.configure(background = "#f0f5ff")

    promtLbl= Label(root1, text="Guess the Jumbled Word", bg="#f0f5ff", fg="black", font=("Arial Bold", 12))
    promtLbl.pack(pady=20)

    lbl = Label(
        root1,
        text = "Your here",
        font = ("Verdana", 18),
        bg = "#f0f5ff",
        fg = "black",
    )
    lbl.pack(pady = 30,ipady=10,ipadx=10)


    ans1 = StringVar()
    e1 = Entry(
        root1,
        font = ("Verdana", 16),
        textvariable = ans1,
    )
    e1.pack(ipady=5,ipadx=5)

    btncheck = Button(
        root1,
        text = "Check",
        font = ("Comic sans ms", 16),
        width = 16,
        bg = "#0652dd",
        fg = "white",
        relief = GROOVE,
        command = checkans,
    )
    btncheck.pack(pady = 20)

    btnreset = Button(
        root1,
        text = "Reset",
        font = ("Comic sans ms", 16),
        width = 16,
        bg = "white",
        fg = "#0652dd",
        relief = GROOVE,
        command = res,
    )
    btnreset.pack()

    default()
    root1.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------

master = Tk()
master.title("Brain Games")
icon = PhotoImage(file = "F:/Project/masterIcon.png")
master.iconphoto(True, icon)
master.geometry("1150x580")
master.resizable(False, False)

topBG="#ffffff"
lightBG="#f0f5ff"

#--------------------------------------------------------------------------

topFrame = Frame(master, bg=topBG, height="80", width="1150")
topFrame.place(x="0", y="0")

welcome = Label(topFrame, bg=topBG, text="Welcome,", font = ("Arial", 12))
welcome.place(x="26", y="10")
userName = Label(topFrame, bg=topBG, text="Prashant Kumar", font = ("Montserrat Bold", 18))
userName.place(x="26", y="30")

def exitClick():
    master.destroy()

logout = Button(topFrame, text="Exit", padx="20", pady="5", fg="red", bg=lightBG, font=("Arial", 10), command=exitClick)
logout.place(x="1020", y="20")

#-------------------------------------------------------------------------------------------------------------------------------------

mainFrame = Frame(master, height="500", width="1150", bg=lightBG)
mainFrame.place(x="0", y="80")

headLine = Label(master, text="Choose a game to play and Launch it... All the best...", fg="#000000", bg=lightBG, font=("Arial", 12))
headLine.place(x="400", y="120")

#------------------------------------------------------------

def launchQuizGame():
    master.destroy()
    theQuizGame()

gameFrame1 = Frame(master, height="300", width="250", bg=topBG)
gameFrame1.place(x="100", y="180")
quizIcon = PhotoImage(file = "quizIcon.png")
icon1 = Label( gameFrame1, image=quizIcon, bg=topBG)
icon1.place(x="50", y="20")
gameName1=Label(gameFrame1, text="Quiz Game", bg=topBG, font=("Arial Bold", 18))
gameName1.place(x="60", y="180")
launch1 = Button(gameFrame1, text="Launch", padx="10", pady="2", bg="#0652dd", fg="white", font=("Arial Bold", 11), command=launchQuizGame)
launch1.place(x="85", y="240")

gameFrame2 = Frame(master, height="300", width="250", bg=topBG)
gameFrame2.place(x="450", y="180")
tttIcon = PhotoImage(file = "tttIcon.png")
icon2 = Label( gameFrame2, image=tttIcon, bg=topBG)
icon2.place(x="50", y="20")
gameName2=Label(gameFrame2, text="Tic-Tac-Toe", bg=topBG, font=("Arial Bold", 18))
gameName2.place(x="55", y="180")
launch2 = Button(gameFrame2, text="Launch", padx="10", pady="2", bg="#0652dd", fg="white", font=("Arial Bold", 11), command=theTicTacToe)
launch2.place(x="85", y="240")

gameFrame3 = Frame(master, height="300", width="250", bg=topBG)
gameFrame3.place(x="800", y="180")
jumbleIcon = PhotoImage(file = "jumbleIcon.png")
icon3 = Label( gameFrame3, image=jumbleIcon, bg=topBG)
icon3.place(x="50", y="20")
gameName3=Label(gameFrame3, text="Jumbled Words", bg=topBG, font=("Arial Bold", 18))
gameName3.place(x="30", y="180")
launch3 = Button(gameFrame3, text="Launch", padx="10", pady="2", bg="#0652dd", fg="white", font=("Arial Bold", 11), command=jumbledWords)
launch3.place(x="85", y="240")

def loggedin():
    pname = inputName.get()
    if pname =="":
        theNameLabel.configure(fg="red")
    else:
        userName.configure(text=pname)
        loginFrame.destroy()

loginFrame= Frame(master, height="580", width="1150", bg=lightBG)
loginFrame.place(x="0", y="0")
iconImage= PhotoImage(file="masterIcon.png")
iconLabel= Label(loginFrame, image=iconImage, bg=lightBG)
iconLabel.place(x="500", y="50")
theIntro= Label(loginFrame, text="Brain Games", bg=lightBG, fg="black", font=("Arial Bold", 28))
theIntro.place(x="450", y="200")
theNameLabel= Label(loginFrame, text="Enter the player name", bg=lightBG, font=("Arial", 10))
theNameLabel.place(x="400", y="300")
inputName = Entry(loginFrame, width="55", bg="white")
inputName.place(x="400", y="320", height="30")
loginBtn= Button(loginFrame, text="Submit", bg="#0652dd", fg="white", font=("Arial Bold", 10), command=loggedin)
loginBtn.place(x="540", y="370")

#------------------------------------------------------------------------------------------------------------------------

master.mainloop()