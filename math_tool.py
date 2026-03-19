import math
import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Fehler: Division durch Null nicht möglich!"
    return x / y

def square_root(x):
    if x < 0:
        return "Fehler: Quadratwurzel aus negativer Zahl im reellen Raum nicht möglich!"
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def run_calculator():
    print("=== Einfaches Mathematik-Tool ===")
    print("Dieses Tool nutzt ausschließlich die in Python integrierte Standardbibliothek ('math').")
    print("Dadurch müssen keine Drittanbieter-Module installiert werden und es werden keine")
    print("externen Lizenzen (wie GPL, MIT, Apache, etc. von PyPI) tangiert.")
    print("==================================\n")

    while True:
        print("Wähle eine Operation:")
        print("1. Addieren")
        print("2. Subtrahieren")
        print("3. Multiplizieren")
        print("4. Dividieren")
        print("5. Quadratwurzel")
        print("6. Potenz (x hoch y)")
        print("7. Beenden")

        choice = input("Deine Wahl (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Programm wird beendet. Auf Wiedersehen!")
            sys.exit(0)

        if choice in ('1', '2', '3', '4', '6'):
            try:
                num1 = float(input("Gib die erste Zahl ein: "))
                num2 = float(input("Gib die zweite Zahl ein: "))
            except ValueError:
                print("Ungültige Eingabe! Bitte gib Zahlen ein.\n")
                continue

            if choice == '1':
                print(f"Ergebnis: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Ergebnis: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Ergebnis: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Ergebnis: {num1} / {num2} = {divide(num1, num2)}")
            elif choice == '6':
                print(f"Ergebnis: {num1} ^ {num2} = {power(num1, num2)}")

        elif choice == '5':
            try:
                num = float(input("Gib die Zahl ein: "))
            except ValueError:
                print("Ungültige Eingabe! Bitte gib eine Zahl ein.\n")
                continue
            
            print(f"Ergebnis: √{num} = {square_root(num)}")
            
        else:
            print("Ungültige Eingabe. Bitte eine der Optionen wählen.")
        
        print("\n" + "-"*30 + "\n")

if __name__ == "__main__":
    try:
        run_calculator()
    except KeyboardInterrupt:
        print("\nProgramm abgebrochen.")
        sys.exit(0)
