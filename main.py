def taschenrechner():
    print("Enfacher Taschenrechner")
    print("Operationen: +, -, *, / ")
while True:
    zahl1= float(input("Erste Zahl eingeben: \n"))
    op= input("Operator (+, -, *, /): \n")
    zahl2= float(input("Zweite zahl eingeben: \n")) 
    ergebnis = None
    if op == "+":
      ergebnis = zahl1 +  zahl2
    elif op == "-" :
      ergebnis = zahl1 - zahl2
    elif op == "*" :
      ergebnis = zahl1 * zahl2
    elif op == "/" :
       if zahl2 == 0:
        print("Fehler: Division durch Null ist nicht erlaubt.")
       else:
        ergebnis = zahl1 / zahl2
    else:
      print("Ungültiger Operator. Bitte verwenden Sie +, -, +, /.")
    print(f" Ergebnis:  {ergebnis}")
    nochmal = input("Noch eine Berechnung? (j/n): ")
    if nochmal.lower() != "j":
      break
