#曲线方形回环

import turtle as t

t.speed(50)

j=1

t.left(90)

for i in range(1,100):
    j += i+1
    t.forward(j)
    t.right(90)

