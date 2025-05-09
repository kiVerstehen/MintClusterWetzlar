import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np
import ipywidgets as widgets
from ipywidgets import interact, FileUpload
import torch
import torch.nn as nn
import torch.optim as optim

from fastbook import *
from fastai.vision.widgets import *
import os
import matplotlib.pyplot as plt
import platform
from PIL import Image, UnidentifiedImageError


import random
import math
import warnings

import time
from IPython.display import clear_output

import random
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from ipywidgets import interactive, widgets
from IPython.display import display, clear_output
import matplotlib.image as mpimg
import numpy as np

def hundOderKatzeAnhandGewicht():
    # Daten
    cat_heights = [20, 24, 31, 44, 50]
    cat_weights = [30, 20, 15, 25, 30]

    dog_heights = [18, 30, 35, 60, 45]
    dog_weights = [37, 27, 35, 30, 38]

    #Load images ONCE as arrays (fast and reusable)
    cat_img_arr = mpimg.imread('Grafiken/cathead.png')
    cat_img_grey_arr = mpimg.imread('Grafiken/cathead_grey.png')
    dog_img_arr = mpimg.imread('Grafiken/doghead.png')
    dog_img_grey_arr = mpimg.imread('Grafiken/doghead_grey.png')

    def get_image_from_array(arr, zoom=0.2):
        return OffsetImage(arr, zoom=zoom)

    def plot_counting(y_achsenabschnitt=0.0):
        clear_output(wait=True)
        fig, ax = plt.subplots()

        # Plot cats
        cat_count = 0
        for i in range(len(cat_heights)):
            image_data = cat_img_grey_arr if cat_weights[i] > y_achsenabschnitt else cat_img_arr
            image = get_image_from_array(image_data)
            ab = AnnotationBbox(image, (cat_heights[i], cat_weights[i]), frameon=False)
            ax.add_artist(ab)
            if image_data is cat_img_grey_arr:
                cat_count += 1

        # Plot dogs
        dog_count = 0
        for i in range(len(dog_heights)):
            image_data = dog_img_grey_arr if dog_weights[i] < y_achsenabschnitt else dog_img_arr
            image = get_image_from_array(image_data)
            ab = AnnotationBbox(image, (dog_heights[i], dog_weights[i]), frameon=False)
            ax.add_artist(ab)
            if image_data is dog_img_grey_arr:
                dog_count += 1

        # Draw decision boundary
        x_vals = np.linspace(10, 70, 100)
        y_vals = y_achsenabschnitt + 0 * x_vals
        ax.plot(x_vals, y_vals, color='royalblue', label=f'Grenze bei {y_achsenabschnitt:.2f} kg')

        # Bereich einfärben
        ax.fill_between(x_vals, y_vals, 12, color='lightblue', alpha=1, label='kategorisiert als Katze')
        ax.fill_between(x_vals, y_vals, 42, where=(y_vals < 42), color='navajowhite', alpha=1, label='kategorisiert als Hund')

        ax.set_xlim(10, 68)
        ax.set_ylim(12, 42)
        ax.set_xlabel('Größe (cm)')
        ax.set_ylabel('Gewicht (kg)')
        ax.legend()

        plt.show()

    randomY = random.uniform(10, 50)
    w = interactive(plot_counting, y_achsenabschnitt=widgets.FloatSlider(min=10, max=50, step=0.05, value=randomY))
    display(w)


  

def hundOderKatzeMitGerade():

    # Feste Werte für Größe (in cm) und Gewicht (in kg)
    # Daten für Katzen
    cat_heights = [20, 24, 31, 44, 50]  # Größe zwischen 22 und 30 cm
    cat_weights = [30, 20, 15, 25, 30]  # Gewicht zwischen 4 und 8 kg

    # Daten für Hunde
    dog_heights = [18, 30, 35, 60, 45]  # Größe zwischen 45 und 65 cm
    dog_weights = [37, 27, 35, 30, 38]  # Gewicht zwischen 15 und 35 kg

    # Lade Bilder EINMAL als Arrays (schnell und wiederverwendbar)
    cat_img_arr = mpimg.imread('Grafiken/cathead.png')
    cat_img_grey_arr = mpimg.imread('Grafiken/cathead_grey.png')
    dog_img_arr = mpimg.imread('Grafiken/doghead.png')
    dog_img_grey_arr = mpimg.imread('Grafiken/doghead_grey.png')

    def get_image_from_array(arr, zoom=0.2):
        return OffsetImage(arr, zoom=zoom)

    def plot_counting(steigung=1.0, y_achsenabschnitt=0.0):
        fig, ax = plt.subplots()

        # Plot Cats
        cat_count = 0
        for i in range(len(cat_heights)):
            image_data = cat_img_grey_arr if cat_weights[i]>steigung*cat_heights[i]+y_achsenabschnitt else cat_img_arr
            image = get_image_from_array(image_data)
            ab = AnnotationBbox(image, (cat_heights[i], cat_weights[i]), frameon=False)
            ax.add_artist(ab)
            if image_data is cat_img_grey_arr:
                cat_count += 1

        # Plot Dogs
        dog_count = 0
        for i in range(len(dog_heights)):
            image_data = dog_img_grey_arr if dog_weights[i]<steigung*dog_heights[i]+y_achsenabschnitt else dog_img_arr
            image = get_image_from_array(image_data)
            ab = AnnotationBbox(image, (dog_heights[i], dog_weights[i]), frameon=False)
            ax.add_artist(ab)
            if image_data is dog_img_grey_arr:
                dog_count += 1

        # Draw decision boundary
        x_vals = np.linspace(10, 70, 100)
        y_vals = y_achsenabschnitt + steigung * x_vals
        ax.plot(x_vals, y_vals, color='royalblue', label=f'Gerade: y = {steigung:.2f}x + {y_achsenabschnitt:.2f}')

        # Bereich einfärben
        
        ax.fill_between(x_vals, y_vals, 42, where=(y_vals < 42), color='navajowhite', alpha=1, label='kategorisiert als Hund')
        ax.fill_between(x_vals, y_vals, 12, color='lightblue', alpha=1, label='kategorisiert als Katze')

        ax.set_xlim(10, 68)
        ax.set_ylim(12, 42)
        ax.set_xlabel('Größe (cm)')
        ax.set_ylabel('Gewicht (kg)')
        ax.legend()
        
        plt.show()

    randomSteigung = random.uniform(-1,1)
    randomY = random.uniform(10,50)
    # Interaktiver Plot mit anpassbarer Gerade und Möglichkeit, den Plot zu speichern
    interact(plot_counting, 
            steigung=widgets.FloatSlider(min=-1, max=1, step=0.05, value=randomSteigung),
            y_achsenabschnitt=widgets.FloatSlider(min=10, max=50, step=0.05, value=randomY))
         


