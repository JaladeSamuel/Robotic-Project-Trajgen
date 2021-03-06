# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 15:17:54 2020

@author: taix
"""
import matplotlib.pylab as plt
import matplotlib.pyplot as pplt
#############################################################################
# Affichage de la fonction f(t) et de ses dérivées fd(t) et fdd(t) 
#           et des temps de commutation
#INPUT:
#    numfig: numéro de la figure (entier)
#    nom: chaîne de caractèreS qui correspond à la fonction à afficher
#    f: valeurs discrètes de la fonction s en ordonnée du subplot haut
#    fd: valeurs discrètes de la fonction fd en ordonnée du subplot milieu
#    fdd: valeurs discrètes de la fonction fdd en ordonnée du subplot bas
#    t: valeurs discrètes du temps de 0 à tf en abscisse des 3 subplot
#    tc: liste des instants de commutation 
#
#    ATTENTION: il faut que les dimensions de f,fd,fdd et t soient identiques
#############################################################################
def affiche3courbes(numfig,nom,f,fd,fdd,t,tc):
    plt.figure(numfig)

    plt.subplot(311)
    plt.plot(t, f, "r--")
    plt.xlabel('Temps')
    plt.ylabel('Valeur de ' + nom)
    plt.grid(True)
    for x in tc:
        plt.axvline(x,color="g",linestyle="--")
    plt.title('Affichage des courbes fonction de ' + nom)
    plt.subplot(312)
    plt.plot(t, fd, "r--")
    plt.xlabel('Temps')
    plt.ylabel('Valeur de ' + nom+'d')
    plt.grid(True)
    for x in tc:
        plt.axvline(x,color="g",linestyle="--")
    plt.subplot(313)
    plt.plot(t, fdd, "r--")
    plt.xlabel('Temps')
    plt.ylabel('Valeur de ' + nom+'dd')
    plt.grid(True)
    for x in tc:
        plt.axvline(x,color="g",linestyle="--")   
    
    plt.show(block=True)
    
#############################################################################
# Affichage d'une courbe 2D d'abscisse t et d'ordonnée d(t)
#INPUT:
#    numfig: numéro de la figure (entier)
#    nom: chaîne de caractèreS qui correspond à la fonction à afficher
#    t: valeurs discrètes du temps  en abscisse
#    d: valeurs discrètes de la fonction s en ordonnée 
#    coul: couleur de la courbe (exemple "r" pour rouge)
#
#    ATTENTION: il faut que les dimensions de d et t soient identiques
#############################################################################  
def affiche_courbe2D(numfig,nom,t,d,coul,xLabel):
    plt.figure(numfig)
    plt.plot(t, d,"o-", label="ligne -",color=coul)
    plt.xlabel(xLabel)
    plt.ylabel('Valeur de ' + nom)
    plt.title('Affichage de la courbe ' + nom)
    plt.show(block=True) # affiche la figure a l'ecran
    
