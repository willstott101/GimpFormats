# GimpPrecision

> Auto-generated documentation for [gimpformats.GimpPrecision](../../gimpformats/GimpPrecision.py) module.

Since the precision code is so unusual, I decided to create a class to parse it.

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / GimpPrecision
    - [Precision](#precision)
        - [Precision().\_\_repr\_\_](#precision__repr__)
        - [Precision().decode](#precisiondecode)
        - [Precision().encode](#precisionencode)
        - [Precision().requiredGimpVersion](#precisionrequiredgimpversion)

## Precision

[[find in source code]](../../gimpformats/GimpPrecision.py#L10)

```python
class Precision():
    def __init__():
```

Since the precision code is so unusual, I decided to create a class to parse it.

### Precision().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpPrecision.py#L85)

```python
def __repr__():
```

Get a textual representation of this object.

### Precision().decode

[[find in source code]](../../gimpformats/GimpPrecision.py#L19)

```python
def decode(gimpVersion: int, ioBuf: IO):
```

Decode the precision code from the file.

### Precision().encode

[[find in source code]](../../gimpformats/GimpPrecision.py#L42)

```python
def encode(gimpVersion: int, ioBuf: IO):
```

Encode this to the file.

NOTE: will not mess with development versions 5 or 6

### Precision().requiredGimpVersion

[[find in source code]](../../gimpformats/GimpPrecision.py#L77)

```python
def requiredGimpVersion():
```

Return the lowest gimp version that supports this precision.
