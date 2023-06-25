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

[Show source in GimpGgrGradient.py:115](../../../gimpformats/GimpGgrGradient.py#L115)

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

[Show source in GimpGgrGradient.py:182](../../../gimpformats/GimpGgrGradient.py#L182)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent=""):
    ...
```

### GimpGgrGradient().decode

[Show source in GimpGgrGradient.py:142](../../../gimpformats/GimpGgrGradient.py#L142)

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

[Show source in GimpGgrGradient.py:162](../../../gimpformats/GimpGgrGradient.py#L162)

Encode this to a byte array.

#### Signature

```python
def encode(self):
    ...
```

### GimpGgrGradient().getColor

[Show source in GimpGgrGradient.py:175](../../../gimpformats/GimpGgrGradient.py#L175)

Given a decimal percent (1.0 = 100%) retrieve...

the appropriate color for this point in the gradient.

#### Signature

```python
def getColor(self, percent):
    ...
```

### GimpGgrGradient().load

[Show source in GimpGgrGradient.py:134](../../../gimpformats/GimpGgrGradient.py#L134)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str):
    ...
```

### GimpGgrGradient().save

[Show source in GimpGgrGradient.py:171](../../../gimpformats/GimpGgrGradient.py#L171)

Save this gimp image to a file.

#### Signature

```python
def save(self, tofileName=None):
    ...
```



## GradientSegment

[Show source in GimpGgrGradient.py:11](../../../gimpformats/GimpGgrGradient.py#L11)

Single segment within a gradient.

#### Signature

```python
class GradientSegment:
    def __init__(self):
        ...
```

### GradientSegment().__repr__

[Show source in GimpGgrGradient.py:96](../../../gimpformats/GimpGgrGradient.py#L96)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent=""):
    ...
```

### GradientSegment().decode

[Show source in GimpGgrGradient.py:50](../../../gimpformats/GimpGgrGradient.py#L50)

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

[Show source in GimpGgrGradient.py:76](../../../gimpformats/GimpGgrGradient.py#L76)

Encode this to a byte array.

#### Signature

```python
def encode(self):
    ...
```

### GradientSegment().getColor

[Show source in GimpGgrGradient.py:43](../../../gimpformats/GimpGgrGradient.py#L43)

Given a decimal percent (1.0 = 100%) retrieve the appropriate color
for this point in the gradient.

#### Signature

```python
def getColor(self, percent: float):
    ...
```


