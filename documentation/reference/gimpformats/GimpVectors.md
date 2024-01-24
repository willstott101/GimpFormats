# Gimpvectors

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpvectors

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

[Show source in GimpVectors.py:142](../../../gimpformats/GimpVectors.py#L142)

A single point within a stroke.

#### Signature

```python
class GimpPoint:
    def __init__(self, parent) -> None: ...
```

### GimpPoint().__repr__

[Show source in GimpVectors.py:208](../../../gimpformats/GimpVectors.py#L208)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: str = "") -> str: ...
```

### GimpPoint().decode

[Show source in GimpVectors.py:157](../../../gimpformats/GimpVectors.py#L157)

Decode a byte buffer.

#### Arguments

----
 - `data` *bytes* - data buffer to decode
 - `index` *int, optional* - index within the buffer to start at. Defaults to 0.
 - `numFloatsPerPoint` *int, optional* - required so we know
 how many different brush dynamic measurements are
 inside each point. Defaults to 0.

#### Returns

-------
 - `int` - offset

#### Signature

```python
def decode(self, data: bytes, index: int = 0, numFloatsPerPoint: int = 0): ...
```

### GimpPoint().encode

[Show source in GimpVectors.py:192](../../../gimpformats/GimpVectors.py#L192)

Encode to binary data.

#### Signature

```python
def encode(self): ...
```



## GimpStroke

[Show source in GimpVectors.py:85](../../../gimpformats/GimpVectors.py#L85)

A single stroke within a vector.

#### Signature

```python
class GimpStroke:
    def __init__(self, parent) -> None: ...
```

### GimpStroke().__repr__

[Show source in GimpVectors.py:131](../../../gimpformats/GimpVectors.py#L131)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: str = "") -> str: ...
```

### GimpStroke().decode

[Show source in GimpVectors.py:97](../../../gimpformats/GimpVectors.py#L97)

Decode a byte buffer.

#### Arguments

----
 - `data` *bytes* - data buffer to decode
 - `index` *int, optional* - index within the buffer to start at. Defaults to 0.

#### Returns

-------
 - `int` - offset

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int: ...
```

### GimpStroke().encode

[Show source in GimpVectors.py:120](../../../gimpformats/GimpVectors.py#L120)

Encode to binary data.

#### Signature

```python
def encode(self): ...
```



## GimpVector

[Show source in GimpVectors.py:10](../../../gimpformats/GimpVectors.py#L10)

A gimp brush stroke vector.

#### Signature

```python
class GimpVector:
    def __init__(self, parent) -> None: ...
```

### GimpVector().__repr__

[Show source in GimpVectors.py:67](../../../gimpformats/GimpVectors.py#L67)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: str = "") -> str: ...
```

### GimpVector().decode

[Show source in GimpVectors.py:23](../../../gimpformats/GimpVectors.py#L23)

Decode a byte buffer.

#### Arguments

----
 - `data` *bytes* - data buffer to decode
 - `index` *int, optional* - index within the buffer to start at. Defaults to 0.

#### Returns

-------
 - `int` - offset

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int: ...
```

### GimpVector().encode

[Show source in GimpVectors.py:52](../../../gimpformats/GimpVectors.py#L52)

Encode to binary data.

#### Signature

```python
def encode(self): ...
```