def hundOderKatzeMitGeradeV1():

    # Feste Werte für Größe (in cm) und Gewicht (in kg)
    # Daten für Katzen
    cat_heights = [20, 24, 31, 44, 50]  # Größe zwischen 22 und 30 cm
    cat_weights = [30, 20, 15, 25, 30]  # Gewicht zwischen 4 und 8 kg

    # Daten für Hunde
    dog_heights = [18, 30, 35, 60, 45]  # Größe zwischen 45 und 65 cm
    dog_weights = [37, 27, 35, 30, 38]  # Gewicht zwischen 15 und 35 kg

    # Lade Bilder EINMAL als Arrays (schnell und wiederverwendbar)
    cat_img_arr = mpimg.imread('Grafiken/cathead.png')
    cat_img_grey_arr = mpimg.imread('Grafiken/cathead_grey.png')
    dog_img_arr = mpimg.imread('Grafiken/doghead.png')
    dog_img_grey_arr = mpimg.imread('Grafiken/doghead_grey.png')

    def get_image_from_array(arr, zoom=0.2):
        return OffsetImage(arr, zoom=zoom)

    def plot_counting(steigung=1.0, y_achsenabschnitt=0.0):
        fig, ax = plt.subplots()

        # Plot Cats
        cat_count = 0
        for i in range(len(cat_heights)):
            image_data = cat_img_grey_arr if cat_weights[i]>steigung*cat_heights[i]+y_achsenabschnitt else cat_img_arr
            image = get_image_from_array(image_data)
            ab = AnnotationBbox(image, (cat_heights[i], cat_weights[i]), frameon=False)
            ax.add_artist(ab)
            if image_data is cat_img_grey_arr:
                cat_count += 1

        # Plot Dogs
        dog_count = 0
        for i in range(len(dog_heights)):
            image_data = dog_img_grey_arr if dog_weights[i]<steigung*dog_heights[i]+y_achsenabschnitt else dog_img_arr
            image = get_image_from_array(image_data)
            ab = AnnotationBbox(image, (dog_heights[i], dog_weights[i]), frameon=False)
            ax.add_artist(ab)
            if image_data is dog_img_grey_arr:
                dog_count += 1

        # Draw decision boundary
        x_vals = np.linspace(10, 70, 100)
        y_vals = y_achsenabschnitt + steigung * x_vals
        ax.plot(x_vals, y_vals, color='royalblue', label=f'Gerade: y = {steigung:.2f}x + {y_achsenabschnitt:.2f}')

        # Bereich einfärben
        
        ax.fill_between(x_vals, y_vals, 42, where=(y_vals < 42), color='navajowhite', alpha=1, label='kategorisiert als Hund')
        ax.fill_between(x_vals, y_vals, 12, color='lightblue', alpha=1, label='kategorisiert als Katze')

        ax.set_xlim(10, 68)
        ax.set_ylim(12, 42)
        ax.set_xlabel('Größe (cm)')
        ax.set_ylabel('Gewicht (kg)')
        ax.legend() # Legende hinzufügen

        # Gesamtabstände ausgeben
        print(f'Anzahl der falsch kategorisierten Katzen: {cat_count:.2f}')
        print(f'Anzahl der falsch kategorisierten Hunde: {dog_count:.2f}')
        print(f'Verlustfunktion - Summe beider Werte:  {cat_count+dog_count:.2f}')

        plt.show()

    randomSteigung = random.uniform(-1,1)
    randomY = random.uniform(10,50)
    # Interaktiver Plot mit anpassbarer Gerade und Möglichkeit, den Plot zu speichern
    interact(plot_counting, 
            steigung=widgets.FloatSlider(min=-1, max=1, step=0.05, value=randomSteigung),
            y_achsenabschnitt=widgets.FloatSlider(min=10, max=50, step=0.05, value=randomY))
 
def hundOderKatzeMitGeradeV2_rect():

    # Feste Werte für Größe (in cm) und Gewicht (in kg)
    # Daten für Katzen
    cat_heights = [20, 24, 31, 44, 50]  # Größe zwischen 22 und 30 cm
    cat_weights = [30, 20, 15, 25, 30]  # Gewicht zwischen 4 und 8 kg

    # Daten für Hunde
    dog_heights = [18, 30, 35, 60, 45]  # Größe zwischen 45 und 65 cm
    dog_weights = [37, 27, 35, 30, 38]  # Gewicht zwischen 15 und 35 kg

    # Bilder laden
    cat_image_path = 'Grafiken/cathead.png'
    cat_image_path_grey = 'Grafiken/cathead_grey.png'
    dog_image_path = 'Grafiken/doghead.png'
    dog_image_path_grey = 'Grafiken/doghead_grey.png'

    def get_image(path, zoom=0.2):  # Angepasste Zoomstufe
        return OffsetImage(mpimg.imread(path), zoom=zoom)

    # Funktion zum Berechnen und Plotten der Abstände zur Geraden
    def plot_with_distances(steigung=1.0, y_achsenabschnitt=0.0):#, save=False):
        fig, ax = plt.subplots()


        # Gerade hinzufügen
        x_vals = np.linspace(10, 70, 100)  # Erzeuge 100 Werte zwischen 10 und 70
        y_vals = y_achsenabschnitt + steigung * x_vals  # Berechne die y-Werte basierend auf der Geradengleichung
        ax.plot(x_vals, y_vals, '--', color='red', label=f'Gerade: y = {steigung:.2f}x + {y_achsenabschnitt:.2f}')

        # Achsenbeschriftungen und -limits setzen
        ax.set_xlim(10, 68)
        ax.set_ylim(12, 42)
        ax.set_xlabel('Größe (cm)')
        ax.set_ylabel('Gewicht (kg)')
        ax.legend()  # Legende hinzufügen

        # Abstände berechnen und anzeigen
        total_distance_cats = 0
        total_distance_dogs = 0

        # Abstände für Katzen (oberhalb der Geraden)
        for i in range(len(cat_heights)):
            y_on_line = steigung * cat_heights[i] + y_achsenabschnitt
            if steigung!=0: 
                #x_on_line_rect = (cat_weights[i]+cat_heights[i]/steigung-y_achsenabschnitt)/(steigung+1/steigung)
                x_on_line_rect = (steigung*cat_weights[i]+cat_heights[i]-steigung*y_achsenabschnitt)/(steigung**2+1)
            else:
                x_on_line_rect = cat_heights[i]
            y_on_line_rect = steigung * x_on_line_rect + y_achsenabschnitt
            if cat_weights[i] > y_on_line:  # nur Katzen oberhalb der Geraden
                distance = math.sqrt((cat_weights[i] - y_on_line_rect)**2 + (cat_heights[i] - x_on_line_rect)**2)
                total_distance_cats += distance
                # Linie für distanz zeichnen
                ax.plot([x_on_line_rect, cat_heights[i]], [y_on_line_rect, cat_weights[i]], 'b-')
                ab = AnnotationBbox(get_image(cat_image_path_grey), (cat_heights[i], cat_weights[i]), frameon=False)
            else:
                ab = AnnotationBbox(get_image(cat_image_path), (cat_heights[i], cat_weights[i]), frameon=False)
            ax.add_artist(ab)
            

        # Abstände für Hunde (unterhalb der Geraden)
        for i in range(len(dog_heights)):
            y_on_line = steigung * dog_heights[i] + y_achsenabschnitt
            if steigung != 0:
                #x_on_line_rect = (dog_weights[i]+dog_heights[i]/steigung-y_achsenabschnitt)/(steigung+1/steigung)
                x_on_line_rect = (steigung*dog_weights[i]+dog_heights[i]-steigung*y_achsenabschnitt)/(steigung**2+1)
            else:
                x_on_line_rect = dog_heights[i]
            y_on_line_rect = steigung * x_on_line_rect + y_achsenabschnitt
            if dog_weights[i] < y_on_line:  # nur Hunde unterhalb der Geraden
                distance = math.sqrt((dog_weights[i] - y_on_line_rect)**2 + (dog_heights[i] - x_on_line_rect)**2)
                total_distance_dogs += distance
                # Linie für distanz zeichnen
                ax.plot([dog_heights[i], x_on_line_rect], [dog_weights[i], y_on_line_rect], 'g-')
                ab = AnnotationBbox(get_image(dog_image_path_grey), (dog_heights[i], dog_weights[i]), frameon=False)
            else:
                ab = AnnotationBbox(get_image(dog_image_path), (dog_heights[i], dog_weights[i]), frameon=False)
            ax.add_artist(ab) 

        # Gesamtabstände ausgeben
        print(f'Abstand der falsch kategorisierten Katzen zur Geraden: {total_distance_cats:.2f}')
        print(f'Abstand der falsch kategorisierten Hunde zur Geraden: {total_distance_dogs:.2f}')
        print(f'Verlustfunktion - Summe der Abstände:  {total_distance_cats+total_distance_dogs:.2f}')

        plt.show()

    randomSteigung = random.uniform(-1,1)
    randomY = random.uniform(10,50)
    # Interaktiver Plot mit anpassbarer Gerade und Möglichkeit, den Plot zu speichern 
    interact(plot_with_distances, 
            steigung=widgets.FloatSlider(min=-1, max=1, step=0.05, value=randomSteigung),
            y_achsenabschnitt=widgets.FloatSlider(min=10, max=50, step=0.05, value=randomY))

    
