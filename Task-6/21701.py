from turtle import *
screensize(3500,3500)
m = 17
tracer(0)
for i in range(2):
    fd(28 * m)
    rt(90)
    fd(18 * m)
    rt(90)
up()
fd(14 * m)
rt(90)
fd(10 * m)
lt(90)
down()
for i in range(2):
    fd(30 * m)
    rt(90)
    fd(7 * m)
    rt(90)
up()
for x in range(0, 45):
    for y in range(-18, 1):
        goto(x * m, y * m)
        dot(3,'blue')
update()
done()

#679

