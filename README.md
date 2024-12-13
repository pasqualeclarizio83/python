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


## Array

```python
# 1. Array Semplice
# Creazione di un array (lista) di numeri interi
numeri = [1, 2, 3, 4, 5]
print(numeri)
```


```python
# 2. Array di Stringhe
# Creazione di un array (lista) di stringhe
frutti = ["mela", "banana", "ciliegia"]
print(frutti)
```


```python
# 3. Array Misto
# Creazione di un array contenente tipi diversi
misto = [1, "ciao", 3.14, True]
print(misto)
```


```python
# 4. Array Bidimensionale (Matrice)
# Creazione di una matrice 2x2
matrice = [
    [1, 2],
    [3, 4]
]
print(matrice)
```


```python
# 5. Aggiungere Elementi all'Array
# Utilizzo del metodo append() per aggiungere un elemento alla fine della lista
numeri.append(6)
print(numeri)
```



```python
# 6. Inserire Elementi in una Posizione Specifica
# Utilizzo del metodo insert() per inserire un elemento in una posizione specifica
frutti.insert(1, "arancia")  # Inserisce "arancia" nella posizione 1
print(frutti)
```



```python
# 7. Rimuovere Elementi dall'Array
# Utilizzo del metodo remove() per rimuovere un elemento specifico
frutti.remove("banana")
print(frutti)
```




```python
# 8. Rimuovere Elementi per Indice
# Utilizzo del metodo pop() per rimuovere un elemento in una posizione specifica
frutti.pop(0)  # Rimuove l'elemento nella posizione 0
print(frutti)
```



```python
# 9. Accedere agli Elementi
# Accesso agli elementi tramite l'indice
print(numeri[0])  # Primo elemento dell'array
```



```python
# 10. Slicing dell'Array
# Estrarre una porzione dell'array utilizzando lo slicing
print(numeri[1:4])  # Estrae gli elementi dall'indice 1 all'indice 3
```



```python
# 10. Slicing dell'Array
# Estrarre una porzione dell'array utilizzando lo slicing
print(numeri[1:4])  # Estrae gli elementi dall'indice 1 all'indice 3
```


```python
# 11. Trovare la Lunghezza dell'Array
# Utilizzo della funzione len() per ottenere la lunghezza dell'array
print(len(numeri))
```


```python
# 12. Ordinare l'Array
# Utilizzo del metodo sort() per ordinare l'array in ordine crescente
numeri.sort()
print(numeri)
```


```python
# 13. Ordinare l'Array in Ordine Decrescente
# Utilizzo del metodo sort() con reverse=True
numeri.sort(reverse=True)
print(numeri)
```


```python
# 14. Copiare un Array
# Utilizzo del metodo copy() per creare una copia dell'array
copia_numeri = numeri.copy()
print(copia_numeri)
```


```python
# 15. Iterare su un Array
# Utilizzo di un ciclo for per iterare sugli elementi di un array
for numero in numeri:
    print(numero)
```


```python
# 16. Verificare se un Elemento è nell'Array
# Utilizzo dell'operatore in per verificare la presenza di un elemento
if 3 in numeri:
    print("3 è presente nell'array")
```


```python
# 17. Sommare gli Elementi di un Array
# Utilizzo della funzione sum() per sommare tutti gli elementi dell'array
somma = sum(numeri)
print(somma)
```



```python
# 18. Funzione che Restituisce un Array
# Funzione che restituisce una lista di numeri quadrati
def crea_quadrati(n):
    return [i ** 2 for i in range(n)]

print(crea_quadrati(5))
```



```python
# 19. Filtrare un Array
# Funzione che filtra i numeri pari da una lista
def filtra_pari(lista):
    return [x for x in lista if x % 2 == 0]

print(filtra_pari(numeri))
```


```python
# 20. Funzione con Parametri di Default
# Funzione che aggiunge un elemento a una lista con parametro di default
def aggiungi_elemento(lista=None):
    if lista is None:
        lista = []
    lista.append("nuovo elemento")
    return lista

print(aggiungi_elemento())
```


## Funzioni con Array


```python
# 1. Funzione Semplice: Somma degli Elementi
# Questa funzione prende un array di numeri e restituisce la loro somma.
def somma_array(numeri):
    return sum(numeri)
```


```python
# 2. Funzione Semplice: Trovare il Massimo
# Questa funzione restituisce il valore massimo in un array di numeri.
def trova_massimo(numeri):
    return max(numeri)
```



