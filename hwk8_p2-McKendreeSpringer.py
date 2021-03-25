import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.optimize as opt

def f(x,y):
    '''function of x and y to plot and find maximum of'''
    return 5*math.exp(-(x-1)**2-2*(y-3)**2)+3*math.exp(-2*(x-4)**2-(y-1)**2)

def f_for_scipy(x,y):
    '''function is f mirrored so that the maximum is now a minimum for use with scipy.optimize.minimize'''
    return -(5*math.exp(-(x-1)**2-2*(y-3)**2)+3*math.exp(-2*(x-4)**2-(y-1)**2))

def f_gradient(x,y):
    '''gradient of f(x,y)'''
    deriv_x = 5*(-2*(x-1))*math.exp(-(x-1)**2-2*(y-3)**2)+3*(-4*(x-4))*math.exp(-2*(x-4)**2-(y-1)**2)
    deriv_y = 5*(-4*(y-3))*math.exp(-(x-1)**2-2*(y-3)**2)+3*(-2*(y-1))*math.exp(-2*(x-4)**2-(y-1)**2)
    return (deriv_x,deriv_y)

def gradient_descent(position_guess, gamma, steps, gradient_func):
    '''finds maximum of gradient function.
    position_guess = coordinates of maximum guess
    gamma = step size
    steps = number of steps to take to find the maximum
    gradient_func = gradient function'''
    pos = position_guess
    for i in range(int(steps)):
        gradient = gradient_func(pos[0],pos[1])
        Xpos = pos[0] - gamma*gradient[0]
        Ypos = pos[1] - gamma*gradient[1]
        pos = (Xpos, Ypos)
    return pos

if __name__ == "__main__":
    #defines domain and finds function values over the domain
    domain = np.arange(0,5.01,step=0.01)
    values = []
    for i in range(len(domain)):
        for j in range(len(domain)):
            values.append(f(domain[j],domain[i]))
    values = np.array(values)
    values = values.reshape((501,501))
    
    #plots f on a contour plot over the domain
    plt.contour(domain, domain, values, levels=50)
    plt.title('f(x,y)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('function_graph.png')
    plt.show()

    #finds global maximum using scipy minimize routine
    print('Global maximum found using scipy.optimize.minimize:')
    #print(opt.minimize(f_for_scipy, (1,1)))
    
    #finds global maximum using gradient descent function
    print('Global maximum found using the gradient descent function:')
    print(gradient_descent((1,1),0.3,20,f_gradient))
