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

## Lambdas


## Resources