def hundOderKatzeMitGeradeV2():

    # Feste Werte für Größe (in cm) und Gewicht (in kg)
    # Daten für Katzen
    cat_heights = [20, 24, 31, 44, 50]  # Größe zwischen 22 und 30 cm
    cat_weights = [30, 20, 15, 25, 30]  # Gewicht zwischen 4 und 8 kg

    # Daten für Hunde
    dog_heights = [18, 30, 35, 60, 45]  # Größe zwischen 45 und 65 cm
    dog_weights = [37, 27, 35, 30, 38]  # Gewicht zwischen 15 und 35 kg

    # Lade Bilder EINMAL als Arrays (schnell und wiederverwendbar)
    cat_img_arr = mpimg.imread('Grafiken/cathead.png')
    cat_img_grey_arr = mpimg.imread('Grafiken/cathead_grey.png')
    dog_img_arr = mpimg.imread('Grafiken/doghead.png')
    dog_img_grey_arr = mpimg.imread('Grafiken/doghead_grey.png')

    def get_image_from_array(arr, zoom=0.2):
        return OffsetImage(arr, zoom=zoom)

    def plot_with_distances(steigung=1.0, y_achsenabschnitt=0.0):
        fig, ax = plt.subplots()

        # Abstände berechnen und anzeigen
        total_distance_cats = 0
        total_distance_dogs = 0
        
        for i in range(len(cat_heights)):
            y_on_line = steigung * cat_heights[i] + y_achsenabschnitt
            if cat_weights[i]>y_on_line:
                image_data = cat_img_grey_arr
                distance = cat_weights[i] - y_on_line
                total_distance_cats += distance
                # Linie für distanz zeichnen
                ax.plot([cat_heights[i], cat_heights[i]], [y_on_line, cat_weights[i]], 'b-')
            else: 
                image_data = cat_img_arr
            image = get_image_from_array(image_data)
            ab = AnnotationBbox(image, (cat_heights[i], cat_weights[i]), frameon=False)
            ax.add_artist(ab)
            #if image_data is cat_img_grey_arr:
            #    cat_count += 1

        
        for i in range(len(dog_heights)):
            y_on_line = steigung*dog_heights[i]+y_achsenabschnitt
            if dog_weights[i]<y_on_line:
                image_data = dog_img_grey_arr 
                distance = y_on_line - dog_weights[i]
                total_distance_dogs += distance
                # Linie für distanz zeichnen
                ax.plot([dog_heights[i], dog_heights[i]], [dog_weights[i], y_on_line], 'g-')
            else:
                image_data = dog_img_arr
            image = get_image_from_array(image_data)
            ab = AnnotationBbox(image, (dog_heights[i], dog_weights[i]), frameon=False)
            ax.add_artist(ab)
            #if image_data is dog_img_grey_arr:
            #    dog_count += 1

        # Draw decision boundary
        x_vals = np.linspace(10, 70, 100)
        y_vals = y_achsenabschnitt + steigung * x_vals
        ax.plot(x_vals, y_vals, color='royalblue', label=f'Gerade: y = {steigung:.2f}x + {y_achsenabschnitt:.2f}')

        # Bereich einfärben
        
        ax.fill_between(x_vals, y_vals, 42, where=(y_vals < 42), color='navajowhite', alpha=1, label='kategorisiert als Hund')
        ax.fill_between(x_vals, y_vals, 12, color='lightblue', alpha=1, label='kategorisiert als Katze')

        ax.set_xlim(10, 68)
        ax.set_ylim(12, 42)
        ax.set_xlabel('Größe (cm)')
        ax.set_ylabel('Gewicht (kg)')
        ax.legend()

        # Gesamtabstände ausgeben
        print(f'Gewichtsdifferenzen der falsch kategorisierten Katzen: {total_distance_cats:.2f}')
        print(f'Gewichtsdifferenzen der falsch kategorisierten Hunde: {total_distance_dogs:.2f}')
        print(f'Verlustfunktion - Summe beider Werte:  {total_distance_cats+total_distance_dogs:.2f}')

        plt.show()

    randomSteigung = random.uniform(-1,1)
    randomY = random.uniform(10,50)
    # Interaktiver Plot mit anpassbarer Gerade und Möglichkeit, den Plot zu speichern 
    interact(plot_with_distances, 
            steigung=widgets.FloatSlider(min=-1, max=1, step=0.05, value=randomSteigung),
            y_achsenabschnitt=widgets.FloatSlider(min=10, max=50, step=0.05, value=randomY))

def krankenkassen(krankenkasse):

    hoffset = 140
    woffset = 50
    cat_heights = [20, 24, 31, 44, 50]  # Größe zwischen 22 und 30 cm
    cat_weights = [30, 20, 15, 25, 30]  # Gewicht zwischen 4 und 8 kg

    cat_heights = [height+hoffset for height in cat_heights] 
    cat_weights = [weight+woffset for weight in cat_weights] 


    # Daten für Hunde
    dog_heights = [18, 30, 35, 60, 45]  # Größe zwischen 45 und 65 cm
    dog_weights = [37, 27, 35, 30, 38]  # Gewicht zwischen 15 und 35 kg

    dog_heights = [height+hoffset for height in dog_heights] 
    dog_weights = [weight+woffset for weight in dog_weights] 

    # Lade Bilder EINMAL als Arrays (schnell und wiederverwendbar)
    cat_img_arr=[]
    cat_img_grey_arr=[]
    dog_img_arr=[]
    dog_img_grey_arr=[]

    for i in range(len(cat_heights)):
        cat_img_arr.append(mpimg.imread('Grafiken/person'+str(i+1)+'a.png'))
        cat_img_grey_arr.append(mpimg.imread('Grafiken/person'+str(i+1)+'ab.png'))
        dog_img_arr.append(mpimg.imread('Grafiken/person'+str(i+6)+'a_krank.png'))
        dog_img_grey_arr.append(mpimg.imread('Grafiken/person'+str(i+6)+'ab_krank.png'))

    def get_image_from_array(arr, zoom=0.07):
        return OffsetImage(arr, zoom=zoom)

    def plot_with_distances(steigung=1.0, y_achsenabschnitt=0.0):
        fig, ax = plt.subplots()

        # Abstände berechnen und anzeigen
        total_distance_cats = 0
        total_distance_dogs = 0
        
        for i in range(len(cat_heights)):
            y_on_line = steigung * (cat_heights[i]-150) + y_achsenabschnitt
            if cat_weights[i]>y_on_line:
                image_data = cat_img_grey_arr[i]
                distance = cat_weights[i] - y_on_line
                total_distance_cats += distance
                # Linie für distanz zeichnen
                ax.plot([cat_heights[i], cat_heights[i]], [y_on_line, cat_weights[i]], 'b-')
            else: 
                image_data = cat_img_arr[i]
            image = get_image_from_array(image_data)
            ab = AnnotationBbox(image, (cat_heights[i], cat_weights[i]), frameon=False)
            ax.add_artist(ab)
            #if image_data is cat_img_grey_arr:
            #    cat_count += 1

        
        for i in range(len(dog_heights)):
            y_on_line = steigung * (dog_heights[i]-150) + y_achsenabschnitt
            if dog_weights[i]<y_on_line:
                image_data = dog_img_grey_arr[i]
                distance = y_on_line - dog_weights[i]
                total_distance_dogs += distance
                # Linie für distanz zeichnen
                ax.plot([dog_heights[i], dog_heights[i]], [dog_weights[i], y_on_line], 'g-')
            else:
                image_data = dog_img_arr[i]
            image = get_image_from_array(image_data)
            ab = AnnotationBbox(image, (dog_heights[i], dog_weights[i]), frameon=False)
            ax.add_artist(ab)


        # Gerade hinzufügen
        x_vals = np.linspace(148, 208, 100)  # Erzeuge 100 Werte zwischen 10 und 70
        y_vals = y_achsenabschnitt + steigung * (x_vals-150)  # Berechne die y-Werte basierend auf der Geradengleichung
        ax.plot(x_vals, y_vals, color='royalblue', label=f'Gerade: y = {steigung:.2f} * (x-150) + {y_achsenabschnitt:.2f}')

        # Bereich einfärben
        
        ax.fill_between(x_vals, y_vals, 92, where=(y_vals < 92), color='navajowhite', alpha=1, label='kategorisiert als krank')
        ax.fill_between(x_vals, y_vals, 62, color='lightblue', alpha=1, label='kategorisiert als gesund')

        # Achsenbeschriftungen und -limits setzen
        ax.set_xlim(148, 208)
        ax.set_ylim(62, 92)
        ax.set_xlabel('Größe (cm)')
        ax.set_ylabel('Gewicht (kg)')
        ax.legend()

        # Gesamtabstände ausgeben
        print(f'Gewichtsdifferenzen der falsch kategorisierten gesunden Personen: {total_distance_cats:.2f}')
        print(f'Gewichtsdifferenzen der falsch kategorisierten kranken Personen: {total_distance_dogs:.2f}')

        plt.title(krankenkasse)
        plt.show()

    randomSteigung = random.uniform(-1,1)
    randomY = random.uniform(10,50)
    # Interaktiver Plot mit anpassbarer Gerade und Möglichkeit, den Plot zu speichern 
    interact(plot_with_distances, 
            steigung=widgets.FloatSlider(min=-1, max=1, step=0.05, value=randomSteigung),
            y_achsenabschnitt=widgets.FloatSlider(min=10, max=150, step=0.05, value=randomY))
            #,save=widgets.Checkbox(value=False, description='Plot speichern'))

