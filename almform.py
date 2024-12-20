import numpy as np
import matplotlib.pyplot as plt
#Assignment
# Write a python code to solve a quadratic equation using functions.
    
  

#    ax^2 + bx + c = 0

def is_quadratic(a,b,c):
    import cmath
    discriminant = b**2 -4*a*c
    if discriminant <= 0:
        return 'The equation has no real root'
    else:
        root1 = (-b + cmath.sqrt(discriminant))/(2*a)
        root2 = (-b - cmath.sqrt(discriminant))/(2*a)
   
    print(f'{root1} and {root2}')
    
    x = np.linspace(-20, 20, 400)  
    y = a*x**2 + b*x + c
    
    #Creating your graph 8 by 6 inches
    plt.figure(figsize=(6,6), facecolor="Green")

    #Plot x values, y values, add label
    plt.plot(x,y,label = f"{a}x^2 + {b}x + {c}")
    
    #Plot horizontal line (X axis) 
    plt.axhline(0, color = "Red", linewidth = 0.5)

    #Plot vertical line (Y axis)
    plt.axvline(0, color = "Blue", linewidth = 0.5)

    plt.grid(color = "Green", linestyle = "--",linewidth = 0.5)
    plt.legend()

    plt.title ("Quadratic equation plot")
    plt.xlabel("x")
    plt.ylabel("y")
    
    plt.show()   

a = 4 ;b = 5; c = -6 
 
is_quadratic(a,b,c)    