import afficheCourbesTP as ac
import math
import numpy as np
import matplotlib.pyplot as plt

A = (0, 0)
B = (0, 10)
C = (4, 10)
V1 = 2
V2 = 1
Amax = 1
AB = BC = 0

def getTime():
    t0 = 0
    
    delta_t0_t1 = V1 / Amax
    delta_t2_t3 = (V2 - V1) / -Amax
    
    integ_t2_t3 = delta_t2_t3 + 1/2 * delta_t2_t3 * (V1 - V2)
    integ_t0_t1 = (delta_t0_t1 * V1) / 2

    delta_t1_t2 = (AB - integ_t2_t3 - integ_t0_t1) / V1

    t1 = delta_t0_t1
    t2 = t1 + delta_t1_t2
    t3 = t2 + delta_t2_t3
    
    delta_t4_t5 = V2 / Amax
    integ_t4_t5 = (delta_t4_t5 * V2) / 2
    delta_t3_t4 = (BC - integ_t4_t5) / V2

    t4 = t3 + delta_t3_t4
    t5 = t4 + delta_t4_t5

    return (t0, t1, t2, t3, t4, t5)

def loi_de_mouvement_ddS(t):
    a = 0 
    if t < t1:
        a = Amax
    elif t>=t2 and t<t3:
        a = -Amax
    elif t>=t4 and t<t5:
        a = -Amax
    return a

def loi_de_mouvement_dS(t):
    v = 0 
    if t < t1:
        v = Amax * t
    elif t>=t1 and t<t2:
        v = V1 
    elif t>=t2 and t<t3:
        v = -Amax * (t-t2) + V1
    elif t>=t3 and t<t4:
        v = V2
    elif t>=t4 and t<t5:
        v = -Amax* (t-t4) + V2
    return v

#loi_de_mouvement_S
#INPUT:
#    t: temps
#OUTPUT:
#    x: position
def loi_de_mouvement_S(t):
    # x = -1
    # if t >= t0 and t < t1:
    #     x =  1/2 * loi_de_mouvement_dS(t) * t #Amax * t = ds(t)
    # elif t >= t1 and t < t2:
    #     x = V1 * t
    # elif t >= t2 and t < t3:
    #     x = -1/2 * loi_de_mouvement_dS(t) * t #-Amax * t = ds(t)
    # elif t >= t3 and t < t4:
    #     x = V2 * t
    # elif t >= t4 and t < t5:
    #     x = -1/2 *loi_de_mouvement_dS(t) #-Amax * t = ds(t)
    # return x
    
    # TODO : utiliser cumsum pour aller plus vite 
    integral = 0
    for i in  np.arange(0., t, 0.1):
        integral = integral + (loi_de_mouvement_dS(i) * 0.1)
    
    return integral

#Echantillonnage 
# INPUT : 
#   ts : t départ
#   tf : t final
#   te : Periode d'echantillonnage en ms
def sampling(ts, tf, te):
    s = []
    ds = []
    dds = []
    time = []
    
    for t in np.arange(ts, tf, te/1000):
        s.append(loi_de_mouvement_S(t))
        ds.append(loi_de_mouvement_dS(t))
        dds.append(loi_de_mouvement_ddS(t))
        time.append(t)
        
    return s, ds, dds, time

def trajectoire(s, t):
    AB = math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
    BC = math.sqrt((B[0] - C[0])**2 + (B[1] - C[1])**2)

    if t <= t3:
        x = A[0] + s * (B[0] - A[0]) / AB
        y = A[1] + s * (B[1] - A[1]) / AB
    else:
        x = B[0] + (s - AB) * (C[0] - B[0]) / BC
        y = B[1] + (s - AB) * (C[1] - B[1]) / BC

    return (x, y)

def d_trajectoire(s, t):
    AB = math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
    BC = math.sqrt((B[0] - C[0])**2 + (B[1] - C[1])**2)

    if t <= t3:
        x = s * (B[0] - A[0]) / AB
        y = s * (B[1] - A[1]) / AB
    else:
        x = s * (C[0] - B[0]) / BC
        y = s * (C[1] - B[1]) / BC

    return (x, y)

def affichageTrajOp(S, X, dX, ddX, label = 'x'):
    plt.figure()
        
    plt.subplot(311)
    plt.plot(S, X,"-", label="ligne -")
    plt.xlabel('Distance')
    plt.ylabel('Valeur de ' + label)
    
    plt.subplot(312)
    plt.plot(S, dX,"-", label="ligne -")
    plt.xlabel('Distance')
    plt.ylabel('Valeur de d' + label)
    
    plt.subplot(313)
    plt.plot(S, ddX,"-", label="ligne -")
    plt.xlabel('Distance')
    plt.ylabel('Valeur de dd' + label)
    
    plt.show()

#############################################################################
# MAIN
#############################################################################
if __name__ == "__main__":
    print("START")
    
    AB = math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
    BC = math.sqrt((B[0] - C[0])**2 + (B[1] - C[1])**2)
    (t0, t1, t2, t3, t4, t5) = getTime()

    print(AB, BC)
    print(t0, t1, t2, t3, t4, t5)
   
    s, ds, dds, time = sampling(0., t5, 1.)
   
    '''plt.plot(time, dds)
    plt.plot(time, ds)
    plt.plot(time, s)
    plt.show()'''
    
    ac.affiche3courbes(1, "s", s, ds, dds, time, [t0, t1, t2, t3, t4, t5])
    
    X = []
    dX = []
    ddX = []

    Y = []
    dY = []
    ddY = []

    S = []
    dS = []
    ddS = []
    T = np.arange(0., t5, 1/1000)
    for t in T:
        s = loi_de_mouvement_S(t)
        S.append(s)
        ds = loi_de_mouvement_dS(t)
        dS.append(ds)
        dds = loi_de_mouvement_ddS(t)
        ddS.append(dds)

        (x, y) = trajectoire(s, t)
        X.append(x)
        Y.append(y)

        (dx, dy) = d_trajectoire(ds, t)
        dX.append(dx)
        dY.append(dy)
        
        (ddx, ddy) = d_trajectoire(dds, t)
        ddX.append(ddx)
        ddY.append(ddy)
    
    # affichage des points (x,)
    # plt.figure(2)
    # plt.figure()
    # plt.plot(X, Y)
    # plt.gca().set_aspect('equal', adjustable='box')
    # plt.show()

    affichageTrajOp(S, X, dX, ddX, 'x')
    affichageTrajOp(S, Y, dY, ddY, 'y')
    ac.affiche3courbes(2, "x", X, dX, ddX, T, [t0, t1, t2, t3, t4, t5])
    ac.affiche3courbes(2, "y", Y, dY, ddY, T, [t0, t1, t2, t3, t4, t5])
