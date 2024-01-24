# Gimpggrgradient

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpggrgradient

> Auto-generated documentation for [gimpformats.GimpGgrGradient](../../../gimpformats/GimpGgrGradient.py) module.

- [Gimpggrgradient](#gimpggrgradient)
  - [GimpGgrGradient](#gimpggrgradient)
    - [GimpGgrGradient().__repr__](#gimpggrgradient()__repr__)
    - [GimpGgrGradient().decode](#gimpggrgradient()decode)
    - [GimpGgrGradient().encode](#gimpggrgradient()encode)
    - [GimpGgrGradient().getColor](#gimpggrgradient()getcolor)
    - [GimpGgrGradient().load](#gimpggrgradient()load)
    - [GimpGgrGradient().save](#gimpggrgradient()save)
  - [GradientSegment](#gradientsegment)
    - [GradientSegment().__repr__](#gradientsegment()__repr__)
    - [GradientSegment().decode](#gradientsegment()decode)
    - [GradientSegment().encode](#gradientsegment()encode)
    - [GradientSegment().getColor](#gradientsegment()getcolor)

## GimpGgrGradient

[Show source in GimpGgrGradient.py:118](../../../gimpformats/GimpGgrGradient.py#L118)

Gimp color gradient.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/ggr.txt

#### Signature

```python
class GimpGgrGradient:
    def __init__(self, fileName: str | None = None) -> None: ...
```

### GimpGgrGradient().__repr__

[Show source in GimpGgrGradient.py:189](../../../gimpformats/GimpGgrGradient.py#L189)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: str = "") -> str: ...
```

### GimpGgrGradient().decode

[Show source in GimpGgrGradient.py:146](../../../gimpformats/GimpGgrGradient.py#L146)

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

[Show source in GimpGgrGradient.py:169](../../../gimpformats/GimpGgrGradient.py#L169)

Encode this to bytes.

#### Signature

```python
def encode(self) -> bytes: ...
```

### GimpGgrGradient().getColor

[Show source in GimpGgrGradient.py:182](../../../gimpformats/GimpGgrGradient.py#L182)

Given a decimal percent (1.0 = 100%) retrieve...

the appropriate color for this point in the gradient.

#### Signature

```python
def getColor(self, percent: float) -> NoReturn: ...
```

### GimpGgrGradient().load

[Show source in GimpGgrGradient.py:138](../../../gimpformats/GimpGgrGradient.py#L138)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str) -> None: ...
```

### GimpGgrGradient().save

[Show source in GimpGgrGradient.py:178](../../../gimpformats/GimpGgrGradient.py#L178)

Save this gimp image to a file.

#### Signature

```python
def save(self, tofileName: str | BytesIO | None = None) -> None: ...
```



## GradientSegment

[Show source in GimpGgrGradient.py:11](../../../gimpformats/GimpGgrGradient.py#L11)

Single segment within a gradient.

#### Signature

```python
class GradientSegment:
    def __init__(self) -> None: ...
```

### GradientSegment().__repr__

[Show source in GimpGgrGradient.py:99](../../../gimpformats/GimpGgrGradient.py#L99)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: str = "") -> str: ...
```

### GradientSegment().decode

[Show source in GimpGgrGradient.py:50](../../../gimpformats/GimpGgrGradient.py#L50)

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

[Show source in GimpGgrGradient.py:79](../../../gimpformats/GimpGgrGradient.py#L79)

Encode this to a string.

#### Signature

```python
def encode(self) -> str: ...
```

### GradientSegment().getColor

[Show source in GimpGgrGradient.py:43](../../../gimpformats/GimpGgrGradient.py#L43)

Given a decimal percent (1.0 = 100%) retrieve the appropriate color
for this point in the gradient.

#### Signature

```python
def getColor(self, percent: float) -> NoReturn: ...
```