import scipy.optimize as opt
import math
import numpy as np
import matplotlib.pyplot as plt

def Buckingham_potential(r,A,B,C):
    '''function calculates potential energy interaction between atoms.
    r = interatomic distance in angstroms
    A, B, and C are constants'''
    return A*math.exp(-B*r)-(C/r**6)

def Buckingham_potential_for_scipy(r):
    '''function is the Buckingham potential equation mirrored across the x-axis
    to reverse placement of min/max, and with A, B, and C all set to 1 for use
    with scipy.optimize.minimize'''
    return -(math.exp(-1*r)-(1/r**6))

if __name__ == "__main__":
    #creates array of distance values for which electric potential will be calculated
    interatomicDist = np.arange(0.5,20,step=0.01)

    #creates a list of electric potentials corresponding to interatomic distance
    potentialEnergy = []
    for dist in interatomicDist:
        potentialEnergy.append(Buckingham_potential(dist,1,1,1))

    #plots potential energy vs interatomic distance
    plt.plot(interatomicDist, potentialEnergy)
    plt.grid(ls='-', lw=1)
    plt.axis([min(interatomicDist), max(interatomicDist), -5, 1])
    plt.xlabel('Angstroms')
    plt.ylabel('eV')
    plt.title('Buckingham Potential Equation Graph')
    plt.savefig('Buckingham_Potential.png')
    plt.show()

    #finds the maximum using scipy.optimize.minimize
    print('Buckingham potential equation maximum:')
    print(opt.minimize(Buckingham_potential_for_scipy, 2))
    
