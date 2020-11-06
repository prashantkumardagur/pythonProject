#!/usr/bin/env python
# coding: utf-8

# In[16]:


import json
import tkinter
from tkinter import *
import random


# loading of  questions and answer choices from json file instead of the using lists
with open('./data.json', encoding="utf8") as f:
    data = json.load(f)

# convert the dictionary in lists of questions and answers
questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]

answers = [1,1,1,1,3,1,0,1,3,3] #list of all the correct answer index values

user_answer = []
indexes = []
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


ques = 1
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
root = tkinter.Tk()
root.title("Quizmaster") # adding title
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)

bgImage= PhotoImage(file=r"nd.png") # adding bg image
labelimages = Label(root,image = bgImage).place(relwidth=1,relheight=1)


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


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




