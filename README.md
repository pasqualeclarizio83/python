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
