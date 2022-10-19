from PIL import Image, ImageDraw, ImageFilter, ImageColor

Gesichtsbild = Image.open(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\imagem qualquer minha.jpeg")
Gesichtsbild_800 = Gesichtsbild.resize((800, 800))


#hier wird geprüft dem Geburtsdatum entsprechend welche Sterzeichen man hat
def sternenbildner(day, monat, bild):
    geburtstag = int(day)
    geburtsmonat = monat
    Gesichtsbild_800 = bild.resize((800, 800))
    try:
        if geburtsmonat == 12 or geburtsmonat == "Dezember":
            sternzeichen = 'Schütze' if (geburtstag < 22) else 'Steinbock'
        elif geburtsmonat == 1 or geburtsmonat == "Januar":
            sternzeichen = 'Steinbock' if (geburtstag < 20) else 'Wassermann'
        elif geburtsmonat == 2 or geburtsmonat == "Februar":
            sternzeichen = 'Wassermann' if (geburtstag < 19) else 'Fische'
        elif geburtsmonat == 3 or geburtsmonat == "März":
            sternzeichen = 'Fische' if (geburtstag < 21) else 'Widder'
        elif geburtsmonat == 4 or geburtsmonat == "April":
            sternzeichen = 'Widder' if (geburtstag < 20) else 'Stier'
        elif geburtsmonat == 5 or geburtsmonat == "Mai":
            sternzeichen = 'Stier' if (geburtstag < 21) else 'Zwilling'
        elif geburtsmonat == 6 or geburtsmonat == "Juni":
            sternzeichen = 'Zwilling' if (geburtstag < 21) else 'Krebs'
        elif geburtsmonat == 7 or geburtsmonat == "Juli":
            sternzeichen = 'Krebs' if (geburtstag < 23) else 'Löwe'
        elif geburtsmonat == 8 or geburtsmonat == "August":
            sternzeichen = 'Löwe' if (geburtstag < 23) else 'Jungfrau'
        elif geburtsmonat == 9 or geburtsmonat == "Sempter":
            sternzeichen = 'Jungfrau' if (geburtstag < 23) else 'Waage'
        elif geburtsmonat == 10 or geburtsmonat == "Oktober":
            sternzeichen = 'Waage' if (geburtstag < 23) else 'Skorpion'
        elif geburtsmonat == 11 or geburtsmonat == "November":
            sternzeichen = 'Skorpion' if (geburtstag < 22) else 'Schütze'
        sternzeichen


        # hier werden die Sternzeichenbilder in entsprechende Variabel gespeichert

        img_Schütze = Image.open(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\Schütze.jpg").resize((100, 100)).convert("L") # setzt das Bild in schwarz-weiß
        img_Schütze.putalpha(130) # setzt das Transparenzniveau meines Bildes zu halbtransparent
        img_Steinbock = Image.open(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\Steinbock.jpg").resize((100, 100)).convert("L")
        img_Steinbock.putalpha(130)
        img_Wassermann = Image.open(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\Wassermann.jpg").resize((100, 100)).convert("L")
        img_Wassermann.putalpha(130)
        img_Fische = Image.open(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\Fische.jpg").resize((100, 100)).convert("L")
        img_Fische.putalpha(130)
        img_Widder = Image.open(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\Widder.jpg").resize((100, 100)).convert("L")
        img_Widder.putalpha(120)
        img_Stier = Image.open(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\Stier.jpg").resize((100, 100)).convert("L")
        img_Stier.putalpha(130)
        img_Zwilling = Image.open(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\Zwillinge.jpg").resize((100, 100)).convert("L")
        img_Zwilling.putalpha(130)
        img_Krebs = Image.open(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\Krebs.jpg").resize((100, 100)).convert("L")
        img_Krebs.putalpha(130)
        img_Löwe = Image.open(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\Löwe.jpg").resize((100, 100)).convert("L")
        img_Löwe.putalpha(130)
        img_Jungfrau = Image.open(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\Jungfrau.jpg").resize((100, 100)).convert("L")
        img_Jungfrau.putalpha(130)
        img_Waage = Image.open(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\Waage.jpg").resize((100, 100)).convert("L")
        img_Waage.putalpha(130)
        img_Skorpion = Image.open(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\Scorpion.jpg").resize((100, 100)).convert("L")
        img_Skorpion.putalpha(130)

        # hier wird das entsprechende Sternzeichenbild auf das Gesichtsbild aufgelegt
        if sternzeichen == "Schütze":
            Gesichtsbild2 = Gesichtsbild_800.copy()
            Gesichtsbild2.paste(img_Schütze, (700,0))
            Gesichtsbild2.save(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\ " + "Gesichtsbild2.jpeg", quality = 95)
            Gesichtsbild2.show()        
        elif sternzeichen == "Steinbock":
            Gesichtsbild2 = Gesichtsbild_800.copy()
            Gesichtsbild2.paste(img_Steinbock, (700,0))
            Gesichtsbild2.save(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\ " + "Gesichtsbild2.jpeg", quality = 95)
            Gesichtsbild2.show()
        elif sternzeichen == "Wassermann":
            Gesichtsbild2 = Gesichtsbild_800.copy()
            Gesichtsbild2.paste(img_Wassermann, (700,0))
            Gesichtsbild2.save(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\ " + "Gesichtsbild2.jpeg", quality = 95)
            Gesichtsbild2.show()
        elif sternzeichen == "Fische":
            Gesichtsbild2 = Gesichtsbild_800.copy()
            Gesichtsbild2.paste(img_Fische, (700,0))
            Gesichtsbild2.save(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\ " + "Gesichtsbild2.jpeg", quality = 95)    
            Gesichtsbild2.show()
        elif sternzeichen == "Widder":
            Gesichtsbild2 = Gesichtsbild_800.copy()
            Gesichtsbild2.paste(img_Widder, (700,0))
            Gesichtsbild2.save(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\ " + "Gesichtsbild2.jpeg", quality = 95)    
            Gesichtsbild2.show()
        elif sternzeichen == "Stier":
            Gesichtsbild2 = Gesichtsbild_800.copy()
            Gesichtsbild2.paste(img_Stier, (700,0))
            Gesichtsbild2.save(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\ " + "Gesichtsbild2.jpeg", quality = 95)    
            Gesichtsbild2.show()
            Gesichtsbild2.show()
        elif sternzeichen == "Zwilling":
            Gesichtsbild2 = Gesichtsbild_800.copy()
            Gesichtsbild2.paste(img_Zwilling, (700,0))
            Gesichtsbild2.save(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\ " + "Gesichtsbild2.jpeg", quality = 95)    
            Gesichtsbild2.show()
        elif sternzeichen == "Krebs":
            Gesichtsbild2 = Gesichtsbild_800.copy()
            Gesichtsbild2.paste(img_Krebs, (700,0))
            Gesichtsbild2.save(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\ " + "Gesichtsbild2.jpeg", quality = 95)    
            Gesichtsbild2.show()
        elif sternzeichen == "Löwe":
            Gesichtsbild2 = Gesichtsbild_800.copy()
            Gesichtsbild2.paste(img_Löwe, (700,0))
            Gesichtsbild2.save(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\ " + "Gesichtsbild2.jpeg", quality = 95)    
            Gesichtsbild2.show()
        elif sternzeichen == "Jungfrau":
            Gesichtsbild2 = Gesichtsbild_800.copy()
            Gesichtsbild2.paste(img_Jungfrau, (700,0))
            Gesichtsbild2.save(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\ " + "Gesichtsbild2.jpeg", quality = 95)
            Gesichtsbild2.show()
        elif sternzeichen == "Waage":
            Gesichtsbild2 = Gesichtsbild_800.copy()
            Gesichtsbild2.paste(img_Waage, (700,0))
            Gesichtsbild2.save(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\ " + "Gesichtsbild2.jpeg", quality = 95)
            Gesichtsbild2.show()
        elif sternzeichen == "Skorpion":
            Gesichtsbild2 = Gesichtsbild_800.copy()
            Gesichtsbild2.paste(img_Skorpion, (700,0))
            Gesichtsbild2.save(r"C:\Users\hhhme\Desktop\Umschulung zum Data Analyst\Python\Praxiswoche 10.10 bis 14.10\Aufgabe 3\ " + "Gesichtsbild2.jpeg", quality = 95)
            Gesichtsbild2.show()
    except UnboundLocalError:
        print("Bitte schreiben Sie den Monat in Zahlform oder anfangend mit Großbuchstabe!")