def zweiGeraden():
    def plot_with_new_function(w1=0.3, b1=17.0, w2=0.3, b2=17.0):
        fig, ax = plt.subplots()

        # Neue Funktion definieren
        def new_function(x):
            y_cat = w1 * x + b1
            y_dog = w2 * x + b2
            return y_cat + y_dog
        
        x_vals = np.linspace(10, 70, 100)  # Erzeuge 100 Werte zwischen 10 und 70
        y_new = new_function(x_vals)
        ax.plot(x_vals, y_new, '-', color='purple', label=f'{round(w1,2)} * x + {round(b1,2)} + {round(w2,2)} * x + {round(b2,2)}')
        ax.plot(x_vals, w1 * x_vals + b1, '--', color='grey', label=f'{round(w1,2)} * x + {round(b1,2)}')
        ax.plot(x_vals, w2 * x_vals + b2, '--', color='grey', label=f'{round(w2,2)} * x + {round(b2,2)}')
        ax.legend()  # Legende aktualisieren

        plt.show()

    rw1=round(random.uniform(-2,2), 2)
    rb1=round(random.uniform(-50,50), 2)
    rw2=round(random.uniform(-2,2), 2)
    rb2=round(random.uniform(-50,50), 2)
    # Interaktiver Plot mit anpassbarer Funktion und Möglichkeit, den Plot zu speichern
    interact(plot_with_new_function, 
            w1=widgets.FloatSlider(min=-2, max=2, step=0.05, value=rw1),
            b1=widgets.FloatSlider(min=-50, max=50, step=0.05, value=rb1),
            w2=widgets.FloatSlider(min=-2, max=2, step=0.05, value=rw2),
            b2=widgets.FloatSlider(min=-50, max=50, step=0.05, value=rb2))


def einNeuron():
    def plot_with_new_function(w1=0.3, b1=17.0):
        fig, ax = plt.subplots()

        # Neue Funktion definieren
        def new_function(x):
            y = np.maximum(0, w1 * x + b1)
            return y
        
        x_vals = np.linspace(0, 100, 100)  # Erzeuge 100 Werte zwischen 10 und 70
        y_new = new_function(x_vals)

        ax.set_xlim(0, 100)
        ax.set_ylim(-20, 50)
        ax.plot(x_vals, y_new, '-', color='purple', label=f'Neuronengleichung')
        ax.plot(x_vals, w1 * x_vals + b1, '--', color='grey', label=f'{round(w1,2)} * x + {round(b1,2)}')
        ax.legend()  # Legende aktualisieren
  
        plt.show()

    rw1=round(random.uniform(-2,2), 2)
    rb1=round(random.uniform(-50,50), 2)
    # Interaktiver Plot mit anpassbarer Funktion und Möglichkeit, den Plot zu speichern
    interact(plot_with_new_function, 
            w1=widgets.FloatSlider(min=-2, max=2, step=0.05, value=rw1),
            b1=widgets.FloatSlider(min=-50, max=50, step=0.05, value=rb1))

def zweiNeuronen():
    def plot_with_new_function(w1=0.3, b1=17.0, w2=0.3, b2=17.0):
        fig, ax = plt.subplots()

        # Neue Funktion definieren
        def new_function(x):
            y = np.maximum(0, w1 * x + b1)
            z = np.maximum(0, w2 * x + b2)
            return y+z
        
        x_vals = np.linspace(0, 100, 100)  # Erzeuge 100 Werte zwischen 10 und 70
        y_new = new_function(x_vals)

        ax.set_xlim(0, 100)
        ax.set_ylim(-20, 50)
        ax.plot(x_vals, y_new, '-', color='purple', label=f'2 Neuronen addiert')
        ax.plot(x_vals, w1 * x_vals + b1, '--', color='grey', label=f'{round(w1,2)} * x + {round(b1,2)}')
        ax.plot(x_vals, w2 * x_vals + b2, '--', color='grey', label=f'{round(w2,2)} * x + {round(b2,2)}')
        ax.legend()  # Legende aktualisieren
  
        plt.show()

    rw1=round(random.uniform(-2,2), 2)
    rb1=round(random.uniform(-50,50), 2)
    rw2=round(random.uniform(-2,2), 2)
    rb2=round(random.uniform(-50,50), 2)
    # Interaktiver Plot mit anpassbarer Funktion und Möglichkeit, den Plot zu speichern
    interact(plot_with_new_function, 
            w1=widgets.FloatSlider(min=-2, max=2, step=0.05, value=rw1),
            b1=widgets.FloatSlider(min=-100, max=100, step=0.05, value=rb1),
            w2=widgets.FloatSlider(min=-2, max=2, step=0.05, value=rw2),
            b2=widgets.FloatSlider(min=-100, max=100, step=0.05, value=rb2))
            #,save=widgets.Checkbox(value=False, description='Plot speichern'))

