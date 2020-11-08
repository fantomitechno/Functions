# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Nom du programme : math_ftt.py
# Version : 0
# Objectifdu programme : Sauvegarder les fonctions que je recontre et que je réutilise
#
# Auteur: Simon RENOUX (fantomitechno)
# date de création : 08/11/2020
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#Importation des bibliothèques nécessaires au fonctionnement du programme
#-------------------------------------------------------------------------------

#Bibliothèque mathématiques
#https://docs.python.org/fr/3.5/library/math.html
from math import*


#-------------------------------------------------------------------------------
#Création des fonctions Python nécessaires au fonctionnement du programme
#-------------------------------------------------------------------------------

#Fonction qui donne le maximum entre a et b
def max(a,b):
    if a<b:
        return b
    else:
        return a

#Fonction qui donne le minimum entre a et b
def min(a,b):
    if a>b:
        return b
    else:
        return a

#Fonction qui donne le reste de la division euclidienne de a par b
def reste(a,b):
    while b<=a:
        a=a-b
    return a

#Fonction qui donne le quotien de la division euclidienne de a par b
def quotien(a,b):
    q = 0
    while b<=a:
        a=a-b
        q = q+1
    return q

#Fonction qui donne le quotient et le reste de la division euclidienne de a par b
def DivisionEuclidienne(a,b):
    q = 0
    while b<=a:
        a=a-b
        q = q+1
    return a,q

#Fonction qui donne le produit de a par b
def multiplication(a,b):
    m = 0
    for k in range(a):
        m = m + b
    return m