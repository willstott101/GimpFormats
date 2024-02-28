# Gimpggrgradient

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpggrgradient

> Auto-generated documentation for [gimpformats.GimpGgrGradient](../../../gimpformats/GimpGgrGradient.py) module.

- [Gimpggrgradient](#gimpggrgradient)
  - [GimpGgrGradient](#gimpggrgradient)
    - [GimpGgrGradient().__repr__](#gimpggrgradient()__repr__)
    - [GimpGgrGradient().__str__](#gimpggrgradient()__str__)
    - [GimpGgrGradient().decode](#gimpggrgradient()decode)
    - [GimpGgrGradient().encode](#gimpggrgradient()encode)
    - [GimpGgrGradient().getColor](#gimpggrgradient()getcolor)
    - [GimpGgrGradient().load](#gimpggrgradient()load)
    - [GimpGgrGradient().save](#gimpggrgradient()save)
  - [GradientSegment](#gradientsegment)
    - [GradientSegment().__repr__](#gradientsegment()__repr__)
    - [GradientSegment().__str__](#gradientsegment()__str__)
    - [GradientSegment().decode](#gradientsegment()decode)
    - [GradientSegment().encode](#gradientsegment()encode)
    - [GradientSegment().getColor](#gradientsegment()getcolor)

## GimpGgrGradient

[Show source in GimpGgrGradient.py:124](../../../gimpformats/GimpGgrGradient.py#L124)

Gimp color gradient.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/ggr.txt

#### Signature

```python
class GimpGgrGradient:
    def __init__(self, fileName: str | None = None) -> None: ...
```

### GimpGgrGradient().__repr__

[Show source in GimpGgrGradient.py:201](../../../gimpformats/GimpGgrGradient.py#L201)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: int = 0) -> str: ...
```

### GimpGgrGradient().__str__

[Show source in GimpGgrGradient.py:197](../../../gimpformats/GimpGgrGradient.py#L197)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpGgrGradient().decode

[Show source in GimpGgrGradient.py:153](../../../gimpformats/GimpGgrGradient.py#L153)

Decode a byte buffer.

#### Arguments

----
 - `dataIn` *bytes* - data buffer to decode

#### Raises

------
 - `RuntimeError` - File format error.  Magic value mismatch.

#### Signature

```python
def decode(self, dataIn: bytes) -> None: ...
```

### GimpGgrGradient().encode

[Show source in GimpGgrGradient.py:177](../../../gimpformats/GimpGgrGradient.py#L177)

Encode this to bytes.

#### Signature

```python
def encode(self) -> bytes: ...
```

### GimpGgrGradient().getColor

[Show source in GimpGgrGradient.py:190](../../../gimpformats/GimpGgrGradient.py#L190)

Given a decimal percent (1.0 = 100%) retrieve...

the appropriate color for this point in the gradient.

#### Signature

```python
def getColor(self, percent: float) -> NoReturn: ...
```

### GimpGgrGradient().load

[Show source in GimpGgrGradient.py:145](../../../gimpformats/GimpGgrGradient.py#L145)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str) -> None: ...
```

### GimpGgrGradient().save

[Show source in GimpGgrGradient.py:186](../../../gimpformats/GimpGgrGradient.py#L186)

Save this gimp image to a file.

#### Signature

```python
def save(self, tofileName: str | BytesIO | None = None) -> None: ...
```



## GradientSegment

[Show source in GimpGgrGradient.py:12](../../../gimpformats/GimpGgrGradient.py#L12)

Single segment within a gradient.

#### Signature

```python
class GradientSegment:
    def __init__(self) -> None: ...
```

### GradientSegment().__repr__

[Show source in GimpGgrGradient.py:105](../../../gimpformats/GimpGgrGradient.py#L105)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: int = 0) -> str: ...
```

### GradientSegment().__str__

[Show source in GimpGgrGradient.py:101](../../../gimpformats/GimpGgrGradient.py#L101)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GradientSegment().decode

[Show source in GimpGgrGradient.py:51](../../../gimpformats/GimpGgrGradient.py#L51)

Decode a byte buffer.

#### Arguments

----
 - `dataIn` *str* - data buffer to decode

#### Raises

------
 - `RuntimeError` - [description]

#### Signature

```python
def decode(self, dataIn: str) -> None: ...
```

### GradientSegment().encode

[Show source in GimpGgrGradient.py:81](../../../gimpformats/GimpGgrGradient.py#L81)

Encode this to a string.

#### Signature

```python
def encode(self) -> str: ...
```

### GradientSegment().getColor

[Show source in GimpGgrGradient.py:44](../../../gimpformats/GimpGgrGradient.py#L44)

Given a decimal percent (1.0 = 100%) retrieve the appropriate color
for this point in the gradient.

#### Signature

```python
def getColor(self, percent: float) -> NoReturn: ...
```