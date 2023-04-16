# CHEATSHEET

## Ternary

```python
# var = value if condition else value
a = 0 if a > 200 else a + 1
```

## Switch

Version 3.10 upwards required.  

```python
def transform(value: str):
    match value:
        case "A":
            result = 0
        case "B":
            result = 1
        case "C":
            result = 2
        case "D":
            result = 3
        case _:
            result = -1
    return result

transform("A")
transform("B")
transform("Bbbb")
```

## Generators

```python
def fibonacci_sequence():
    num1, num2 = 0, 1
    while True:
        yield num1
        num1, num2 = num2, num1 + num2


g = fibonacci_sequence()
next(g)
```

### Arrays

```python
# 1d array
[i for i in range(10)]

# 2d array
[[i for i in range(10)] for j in range(5)]

# array of dict
[{"x": 0, "y" :0} for j in range(5)]
```

## Lambdas


## Resources

https://realpython.com/introduction-to-python-generators/