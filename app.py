import afficheCourbesTP as ac
import math
import numpy as np
import matplotlib.pyplot as plt

def getTime(V1, V2, AB, BC, Amax):
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

    return [t0, t1, t2, t3, t4, t5]

def loi_de_mouvement_ddS(t, ti, Amax):
    (_, t1, t2, t3, t4, t5) = ti
    a = 0
    
    if t < t1:
        a = Amax
    elif t >= t2 and t < t3:
        a = -Amax
    elif t >= t4 and t < t5:
        a = -Amax
    
    return a

def loi_de_mouvement_dS(t, ti, Amax, V1, V2):
    (_, t1, t2, t3, t4, t5) = ti
    v = 0

    if t < t1:
        v = Amax * t
    elif t >= t1 and t<t2:
        v = V1 
    elif t >= t2 and t<t3:
        v = -Amax * (t-t2) + V1
    elif t >= t3 and t<t4:
        v = V2
    elif t >= t4 and t<t5:
        v = -Amax* (t-t4) + V2
    
    return v

#loi_de_mouvement_S
#INPUT:
#    t: temps
#OUTPUT:
#    x: position
def loi_de_mouvement_S(t, ti, Amax, V1, V2):
    # TODO : préciser dans le compte rendu ce qu'on a pas réussi 
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
        integral = integral + (loi_de_mouvement_dS(i, ti, Amax, V1, V2) * 0.1)
    
    return integral

#Echantillonnage 
# INPUT : 
#   ts : t départ
#   tf : t final
#   te : Periode d'echantillonnage en ms
def sampling(ts, tf, te, ti, Amax, V1, V2):
    s = []
    ds = []
    dds = []
    time = []
    
    for t in np.arange(ts, tf, te/1000):
        s.append(loi_de_mouvement_S(t, ti, Amax, V1, V2))
        ds.append(loi_de_mouvement_dS(t, ti, Amax, V1, V2))
        dds.append(loi_de_mouvement_ddS(t, ti, Amax))
        time.append(t)
    
    return s, ds, dds, time

def trajectoire(A, B, C, s, t, ti):
    AB = math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
    BC = math.sqrt((B[0] - C[0])**2 + (B[1] - C[1])**2)
    (_, _, _, t3, _, _) = ti

    if t <= t3:
        x = A[0] + s * (B[0] - A[0]) / AB
        y = A[1] + s * (B[1] - A[1]) / AB
    else:
        x = B[0] + (s - AB) * (C[0] - B[0]) / BC
        y = B[1] + (s - AB) * (C[1] - B[1]) / BC

    return (x, y)

def d_trajectoire(A, B, C, s, t, ti):
    AB = math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
    BC = math.sqrt((B[0] - C[0])**2 + (B[1] - C[1])**2)
    (_, _, _, t3, _, _) = ti

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

def trajrecouvre(A, B, C, V1, V2, Vmax, Amax):
    AB = math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
    BC = math.sqrt((B[0] - C[0])**2 + (B[1] - C[1])**2)
    (t0, t1, t2, t3, t4, t5) = getTime(V1, V2, AB, BC, Amax)
    ti = [t0, t1, t2, t3, t4, t5]

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
        s = loi_de_mouvement_S(t, ti, Amax, V1, V2)
        S.append(s)
        ds = loi_de_mouvement_dS(t, ti, Amax, V1, V2)
        dS.append(ds)
        dds = loi_de_mouvement_ddS(t, ti, Amax)
        ddS.append(dds)

        (x, y) = trajectoire(A, B, C, s, t, ti)
        X.append(x)
        Y.append(y)

        (dx, dy) = d_trajectoire(A, B, C, ds, t, ti)
        dX.append(dx)
        dY.append(dy)
        
        (ddx, ddy) = d_trajectoire(A, B, C, dds, t, ti)
        ddX.append(ddx)
        ddY.append(ddy)
    
    return (S, dS, ddS, X, dX, ddX, Y, dY, ddY)

def mgd(q):
    (q1, q2, q3) = q
    l = 1
    x = l * math.cos(q1 + q3) - math.sin(q1) * q2
    y = l * math.sin(q1 + q3) + math.cos(q1) * q2
    theta = q1 + q3

    return x, y, theta

#############################################################################
# MAIN
#############################################################################
if __name__ == "__main__":
    A = (0, 0)
    B = (0, 10)
    C = (0, 14)
    V1 = 2
    V2 = 1
    Vmax = 2
    Amax = 1
    
    AB = math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
    BC = math.sqrt((B[0] - C[0])**2 + (B[1] - C[1])**2)
    ti = getTime(V1, V2, AB, BC, Amax)
    (t0, t1, t2, t3, t4, t5) = ti
    T = np.arange(0., t5, 1/1000)

    print("AB :", AB)
    print("BC :", BC)
    print("ti :", t0, t1, t2, t3, t4, t5)
   
    s, ds, dds, time = sampling(0., t5, 1., ti, Amax, V1, V2)
   
    ac.affiche3courbes(1, "s", s, ds, dds, time, [t0, t1, t2, t3, t4, t5])
    
    (S, dS, ddS, X, dX, ddX, Y, dY, ddY) = trajrecouvre(A, B, C, V1, V2, Vmax, Amax)
    
    affichageTrajOp(S, X, dX, ddX, 'x')
    affichageTrajOp(S, Y, dY, ddY, 'y')
    ac.affiche3courbes(2, "x", X, dX, ddX, T, [t0, t1, t2, t3, t4, t5])
    ac.affiche3courbes(2, "y", Y, dY, ddY, T, [t0, t1, t2, t3, t4, t5])

    # vitesse point O4, pour faire une vérification
    vitO4 = []
    for i in range(len(dX)):
        vit = math.sqrt(dX[i]**2 + dY[i]*2)
        vitO4.append(vit)
    
    plt.figure()
    plt.plot(T, vitO4)
    plt.show()

    q1 = math.pi / 4
    q2 = 1
    q3 = math.pi / 4
    q = [q1, q2, q3]
    x, y, theta = mgd(q)
    print("x :", x, "| y :", y, "| theta :", theta)