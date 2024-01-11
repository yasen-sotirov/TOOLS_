<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg" alt="logo" width="300px" style="margin-top: 20px"/>

# Algorithm Complexity Tasks

Define the complexity of each program/algorithm.

## Task 1

```py
def product(a, b): 
    sum = 0
    for _ in range(b): 
        sum += a
    
    return sum
```

## Task 2

```py
def power(a, b): 
    if b < 0: 
        return 0
    
    if b == 0: 
        return 1
    
    power = a
    while b > 1: 
        power *= a
        b -= 1
    
    return power
```

## Task 3

```py
def mod(a, b): 
    if b < 0: 
        return -1
    
    div = a // b
    return a - div * b
```

## Task 4

```py
def sum3(n): 
    sum = 0
    for a in range(n): 
        for b in range(n): 
            for c in range(n): 
                sum += (a * b * c)
            
    return sum
```

## Task 5

```py
def sum_NM(n, m): 
    sum = 0
    for a in range(n):
        for b in range(m): 
            sum += (a * b)
        
    return sum
```

## Task 6

```py
def sum_NM(n, m): 
    sum = 0
    for a in range(n):
        for b in range(m):
            if a == b: 
                for c in range(n):
                    sum += (a * b * c)

    return sum
```

## Task 7

```py
def factorial(n): 
    f = 1
    while n > 1: 
        f *= n
        n -= 1
    
    return f
```
