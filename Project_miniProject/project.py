import turtle
import math

bob = turtle.Turtle()

#math

def line(t,n,dlina,uhol):
    for i in range(n):
            t.fd(dlina)
            t.lt(uhol)
            

def arc(t, r, uhol):
    dlina = 2 * math.pi * r * abs(uhol)/360
    a = int(dlina / 4)
    uhol2= float(uhol/a)

    t.lt(uhol2/2)
    line(t,a, int(dlina),uhol2)
    t.rt(uhol2/2)


#math+all

#def circus(t, radius):
 #   arc(t, radius, 360)

def list(t, r , uhol):
    for i in range(2):
        arc(t, r, uhol)
        t.lt(180-uhol)



#all stuff
#t-turtle,n-kolto listov, uhol uhol-povorota
    
def flower(t,radius,n,uhol):
       for i in range(n):
           list(t,radius,uhol)
           t.lt(360/n)

def steble(t,radius,uhol):
    t.lt(270-(uhol/2))
    arc(t,radius,uhol)

def steble2(t,radius,uhol):
    t.setheading(180)
    t.lt(90-(uhol/2))
    arc(t,radius,uhol)


        
def list1 (t,radius,uhol):
    t.setheading(45-(uhol/2))
    for i in range(2):    
        list(t,radius/1.5,uhol)
        t.lt(90)
        

def list2 (t,radius,uhol):
    t.setheading(45+(uhol/4))
    for i in range(2):    
        list(t,radius/1.5,uhol)
        t.lt(45)


    
def go(t, x):

    t.pu()
    t.setx(x)
    t.sety(0)
    t.pd()

    

go(bob,-200)
flower(bob,15,7,60)
steble(bob,25,50)
list1(bob,15,70)

go(bob,0)
flower(bob,10,10,80)
steble2(bob,20,70)
list2(bob,50,30)

go(bob,200)
flower(bob,20,20,40)
steble2(bob,25,50)
list1(bob,25,80)



turtle.mainloop()
