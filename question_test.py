#Quiz assingment
import easygui as e
import random as r

qone = e.buttonbox("What is the capital of New Zealand?", title= "Question 1",  choices= ["Wellington", "Auckland", "Christchurch", "Hamilton"])
if qone == "Wellington":
    e.msgbox("You got the question right first try")

if qone != "Wellington":
    e.msgbox("You got the question wrong. You have 1 more attempts to try again")
    qoner = e.buttonbox("What is the capital of New Zealand?", title= "Question 1", choices= ["Wellington", "Auckland", "Christchurch", "Hamilton"])
    if qoner == "Wellington":
        e.msgbox("You got the question right on second attempt")
    if qoner != "Wellington":
        e.msgbox("You got question wrong, no more attempts can be made")

print("close")