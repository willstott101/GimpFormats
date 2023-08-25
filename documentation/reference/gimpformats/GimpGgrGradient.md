# Gimpggrgradient

[Gimpformats Index](../README.md#gimpformats-index) /
[Gimpformats](./index.md#gimpformats) /
Gimpggrgradient

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

[Show source in GimpGgrGradient.py:114](../../../gimpformats/GimpGgrGradient.py#L114)

Gimp color gradient.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/ggr.txt

#### Signature

```python
class GimpGgrGradient:
    def __init__(self, fileName: str | None = None):
        ...
```

### GimpGgrGradient().__repr__

[Show source in GimpGgrGradient.py:181](../../../gimpformats/GimpGgrGradient.py#L181)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent=""):
    ...
```

### GimpGgrGradient().decode

[Show source in GimpGgrGradient.py:141](../../../gimpformats/GimpGgrGradient.py#L141)

Decode a byte buffer.

#### Arguments

- `dataIn` *bytes* - data buffer to decode

#### Raises

- `RuntimeError` - File format error.  Magic value mismatch.

#### Signature

```python
def decode(self, dataIn: bytes):
    ...
```

### GimpGgrGradient().encode

[Show source in GimpGgrGradient.py:161](../../../gimpformats/GimpGgrGradient.py#L161)

Encode this to a byte array.

#### Signature

```python
def encode(self):
    ...
```

### GimpGgrGradient().getColor

[Show source in GimpGgrGradient.py:174](../../../gimpformats/GimpGgrGradient.py#L174)

Given a decimal percent (1.0 = 100%) retrieve...

the appropriate color for this point in the gradient.

#### Signature

```python
def getColor(self, percent):
    ...
```

### GimpGgrGradient().load

[Show source in GimpGgrGradient.py:133](../../../gimpformats/GimpGgrGradient.py#L133)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str):
    ...
```

### GimpGgrGradient().save

[Show source in GimpGgrGradient.py:170](../../../gimpformats/GimpGgrGradient.py#L170)

Save this gimp image to a file.

#### Signature

```python
def save(self, tofileName=None):
    ...
```



## GradientSegment

[Show source in GimpGgrGradient.py:10](../../../gimpformats/GimpGgrGradient.py#L10)

Single segment within a gradient.

#### Signature

```python
class GradientSegment:
    def __init__(self):
        ...
```

### GradientSegment().__repr__

[Show source in GimpGgrGradient.py:95](../../../gimpformats/GimpGgrGradient.py#L95)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent=""):
    ...
```

### GradientSegment().decode

[Show source in GimpGgrGradient.py:49](../../../gimpformats/GimpGgrGradient.py#L49)

Decode a byte buffer.

#### Arguments

- `dataIn` *str* - data buffer to decode

#### Raises

- `RuntimeError` - [description]

#### Signature

```python
def decode(self, dataIn: str):
    ...
```

### GradientSegment().encode

[Show source in GimpGgrGradient.py:75](../../../gimpformats/GimpGgrGradient.py#L75)

Encode this to a byte array.

#### Signature

```python
def encode(self):
    ...
```

### GradientSegment().getColor

[Show source in GimpGgrGradient.py:42](../../../gimpformats/GimpGgrGradient.py#L42)

Given a decimal percent (1.0 = 100%) retrieve the appropriate color
for this point in the gradient.

#### Signature

```python
def getColor(self, percent: float):
    ...
```