def hundOderKatzeZweiNeuronen():
    # Feste Werte für Größe (in cm) und Gewicht (in kg)
    # Daten für Katzen
    cat_heights = [20, 24, 31, 44, 50]  # Größe zwischen 20 und 50 cm
    cat_weights = [30, 20, 15, 25, 30]  # Gewicht zwischen 15 und 30 kg

    # Daten für Hunde
    dog_heights = [18, 30, 35, 60, 45]  # Größe zwischen 18 und 60 cm
    dog_weights = [37, 27, 35, 30, 38]  # Gewicht zwischen 27 und 38 kg

    # Bilder laden
    cat_image_path = 'Grafiken/cathead.png'
    cat_image_path_grey = 'Grafiken/cathead_grey.png'
    dog_image_path = 'Grafiken/doghead.png'
    dog_image_path_grey = 'Grafiken/doghead_grey.png'

    def get_image(path, zoom=0.2):  # Angepasste Zoomstufe
        return OffsetImage(mpimg.imread(path), zoom=zoom)

    # Funktion zum Berechnen und Plotten der Abstände zur neuen Funktion
    def plot_with_new_function(w1=0.3, b1=17.0, w2=0.3, b2=17.0):
        fig, ax = plt.subplots()

        # Achsenbeschriftungen und -limits setzen
        ax.set_xlim(10, 68)
        ax.set_ylim(12, 42)
        ax.set_xlabel('Größe (cm)')
        ax.set_ylabel('Gewicht (kg)')
    # ax.legend()  # Legende hinzufügen

        # Neue Funktion definieren
        def new_function(x):
            y_cat = np.maximum(0, w1 * x + b1)
            y_dog = np.maximum(0, w2 * x + b2)
            return y_cat + y_dog
        
        x_vals = np.linspace(10, 70, 100)  # Erzeuge 100 Werte zwischen 10 und 70 | max(0,{w1} * x + {b1}) + max(0,{w2} * x + {b2})
        y_new = new_function(x_vals)
        ax.plot(x_vals, y_new, '-', color='purple', label=f'2 Neuronen addiert')
        ax.legend()  # Legende aktualisieren

        # Abstände berechnen und anzeigen
        total_distance_cats_above = 0
        total_distance_dogs_below = 0

        # Abstände für Katzen
        for i in range(len(cat_heights)):
            y_on_line = new_function(cat_heights[i])
            if cat_weights[i] > y_on_line:  # nur Katzen oberhalb der Geraden
                distance = cat_weights[i] - y_on_line
                total_distance_cats_above += distance
                # Linie für distanz zeichnen
                ax.plot([cat_heights[i], cat_heights[i]], [y_on_line, cat_weights[i]], 'b-')
                ab = AnnotationBbox(get_image(cat_image_path_grey), (cat_heights[i], cat_weights[i]), frameon=False)
            else:
                ab = AnnotationBbox(get_image(cat_image_path), (cat_heights[i], cat_weights[i]), frameon=False)
            ax.add_artist(ab)

        # Abstände für Hunde
        for i in range(len(dog_heights)):
            y_on_line = new_function(dog_heights[i])
            if dog_weights[i] < y_on_line:  # nur Hunde unterhalb der Geraden
                distance = y_on_line - dog_weights[i]
                total_distance_dogs_below += distance
                # Linie für distanz zeichnen
                ax.plot([dog_heights[i], dog_heights[i]], [dog_weights[i], y_on_line], 'g-')
                ab = AnnotationBbox(get_image(dog_image_path_grey), (dog_heights[i], dog_weights[i]), frameon=False)
            else:
                ab = AnnotationBbox(get_image(dog_image_path), (dog_heights[i], dog_weights[i]), frameon=False)
            ax.add_artist(ab) 

        # Gesamtabstände ausgeben
        print(f'Gewichtsdifferenzen der falsch kategorisierten Katzen: {total_distance_cats_above:.2f}')
        print(f'Gewichtsdifferenzen der falsch kategorisierten Hunde: {total_distance_dogs_below:.2f}')
        print(f'Verlustfunktion - Summe beider Werte: {total_distance_cats_above + total_distance_dogs_below:.2f}')
        
        plt.show()

    rw1=round(random.uniform(-2,1), 2)
    rb1=round(random.uniform(0,50), 2)
    rw2=round(random.uniform(-0.5,2), 2)
    rb2=round(random.uniform(-10,20), 2)
    # Interaktiver Plot mit anpassbarer Funktion und Möglichkeit, den Plot zu speichern
    interact(plot_with_new_function, 
            w1=widgets.FloatSlider(min=-2, max=1, step=0.05, value=rw1),
            b1=widgets.FloatSlider(min=0, max=50, step=0.05, value=rb1),
            w2=widgets.FloatSlider(min=-0.5, max=2, step=0.05, value=rw2),
            b2=widgets.FloatSlider(min=-10, max=20, step=0.05, value=rb2))
            #,save=widgets.Checkbox(value=False, description='Plot speichern'))

def hundOderKatzeNNtesten(größe=50,gewicht=10):

    class SimpleNN(nn.Module):
        def __init__(self):
            super(SimpleNN, self).__init__()
            self.fc1 = nn.Linear(2, 10)
            self.fc2 = nn.Linear(10, 10)
            self.fc3 = nn.Linear(10, 10)
            self.fc4 = nn.Linear(10, 10)
            self.fc5 = nn.Linear(10, 10)
            self.fc6 = nn.Linear(10, 10)
            self.fc7 = nn.Linear(10, 10)
            self.fc8 = nn.Linear(10, 10)
            self.fc9 = nn.Linear(10, 10)
            self.fc10 = nn.Linear(10, 10)
            self.fc11 = nn.Linear(10, 10)
            self.fc12 = nn.Linear(10, 10)
            self.fc13 = nn.Linear(10, 10)
            self.fc14 = nn.Linear(10, 10)
            self.fc15 = nn.Linear(10, 10)
            self.fc16 = nn.Linear(10, 10)
            self.fc17 = nn.Linear(10, 10)
            self.fc18 = nn.Linear(10, 10)
            self.fc19 = nn.Linear(10, 10)
            self.fc20 = nn.Linear(10, 1)
            self.relu = nn.ReLU()
            self.sigmoid = nn.Sigmoid()

        def forward(self, x):
            x = self.relu(self.fc1(x))
            x = self.relu(self.fc2(x))
            x = self.relu(self.fc3(x))
            x = self.relu(self.fc4(x))
            x = self.relu(self.fc5(x))
            x = self.relu(self.fc6(x))
            x = self.relu(self.fc7(x))
            x = self.relu(self.fc8(x))
            x = self.relu(self.fc9(x))
            x = self.relu(self.fc10(x))
            x = self.relu(self.fc11(x))
            x = self.relu(self.fc12(x))
            x = self.relu(self.fc13(x))
            x = self.relu(self.fc14(x))
            x = self.relu(self.fc15(x))
            x = self.relu(self.fc16(x))
            x = self.relu(self.fc17(x))
            x = self.relu(self.fc18(x))
            x = self.relu(self.fc19(x))
            x = self.sigmoid(self.fc20(x))
            return x

    # Modell laden
    model_path="Beispiel-Modelle/Modelle/katzeOderHundGrößeGewicht.pth"
    model = SimpleNN()  # Initialisiere das Modell
    model.load_state_dict(torch.load(model_path, weights_only=True))
    model.eval()  # Setze das Modell in den Evaluationsmodus
    #print("Modell erfolgreich geladen!")
    # Beispielvorhersage
    test_data = torch.tensor([[größe, gewicht]], dtype=torch.float32)  # Größe und Gewicht
    prediction = model(test_data)
    hundchance = round(prediction.item(),3)
    katzchance = 1 - hundchance
    print(f"Vorhersage für {größe} kg und {gewicht} cm:")
    print(f"Hund:  {hundchance}")
    print(f"Katze: {katzchance}")
    

