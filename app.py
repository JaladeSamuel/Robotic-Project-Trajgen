import afficheCourbesTP
import math

A = (0, 0)
B = (0, 10)
C = (4, 10)
V1 = 2
V2 = 1
Amax = 1
Vmax = 10
AB = BC = 0

def getTime():
    t0 = 0
    t1 = V1 / Amax
    t2 = ((Amax * (t1**2 / 2) - Amax * ((V2 - V1) / Amax)**2 / 2 - AB) / -V1) - t1
    t3 = (V2 - V1) / Amax + t2
    t4 = (-Amax * (-V2 / Amax)**2 / 2 - BC) / -V2 + t3
    t5 = (-V2 / Amax) + t4

    return (t0, t1, t2, t3, t4, t5)

def loi_de_mouvement_ddS(t):
    a = 0 
    if t < t1:
        a = Amax
    elif t>t2 and t<t3:
        a = -Amax
    elif t>t4 and t<t5:
        a = -Amax
    return a

#############################################################################
# MAIN
#############################################################################
if __name__ == "__main__":
    print("START")
    
    AB = math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
    BC = math.sqrt((B[0] - B[0])**2 + (C[1] - C[1])**2)
    (t0, t1, t2, t3, t4, t5) = getTime()

    print(t0, t1, t2, t3, t4, t5)