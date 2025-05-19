#Quiz assingment
import easygui as e
import random as r
score = 0

#intro
welcome = e.msgbox("Hi! this is a quiz for a school assingment", title= "Welcome!")
name = e.enterbox("What is your name", title= "Name")
hi = e.msgbox("Hello " + name)
age = e.integerbox(name + " what is your age?", title= "Age")

#print first 2 user inputs
print("name is " + name)
print(name + "'s age is", age)

#let me see if you can play
if age < 15:
    e.msgbox("You are not old enough to play.", title= "Too Young")
    e.msgbox("Thank you for attempting to play ", name)
    print(name + " has been kicked for not being old enough")
    quit()
if age > 18:
    e.msgbox ("You are too old to play", title= "Too Old")
    e.msgbox ("Thank you for atempting to play ", name)
    print(name + " has been kicked for being to old")
    quit()
e.msgbox("You are old enough to play", title= "Right Age")
print(name + " is the right age to play")

#no will quit program
e.msgbox("This quiz will be filled with random questions from all sorts of fields")

ayr = e.buttonbox("Are you ready to play the quiz? (No will quit program)", title= "Are You Ready?", choices= ["Yes", "No"])

#yes means continue, no means quit
if ayr == "Yes":
    print("user wants to continue with quiz")
if ayr == "No":
    print("user doesn't want to continue with quiz")
    quit()

print("Quiz is loading")

#8 questions currently on 8/05/2025
qone = e.buttonbox("What is the capital of New Zealand?", title= "Question 1",  choices= ["Wellington", "Auckland", "Christchurch", "Hamilton"])
if qone == "Wellington":
    e.msgbox("You got the question right first try")
    score += 1

if qone != "Wellington":
    e.msgbox("You got the question wrong. You have 1 more attempts to try again")
    qoner = e.buttonbox("What is the capital of New Zealand?", title= "Question 1", choices= ["Wellington", "Auckland", "Christchurch", "Hamilton"])
    if qoner == "Wellington":
        e.msgbox("You got the question right on second attempt")
    if qoner != "Wellington":
        e.msgbox("You got question wrong, no more attempts can be made")


qtwo = e.buttonbox("What is the largest country in the world?", title= "Question 2",  choices= ["Canada", "China", "Russia", "United States"])
if qtwo == "Russia":
    e.msgbox("You got the question right first try")
    score += 1

if qtwo != "Russia":
    e.msgbox("You got the question wrong. You have 1 more attempts to try again")
    qtwor = e.buttonbox("What is the largest country in the world?", title= "Question 2", choices= ["Canada", "China", "Russia", "United States"])
    if qtwor == "Russia":
        e.msgbox("You got the question right on second attempt")
    if qtwor != "Russia":
        e.msgbox("You got question wrong, no more attempts can be made")


qtre = e.buttonbox("What is the best selling console of all time?", title= "Question 3",  choices= ["PlayStation 2", "Nintendo DS", "Game Boy", "PlayStation"])
if qtre == "PlayStation 2":
    e.msgbox("You got the question right first try")
    score += 1

if qtre != "PlayStation 2":
    e.msgbox("You got the question wrong. You have 1 more attempts to try again")
    qtrer = e.buttonbox("What is the best selling console of all time?", title= "Question 3", choices= ["PlayStation 2", "Nintendo DS", "Game Boy", "PlayStation"])
    if qtrer == "PlayStation 2":
        e.msgbox("You got the question right on second attempt")
    if qtrer != "PlayStation 2":
        e.msgbox("You got question wrong, no more attempts can be made")


qfou = e.buttonbox("Who was the best selling music artist in 2002?", title= "Question 4",  choices= ["Nelly", "Eminem", "Gorillaz", "Dixie Chicks"])
if qfou == "Eminem":
    e.msgbox("You got the question right first try")
    score += 1

if qfou != "Eminem":
    e.msgbox("You got the question wrong. You have 1 more attempts to try again")
    qfour = e.buttonbox("Who was the best selling music artist in 2002 ?", title= "Question 4", choices= ["Nelly", "Eminem", "Gorillaz", "Dixie Chicks"])
    if qfour == "Eminem":
        e.msgbox("You got the question right on second attempt")
    if qfour != "Eminem":
        e.msgbox("You got question wrong, no more attempts can be made")


