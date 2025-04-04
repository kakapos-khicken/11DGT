#Quiz assingment
import easygui as e
import random as r

#Basic intro
welcome = e.msgbox("Hi! this is a quiz for a school assingment", title= "Welcome!")
name = e.enterbox("What is your name", title= "Name")
hi = e.msgbox("Hello" + name)
age = e.integerbox("What is your age?", title= "Age")

if age < 15:
    e.msgbox("You are not old enough.")
    quit
else:
    e.msgbox ("You are old enough to play")