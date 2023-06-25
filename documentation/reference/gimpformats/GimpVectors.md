# Gimpvectors

[Gimpformats Index](../README.md#gimpformats-index) /
[Gimpformats](./index.md#gimpformats) /
Gimpvectors

> Auto-generated documentation for [gimpformats.GimpVectors](../../../gimpformats/GimpVectors.py) module.

- [Gimpvectors](#gimpvectors)
  - [GimpPoint](#gimppoint)
    - [GimpPoint().__repr__](#gimppoint()__repr__)
    - [GimpPoint().decode](#gimppoint()decode)
    - [GimpPoint().encode](#gimppoint()encode)
  - [GimpStroke](#gimpstroke)
    - [GimpStroke().__repr__](#gimpstroke()__repr__)
    - [GimpStroke().decode](#gimpstroke()decode)
    - [GimpStroke().encode](#gimpstroke()encode)
  - [GimpVector](#gimpvector)
    - [GimpVector().__repr__](#gimpvector()__repr__)
    - [GimpVector().decode](#gimpvector()decode)
    - [GimpVector().encode](#gimpvector()encode)

## GimpPoint

[Show source in GimpVectors.py:140](../../../gimpformats/GimpVectors.py#L140)

A single point within a stroke.

#### Signature

```python
class GimpPoint:
    def __init__(self, parent):
        ...
```

### GimpPoint().__repr__

[Show source in GimpVectors.py:204](../../../gimpformats/GimpVectors.py#L204)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent=""):
    ...
```

### GimpPoint().decode

[Show source in GimpVectors.py:155](../../../gimpformats/GimpVectors.py#L155)

Decode a byte buffer.

#### Arguments

- `data` *bytes* - data buffer to decode
- `index` *int, optional* - index within the buffer to start at. Defaults to 0.
- `numFloatsPerPoint` *int, optional* - required so we know
how many different brush dynamic measurements are
inside each point. Defaults to 0.

#### Returns

- `int` - offset

#### Signature

```python
def decode(self, data: bytes, index: int = 0, numFloatsPerPoint: int = 0):
    ...
```

### GimpPoint().encode

[Show source in GimpVectors.py:188](../../../gimpformats/GimpVectors.py#L188)

Encode to binary data.

#### Signature

```python
def encode(self):
    ...
```



## GimpStroke

[Show source in GimpVectors.py:85](../../../gimpformats/GimpVectors.py#L85)

A single stroke within a vector.

#### Signature

```python
class GimpStroke:
    def __init__(self, parent):
        ...
```

### GimpStroke().__repr__

[Show source in GimpVectors.py:129](../../../gimpformats/GimpVectors.py#L129)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: str = ""):
    ...
```

### GimpStroke().decode

[Show source in GimpVectors.py:97](../../../gimpformats/GimpVectors.py#L97)

Decode a byte buffer.

#### Arguments

- `data` *bytes* - data buffer to decode
- `index` *int, optional* - index within the buffer to start at. Defaults to 0.

#### Returns

- `int` - offset

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int:
    ...
```

### GimpStroke().encode

[Show source in GimpVectors.py:118](../../../gimpformats/GimpVectors.py#L118)

Encode to binary data.

#### Signature

```python
def encode(self):
    ...
```



## GimpVector

[Show source in GimpVectors.py:12](../../../gimpformats/GimpVectors.py#L12)

A gimp brush stroke vector.

#### Signature

```python
class GimpVector:
    def __init__(self, parent):
        ...
```

### GimpVector().__repr__

[Show source in GimpVectors.py:67](../../../gimpformats/GimpVectors.py#L67)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: str = "") -> str:
    ...
```

### GimpVector().decode

[Show source in GimpVectors.py:25](../../../gimpformats/GimpVectors.py#L25)

Decode a byte buffer.

#### Arguments

- `data` *bytes* - data buffer to decode
- `index` *int, optional* - index within the buffer to start at. Defaults to 0.

#### Returns

- `int` - offset

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int:
    ...
```

### GimpVector().encode

[Show source in GimpVectors.py:52](../../../gimpformats/GimpVectors.py#L52)

Encode to binary data.

#### Signature

```python
def encode(self):
    ...
```


