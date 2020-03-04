import afficheCourbesTP

A = (2, 1)
B = (3, 5)
C = (1, 4)
V1 = 10
V2 = 10
Amax = 10
Vmax = 10
t0, t1, t2, t3, t4, t5 = 0

def getTime():
    t0 = 0
    t1 = V1 / Amax
    t2 = ((Amax * (t1**2 / 2) - Amax * ((V2 - V1) / Amax)**2 / 2 - AB) / -V1) - t1
    t3 = (V2 - V1) / Amax + t2

#loi_de_mouvement_S
#Retourne la position x
def loi_de_mouvement_S(t):
    x = -1
    if t >= t0 and t < t1:
        x =  1/2 * (Amax * t) * t #Amax * t = sd(t)
    elif t >= t1 and t < t2:
        x = V1 * t
    elif t >= t2 and t < t3:
        x = -1/2 * (-Amax * t) * t #-Amax * t = sd(t)
    elif t >= t3 and t < t4:
        x = V2 * t
    elif t >= t4 and t < t5:
        x = -1/2 * -Amax * t #-Amax * t = sd(t)
    return x
     
        

#############################################################################
# MAIN
#############################################################################
if __name__ == "__main__":
    print("START")
    

