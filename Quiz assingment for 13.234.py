#Quiz assingment
import easygui as e
import random as r

#intro
welcome = e.msgbox("Hi! this is a quiz for a school assingment", title= "Welcome!")
name = e.enterbox("What is your name", title= "Name")
hi = e.msgbox("Hello" + name)
age = e.integerbox("What is your age?", title= "Age")

#print first 2 user inputs
print(name)
print(age)

#let me see if you can play
if age < 15:
    e.msgbox("You are not old enough to play.")
    print("user has been kicked for not being old enough")
    quit()
else:
    e.msgbox ("You are old enough to play")
    print("user is old enough to play")

#no will quit program
e.msgbox("This quiz will be filled with random questions from all sorts of fields")
ayr = e.buttonbox("Are you ready to play the quiz? (No will quit program)", choices= ["Yes", "No"])

#yes means continue, no means quit
if ayr == "Yes":
    print("user wants to continue with quiz")
if ayr == "No":
    print("user doesn't want to continue with quiz")
    quit()
