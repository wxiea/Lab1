import numpy as np
import matplotlib.pyplot as plt
import math

def square(ax,n,p,w):
    if n>0:
        i1 = [1]
        t = (p*w) + p[i1]
        q = (p*w) - 400
        ax.plot(p[:,0],p[:,1],color='k')
        square(ax,n-1,t,w)#left top
        square(ax,n-1,q,w)#left bot
        square(ax,n-1,q*-1,w)#right top
        square(ax,n-1,t*-1,w)#right bot

plt.close('all') 
orig_size = 400
w = 0.5
p = np.array([[-orig_size,-orig_size],[-orig_size,orig_size],[orig_size,orig_size],[orig_size,-orig_size],[-orig_size,-orig_size]])
fig, ax = plt.subplots()
square(ax,2,p,w)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()


def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,color='k')
        center[0] = center[0]*w
        draw_circles(ax,n-1,center,radius*w,w)
   
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 10, [100,0], 100,.6)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()


def draw_triangle(ax,n,p,w):
        ax.plot(p[:,0],p[:,1],color='k')
        triangles(ax,n,p,w)
        
def triangles(ax,n,q,w):
    if n>0:
        neg = (q - 800)
        ax.plot(neg[:,0],neg[:,1],color='k')
        pos = (q + 800)
        ax.plot(pos[:,0],pos[:,1],color='b')
        triangles(ax,n-1,q,w)

orig_size = 800
p = np.array([[orig_size,orig_size],[-orig_size,orig_size],[0,0],[orig_size,-orig_size],[-orig_size,-orig_size]])
fig, ax = plt.subplots()
draw_triangle(ax,1,p,.2)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()


def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y =circle(center,radius)
        ax.plot(x,y,color='k')
        r1 = [center[0] - radius*(2/3),center[1]]
        r2 = [center[0] + radius*(2/3),center[1]]
        r3 = [center[0],center[1] + radius*(2/3)]
        r4 = [center[0],center[1] - radius*(2/3)]
        
        draw_circles(ax,n-1,center,radius/3,w)#center
        draw_circles(ax,n-1,r1,radius/3,w)#left
        draw_circles(ax,n-1,r2,radius/3,w)#right
        draw_circles(ax,n-1,r3,radius/3,w)#top
        draw_circles(ax,n-1,r4,radius/3,w)#bot

plt.close('all')      
fig, ax = plt.subplots() 
draw_circles(ax, 3, [100,0], 100,0.9)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()



