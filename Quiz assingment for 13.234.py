#Quiz assingment
import easygui as e
import random as r

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
ansor = e.msgbox("All answers must have capital letters and correct spelling (if needed)", title= "idk")

ayr = e.buttonbox("Are you ready to play the quiz? (No will quit program)", title= "Are You Ready?", choices= ["Yes", "No"])

#yes means continue, no means quit
if ayr == "Yes":
    print("user wants to continue with quiz")
if ayr == "No":
    print("user doesn't want to continue with quiz")
    quit()

print("Quiz is loading")

qone = e.buttonbox("What is the capital of New Zealand?", title= "Question 1",  choices= ["Wellington", "Auckland", "Christchurch", "Hamilton"])
if qone == "Wellington":
    e.msgbox("You got the question right first try")
    print(name + " has earnt 1 point")
if qone == "Auckland" + "Christchurch" + "Hamilton":
    e.msgbox("You got the question wrong. You have 1 more attempts to try again")
    qoner = e.buttonbox("What is the capital of New Zealand?", title= "Question 1", choices= ["Wellington", "Auckland", "Christchurch", "Hamilton"])

e.msgbox("Question 2 will come soon")


print("If you can see this, code had a porblem")

#must figure out how many questions i want or need for this quiz
#next time figure out or ask sir how to make the question work properly