qfiv = e.buttonbox("What is Eminem's best selling album?", title= "Question 5",  choices= ["Recovery", "The Marshall Mathers LP", "Encore", "The Eminem Show"])
if qfiv == "The Eminem Show":
    e.msgbox("You got the question right first try")
    score += 1

if qfiv != "The Eminem Show":
    e.msgbox("You got the question wrong. You have 1 more attempts to try again")
    qfivr = e.buttonbox("What is Eminem's best selling album?", title= "Question 5", choices= ["Recovery", "The Marshall Mathers LP", "Encore", "The Eminem Show"])
    if qfivr == "The Eminem Show":
        e.msgbox("You got the question right on second attempt")
    if qfivr != "The Eminem Show":
        e.msgbox("You got question wrong, no more attempts can be made")


qsix = e.buttonbox("What is the best selling video game of all time?", title= "Question 6",  choices= ["ARK", "GTA V", "Wii Sports", "Minecraft"])
if qsix == "Minecraft":
    e.msgbox("You got the question right first try")
    score += 1

if qsix != "Minecraft":
    e.msgbox("You got the question wrong. You have 1 more attempts to try again")
    qsixr = e.buttonbox("What is the best selling video game of all time?", title= "Question 6", choices= ["ARK", "GTA V", "Wii Sports", "Minecraft"])
    if qsixr == "Minecraft":
        e.msgbox("You got the question right on second attempt")
    if qsixr != "Minecraft":
        e.msgbox("You got question wrong, no more attempts can be made")


qsev = e.buttonbox("Who made the video game Minecraft?", title= "Question 7",  choices= ["Rockstar", "Mojang", "Microsoft", "Activision"])
if qsev == "Mojang":
    e.msgbox("You got the question right first try")
    score += 1

if qsev != "Mojang":
    e.msgbox("You got the question wrong. You have 1 more attempts to try again")
    qsevr = e.buttonbox("Who made the video game Minecaft?", title= "Question 7", choices= ["Rockstar", "Mojang", "Microsoft", "Activision"])
    if qsevr == "Mojang":
        e.msgbox("You got the question right on second attempt")
    if qsevr != "Mojang":
        e.msgbox("You got question wrong, no more attempts can be made")


qeng = e.buttonbox("What ocean is New Zealand located in?", title= "Question 8",  choices= ["Atlantic", "Indian", "Arctic", "Pacific"])
if qeng == "Pacific":
    e.msgbox("You got the question right first try")
    score += 1

if qeng != "Pacific":
    e.msgbox("You got the question wrong. You have 1 more attempts to try again")
    qengr = e.buttonbox("What ocean is New Zealand located in?", title= "Question 8", choices= ["Atlantic", "Indian", "Arctic", "Pacific"])
    if qengr == "Pacific":
        e.msgbox("You got the question right on second attempt")
    if qengr != "Pacific":
        e.msgbox("You got question wrong, no more attempts can be made")


qnin = e.buttonbox("Who was the main character in The Matrix (1999)?", title= "Question 9",  choices= ["Morpheus", "Trinity", "Neo", "Agent Smith"])
if qnin == "Neo":
    e.msgbox("You got the question right first try")
    score += 1

if qnin != "Neo":
    e.msgbox("You got the question wrong. You have 1 more attempts to try again")
    qninr = e.buttonbox("Who was the main character in The Matrix (1999)?", title= "Question 9", choices= ["Morpheus", "Trinity", "Neo", "Agent Smith"])
    if qninr == "Neo":
        e.msgbox("You got the question right on second attempt")
    if qninr != "Neo":
        e.msgbox("You got question wrong, no more attempts can be made")


qten = e.buttonbox("When was Limp Bizkit's album Chocolate Starfish And The Hot Dog Flavored Water released?", title= "Question 10",  choices= ["2000", "2001", "1999", "1998"])
if qten == "2000":
    e.msgbox("You got the question right first try")
    score += 1

if qten != "2000":
    e.msgbox("You got the question wrong. You have 1 more attempts to try again")
    qtenr = e.buttonbox("When was Limp Bizkit's album Chocolate Starfish And The Hot Dog Flavored Water released?", title= "Question 10", choices= ["2000", "2001", "1999", "1998"])
    if qtenr == "2000":
        e.msgbox("You got the question right on second attempt")
    if qtenr != "2000":
        e.msgbox("You got question wrong, no more attempts can be made")

str

print("Your score is ", str(score))

print("If you can see this, code had a porblem")

#must figure out how many questions i want or need for this quiz
#next time figure out or ask sir how to make the question work properly