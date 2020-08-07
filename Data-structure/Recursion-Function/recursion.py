import sys
import turtle

def tostr(n,base):
    convertString="0123456789ABCDEF"
    if n<base:
        return convertString[n]
    else:
        return tostr(n//base,base)+convertString[n%base]

t=turtle.Turtle()


def pirture(t,linelen):
    t.pencolor("red")
    t.pensize(3)
    if linelen>0: 
        t.forward(linelen)
        t.right(90)
        pirture(t,linelen-5)
pirture(t,100)
t.hideturtle()
turtle.done()
