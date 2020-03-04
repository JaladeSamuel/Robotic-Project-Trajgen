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
    