def hundOderKatzeNNtrainieren(epochen=1000):
    # Originaldaten
    cat_heights = np.array([20, 24, 31, 44, 50], dtype=np.float32).reshape(-1, 1)
    cat_weights = np.array([30, 20, 15, 25, 30], dtype=np.float32).reshape(-1, 1)

    dog_heights = np.array([18, 30, 35, 60, 45], dtype=np.float32).reshape(-1, 1)
    dog_weights = np.array([37, 27, 35, 30, 38], dtype=np.float32).reshape(-1, 1)

    # Zusätzliche Datenpunkte generieren
    #np.random.seed(42)
    additional_cat_heights = [[28.72700594], [57.53571532], [46.59969709], [39.93292421], [17.80093202], [17.79972602], [12.90418061], [53.30880729], [40.05575059], [45.40362889], [11.02922471], [58.49549261], [51.62213204], [20.61695553], [19.09124836], [19.17022549], [25.21211215], [36.23782158], [31.59725093], [24.56145701], [40.59264474], [16.97469303], [24.60723243], [28.31809216], [32.80349921], [49.25879807], [19.98368911], [35.71172192], [39.62072844], [12.32252064]]
    additional_cat_weights = [[22.15089704], [13.41048247], [11.30103186], [28.97771075], [29.31264066], [26.16794696], [16.09227538], [11.95344228], [23.68466053], [18.80304987], [12.4407647], [19.9035382], [10.68777042], [28.18640804], [15.17559963], [23.25044569], [16.23422152], [20.40136042], [20.93420559], [13.69708911], [29.39169256], [25.50265647], [28.78997883], [27.89654701], [21.95799958], [28.4374847], [11.76985004], [13.91965725], [10.90454578], [16.50660662]]

    additional_dog_heights = [[33.32063738], [26.28094191], [59.72425055], [31.4051996], [26.85607058], [42.56176499], [18.4554535], [58.13181885], [14.47303862], [69.2132162], [56.33468616], [21.92294089], [10.33132703], [58.92768571], [52.41144063], [53.74043008], [56.2762208], [14.4426791], [31.50794371], [16.95214357], [61.78620555], [47.39788761], [29.85388149], [13.81350102], [28.6589393], [29.51099932], [53.7763707], [48.25344828], [63.23276455], [38.33289551]]
    additional_dog_weights = [[27.39188492], [39.26489574], [40.21570097], [36.22554395], [40.4193436], [34.87591193], [35.45465659], [33.55082037], [25.50838253], [27.15782854], [25.62858371], [37.72820823], [31.28711962], [35.17141382], [43.15132948], [29.98584458], [33.20765846], [40.11102277], [29.57596331], [26.5395982], [30.79502906], [28.22442575], [43.59395305], [41.16240759], [37.66807513], [42.4292118], [41.07344154], [28.73140118], [42.85117997], [35.78684484]]


    # Kombiniere die Originaldaten mit den zusätzlichen Datenpunkten
    all_cat_heights = np.vstack((cat_heights, additional_cat_heights))
    all_cat_weights = np.vstack((cat_weights, additional_cat_weights))

    all_dog_heights = np.vstack((dog_heights, additional_dog_heights))
    all_dog_weights = np.vstack((dog_weights, additional_dog_weights))

    # Labels erstellen: 0 für Katzen, 1 für Hunde
    cat_labels = np.zeros((all_cat_heights.shape[0], 1))
    dog_labels = np.ones((all_dog_heights.shape[0], 1))

    # Daten und Labels kombinieren
    all_heights = np.vstack((all_cat_heights, all_dog_heights))
    all_weights = np.vstack((all_cat_weights, all_dog_weights))
    all_labels = np.vstack((cat_labels, dog_labels))

    # Kombiniere Höhen und Gewichte zu Eingabedaten
    all_data = np.hstack((all_heights, all_weights))

    # In Tensoren konvertieren
    data_tensor = torch.tensor(all_data, dtype=torch.float32)
    labels_tensor = torch.tensor(all_labels, dtype=torch.float32)

    # Definiere das neuronale Netzwerk
    class SimpleNN(nn.Module):
        def __init__(self):
            super(SimpleNN, self).__init__()
            self.fc1 = nn.Linear(2, 10)
            self.fc2 = nn.Linear(10, 10)
            self.fc3 = nn.Linear(10, 10)
            self.fc4 = nn.Linear(10, 10)
            self.fc5 = nn.Linear(10, 10)
            self.fc6 = nn.Linear(10, 10)
            self.fc7 = nn.Linear(10, 10)
            self.fc8 = nn.Linear(10, 10)
            self.fc9 = nn.Linear(10, 10)
            self.fc10 = nn.Linear(10, 10)
            self.fc11 = nn.Linear(10, 10)
            self.fc12 = nn.Linear(10, 10)
            self.fc13 = nn.Linear(10, 10)
            self.fc14 = nn.Linear(10, 10)
            self.fc15 = nn.Linear(10, 10)
            self.fc16 = nn.Linear(10, 10)
            self.fc17 = nn.Linear(10, 10)
            self.fc18 = nn.Linear(10, 10)
            self.fc19 = nn.Linear(10, 10)
            self.fc20 = nn.Linear(10, 1)
            self.relu = nn.ReLU()
            self.sigmoid = nn.Sigmoid()

        def forward(self, x):
            x = self.relu(self.fc1(x))
            x = self.relu(self.fc2(x))
            x = self.relu(self.fc3(x))
            x = self.relu(self.fc4(x))
            x = self.relu(self.fc5(x))
            x = self.relu(self.fc6(x))
            x = self.relu(self.fc7(x))
            x = self.relu(self.fc8(x))
            x = self.relu(self.fc9(x))
            x = self.relu(self.fc10(x))
            x = self.relu(self.fc11(x))
            x = self.relu(self.fc12(x))
            x = self.relu(self.fc13(x))
            x = self.relu(self.fc14(x))
            x = self.relu(self.fc15(x))
            x = self.relu(self.fc16(x))
            x = self.relu(self.fc17(x))
            x = self.relu(self.fc18(x))
            x = self.relu(self.fc19(x))
            x = self.sigmoid(self.fc20(x))
            return x

    # Initialisiere das Netzwerk
    model = SimpleNN()

    # Verlustfunktion und Optimizer
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    # Training des Netzes
    def train_model(model, data, labels, epochs=epochen):
        model.train()
        for epoch in range(epochs):
            optimizer.zero_grad()

            outputs = model(data)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            if (epoch + 1) % 100 == 0:
                print(f'Epoche [{epoch+1}/{epochs}], Verlust: {loss.item():.4f}')
                

    train_model(model, data_tensor, labels_tensor)

    # Visualisiere die Ergebnisse
    def plot_data_and_decision_boundary(model, data, labels):
        plt.figure(figsize=(10, 6))

        # Gesamtdaten plotten
        plt.scatter(all_cat_heights, all_cat_weights, color='blue', label='Katzen')
        plt.scatter(all_dog_heights, all_dog_weights, color='red', label='Hunde')

        # Entscheidunggrenze plotten
        x_min, x_max = all_heights.min() - 1, all_heights.max() + 1
        y_min, y_max = all_weights.min() - 1, all_weights.max() + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                            np.arange(y_min, y_max, 0.1))
        grid = np.c_[xx.ravel(), yy.ravel()]
        grid_tensor = torch.tensor(grid, dtype=torch.float32)
        with torch.no_grad():
            decision_boundary = model(grid_tensor).numpy().reshape(xx.shape)
        contour = plt.contourf(xx, yy, decision_boundary, alpha=0.5, cmap='coolwarm', levels=np.linspace(0, 1, 11))
        plt.colorbar(contour, ticks=np.linspace(0, 1, 11))
        
        # Achsenbeschriftungen und Titel setzen
        # plt.title('Wahrscheinlichkeit Hund')
        plt.xlabel('Größe (cm)')
        plt.ylabel('Gewicht (kg)')
        #plt.title('Scatterplot von Katzen und Hunden mit Entscheidunggrenze')
        plt.legend()
        plt.show()

    plot_data_and_decision_boundary(model, data_tensor, labels_tensor)

def zeigeBeispielBilder(projektname):
    #laden der bilder in fns
    path = Path(f'Beispiel-Modelle/{projektName}')
    fns = get_image_files(path)
    daten = DataBlock(
    blocks=(ImageBlock, CategoryBlock), 
    get_items=get_image_files, 
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=Resize(128))
    dls = daten.dataloaders(path)
    dls.valid.show_batch(max_n=8, nrows=2)

