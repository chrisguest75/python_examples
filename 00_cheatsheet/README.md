# CHEATSHEET

## Contents

- [CHEATSHEET](#cheatsheet)
  - [Contents](#contents)
  - [sleeping](#sleeping)
  - [conditional args](#conditional-args)
  - [args](#args)
  - [kwargs](#kwargs)
  - [Ternary](#ternary)
  - [Switch](#switch)
  - [Generators](#generators)
    - [Arrays](#arrays)
  - [Lambdas](#lambdas)
  - [Resources](#resources)

## sleeping

```sh
import time

time.sleep(3) # Sleep for 3 seconds
```

## conditional args

args is for lists of positional arguments.

```python
def test_function(value1, value2, value3):
    print(f"{value1} {value2} {value3}")

config = { "value1": "v1", "value2": "v2", "value3": "v3" }
# explode values into parameters
test_function(**config)

config = { "value1": "v1", "value2": "v2" }
# fails as missing value3
test_function(**config)
```

## args

args is for lists of positional arguments.

```python
def sum_function(*args):
    result=0
    for x in args:
        result += x
    print(result)

sum_function(1,2,3,4,5)
```

## kwargs

kwargs is for named arguments.

```python
def named_args_function(**args):
    for x in args.keys():
        print(f"{x}={args[x]}")

named_args_function(a=1, b=2, c=3)
```

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

- How to Use Generators and yield in Python [here](https://realpython.com/introduction-to-python-generators/)
- Python args and kwargs: Demystified [here](https://realpython.com/python-kwargs-and-args/)
