#오륜기 그리기(exam04.py)
# t.circle(80) 명령어를 조합하여 화면에 오륜기를 그리는 프로그램을 작성해보자(반지름은 80pixel)

import turtle
t = turtle.Turtle()
t.shape("turtle")

t.up()
t.goto(-150,0)
t.down()
t.circle(80);

t.up()
t.goto(0,0)
t.down()
t.circle(80);

t.up()
t.goto(150,0)
t.down()
t.circle(80);

t.up()
t.goto(-80,-100)
t.down()
t.circle(80);

t.up()
t.goto(80,-100)
t.down()
t.circle(80);
