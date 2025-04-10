# py1010-1_prosjektoppgave

# 💧 Analyse av vannforbruk per husholdning

> **DISCLAIMER**  
> Alle data i dette prosjektet er autogenerert for oppgaven og representerer ikke reelle verdier for vannforbruk eller antall personer.  
> Grunnlagsdata er hentet fra åpne datasett på GeoNorge, deretter manipulert med FME (Feature Manipulation Engine) for å lage tilfeldige tall. 
> Kilde: [GeoNorge Matrikkel](https://kartkatalog.geonorge.no/metadata?text=matrikkel)

---

## 📌 Om prosjektet

Dette prosjektet analyserer vannforbruk i ulike husholdninger, med fokus på forskjeller mellom enheter **med** og **uten** vannmåler. Det inkluderer også visuelle fremstillinger av vannforbruk fordelt på **geografiske soner** og **måneder**.

**Funksjonalitet:**
- Automatisk beregning av vannforbruk for enheter uten vannmåler (basert på bruksareal)
- Sammenstilling og gruppering av data per sone og måned
- Visualisering i form av søyle- og linjediagrammer
- Eksport av bearbeidede data til ny Excel-fil

Prosjektet er levert som del av **PY1010 - Grunnleggende programmering** og oppfyller krav om bruk av:
- Arrays og vektoriserte beregninger
- If/else-tester og løkker
- Lese/skrive filer
- Plotting med matplotlib
- Egendefinerte funksjoner

---

## ▶️ Bruksanvisning

1. Sørg for at følgende er installert:
   - Python 3.x
   - Pakker: `pandas`, `numpy`, `matplotlib`, `openpyxl`

   Installer dem enkelt med:
   ```bash
   pip install -r requirements.txt
