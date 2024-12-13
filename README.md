# Python - Basi Complete

```python
# 1. Hello World - Stampa semplice
# Stampa "Hello, World!" sullo schermo
print("Hello, World!")
```

```python
# 2. Funzione che stampa "Hello, World!"
# Definiamo una funzione che stampa "Hello, World!"
def hello_world():
    print("Hello, World!")

hello_world()
```

```python
# 3. Funzione Lambda
# Utilizzando una funzione lambda per stampare "Hello, World!"
hello = lambda: print("Hello, World!")
hello()
```

```python
# 4. Funzione di ordine superiore
# Passando una funzione come argomento a un'altra funzione
def print_message(func):
    func()

print_message(lambda: print("Hello, World!"))
```

```python
# 5. Uso di map
# Usando map per applicare una funzione che stampa "Hello, World!" a una lista
list(map(lambda x: print("Hello, World!"), [1]))
```

```python
# 6. Uso di filter
# Usando filter con una funzione che stampa "Hello, World!"
# (Il filtro non viene effettivamente usato, ma mostra come funziona)
list(filter(lambda x: print("Hello, World!"), [True]))
```

```python
# 7. Uso di una comprensione di lista
# Una lista che stampa "Hello, World!" tramite una comprensione di lista
[print("Hello, World!") for _ in range(1)]
```

```python
# 8. Funzione ricorsiva
# Una funzione che chiama se stessa per stampare "Hello, World!"
def recursive_hello(n):
    if n > 0:
        print("Hello, World!")
        recursive_hello(n - 1)

recursive_hello(1)
```

```python
# 9. Uso di una classe
# Creiamo una classe con un metodo che stampa "Hello, World!"
class HelloWorld:
    def greet(self):
        print("Hello, World!")

hello_instance = HelloWorld()
hello_instance.greet()
```

```python
# 10. Uso di un thread
# Utilizzando il modulo threading per stampare "Hello, World!" in un thread separato
import threading

def print_hello():
    print("Hello, World!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
```


## Funzioni
#### partendo dal concetto matematico, una funzione è una relazione tra due insiemi, chiamati dominio e codominio. A ogni elemento del dominio corrisponde uno e un solo elemento del codominio. In parole più semplici, una funzione è come una "macchina" che prende in ingresso un valore (l'argomento) e restituisce in uscita un altro valore (il risultato).
#### Esempio: La funzione f(x) = 2x prende un numero x in ingresso e restituisce il doppio di quel numero. Se inserisci 3, la funzione restituirà 6.

#### In informatica, il concetto di funzione è molto simile. Una funzione è un blocco di codice che svolge un compito specifico. Essa riceve in ingresso dei dati (parametri) e restituisce un risultato. Le funzioni sono fondamentali per:
#### Modularizzare il codice: Dividendo un programma in funzioni più piccole, il codice diventa più organizzato, leggibile e riutilizzabile.
#### Rendere il codice più efficiente: Scrivendo una funzione una volta sola, puoi richiamarla più volte in diverse parti del tuo programma, evitando di ripetere lo stesso codice.
#### Abstrazione: Le funzioni permettono di nascondere la complessità di un algoritmo, esponendo all'utente solo l'interfaccia necessaria per utilizzarlo.


### Return
#### Il return è come la ciliegina sulla torta di una funzione. È ciò che permette alla funzione di "dare qualcosa in cambio" a chi la chiama. Senza il return, la funzione eseguirebbe le sue operazioni, ma non fornirebbe alcun risultato utile.
#### Il return serve a:

#### Trasmettere il risultato di un calcolo: Ad esempio, una funzione che calcola la somma di due numeri utilizzerà return per restituire il risultato di questa somma.
#### Passare un valore a un'altra parte del codice: Il valore restituito da una funzione può essere assegnato a una variabile o utilizzato come argomento per un'altra funzione.
#### Terminare l'esecuzione della funzione: Quando return viene eseguito, la funzione si interrompe e il controllo viene restituito al punto in cui la funzione è stata chiamata.

```python
# 3. Funzione con valore di ritorno
# Una funzione che restituisce un valore, che può essere utilizzato al di fuori della funzione stessa.
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Stampa 8
```


