# GimpPrecision

> Auto-generated documentation for [gimpformats.GimpPrecision](../../gimpformats/GimpPrecision.py) module.

Since the precision code is so unusual, I decided to create a class
to parse it.

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / GimpPrecision
    - [Precision](#precision)
        - [Precision().decode](#precisiondecode)
        - [Precision().encode](#precisionencode)
        - [Precision().requiredGimpVersion](#precisionrequiredgimpversion)

## Precision

[[find in source code]](../../gimpformats/GimpPrecision.py#L10)

```python
class Precision():
    def __init__():
```

Since the precision code is so unusual, I decided to create a class
to parse it.

### Precision().decode

[[find in source code]](../../gimpformats/GimpPrecision.py#L20)

```python
def decode(gimpVersion: int, ioBuf: IO):
```

decode the precision code from the file

### Precision().encode

[[find in source code]](../../gimpformats/GimpPrecision.py#L45)

```python
def encode(gimpVersion: int, ioBuf: IO):
```

encode this to the file

NOTE: will not mess with development versions 5 or 6

### Precision().requiredGimpVersion

[[find in source code]](../../gimpformats/GimpPrecision.py#L80)

```python
def requiredGimpVersion():
```

return the lowest gimp version that supports this precision
