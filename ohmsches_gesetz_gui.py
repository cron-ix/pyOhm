import tkinter as tk
import math

class Application(tk.Frame):
    # Frame intialisieren
    def __init__(self, master=None):
        super().__init__(master)
        # Application konfigurieren
        self.master = master
        self.master.title ("Ohmsches Gesetz")
        self.master.minsize(354, 213)
        self.master.maxsize(1000, 720)
        # Event-Handler für Fensteränderungen (Größe/Position)
        self.master.bind("<Configure>", self.handleConfigure)
        # Event-Handler: Enter-Taste führt Berechnung aus
        self.master.bind("<Return>", self.handleCalculate)
        # Escape-Taste zum Beenden - tut Fehler: destroy() takes 1 positional argument but 2 were given
        # self.master.bind("<Escape>", self.master.destroy)
        self.pack(fill='both')
        # Widgets hinzufügen
        self.createWidgets()
        # Größenänderung für Spalte 1 = Texteingabe anpassen (funzt nur mit pack(fill='both'))
        self.grid_columnconfigure(1, weight=1)

    # Validierungsfunktion der Eingabe im Entry-Widget
    def isFloat(self, content):
        try:
            return float(content)
        except:
            return content==""
    
    # Entry mit Inhalt setzen
    def setEntry(self, where, what):
        if where.get():
            where.delete(0, len(where.get()))
        where.insert(0, str(what))
    
    # Anweisungen für Button-Click
    def handleCalculate(self, event):
        # Spannung und Stromstärke aus Leistung P und Widerstand R
        if self.inp_Power.get() and self.inp_Resistance.get():
            # V = Wurzel(P * R)
            self.setEntry(self.inp_Voltage, round(math.sqrt(float(self.inp_Power.get()) * float(self.inp_Resistance.get())), 2))
            # I = Wurzel (P / R)
            self.setEntry(self.inp_Current, round(math.sqrt(float(self.inp_Power.get()) / float(self.inp_Resistance.get())), 2))
            return
        # Widerstand und Stromstärke aus Leistung P und Spannung V
        if self.inp_Power.get() and self.inp_Voltage.get():
            # R = V² / P
            self.setEntry(self.inp_Resistance, round(math.pow(float(self.inp_Voltage.get()), 2) / float(self.inp_Power.get()), 2))
            # I = P / V
            self.setEntry(self.inp_Current, round(float(self.inp_Power.get()) / float(self.inp_Voltage.get()), 2))
            return
        # Widerstand R und Spannung V aus Leistung P und Stromstärke I
        if self.inp_Power.get() and self.inp_Current.get():
            # R = P / I²
            self.setEntry(self.inp_Resistance, round(float(self.inp_Power.get()) / math.pow(float(self.inp_Current.get()), 2), 2))
            # V = P / I
            self.setEntry(self.inp_Voltage, round(float(self.inp_Power.get()) / float(self.inp_Current.get()), 2))
            return
        # Leistung P und Stromstärke I aus Widerstand R und Spannung V
        if self.inp_Resistance.get() and self.inp_Voltage.get():
            # P = V² / R
            self.setEntry(self.inp_Power, round(math.pow(float(self.inp_Voltage.get()), 2) / float(self.inp_Resistance.get()), 2))
            # I = V / R
            self.setEntry(self.inp_Current, round(float(self.inp_Voltage.get()) / float(self.inp_Resistance.get()), 2))
            return
        # Leistung P und Spannung V aus Widerstand R und Stromstärke I
        if self.inp_Resistance.get() and self.inp_Current.get():
            # P = I² * R
            self.setEntry(self.inp_Power, round(math.pow(float(self.inp_Current.get()), 2) * float(self.inp_Resistance.get()), 2))
            # V = I * R
            self.setEntry(self.inp_Voltage, round(float(self.inp_Current.get()) * float(self.inp_Resistance.get()), 2))
            return
        # Leistung P und Widerstand R aus Spannung V und Stromstärke I
        if self.inp_Voltage.get() and self.inp_Current.get():
            # P = V * I
            self.setEntry(self.inp_Power, round(float(self.inp_Voltage.get()) * float(self.inp_Current.get()), 2))
            # R = V / I
            self.setEntry(self.inp_Resistance, round(float(self.inp_Voltage.get()) / float(self.inp_Current.get()), 2))
            return

    # Änderung des Fensters verarbeiten
    def handleConfigure(self, event):
        print("window size and position: ", self.master.winfo_geometry())

    # Eingabefelder zurücksetzen
    def clearEntries(self, event):
        self.setEntry(self.inp_Power, "")
        self.setEntry(self.inp_Resistance, "")
        self.setEntry(self.inp_Voltage, "")
        self.setEntry(self.inp_Current, "")

    # Widgets hinzufügen
    def createWidgets(self):
        # Validierungsfunktion 'isFloat' registrieren
        vcmd = self.register(self.isFloat), '%P'

        # Überschrift:
        # Row 0
        self.lbl_Header = tk.Label(self, text="Ohmsches Gesetz", font=(None, 14))
        self.lbl_Header.grid(column=0, row=0, columnspan=3, padx='5', pady='5', sticky='nesw')

        # Eingabefelder:
        # Row 1 (Leistung P in Watt)
        self.lbl_Power = tk.Label(self, text="Leistung (P in Watt):").grid(column=0, row=1, padx='5', pady='5', sticky='nesw')
        self.inp_Power = tk.Entry(self, textvariable="", validate="key", validatecommand=vcmd)
        self.inp_Power.grid(column=1, row=1, columnspan=2, padx='5', pady='5', sticky="nesw")
        # Row 2 (Widerstand R in Ohm)
        self.lbl_Resistance = tk.Label(self, text="Widerstand (R in Ohm):").grid(column=0, row=2, padx='5', pady='5', sticky='nesw')
        self.inp_Resistance = tk.Entry(self, textvariable="", validate="key", validatecommand=vcmd)
        self.inp_Resistance.grid(column=1, row=2, columnspan=2, padx='5', pady='5', sticky="nesw")
        # Row 3 (Spannung V in Volt)
        self.lbl_Voltage = tk.Label(self, text="Spannung (V in Volt):").grid(column=0, row=3, padx='5', pady='5', sticky='nesw')
        self.inp_Voltage = tk.Entry(self, textvariable="", validate="key", validatecommand=vcmd)
        self.inp_Voltage.grid(column=1, row=3, columnspan=2, padx='5', pady='5', sticky="nesw")
        # Row 4 (Stromstärle I in Ampere )
        self.lbl_Current = tk.Label(self, text="Stromstärke (I in Ampere):").grid(column=0, row=4, padx='5', pady='5', sticky='nesw')
        self.inp_Current = tk.Entry(self, textvariable="", validate="key", validatecommand=vcmd)
        self.inp_Current.grid(column=1, row=4, columnspan=2, padx='5', pady='5', sticky="nesw")

        # Leerzeile
        # Row 5
        # tk.Label(self).grid(column=0, row=5, padx='5', pady='5', sticky="nesw")

        # Quit-Button erzeugen
        # Row 5
        # self.btn_quit = tk.Button(self, text="Beenden", command=self.master.destroy).grid(column=1, row=5, padx='5', pady='5', sticky="nes")
        self.btn_clear = tk.Button(self, text="Löschen")
        self.btn_clear.grid(column=1, row=5, padx='5', pady='5', sticky="nes")
        self.btn_clear.bind("<Button-1>", self.clearEntries)
        self.btn_run = tk.Button(self, text="Berechnen")
        self.btn_run.grid(column=2, row=5, padx='5', pady='5', sticky="nesw")
        self.btn_run.bind("<Button-1>", self.handleCalculate)

# 
# Hauptfensterinstanz (Frame-Widget)
#
root = tk.Tk()

# If you have a large number of widgets, 
# you can specify the standard attributes for all widgets simply like this.
# root.option_add("*Button.Background", "black")
# root.option_add("*Button.Foreground", "red")

# Fenster in Frame-Widget (Haupfensterinstanz) aus der Klasse "Appication" (s.o.) erzeugen/befüllen
app = Application(master=root)

# Application anzeigen
app.mainloop()