```python
# 4. Funzione con argomenti predefiniti
# Una funzione che ha valori di default per uno o più argomenti, che vengono utilizzati se non vengono forniti argomenti.
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # Stampa "Hello, Guest!"
greet("Bob")    # Stampa "Hello, Bob!"
```


```python
# 5. Funzione variadica
# Una funzione che può accettare un numero variabile di argomenti.
def sum_all(*args):
    return sum(args)

result = sum_all(1, 2, 3, 4, 5)
print(result)  # Stampa 15
```


```python
# 6. Funzione con argomenti nominati
# Una funzione che accetta argomenti con nomi espliciti.
def person_info(name, age):
    print(f"Name: {name}, Age: {age}")

person_info(age=25, name="Alice")
```


```python
# 7. Funzione ricorsiva
# Una funzione che si chiama da sola per risolvere un problema suddiviso in sottoproblemi più piccoli.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Stampa 120
```


```python
# 8. Funzione lambda
# Una funzione anonima che può essere definita in una singola riga.
add = lambda x, y: x + y

print(add(3, 4))  # Stampa 7
```

```python
# 9. Funzione di ordine superiore
# Una funzione che accetta una funzione come argomento o restituisce una funzione.
def apply_function(f, x):
    return f(x)

result = apply_function(lambda x: x * x, 4)
print(result)  # Stampa 16
```

```python
# 10. Funzione decoratore
# Una funzione che modifica il comportamento di un'altra funzione senza modificarne il codice.
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def say_hello():
    print("Hello, World!")

say_hello()
```

```python
# 11. Funzione con variabili globali
# Una funzione che accede e modifica variabili definite fuori dalla funzione.
x = 10

def increment():
    global x
    x += 1

increment()
print(x)  # Stampa 11
```

```python
# 12. Funzione con tipi di ritorno complessi
# Una funzione che restituisce un valore di tipo complesso, come una lista o un dizionario.
def get_person_info():
    return {"name": "Alice", "age": 25}

person = get_person_info()
print(person)  # Stampa {'name': 'Alice', 'age': 25}
```



## Variabili

```python
# 1. Variabile semplice (intero)
# Una variabile che contiene un numero intero.
numero = 10
print(numero)  # Stampa 10
```

```python
# 2. Variabile stringa
# Una variabile che contiene una sequenza di caratteri.
nome = "Alice"
print(nome)  # Stampa "Alice"
```


```python
# 3. Variabile float (numero decimale)
# Una variabile che contiene un numero con la virgola decimale.
pi_greco = 3.14
print(pi_greco)  # Stampa 3.14
```

```python
# 4. Variabile booleana
# Una variabile che può essere vera o falsa.
is_python_fun = True
print(is_python_fun)  # Stampa True
```


```python
# 5. Variabile lista
# Una variabile che contiene una collezione ordinata di elementi.
numeri = [1, 2, 3, 4, 5]
print(numeri)  # Stampa [1, 2, 3, 4, 5]
```


```python
# 6. Variabile dizionario
# Una variabile che contiene coppie chiave-valore.
persona = {"nome": "Alice", "età": 25}
print(persona)  # Stampa {'nome': 'Alice', 'età': 25}
```


```python
# 8. Variabile set (insieme)
# Una variabile che contiene una collezione non ordinata di elementi univoci.
frutti = {"mela", "banana", "arancia"}
print(frutti)  # Stampa {'mela', 'banana', 'arancia'}
```


```python
# 9. Variabile complessa (numero complesso)
# Una variabile che rappresenta un numero complesso con una parte reale e una parte immaginaria.
numero_complesso = 3 + 4j
print(numero_complesso)  # Stampa (3+4j)
```



```python
# 11. Variabile globale
# Una variabile definita fuori da una funzione e accessibile al suo interno con la parola chiave 'global'.
x = 5

def modifica_x():
    global x
    x = 10

modifica_x()
print(x)  # Stampa 10
```


```python
# 12. Variabile locale
# Una variabile definita all'interno di una funzione e visibile solo all'interno di quella funzione.
def somma():
    y = 5
    return y + 3

print(somma())  # Stampa 8
# print(y)       # Genererebbe un errore, perché 'y' è una variabile locale.
```




