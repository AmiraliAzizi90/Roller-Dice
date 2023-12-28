from conec import *

def rb(r1, Px, Py, Pz, px, py, pz):

    if r1 == 2:
        for i in range(1,6):
            for j in range(1,6):
                if i == 2 and j == 3:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_BLACK)
                elif i == 4 and j == 3:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_BLACK)
                else:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_WHITE)

    elif r1 == 3:
        for i in range(1,6):
            for j in range(1,6):
                if i == 2 and j == 2:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_BLACK)
                elif i == 3 and j == 3:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_BLACK)
                elif i == 4 and j == 4:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_BLACK)
                else:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_WHITE)

    elif r1 == 4:
        for i in range(1,6):
            for j in range(1,6):
                if i == 2 and j == 2:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_BLACK)
                elif i == 4 and j == 2:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_BLACK)
                elif i == 2 and j == 4:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_BLACK)
                elif i == 4 and j == 4:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_BLACK)
                else:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_WHITE)
                
    elif r1 == 5:
        for i in range(1,6):
            for j in range(1,6):
                if i == 2 and j == 2:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_BLACK)
                elif i == 4 and j == 2:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_BLACK)
                elif i == 3 and j == 3:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_BLACK)
                elif i == 2 and j == 4:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_BLACK)
                elif i == 4 and j == 4:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_BLACK)
                else:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_WHITE)

    elif r1 == 6:
        for i in range(1,6):
            for j in range(1,6):
                if i == 2 and j == 1:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_BLACK)
                elif i == 4 and j == 1:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_BLACK)
                elif i == 2 and j == 3:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_BLACK)
                elif i == 4 and j == 3:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_BLACK)
                elif i == 2 and j == 5:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_BLACK)
                elif i == 4 and j == 5:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_BLACK)
                else:
                    mc.setBlock(px+Px-i, py+Py+j, pz+Pz, WOOL_WHITE)