```python
# 3. Funzione con Parametro di Default
# Aggiunge un elemento all'array con un valore di default.
def aggiungi_elemento(lista=None):
    if lista is None:
        lista = []
    lista.append("elemento")
    return lista
```


```python
# 4. Funzione con Filtraggio: Numeri Pari
# Restituisce solo i numeri pari presenti nell'array.
def filtra_pari(numeri):
    return [num for num in numeri if num % 2 == 0]
```


```python
# 5. Funzione con Filtraggio: Parole Lunghe
# Restituisce solo le parole con più di 5 caratteri.
def filtra_parole_lunghe(parole):
    return [parola for parola in parole if len(parola) > 5]
```


```python
# 6. Funzione con Mappatura: Quadrati dei Numeri
# Restituisce un nuovo array con i quadrati degli elementi originali.
def quadrati(numeri):
    return [num ** 2 for num in numeri]
```



```python
# 7. Funzione con Riduzione: Prodotto degli Elementi
# Calcola il prodotto di tutti gli elementi nell'array.
from functools import reduce

def prodotto_array(numeri):
    return reduce(lambda x, y: x * y, numeri)
```



```python
# 8. Funzione Complessa: Matrice Trasposta
# Restituisce la trasposta di una matrice (array bidimensionale).
def trasponi_matrice(matrice):
    return [[riga[i] for riga in matrice] for i in range(len(matrice[0]))]

# Esempio di utilizzo
matrice = [
    [1, 2, 3],
    [4, 5, 6]
]
```



```python
# 9. Funzione Complessa: Merge di Due Liste Ordinate
# Unisce due liste ordinate in una singola lista ordinata.
def merge(l1, l2):
    risultato = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            risultato.append(l1[i])
            i += 1
        else:
            risultato.append(l2[j])
            j += 1
    risultato.extend(l1[i:])
    risultato.extend(l2[j:])
    return risultato
```


```python
# 10. Funzione Complessa: Eliminare Duplicati
# Restituisce un array senza elementi duplicati mantenendo l'ordine originale.
def rimuovi_duplicati(lista):
    vista = set()
    risultato = []
    for elemento in lista:
        if elemento not in vista:
            vista.add(elemento)
            risultato.append(elemento)
    return risultato
```


## Algoritmi di Ordinamento

```python
# Bubble Sort - Ordina una lista in ordine crescente
def bubble_sort(arr):
    n = len(arr)
    # Passa attraverso la lista ripetutamente
    for i in range(n):
        # Ultimi i elementi sono già ordinati
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Scambia gli elementi
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Esempio di utilizzo
numeri = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numeri)
print(numeri)  # Output: [11, 12, 22, 25, 34, 64, 90]

```


```python
# Selection Sort - Ordina una lista in ordine crescente
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Trova l'indice del minimo elemento nella parte non ordinata
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Scambia il minimo elemento con il primo elemento non ordinato
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Esempio di utilizzo
numeri = [64, 25, 12, 22, 11]
selection_sort(numeri)
print(numeri)  # Output: [11, 12, 22, 25, 64]


```


```python
# Insertion Sort - Ordina una lista in ordine crescente
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Sposta gli elementi dell'array che sono maggiori della chiave
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Esempio di utilizzo
numeri = [12, 11, 13, 5, 6]
insertion_sort(numeri)
print(numeri)  # Output: [5, 6, 11, 12, 13]



```


```python
# Merge Sort - Ordina una lista in ordine crescente
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Trova il punto medio
        L = arr[:mid]
        R = arr[mid:]

        # Ordina le due metà
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Fonde le due metà ordinate
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copia gli elementi rimanenti di L, se presenti
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copia gli elementi rimanenti di R, se presenti
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Esempio di utilizzo
numeri = [38, 27, 43, 3, 9, 82, 10]
merge_sort(numeri)
print(numeri)  # Output: [3, 9, 10, 27, 38, 43, 82]



```


```python
# Quick Sort - Ordina una lista in ordine crescente
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        # Elementi minori del pivot
        left = [x for x in arr[1:] if x <= pivot]
        # Elementi maggiori del pivot
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

# Esempio di utilizzo
numeri = [10, 7, 8, 9, 1, 5]
numeri_ordinati = quick_sort(numeri)
print(numeri_ordinati)  # Output: [1, 5, 7, 8, 9, 10]

```