def testeBildInModell(projektname, bildname):

    def andereKat(zahl):
        if zahl==tensor(1): return tensor(0)
        if zahl==tensor(0): return tensor(1)

    im = Image.open(f'Beispiel-Modelle/Testbilder/{bildname}')
    #frag das Modell, ob es sich beim Bild um x oder y handelt.
    
    #load pkl-model
    if platform.system() == "Linux":
        learn_inf = load_learner(f'Beispiel-Modelle/Modelle/{projektname}-linux.pkl')
    elif platform.system() == "Windows":
        learn_inf = load_learner(f'Beispiel-Modelle/Modelle/{projektname}.pkl')
    
    #predict for image 'blabla.jpeg'
    img = PILImage.create(f'Beispiel-Modelle/Testbilder/{bildname}') 
    pred,pred_idx,probs = learn_inf.predict(img)
    #gebe die prediction aus
    print(f'Das Bild ist zu {probs[pred_idx]*100:.2f}% {learn_inf.dls.vocab[pred_idx].capitalize()} und zu {100-probs[pred_idx]*100:.2f}% {learn_inf.dls.vocab[andereKat(pred_idx)].capitalize()}.')
    return im.to_thumb(256,256)

def uploadBild():
    #global upload
    upload = FileUpload(multiple=False)
    return upload

def testeUploadInModell(upload):
    warnings.filterwarnings("ignore")
    projektname = 'hund oder katze'
    def andereKat(zahl):
        if zahl==tensor(1): return tensor(0)
        if zahl==tensor(0): return tensor(1)

    im = PILImage.create(upload.data[0])

    #load pkl-model
    if platform.system() == "Linux":
        learn_inf = load_learner(f'Beispiel-Modelle/Modelle/{projektname}-linux.pkl')
    elif platform.system() == "Windows":
        learn_inf = load_learner(f'Beispiel-Modelle/Modelle/{projektname}.pkl')
    
    #predict for image 'blabla.jpeg'
    pred,pred_idx,probs = learn_inf.predict(im)
    
    #gebe die prediction aus
    print(f'Das Bild ist zu {probs[pred_idx]*100:.2f}% {learn_inf.dls.vocab[pred_idx].capitalize()} und zu {100-probs[pred_idx]*100:.2f}% {learn_inf.dls.vocab[andereKat(pred_idx)].capitalize()}.')
    return im.to_thumb(256,256)    


def trainingsdatenAnzeigen(name, num_cols=5, figsize=(9, 2)):
    """
    Zeigt Bilder aus den Unterordnern eines Hauptordners in einem Raster an.
    
    Args:
        name (str): Pfad zum Hauptordner, der die Unterordner mit den Bildern enthält.
        num_cols (int): Anzahl der Spalten im Raster.
        figsize (tuple): Größe der gesamten Abbildung.
    """
    main_folder = "Beispiel-Modelle/Trainingsdaten/" + name
    
    def load_images_from_subfolders(folder):
        images = []
        for subfolder in os.listdir(folder):
            subfolder_path = os.path.join(folder, subfolder)
            if os.path.isdir(subfolder_path):
                for filename in os.listdir(subfolder_path):
                    img_path = os.path.join(subfolder_path, filename)
                    if os.path.isfile(img_path) and img_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                        try:
                            with open(img_path, 'rb') as f:
                                img = mpimg.imread(f)
                            images.append((img_path, subfolder))
                        except (UnidentifiedImageError, OSError, SyntaxError):
                            print(f"Überspringe ungültige Bilddatei: {img_path}")
        return images

    # Lade die Bilder
    images = load_images_from_subfolders(main_folder)

    # Anzahl der Bilder
    num_images = len(images)

    # Debug-Ausgabe
    print(f"Gesamtanzahl der Bilder: {num_images}")

    # Berechne die Anzahl der Zeilen
    num_rows = num_images // num_cols + int(num_images % num_cols != 0)

    # Erstelle die Plotfigur
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(figsize[0], num_rows * figsize[1]))

    # Zeige die Bilder und Bildunterschriften
    for i, ax in enumerate(axes.flat):
        if i < num_images:
            img_path, label = images[i]
            img = mpimg.imread(img_path)
            ax.imshow(img)
            ax.set_title(label)
        ax.axis('off')

    plt.tight_layout()
    return plt.show()

def beispielbilderAnzeigen(num_cols=5, figsize=(9, 2)):
    """
    Zeigt Bilder aus den Unterordnern eines Hauptordners in einem Raster an.
    
    Args:
        name (str): Pfad zum Hauptordner, der die Unterordner mit den Bildern enthält.
        num_cols (int): Anzahl der Spalten im Raster.
        figsize (tuple): Größe der gesamten Abbildung.
    """
    main_folder = "Testbilder"
    
    def take2(vector):
        return vector[1]

    def load_images(folder):
        images = []
        main_folder_path = main_folder
        for filename in os.listdir(main_folder_path):
            img_path = os.path.join(main_folder_path, filename)
            if os.path.isfile(img_path) and img_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                try:
                    with open(img_path, 'rb') as f:
                        img = mpimg.imread(f)
                    images.append((img_path, filename))
                except (UnidentifiedImageError, OSError, SyntaxError):
                    print(f"Überspringe ungültige Bilddatei: {img_path}")
        images = sorted(images, key=take2)
        return images

    # Lade die Bilder
    images = load_images(main_folder)

    # Anzahl der Bilder
    num_images = len(images)

    # Debug-Ausgabe
    #print(f"Gesamtanzahl der Testbilder: {num_images}")

    # Berechne die Anzahl der Zeilen
    num_rows = num_images // num_cols + int(num_images % num_cols != 0)

    # Erstelle die Plotfigur
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(figsize[0], num_rows * figsize[1]))

    # Zeige die Bilder und Bildunterschriften
    for i, ax in enumerate(axes.flat):
        if i < num_images:
            img_path, label = images[i]
            img = mpimg.imread(img_path)
            ax.imshow(img)
            ax.set_title(label)
        ax.axis('off')

    plt.tight_layout()
    return plt.show()


def temp_print(val,secs):
    print(val)
    time.sleep(secs)
    clear_output()

def make_bold(string):
    return "\033[1m"+string+"\033[0;0m"


def zeitlimit(minuten):
    for i in range(minuten*60, 0, -1):
        clear_output(wait=True)
        if i//60!=1 and i%60!=1:
            print(f"Zeit über: {i//60} Minuten und {i%60} Sekunden")
        elif i//60==1 and i%60!=1:
            print(f"Zeit über: {i//60} Minute und {i%60} Sekunden")
        elif i//60!=1 and i%60==1:
            print(f"Zeit über: {i//60} Minuten und {i%60} Sekunde")
        elif i//60==1 and i%60==1:
            print(f"Zeit über: {i//60} Minute und {i%60} Sekunde")
        time.sleep(1)
    clear_output(wait=True)
    print("Zeit um!")
    time.sleep(2)
    clear_output(wait=False)

