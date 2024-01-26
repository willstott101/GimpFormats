# Gimpvectors

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpvectors

> Auto-generated documentation for [gimpformats.GimpVectors](../../../gimpformats/GimpVectors.py) module.

- [Gimpvectors](#gimpvectors)
  - [GimpPoint](#gimppoint)
    - [GimpPoint().__repr__](#gimppoint()__repr__)
    - [GimpPoint().__str__](#gimppoint()__str__)
    - [GimpPoint().decode](#gimppoint()decode)
    - [GimpPoint().encode](#gimppoint()encode)
  - [GimpStroke](#gimpstroke)
    - [GimpStroke().__repr__](#gimpstroke()__repr__)
    - [GimpStroke().__str__](#gimpstroke()__str__)
    - [GimpStroke().decode](#gimpstroke()decode)
    - [GimpStroke().encode](#gimpstroke()encode)
  - [GimpVector](#gimpvector)
    - [GimpVector().__repr__](#gimpvector()__repr__)
    - [GimpVector().__str__](#gimpvector()__str__)
    - [GimpVector().decode](#gimpvector()decode)
    - [GimpVector().encode](#gimpvector()encode)

## GimpPoint

[Show source in GimpVectors.py:149](../../../gimpformats/GimpVectors.py#L149)

A single point within a stroke.

#### Signature

```python
class GimpPoint:
    def __init__(self, parent) -> None: ...
```

### GimpPoint().__repr__

[Show source in GimpVectors.py:219](../../../gimpformats/GimpVectors.py#L219)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: int = 0) -> str: ...
```

### GimpPoint().__str__

[Show source in GimpVectors.py:215](../../../gimpformats/GimpVectors.py#L215)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpPoint().decode

[Show source in GimpVectors.py:164](../../../gimpformats/GimpVectors.py#L164)

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

[Show source in GimpVectors.py:199](../../../gimpformats/GimpVectors.py#L199)

Encode to binary data.

#### Signature

```python
def encode(self): ...
```



## GimpStroke

[Show source in GimpVectors.py:88](../../../gimpformats/GimpVectors.py#L88)

A single stroke within a vector.

#### Signature

```python
class GimpStroke:
    def __init__(self, parent) -> None: ...
```

### GimpStroke().__repr__

[Show source in GimpVectors.py:138](../../../gimpformats/GimpVectors.py#L138)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: int = 0) -> str: ...
```

### GimpStroke().__str__

[Show source in GimpVectors.py:134](../../../gimpformats/GimpVectors.py#L134)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpStroke().decode

[Show source in GimpVectors.py:100](../../../gimpformats/GimpVectors.py#L100)

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

[Show source in GimpVectors.py:123](../../../gimpformats/GimpVectors.py#L123)

Encode to binary data.

#### Signature

```python
def encode(self): ...
```



## GimpVector

[Show source in GimpVectors.py:9](../../../gimpformats/GimpVectors.py#L9)

A gimp brush stroke vector.

#### Signature

```python
class GimpVector:
    def __init__(self, parent) -> None: ...
```

### GimpVector().__repr__

[Show source in GimpVectors.py:70](../../../gimpformats/GimpVectors.py#L70)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: int = 0) -> str: ...
```

### GimpVector().__str__

[Show source in GimpVectors.py:66](../../../gimpformats/GimpVectors.py#L66)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpVector().decode

[Show source in GimpVectors.py:22](../../../gimpformats/GimpVectors.py#L22)

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

[Show source in GimpVectors.py:51](../../../gimpformats/GimpVectors.py#L51)

Encode to binary data.

#### Signature

```python
def encode(self): ...
```