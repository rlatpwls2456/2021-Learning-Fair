import turtle as t
import random
import time

score=0     
playing=False 
boost=False 
tspeed=1

scr=t.Screen()
scr.setup(1000,700)
scr.title("Turtle Steeplerace")
scr.bgcolor("CadetBlue2")

line=t.Turtle()
line.shape("arrow")
line.color("brown1")
line.penup()
line.goto(-300,-300)
line.pensize(3)
line.pendown()
for i in range(4):
         line.ht()    
         line.forward(600)
         line.left(90)
       
t.shape("turtle")
t.speed(0) 
t.up()
t.color("white")
t.goto(0,90)

tb=t.Turtle()
tb.shape("turtle")
tb.color("red")
tb.speed(0)
tb.up()
tb.goto(0,0)

tc=t.Turtle()    
tc.shape("turtle")
tc.color("black")
tc.speed(0)
tc.up()
tc.goto(0,40)

td=t.Turtle() 
td.shape("circle")
td.color("green")
td.speed(0)
td.up()
td.goto(-200,40)

te=t.Turtle() 
te.shape("triangle")
te.color("blue")
te.speed()
te.up()
te.goto(0,200)

tf=t.Turtle() 
tf.shape("square")
tf.color("yellow")
tf.speed(0)
tf.up()
tf.goto(200,40)

tg=t.Turtle()   
tg.shape("square")
tg.color("red")
tg.speed(0)
tg.up()
tg.goto(-150,-150)

th=t.Turtle() 
th.shape("triangle")
th.color("red")
th.speed(0)
th.up()
th.goto(150,-150)

def turn_right():    
    t.setheading(0)

def turn_up():       
    t.setheading(90)

def turn_left():     
    t.setheading(180)

def turn_down():    
    t.setheading(270)
    
def message(m1,m2,m3):   
    t.clear()
    t.goto(0,100)
    t.write(m1,False,"center",font=("Dejavu Sans Mono",30,"bold"))
    t.goto(0,-80)
    t.write(m2,False,"center",font=("Dejavu Sans Mono",25,"bold"))
    t.goto(0,-135)
    t.write(m3,False,"center",font=("Dejavu Sans Mono",15,"bold"))
    t.goto(0,100)

def die():
    global playing
    text="Score:"+str(score)
    message("Game Over", text, "you bad")
    playing=False
    score=0

def start():                
    global playing
    if playing==False:
        playing=True
        t.clear()     
        play()

def speeditem():
    global tspeed, canitem
    if tspeed>10:
        canitem=55
    if tspeed>20:
        canitem=60
    if tspeed>30:
        canitem=65
    if tspeed>40:
        canitem=70
    if tspeed>50:
        canitem=80
    if tspeed>60:
        canitem=110
    if tspeed>70:
        canitem=130
    if tspeed>80:
        canitem=150
        
def play():  
    canitem=20
    global boost
    global score
    global playing
    global tspeed
    for i in range(tspeed):
        t.forward(4)
        speeditem()

    if t.xcor() <=-300 or t.xcor()>=300:
          t.right(180)
    if t.ycor() <=-300 or t.ycor()>=300:
          t.right(180)

    if random.randint(1,50)== 5:     
       ang= tb.towards(t.pos())
       tb.setheading(ang) 
    speed=score-5
    
    for x in range(speed):                  
        if random.randint(1,50)==3:
           ang=tb.towards(t.pos())
           tb.setheading(ang)
        tb.forward(3)

    if random.randint(1,50)==5:
        ang=tc.towards(t.pos())
        tc.setheading(ang)
    speed=score-5

    for x in range(speed):
        if random.randint(1,50)==3:
            ang=tc.towards(t.pos())
            tc.setheading(ang)
        tc.forward(3)
        
    if t.distance(td)<30 :
        score=score+10          
        t.write("점수:"+str(score), font=("Dejavu Sans Mono",15,"bold"))          
        star_x=random.randint(-280,280)
        star_y=random.randint(-280,280)
        td.goto(star_x,star_y)   

    if  t.distance(te)<30:        
        tspeed=tspeed+3
        t.write("속도 :"+str(tspeed), font=("Dejavu Sans Mono",15,"bold"))
        star2_x=random.randint(-280,280)
        star2_y=random.randint(-280,280)
        te.goto(star2_x, star2_y)    

    if t.distance(tf)<canitem:    
        if boost==True:
           t.write('이미 쉴드가 있습니다!',font=("Dejavu Sans Mono",15,"bold"))
        if boost==False:
            boost=True
            t.write("쉴드", font=("Dejavu Sans Mono",15,"bold"))
            star3_x=random.randint(-280,280)
            star3_y=random.randint(-280,280)
            tf.goto(star3_x,star3_y)

    if t.distance(tb)<canitem:     
       if boost==True:
          score+=5
          t.write("점수 :"+str(score),font=("Dejavu Sans Mono",15,"bold"))
          star_x=random.randint(-280,280)
          star_y=random.randint(-280,280)
          tb.goto(star_x,star_y)
          boost=False
       else:
          text=("점수 :"+str(score))
          message("Game Over", text, "you bad")
          playing=False
          score=0

    if t.distance(tc)<canitem:     
       if boost==True:
          score+=5
          t.write("점수 :"+str(score),font=("Dejavu Sans Mono",15,"bold"))
          star_x=random.randint(-280,280)
          star_y=random.randint(-280,280)
          tc.goto(star_x,star_y)
          boost=False
       else:
          text=("점수 :"+str(score))
          message("Game Over", text, "you bad")
          playing=False
          score=0
    
    if t.distance(tg)<30:
        tg.goto(random.randint(-280,280), random.randint(-280,280))
        t.write("3초간 정지",font=("Dejavu Sans Mono",15,"bold"))
        time.sleep(3)

    if t.distance(th)<30:
        th.goto(random.randint(-280,280), random.randint(-280,280))
        tspeed=tspeed-3
        t.write("속도 :"+str(tspeed),font=("Dejavu Sans Mono",15,"bold"))

    if score>=100:
       text=("Score :"+str(score))
       message("Game Clear", text, "Good Job!")
       playing=False
       score=100
       
    if playing:
       t.ontimer(play,200)  


scr.onkeypress(turn_right, "Right")
scr.onkeypress(turn_up,"Up")
scr.onkeypress(turn_left,"Left")
scr.onkeypress(turn_down,"Down")
scr.onkeypress(start,"space")
t.listen()
message("Turtle Run","[Space]","게임시작:Space")