```python
# Heap Sort - Ordina una lista in ordine crescente
def heapify(arr, n, i):
    largest = i  # Inizializza il nodo più grande come radice
    left = 2 * i + 1
    right = 2 * i + 2

    # Verifica se il figlio sinistro è più grande della radice
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Verifica se il figlio destro è più grande della radice
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Se la radice non è il più grande, scambia e continua l'heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Costruisce un max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Estrae gli elementi uno alla volta
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Esempio di utilizzo
numeri = [12, 11, 13, 5, 6, 7]
heap_sort(numeri)
print(numeri)  # Output: [5, 6, 7, 11, 12, 13]

```



```python
# Tim Sort - Un algoritmo di ordinamento ibrido che combina Merge Sort e Insertion Sort
def tim_sort(arr):
    # Funzione di utilità per l'ordinamento tramite Insertion Sort su piccole porzioni dell'array
    def insertion_sort(arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    # Dimensione della sub-array in cui utilizziamo Insertion Sort
    RUN = 32
    n = len(arr)

    # Ordina le sub-array utilizzando Insertion Sort
    for i in range(0, n, RUN):
        insertion_sort(arr, i, min(i + RUN - 1, n - 1))

    # Ora uniamo le sub-array ordinate utilizzando Merge Sort
    size = RUN
    while size < n:
        for start in range(0, n, 2 * size):
            mid = min(n - 1, start + size - 1)
            end = min((start + 2 * size - 1), (n - 1))
            if mid < end:
                merge(arr, start, mid, end)
        size *= 2

# Funzione di unione per il merge sort
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = arr[left:left + n1]
    R = arr[mid + 1:mid + 1 + n2]
    i = j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Esempio di utilizzo
arr = [5, 21, 7, 23, 19]
tim_sort(arr)
print(arr)  # Output: [5, 7, 19, 21, 23]

```


```python
# Radix Sort - Ordina una lista di numeri interi
def radix_sort(arr):
    # Trova il valore massimo
    max_num = max(arr)

    # Esegui il count sort per ogni cifra
    exp = 1  # L'unità di ordinamento (1s, 10s, 100s, etc.)
    while max_num // exp > 0:
        count_sort(arr, exp)
        exp *= 10

# Funzione di Count Sort
def count_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Poiché le cifre vanno da 0 a 9

    # Conta le occorrenze delle cifre
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Modifica il count array per tenere traccia degli indici
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Costruisci l'array di output ordinato
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copia l'array ordinato nel array originale
    for i in range(n):
        arr[i] = output[i]

# Esempio di utilizzo
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print(arr)  # Output: [2, 24, 45, 66, 75, 90, 170, 802]

```



```python
# Bucket Sort - Ordina una lista di numeri in modo efficiente
def bucket_sort(arr):
    # Se l'array è vuoto, restituisci l'array vuoto
    if len(arr) == 0:
        return arr
    
    # Trova il valore massimo e minimo
    min_value = min(arr)
    max_value = max(arr)

    # Definisci la dimensione del bucket
    bucket_count = 10  # Ad esempio, 10 bucket

    # Crea i bucket
    buckets = [[] for _ in range(bucket_count)]

    # Distribuisci gli elementi nei bucket
    for num in arr:
        index = int((num - min_value) / (max_value - min_value + 1) * (bucket_count - 1))
        buckets[index].append(num)

    # Ordina ciascun bucket
    for i in range(bucket_count):
        buckets[i] = sorted(buckets[i])

    # Unisci tutti i bucket
    sorted_arr = []
    for i in range(bucket_count):
        sorted_arr.extend(buckets[i])

    return sorted_arr

# Esempio di utilizzo
arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
arr = bucket_sort(arr)
print(arr)  # Output: [0.32, 0.33, 0.37, 0.42, 0.47, 0.51, 0.52]

```


```python
# Shell Sort - Una versione ottimizzata dell'Insertion Sort
def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Inizializza l'intervallo

    # Continua finché l'intervallo non è ridotto a 1
    while gap > 0:
        # Esegui l'insertion sort per ogni "gap"
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

        gap //= 2  # Riduci l'intervallo

# Esempio di utilizzo
arr = [12, 34, 54, 2, 3]
shell_sort(arr)
print(arr)  # Output: [2, 3, 12, 34, 54]
```