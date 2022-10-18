import pandas as pd
import matplotlib.pyplot as plt
from tkinter.ttk import Combobox
import tkinter as tk



preistabelle_original = pd.read_excel(r"C:\Users\hhhme\Documents\GitHub\my-projects\first_projects_onDatacraft\Project_withInterfaceTkinter\Preisinformation.xlsx")

# Bundesland und Kostenfaktor:
BundK = pd.read_excel("Preisinformation.xlsx",sheet_name="Tabelle1", usecols=("B:C"), skiprows=2).set_index(["Bundesland"])  
# StadtvsLand und Kostenfaktor:
SLundK = pd.read_excel("Preisinformation.xlsx",sheet_name="Tabelle1", usecols=("E:F"), skiprows=2, nrows = 2).set_index(["Stadt vs Land"]) 
# Ausstattung und Kostenfaktor
AundK = pd.read_excel("Preisinformation.xlsx",sheet_name="Tabelle1", usecols=("E:F"), skiprows=6, nrows = 5).set_index(["Ausstattung"]) 
# Hausart und Kostenfaktor
HundK = pd.read_excel("Preisinformation.xlsx",sheet_name="Tabelle1", usecols=("E:F"), skiprows=13, nrows = 3).set_index(["Hausart"])
# Weitere Kostenfaktoren pro Preis und Einheit
WKproPE = pd.read_excel("Preisinformation.xlsx",sheet_name="Tabelle1", usecols=("H:I"), skiprows=2, nrows = 6).set_index(["Weitere Kostenfaktoren"]) 


# my interface Tkinter:

window = tk.Tk()
window.geometry("700x400")
window.title("Hauspreisrechner")

#Erstellung meiner Arbeitswindow:
labelGrundstück = tk.Label(window, text="Grundstück in m2")
Grundstück_m2 = tk.Entry(window)
labelWohnfläche = tk.Label(window, text="Wohnfläche in m2")
Wohnfläche_m2 = tk.Entry(window)
labelBaujahr = tk.Label(window, text="Baujahr")
Baujahr = tk.Entry(window)
ausgabe = tk.Label(window)


# meine Berechnungen:

preis_fallsMakler = float(WKproPE.loc["Makler"])*0.01 # → mal 0.01 um es in % zu konvertieren
preis_fallsDenkmalschutz = float(WKproPE.loc["Denkmalschutz"])*0.01
preis_QM_Grundstück_nachTabelle = float(WKproPE.loc["QM-Grundstück"])   
preis_QM_Wohnfläche_nachTabelle = float(WKproPE.loc["QM-Wohnfläche"])   
    
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------
def berechnen():
    bdl = comboBox_Bundesland.get()
    slk = comboBox_StadtvsLand.get()
    ak = comboBox_Ausstattung.get()
    ha = comboBox_Hausart.get()
    Gm2 = float(Grundstück_m2.get())
    berechnung_Grundstück = Gm2 * preis_QM_Grundstück_nachTabelle
    WohnFm2 = float(Wohnfläche_m2.get()) 
    berechnung_Wohnfläche = WohnFm2 * preis_QM_Wohnfläche_nachTabelle
    Baujahrkosten = (float(Baujahr.get()) - 2022) * (float(WKproPE.loc["Baujahr"])/100)    
    flächegesamt = berechnung_Grundstück + berechnung_Wohnfläche - Baujahrkosten 
    ergebnis = round(flächegesamt * float(BundK.loc[bdl]) * float(SLundK.loc[slk]) * float(AundK.loc[ak]) * float(HundK.loc[ha]))
    mitMakler = ergebnis*preis_fallsMakler if var_Makler.get() == 1 else 0
    mitDSchutz = ergebnis*preis_fallsDenkmalschutz if var_Makler.get() == 1 else 0
    ende_ergebnis = ergebnis + mitMakler + mitDSchutz
    ausgabe.configure(text=f"ihr zukunftiges Haus wird {ende_ergebnis}€ kosten")
#------------------------------------------------------------------------------------------------------------------------------------------------

#my variables for the buttons:
var_Makler = tk.DoubleVar()         #Tkinter hast its own variables, for my calculations I chose the float format, hence tk.DoubleVar()
var_Denkmalschutz = tk.DoubleVar()
var_Bundesland = list(BundK.index)
var_StadtvsLand = list(SLundK.index)
var_Ausstattung = list(AundK.index)
var_Hausart = list(HundK.index)
var_weitereKosten = list(WKproPE.index)

# o que eu escolho passa entao para a variavel listbox_Bundesland zB, valor esse determinado pelos itens 
#q eu add à Listbox através do meu listvariable, que estao em var_Bundesland

def resetFunktion():
    var_Makler.set(0)
    var_Denkmalschutz.set(0)




#Erstellung meiner Buttons:
labelComboboxBundesland =tk.Label(window, text="Wählen Sie bitte ein Bundesland aus")
comboBox_Bundesland = Combobox(window, value= var_Bundesland, width=22)
#listbox_Bundesland = tk.Listbox(window, listvariable = var_Bundesland, height=2, selectmode=tk.EXTENDED, exportselection = 0)

labelComboboxStadtvsLand =tk.Label(window, text="Wählen Sie die Wohnortart")
comboBox_StadtvsLand = Combobox(window, value= var_StadtvsLand, width=22)
#listbox_StadtvsLand = tk.Listbox(window, listvariable = var_StadtvsLand, height=1, selectmode=tk.EXTENDED, exportselection = 0)

labelComboboxAusstattung =tk.Label(window, text="Wählen Sie bitte die Ausstattungsform aus")
comboBox_Ausstattung = Combobox(window, value = var_Ausstattung, width=22)
#listbox_Ausstattung = tk.Listbox(window, listvariable = var_Ausstattung, height=2, selectmode=tk.EXTENDED, exportselection = 0)

labelComboboxHausart =tk.Label(window, text="Wählen Sie bitte die Hausart aus")
comboBox_Hausart = Combobox(window, value = var_Hausart, width=22)
#listbox_Hausart = tk.Listbox(window, listvariable = var_Hausart, height=2, selectmode=tk.EXTENDED, exportselection = 0)

Radiobutton_Makler = tk.Radiobutton(window, text="Makler", variable = var_Makler, value = 1)                            
Radiobutton_Denkmalschutz = tk.Radiobutton(window, text="Denkmalschutz", variable = var_Denkmalschutz, value = 1)

ErgebnisButton = tk.Button(window, text="Hauspreis", command = berechnen)
ResetButton = tk.Button(window, text="Reset Makler und Denkmalschutz", command=resetFunktion)

# alles ins Window
labelGrundstück.place(x=20,y=20)
Grundstück_m2.place(x=400,y=20)
labelWohnfläche.place(x=20,y=50)
Wohnfläche_m2.place(x=400,y=50)
labelBaujahr.place(x=20,y=80)
Baujahr.place(x=400,y=80)
ausgabe.place(x=300,y=365)

labelComboboxBundesland.place(x=20,y=140)
comboBox_Bundesland.place(x=400,y=140)

labelComboboxStadtvsLand.place(x=20,y=170)
comboBox_StadtvsLand.place(x=400,y=170)

labelComboboxAusstattung.place(x=20,y=200)
comboBox_Ausstattung.place(x=400,y=200)

labelComboboxHausart.place(x=20,y=230)
comboBox_Hausart.place(x=400,y=230)

Radiobutton_Makler.place(x=350,y=260)
Radiobutton_Denkmalschutz.place(x=350,y=290)

ErgebnisButton.place(x=330,y=310)
ResetButton.place(x=330,y=330)

#Los!
tk.mainloop()



















































































