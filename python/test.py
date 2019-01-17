import numpy as np
import matplotlib.pyplot as plt


def shear(x, P, L):
    return -P

def moment(x, P, L):
    return P*L - x

def curvature(x, P, L, EI):
    momt = moment(x, P, L)
    curv = momt / EI
    return curv

def rotation(x, P, L, EI):
    rot = (P*L*x - P*x**2/2)/EI
    return rot

def displacement(x, P, L, EI):
    disp = P*x**2 / (6*EI) * (3*L-x)
    return disp

# Parameters for an example
L = 4
P = 1
EI = 1

x = np.arange(0, L+1, 1)
shears = shear(x, P, L)
moments = moment(x, P, L)
curvs = curvature(x, P, L, EI)
rots = rotation(x, P, L, EI)
print("Tip Rotation = " + str(rots[-1]))
rots = rots / rots[-1] #Normalize
disps = displacement(x, P, L, EI)
print("Tip Displacement = " + str(disps[-1]))
disps = disps / disps[-1]  #Normalize

#Plot the beam response
f1 = plt.figure(1)
plt.plot(x,moments)
f2 = plt.figure(2)
plt.plot(x,curvs)
f3 = plt.figure(3)
plt.plot(x,rots)
f4 = plt.figure(4)
plt.plot(x,disps)

plt.show()