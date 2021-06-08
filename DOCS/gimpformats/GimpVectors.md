# GimpVectors

> Auto-generated documentation for [gimpformats.GimpVectors](../../gimpformats/GimpVectors.py) module.

Stuff related to vectors/paths within a gimp document.

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / GimpVectors
    - [GimpPoint](#gimppoint)
        - [GimpPoint().\_\_repr\_\_](#gimppoint__repr__)
        - [GimpPoint().decode](#gimppointdecode)
        - [GimpPoint().encode](#gimppointencode)
    - [GimpStroke](#gimpstroke)
        - [GimpStroke().\_\_repr\_\_](#gimpstroke__repr__)
        - [GimpStroke().decode](#gimpstrokedecode)
        - [GimpStroke().encode](#gimpstrokeencode)
    - [GimpVector](#gimpvector)
        - [GimpVector().\_\_repr\_\_](#gimpvector__repr__)
        - [GimpVector().decode](#gimpvectordecode)
        - [GimpVector().encode](#gimpvectorencode)

## GimpPoint

[[find in source code]](../../gimpformats/GimpVectors.py#L138)

```python
class GimpPoint():
    def __init__(parent):
```

A single point within a stroke.

### GimpPoint().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpVectors.py#L201)

```python
def __repr__(indent=''):
```

Get a textual representation of this object.

### GimpPoint().decode

[[find in source code]](../../gimpformats/GimpVectors.py#L152)

```python
def decode(data: bytes, index: int = 0, numFloatsPerPoint: int = 0):
```

Decode a byte buffer.

#### Arguments

- `data` *bytes* - data buffer to decode
- `index` *int, optional* - index within the buffer to start at. Defaults to 0.
- `numFloatsPerPoint` *int, optional* - required so we know
how many different brush dynamic measurements are
inside each point. Defaults to 0.

#### Returns

- `int` - offset

### GimpPoint().encode

[[find in source code]](../../gimpformats/GimpVectors.py#L185)

```python
def encode():
```

Encode to binary data.

## GimpStroke

[[find in source code]](../../gimpformats/GimpVectors.py#L84)

```python
class GimpStroke():
    def __init__(parent):
```

A single stroke within a vector.

### GimpStroke().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpVectors.py#L127)

```python
def __repr__(indent: str = ''):
```

Get a textual representation of this object.

### GimpStroke().decode

[[find in source code]](../../gimpformats/GimpVectors.py#L95)

```python
def decode(data: bytes, index: int = 0) -> int:
```

Decode a byte buffer.

#### Arguments

- `data` *bytes* - data buffer to decode
- `index` *int, optional* - index within the buffer to start at. Defaults to 0.

#### Returns

- `int` - offset

### GimpStroke().encode

[[find in source code]](../../gimpformats/GimpVectors.py#L116)

```python
def encode():
```

Encode to binary data.

## GimpVector

[[find in source code]](../../gimpformats/GimpVectors.py#L12)

```python
class GimpVector():
    def __init__(parent):
```

A gimp brush stroke vector.

### GimpVector().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpVectors.py#L66)

```python
def __repr__(indent: str = '') -> str:
```

Get a textual representation of this object.

### GimpVector().decode

[[find in source code]](../../gimpformats/GimpVectors.py#L24)

```python
def decode(data: bytes, index: int = 0) -> int:
```

Decode a byte buffer.

#### Arguments

- `data` *bytes* - data buffer to decode
- `index` *int, optional* - index within the buffer to start at. Defaults to 0.

#### Returns

- `int` - offset

### GimpVector().encode

[[find in source code]](../../gimpformats/GimpVectors.py#L51)

```python
def encode():
```

Encode to binary data.
