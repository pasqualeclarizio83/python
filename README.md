# Python - Basi Complete con Commenti

```python
# 1. Hello World
# Stampa "Hello, World!" sullo schermo
print("Hello, World!")

# 2. Variabili e Tipi di Dati
# Assegna un valore intero alla variabile x
x = 10          # Intero (int)
# Assegna un valore decimale alla variabile y
y = 3.14        # Numero con decimali (float)
# Assegna una stringa alla variabile z
z = "Ciao"      # Stringa di testo (str)
# Assegna un valore booleano alla variabile flag
flag = True     # Valore booleano (bool)

# Stampa tutti i valori delle variabili
print(x, y, z, flag)


# 3. Operatori
# Operazione di somma tra due numeri
a = 10
b = 3
print(a + b)  # Somma (10 + 3)

# Sottrazione di due numeri
print(a - b)  # Sottrazione (10 - 3)

# Moltiplicazione tra due numeri
print(a * b)  # Moltiplicazione (10 * 3)

# Divisione tra due numeri
print(a / b)  # Divisione (10 / 3)

# Modulo (resto della divisione tra a e b)
print(a % b)  # Modulo (resto della divisione)

# Potenza: elevamento di un numero a una potenza
print(a ** b) # Potenza (10 elevato a 3)


# 4. Condizioni
# Verifica se x è maggiore di 5, uguale a 5 o minore di 5
x = 10
if x > 5:  # Se x è maggiore di 5
    print("Maggiore di 5")
elif x == 5:  # Se x è uguale a 5
    print("Uguale a 5")
else:  # Se x è minore di 5
    print("Minore di 5")


# 5. Ciclo For
# Esegue un ciclo da 0 a 4 (range crea una sequenza di numeri)
for i in range(5):  # Esegui il ciclo 5 volte
    print(i)  # Stampa il valore di i (da 0 a 4)


# 6. Ciclo While
# Esegue un ciclo finché x è maggiore di 0
x = 5
while x > 0:  # Finché x è maggiore di 0
    print(x)  # Stampa il valore di x
    x -= 1    # Diminuisce x di 1 ogni volta


# 7. Funzioni
# Definisce una funzione che saluta una persona
def saluta(nome):  # La funzione prende un parametro "nome"
    return f"Ciao, {nome}!"  # Restituisce un saluto formattato con il nome

# Chiamata alla funzione passando "Python" come argomento
print(saluta("Python"))


# 8. Classi e Oggetti
# Definisce una classe Persona con nome e età
class Persona:
    def __init__(self, nome, eta):  # Il costruttore inizializza gli attributi
        self.nome = nome  # Assegna il valore di nome all'attributo "nome"
        self.eta = eta    # Assegna il valore di eta all'attributo "eta"

    def descrizione(self):  # Metodo che restituisce una descrizione della persona
        return f"{self.nome} ha {self.eta} anni."

# Crea un oggetto della classe Persona
persona = Persona("Mario", 30)
# Chiama il metodo descrizione sull'oggetto
print(persona.descrizione())


# 9. Gestione degli Errori
# Gestisce un errore di divisione per zero
try:
    # Prova a fare una divisione per zero
    risultato = 10 / 0
except ZeroDivisionError:  # Se si verifica un errore di divisione per zero
    print("Errore: divisione per zero!")  # Gestisce l'errore con un messaggio


# 10. Leggere e Scrivere File
# Scrive nel file esempio.txt
with open("esempio.txt", "w") as file:  # Apre il file in modalità scrittura
    file.write("Ciao, file!")  # Scrive il testo nel file

# Legge dal file esempio.txt
with open("esempio.txt", "r") as file:  # Apre il file in modalità lettura
    print(file.read())  # Legge il contenuto del file e lo stampa


# 11. Importare Librerie
# Importa il modulo math per operazioni matematiche avanzate
import math

# Calcola la radice quadrata di 16
print(math.sqrt(16))  # Stampa 4.0


