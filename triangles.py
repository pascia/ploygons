import matplotlib.pyplot as plt
import numpy as np
import math

def program():    
    plotx = 128
    ploty = 128
    plot = np.empty([plotx, ploty])
    plot[0:-1,0:-1] = 0
    s=1
    Px=[[None,None,None]]
    Py=[[None,None,None]]
    Points=[]
    
    def clearplt():
        plot[0:-1,0:-1] = 0
        return plot
    
    def triangle(Ax,Ay,Bx,By,Cx,Cy,s):
        bx = Bx-Ax
        by = By-Ay
        cx = Cx-Ax
        cy = Cy-Ay
        
        d=bx*cy-cx*by
        if d == 0:
            d = 1
        
        for Px in range(plotx):
            for Py in range(ploty):
                x = Px-Ax
                y = Py-Ay
                
                WA=(x*(by-cy)+y*(cx-bx)+bx*cy-cx*by)/d
                WB=(x*cy-y*cx)/d
                WC=(y*bx-x*by)/d
        
                if 1>=WA>=0 and 1>=WB>=0 and 1>=WC>=0:
                    plot[x+Ax,y+Ay]=2
        
        plot[Ax-1:Ax+1,Ay-1:Ay+1]=6
        plot[Bx-1:Bx+1,By-1:By+1]=6
        plot[Cx-1:Cx+1,Cy-1:Cy+1]=6
        
        plt.imshow(plot, cmap="gray", vmax=7, vmin=0)
        ax = plt.gca()
        ax.axes.xaxis.set_visible(False)#clear xaxis info
        ax.axes.yaxis.set_visible(False)#clear yaxis info
        if s == True:
            plt.show()
        elif s == False:
            None  
        
    class Polynom():
        def __init__(self,int1,int2,int3,int4,int5,int6):
            l = len(Px)-1
            Px[l][0]=int(int1)
            Px[l][1]=int(int2)
            Px[l][2]=int(int3)
            Py[l][0]=int(int4)
            Py[l][1]=int(int5)
            Py[l][2]=int(int6)
            triangle(Px[l][0], Py[l][0], Px[l][1], Py[l][1], Px[l][2], Py[l][2], s)
            Points.append([int(int1),int(int4)])
            Points.append([int(int2),int(int5)])
            Points.append([int(int3),int(int6)])
            print(Points)
            
        def addpoint(self,intx,inty,tri1,tri2,printy):
            x1 = Points[int(tri1)-1][0]
            y1 = Points[int(tri1)-1][1]
            x2 = Points[int(tri2)-1][0]
            y2 = Points[int(tri2)-1][1]
            triangle(int(intx), int(inty), x1, y1, x2, y2, printy)
            l = len(Px)-1
            Px[l][0]=int(intx)
            Py[l][0]=int(inty)
            Px[l][1]=Points[int(tri1)-1][0]
            Py[l][1]=Points[int(tri1)-1][1]
            Px[l][2]=Points[int(tri2)-1][0]
            Py[l][2]=Points[int(tri2)-1][1]
            Points.append([int(intx),int(inty)])
            if(printy):
                print(Px)
        
        def rotate(self):
            nPx = []
            nPy = []
            for li in range(len(Px)):
                nPx.append(Px[li])
                nPy.append(Py[li])
            disy = 0.0
            print(Py)
            T = len(Px)
            for d in range(30):
                plt.show()
                clearplt()
                for i in range(T):
                    for a in range(3): 
                            radyan = d*2 * (math.pi/180)
                            disy=(Py[i][a]-ploty/2)/(ploty/2)
                            print(Py[i][a])
                            newdis = math.cos(radyan)*disy
                            nPy[i][a] = newdis*(ploty/2)+ploty/2
                            
                    s=False
                    triangle(nPx[i][0], int(round(nPy[i][0])), nPx[i][1], int(round(nPy[i][1])), nPx[i][2], int(round(nPy[i][2])), s)
            for i in range(T):
                s=True
                triangle(Px[i][0], Py[i][0], Px[i][1], Py[i][1], Px[i][2], Py[i][2], s)
                
            
    if(input("Input:") == "star"):
        drawing = Polynom(16,40,40,64,54,74)
        drawing.addpoint(50,64,2,3,False)#4 orta
        drawing.addpoint(55,50,2,4,False)#5 sol iç
        drawing.addpoint(55,78,3,4,False)#6 sağ iç
        drawing.addpoint(40,34,2,5,False)#7 sol uzun
        drawing.addpoint(40,94,3,6,False)#8 sağ uzun
        drawing.addpoint(64,64,4,5,False)#9 alt iç
        drawing.addpoint(64,64,4,6,False)#10 alt iç
        drawing.addpoint(77,44,5,9,False)#11 alt sol uzun
        drawing.addpoint(77,83,6,9,True)#12 alt sağ uzun


    else:
        drawing = Polynom(input("1.x:"),input("2.x:"),input("3.x:"),input("1.y:"),input("2.y:"),input("3.y:"))
    while True:
        inputcmd = input("command:")
        if inputcmd == "addpoint":#
            drawing.addpoint(input("new X:"),input("new Y:"),input("Connection1:"),input("Connection2:"),True)
        elif inputcmd == "rotate":#
            drawing.rotate()                            
        elif inputcmd == "stop":
            exit(1)
        
program()
