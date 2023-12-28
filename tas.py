from conec import *
from random import *
from tas_number import *
from mcpi_e.block import *
from gu import *


gu()

Px = 0
Py = 0
Pz = 8

mc.setBlock(px+Px, py+Py, pz+Pz, GOLD_BLOCK)

Pz = 11
Px = -3

for z in range(1,6):
    for y in range(1,6):
        for x in range(1,6):
            if y==3 and x==3 and z==1:
                mc.setBlock(px+x+Px, py+y+Py, pz+z+Pz, WOOL_BLACK)
            elif y==3 and x==3 and z==5:
                mc.setBlock(px+x+Px, py+y+Py, pz+z+Pz, WOOL_BLACK)
            else:
                mc.setBlock(px+x+Px, py+y+Py, pz+z+Pz, WOOL_WHITE)

Pz += 9
Px += 3

mc.setBlock(px+Px, py+Py, pz+Pz, DIAMOND_BLOCK)

t = 0

while True:
    if mc.player.pollChatPosts() == "finish":
        quit()

    px , py, pz = mc.player.getPos()

    if mc.getBlock(px, py-1, pz) == 41:
        r = randint(1,6)
        Px = 3
        Py = -1
        Pz = 4

        rb(r, Px, Py, Pz, px, py, pz)
        t = 1
        break
            

    elif mc.getBlock(px, py-1, pz) == 57:
        b = randint(1,6)
        Px = 3
        Py = -1
        Pz = -4

        rb(b, Px, Py, Pz, px, py, pz)
        t =2
        break
            
if t == 2:
    while True:
        if mc.player.pollChatPosts() == "finish":
            exit

        px , py, pz = mc.player.getPos()

        if mc.getBlock(px, py-1, pz) == 41:
            r = randint(1,6)
            Px = 3
            Py = -1
            Pz = 4

            rb(r, Px, Py, Pz, px, py, pz)
            break

elif t == 1:
    while True:
        if mc.player.pollChatPosts() == "finish":
            exit

        px , py, pz = mc.player.getPos()

        if mc.getBlock(px, py-1, pz) == 57:
            b = randint(1,6)
            Px = 3
            Py = -1
            Pz = -4

            rb(b, Px, Py, Pz, px, py, pz)
            break

mc.postToChat(f"pleyer1 or GOLD_BLOCK: {r}")
mc.postToChat(f"pleyer2 or DIAMOND_BLOCK: {b}")

if r>b:
    mc.postToChat("winner is pleyer1")

elif r<b:
    mc.postToChat("winner is pleyer2")

else:
    mc.postToChat("no winner. both equal")



    

    


