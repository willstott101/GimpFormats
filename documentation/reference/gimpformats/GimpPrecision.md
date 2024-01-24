# Gimpprecision

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpprecision

> Auto-generated documentation for [gimpformats.GimpPrecision](../../../gimpformats/GimpPrecision.py) module.

- [Gimpprecision](#gimpprecision)
  - [Precision](#precision)
    - [Precision().__repr__](#precision()__repr__)
    - [Precision().decode](#precision()decode)
    - [Precision().encode](#precision()encode)
    - [Precision().requiredGimpVersion](#precision()requiredgimpversion)

## Precision

[Show source in GimpPrecision.py:10](../../../gimpformats/GimpPrecision.py#L10)

Since the precision code is so unusual, I decided to create a class to parse it.

#### Signature

```python
class Precision:
    def __init__(self) -> None: ...
```

### Precision().__repr__

[Show source in GimpPrecision.py:86](../../../gimpformats/GimpPrecision.py#L86)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### Precision().decode

[Show source in GimpPrecision.py:19](../../../gimpformats/GimpPrecision.py#L19)

Decode the precision code from the file.

#### Signature

```python
def decode(self, gimpVersion: int, ioBuf: IO) -> None: ...
```

### Precision().encode

[Show source in GimpPrecision.py:42](../../../gimpformats/GimpPrecision.py#L42)

Encode this to the file.

NOTE: will not mess with development versions 5 or 6

#### Signature

```python
def encode(self, gimpVersion: int, ioBuf: IO) -> None: ...
```

### Precision().requiredGimpVersion

[Show source in GimpPrecision.py:78](../../../gimpformats/GimpPrecision.py#L78)

Return the lowest gimp version that supports this precision.

#### Signature

```python
def requiredGimpVersion(self) -> int: ...
```