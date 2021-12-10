# GimpGgrGradient

> Auto-generated documentation for [gimpformats.GimpGgrGradient](../../gimpformats/GimpGgrGradient.py) module.

Gimp color gradient.

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / GimpGgrGradient
    - [GimpGgrGradient](#gimpggrgradient)
        - [GimpGgrGradient().\_\_repr\_\_](#gimpggrgradient__repr__)
        - [GimpGgrGradient().decode](#gimpggrgradientdecode)
        - [GimpGgrGradient().encode](#gimpggrgradientencode)
        - [GimpGgrGradient().getColor](#gimpggrgradientgetcolor)
        - [GimpGgrGradient().load](#gimpggrgradientload)
        - [GimpGgrGradient().save](#gimpggrgradientsave)
    - [GradientSegment](#gradientsegment)
        - [GradientSegment().\_\_repr\_\_](#gradientsegment__repr__)
        - [GradientSegment().decode](#gradientsegmentdecode)
        - [GradientSegment().encode](#gradientsegmentencode)
        - [GradientSegment().getColor](#gradientsegmentgetcolor)

## GimpGgrGradient

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L115)

```python
class GimpGgrGradient():
    def __init__(fileName: str | None = None):
```

Gimp color gradient.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/ggr.txt

### GimpGgrGradient().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L182)

```python
def __repr__(indent=''):
```

Get a textual representation of this object.

### GimpGgrGradient().decode

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L142)

```python
def decode(dataIn: bytes):
```

Decode a byte buffer.

#### Arguments

- `dataIn` *bytes* - data buffer to decode

#### Raises

- `RuntimeError` - File format error.  Magic value mismatch.

### GimpGgrGradient().encode

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L162)

```python
def encode():
```

Encode this to a byte array.

### GimpGgrGradient().getColor

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L175)

```python
def getColor(percent):
```

Given a decimal percent (1.0 = 100%) retrieve...

the appropriate color for this point in the gradient.

### GimpGgrGradient().load

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L134)

```python
def load(fileName: BytesIO | str):
```

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

### GimpGgrGradient().save

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L171)

```python
def save(tofileName=None):
```

Save this gimp image to a file.

## GradientSegment

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L11)

```python
class GradientSegment():
    def __init__():
```

Single segment within a gradient.

### GradientSegment().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L96)

```python
def __repr__(indent=''):
```

Get a textual representation of this object.

### GradientSegment().decode

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L50)

```python
def decode(dataIn: str):
```

Decode a byte buffer.

#### Arguments

- `dataIn` *str* - data buffer to decode

#### Raises

- `RuntimeError` - [description]

### GradientSegment().encode

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L76)

```python
def encode():
```

Encode this to a byte array.

### GradientSegment().getColor

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L43)

```python
def getColor(percent: float):
```

Given a decimal percent (1.0 = 100%) retrieve the appropriate color
for this point in the gradient.
