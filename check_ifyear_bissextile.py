#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
#
#       check_ifyear_bissextile.py
#  
#  Copyright 2016 Bernardin.H 
# 
#  ---------------------------------------------------------------------------  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.to
#  --------------------------------------------------------------------------- 
#  
#
# Programme testant si une année, saisie par l'utilisateur,
# est bissextile ou non

import os # On importe le module os qui dispose de variables 

          # et de fonctions utiles pour dialoguer avec votre 

          # système d'exploitation

annee = input("\n Saisissez une annee : ") # On attend que l'utilisateur saisisse l'année qu'il désire tester
annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre
bissextile = False # On crée un booléen qui vaut vrai ou faux
                   # selon que l'année est bissextile ou non

if annee % 400 == 0:
    bissextile = True
elif annee % 100 == 0:
    bissextile = False
elif annee % 4 == 0:
    bissextile = True
else:
    bissextile = False

if bissextile: # Si l'année est bcdissextile
    print("L'annee saisie est bissextile.")
else:
    print("L'annee saisie n'est pas bissextile.\n")

# On met en pause le système (Windows)
os.system("pause")