def hundOderKatzeAnhandGewicht_V2_zeichneVerlust():
    # Daten
    cat_heights = [20, 24, 31, 44, 50]
    cat_weights = [30, 20, 15, 25, 30]

    dog_heights = [18, 30, 35, 60, 45]
    dog_weights = [37, 27, 35, 30, 38]

    #Load images ONCE as arrays (fast and reusable)
    cat_img_arr = mpimg.imread('Grafiken/cathead.png')
    cat_img_grey_arr = mpimg.imread('Grafiken/cathead_grey.png')
    dog_img_arr = mpimg.imread('Grafiken/doghead.png')
    dog_img_grey_arr = mpimg.imread('Grafiken/doghead_grey.png')

    # Abstände berechnen und anzeigen
    total_distance_cats = 0
    total_distance_dogs = 0

    def calc_verlust(x):
        cat_heights = [20, 24, 31, 44, 50]
        cat_weights = [30, 20, 15, 25, 30]
    
        dog_heights = [18, 30, 35, 60, 45]
        dog_weights = [37, 27, 35, 30, 38]

        total_distance_cats = 0
        total_distance_dogs = 0
        
        for i in range(len(cat_heights)):
            if cat_weights[i]> x:
                distance = cat_weights[i] - x
                total_distance_cats += distance
            
        for i in range(len(dog_heights)):
            if dog_weights[i]<x:
                distance = x - dog_weights[i]
                total_distance_dogs += distance
                
        return total_distance_cats+total_distance_dogs
    
    def get_image_from_array(arr, zoom=0.2):
        return OffsetImage(arr, zoom=zoom)

    def plot_counting(y_achsenabschnitt=0.0):
        clear_output(wait=True)
        fig, ax = plt.subplots(1, 2, figsize=(10, 5))

        steigung=0
        # Abstände berechnen und anzeigen
        total_distance_cats = 0
        total_distance_dogs = 0
        
        for i in range(len(cat_heights)):
            y_on_line = steigung * cat_heights[i] + y_achsenabschnitt
            if cat_weights[i]>y_on_line:
                image_data = cat_img_grey_arr
                distance = cat_weights[i] - y_on_line
                total_distance_cats += distance
                # Linie für distanz zeichnen
                ax[0].plot([cat_heights[i], cat_heights[i]], [y_on_line, cat_weights[i]], 'b-')
            else: 
                image_data = cat_img_arr
            image = get_image_from_array(image_data)
            ab = AnnotationBbox(image, (cat_heights[i], cat_weights[i]), frameon=False)
            ax[0].add_artist(ab)
            
        for i in range(len(dog_heights)):
            y_on_line = steigung*dog_heights[i]+y_achsenabschnitt
            if dog_weights[i]<y_on_line:
                image_data = dog_img_grey_arr 
                distance = y_on_line - dog_weights[i]
                total_distance_dogs += distance
                # Linie für distanz zeichnen
                ax[0].plot([dog_heights[i], dog_heights[i]], [dog_weights[i], y_on_line], 'g-')
            else:
                image_data = dog_img_arr
            image = get_image_from_array(image_data)
            ab = AnnotationBbox(image, (dog_heights[i], dog_weights[i]), frameon=False)
            ax[0].add_artist(ab)

        # Draw decision boundary
        x_vals = np.linspace(10, 70, 100)
        y_vals = y_achsenabschnitt + 0 * x_vals
        ax[0].plot(x_vals, y_vals, color='royalblue', label=f'Grenze bei {y_achsenabschnitt:.2f} kg')

        # Bereich einfärben
        ax[0].fill_between(x_vals, y_vals, 12, color='lightblue', alpha=1, label='kategorisiert als Katze')
        ax[0].fill_between(x_vals, y_vals, 42, where=(y_vals < 42), color='navajowhite', alpha=1, label='kategorisiert als Hund')

        ax[0].set_xlim(10, 68)
        ax[0].set_ylim(12, 42)
        ax[0].set_xlabel('Größe (cm)')
        ax[0].set_ylabel('Gewicht (kg)')
        ax[0].legend()

        # Vectorize the function to handle arrays
        vectorized_verlust = np.vectorize(calc_verlust)
        
        x2_vals = np.linspace(10,50,100)
        y2_vals = vectorized_verlust(x2_vals)

        ax[1].set_xlabel('Gewichtsgrenze (kg)')
        ax[1].set_ylabel('Verlust')
        ax[1].plot(x2_vals, y2_vals, color="royalblue")
        ax[1].plot(y_achsenabschnitt, calc_verlust(y_achsenabschnitt), 'ro') 

        plt.show()

    randomY = random.uniform(10, 50)
    w = interactive(plot_counting, y_achsenabschnitt=widgets.FloatSlider(min=10, max=50, step=0.05, value=randomY))
    display(w)

def hundOderKatzeAnhandGewicht_V1_zeichneVerlust():
    # Daten
    cat_heights = [20, 24, 31, 44, 50]
    cat_weights = [30, 20, 15, 25, 30]

    dog_heights = [18, 30, 35, 60, 45]
    dog_weights = [37, 27, 35, 30, 38]

    #Load images ONCE as arrays (fast and reusable)
    cat_img_arr = mpimg.imread('Grafiken/cathead.png')
    cat_img_grey_arr = mpimg.imread('Grafiken/cathead_grey.png')
    dog_img_arr = mpimg.imread('Grafiken/doghead.png')
    dog_img_grey_arr = mpimg.imread('Grafiken/doghead_grey.png')

    # Abstände berechnen und anzeigen
    total_distance_cats = 0
    total_distance_dogs = 0

    def calc_verlust(x):
        cat_heights = [20, 24, 31, 44, 50]
        cat_weights = [30, 20, 15, 25, 30]
    
        dog_heights = [18, 30, 35, 60, 45]
        dog_weights = [37, 27, 35, 30, 38]

        total_distance_cats = 0
        total_distance_dogs = 0
        
        for i in range(len(cat_heights)):
            if cat_weights[i]> x:
                total_distance_cats += 1
            
        for i in range(len(dog_heights)):
            if dog_weights[i]<x:
                total_distance_dogs += 1
                
        return total_distance_cats+total_distance_dogs
    
    def get_image_from_array(arr, zoom=0.2):
        return OffsetImage(arr, zoom=zoom)

    def plot_counting(y_achsenabschnitt=0.0):
        clear_output(wait=True)
        fig, ax = plt.subplots(1, 2, figsize=(10, 5))

        steigung=0
        # Abstände berechnen und anzeigen
        total_distance_cats = 0
        total_distance_dogs = 0
        
        for i in range(len(cat_heights)):
            y_on_line = steigung * cat_heights[i] + y_achsenabschnitt
            if cat_weights[i]>y_on_line:
                image_data = cat_img_grey_arr
                total_distance_cats += 1
                # Linie für distanz zeichnen
                ax[0].plot([cat_heights[i], cat_heights[i]], [y_on_line, cat_weights[i]], 'b-')
            else: 
                image_data = cat_img_arr
            image = get_image_from_array(image_data)
            ab = AnnotationBbox(image, (cat_heights[i], cat_weights[i]), frameon=False)
            ax[0].add_artist(ab)
            
        for i in range(len(dog_heights)):
            y_on_line = steigung*dog_heights[i]+y_achsenabschnitt
            if dog_weights[i]<y_on_line:
                image_data = dog_img_grey_arr 
                total_distance_dogs += 1
                # Linie für distanz zeichnen
                ax[0].plot([dog_heights[i], dog_heights[i]], [dog_weights[i], y_on_line], 'g-')
            else:
                image_data = dog_img_arr
            image = get_image_from_array(image_data)
            ab = AnnotationBbox(image, (dog_heights[i], dog_weights[i]), frameon=False)
            ax[0].add_artist(ab)

        # Draw decision boundary
        x_vals = np.linspace(10, 70, 100)
        y_vals = y_achsenabschnitt + 0 * x_vals
        ax[0].plot(x_vals, y_vals, color='royalblue', label=f'Grenze bei {y_achsenabschnitt:.2f} kg')

        # Bereich einfärben
        ax[0].fill_between(x_vals, y_vals, 12, color='lightblue', alpha=1, label='kategorisiert als Katze')
        ax[0].fill_between(x_vals, y_vals, 42, where=(y_vals < 42), color='navajowhite', alpha=1, label='kategorisiert als Hund')

        ax[0].set_xlim(10, 68)
        ax[0].set_ylim(12, 42)
        ax[0].set_xlabel('Größe (cm)')
        ax[0].set_ylabel('Gewicht (kg)')
        ax[0].legend()

        # Vectorize the function to handle arrays
        vectorized_verlust = np.vectorize(calc_verlust)
        
        x2_vals = np.linspace(10,50,100)
        y2_vals = vectorized_verlust(x2_vals)

        ax[1].set_xlabel('Gewichtsgrenze (kg)')
        ax[1].set_ylabel('Verlust')
        ax[1].plot(x2_vals, y2_vals, color="royalblue")
        ax[1].plot(y_achsenabschnitt, calc_verlust(y_achsenabschnitt), 'ro') 

        plt.show()

    randomY = random.uniform(10, 50)
    w = interactive(plot_counting, y_achsenabschnitt=widgets.FloatSlider(min=10, max=50, step=0.05, value=randomY))
    display(w)
