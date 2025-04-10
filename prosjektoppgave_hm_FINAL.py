# -*- coding: utf-8 -*-
"""
Prosjektoppgave USN, PY1010
@author: haavard mallaug
Created on Wed Mar 12 12:30:38 2025
Tema: Beregning av vannforbruk



"""


#%% Henter inn aktuelle biblioteker.



import matplotlib.pyplot as plt   # For plotting av data
import pandas as pd   # Analyse og databehandling



#%% Leser inn "vannforbruk.xlsx"-filen og oppdaterer data for de uten vannmåler. Skriver deretter ut en ny fil med vannforbruk på de uten vannmåler.



data = pd.read_excel('vannforbruk.xlsx')   # Leser data fra excel-arket 'vannforbruk'


def vannforbruk_areal(Bruksareal):   # Definerer funksjon for å beregne vannforbruk basert på arealmetoden

    if Bruksareal <= 100:   # Denne henter alle eiendommer med bruksareal lik eller mindre enn 100 m²
        return (Bruksareal*0.9)/12   # Deretter returnerer den at bruksarealet skal multipliseres med 0.9 deretter deles på 12 måneder

    elif Bruksareal <= 150:   # Henter eiendommer fra 101 til og med 150 m² 
        return (Bruksareal*0.9)/12   # Returnerer at bruksarealet skal multipliseres med 0.9 deretter deles på 12 måneder

    else:
        return (Bruksareal - 25)*0.9/12   # Hvis ingen av de 2 overnevnte betingelesene oppfylles, skal resterende, dvs alt over 150 m² få et avslag på 25 m²


data.loc[data['HarVannmaaler'] == 'Nei', 'Forbruk'] = data['Bruksareal'].apply(vannforbruk_areal)   # Oppdaterer forbruk for husstander uten vannmåler


data.to_excel('vannforbruk_ny.xlsx', index=False)   # Lagre de oppdaterte dataene til et nytt Excel-ark og sørge for at formatet er iht excel-arket med dd.mm.yyyy, 'index=false' for å unngå en ekstra nummerkolonne i utdataene 'vannforbruk_ny.xlsx'



#%% Lese inn nytt Excel-ark og lage søylediagram for vannforbruk per sone



data = pd.read_excel('vannforbruk_ny.xlsx')   # Leser inn oppdaterte data


forbruk_per_sone = data.groupby('Sone')['Forbruk'].sum()   # Beregner forbruk per sone


farger1 = ['#002F8D', '#0054BD', '#006CF7', '#A9DFFF', '#B8A9FF', '#E5A9FF']   # Plotter søylediagram, farger er generert i visualiseringsmodulen til et GIS-program som heter ArcGIS Pro
plt.figure(figsize=(8, 5))
plt.bar(forbruk_per_sone.index, forbruk_per_sone.values, color=farger1)


plt.xlabel('Sone', fontsize=10)   # Tilpasning av akser og diamgramtittel
plt.ylabel('Totalt vannforbruk (m³)', fontsize=10)
plt.title('Vannforbruk per sone', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)


for i, v in enumerate(forbruk_per_sone.values):   # Legger til verdier på toppen av søylene for bedre lesbarhet
    plt.text(i, v + 1000, f"{v:.0f} m³", ha='center', fontsize=12)


plt.show()   # Denne trenger egentlig ikke være med her men i tilfellet koden skal kjøres utenfor Notebook/iPython/Spyder feks vanlig py-fil må den visstnok være med  



#%% Lager en ny funksjon som gir vannforbruk fra nyberegnet excel-ark 'vannforbruk_ny'



data = pd.read_excel('vannforbruk_ny.xlsx')   # Leser inn oppdaterte data


forbruk_per_mnd = data.groupby('Mnd')['Forbruk'].sum()   # Grupperer data per måned


forbruk_per_mnd = forbruk_per_mnd.sort_index()   # Sorterer månedene i riktig rekkefølge (1 = Januar, 12 = Desember)


plt.figure(figsize=(8, 5))   # Lager linjediagram
plt.plot(forbruk_per_mnd.index, forbruk_per_mnd.values, marker='o', linestyle='--', color='c')   # Plotter forbruk per måned


plt.xlabel("Måned", fontsize=10)   # Jeg styler grafen
plt.ylabel("Totalt vannforbruk (m³)", fontsize=10)
plt.title("Vannforbruk per måned", fontsize=12)
plt.grid()
plt.xticks(forbruk_per_mnd.index, labels=["Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Des"])  # Setter månedsnavn på x-aksen


plt.show()   # Viser plottet


print (forbruk_per_mnd)   # Ønsker data  













