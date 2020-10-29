# GimpVectors

> Auto-generated documentation for [gimpformats.GimpVectors](../../gimpformats/GimpVectors.py) module.

Stuff related to vectors/paths within a gimp document

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

[[find in source code]](../../gimpformats/GimpVectors.py#L141)

```python
class GimpPoint():
    def __init__(parent):
```

A single point within a stroke

### GimpPoint().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpVectors.py#L206)

```python
def __repr__(indent=''):
```

Get a textual representation of this object

### GimpPoint().decode

[[find in source code]](../../gimpformats/GimpVectors.py#L158)

```python
def decode(data, index=0, numFloatsPerPoint=0):
```

decode a byte buffer

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at
- `numFloatsPerPoint` - required so we know
 how many different brush dynamic measurements are
 inside each point

### GimpPoint().encode

[[find in source code]](../../gimpformats/GimpVectors.py#L188)

```python
def encode():
```

encode to binary data

## GimpStroke

[[find in source code]](../../gimpformats/GimpVectors.py#L84)

```python
class GimpStroke():
    def __init__(parent):
```

A single stroke within a vector

### GimpStroke().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpVectors.py#L128)

```python
def __repr__(indent=''):
```

Get a textual representation of this object

### GimpStroke().decode

[[find in source code]](../../gimpformats/GimpVectors.py#L97)

```python
def decode(data, index=0):
```

decode a byte buffer

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

### GimpStroke().encode

[[find in source code]](../../gimpformats/GimpVectors.py#L115)

```python
def encode():
```

encode to binary data

## GimpVector

[[find in source code]](../../gimpformats/GimpVectors.py#L10)

```python
class GimpVector():
    def __init__(parent):
```

A gimp brush stroke vector

### GimpVector().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpVectors.py#L64)

```python
def __repr__(indent: str = '') -> str:
```

Get a textual representation of this object

### GimpVector().decode

[[find in source code]](../../gimpformats/GimpVectors.py#L23)

```python
def decode(data, index=0):
```

decode a byte buffer

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

### GimpVector().encode

[[find in source code]](../../gimpformats/GimpVectors.py#L47)

```python
def encode():
```

encode to binary data
