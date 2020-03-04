import afficheCourbesTP
import math

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
        v = -Amax*t
    elif t>=t3 and t<t4:
        v = V2
    elif t>=t4 and t<t5:
        v = -Amax*t
    return v

#loi_de_mouvement_S
#INPUT:
#    t: temps
#OUTPUT:
#    x: position
def loi_de_mouvement_S(t):
    x = -1
    if t >= t0 and t < t1:
        x =  1/2 * loi_de_mouvement_dS(t) * t #Amax * t = ds(t)
    elif t >= t1 and t < t2:
        x = V1 * t
    elif t >= t2 and t < t3:
        x = -1/2 * loi_de_mouvement_dS(t) * t #-Amax * t = ds(t)
    elif t >= t3 and t < t4:
        x = V2 * t
    elif t >= t4 and t < t5:
        x = -1/2 *loi_de_mouvement_dS(t) #-Amax * t = ds(t)
    return x
     
        

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