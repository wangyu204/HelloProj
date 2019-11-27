# coding=utf-8

# 元组实现 多值返回
def position(dt, speed):
    posx = speed[0] * dt
    posy = speed[1] * dt
    return (posx, posy)


move = position(60.0, (10, -5))

print("物体位移：({0}, {1})".format(move[0], move[1]))
