# GimpGgrGradient

> Auto-generated documentation for [gimpformats.GimpGgrGradient](../../gimpformats/GimpGgrGradient.py) module.

Gimp color gradient

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

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L113)

```python
class GimpGgrGradient():
    def __init__(fileName=None):
```

Gimp color gradient.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/ggr.txt

### GimpGgrGradient().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L185)

```python
def __repr__(indent=''):
```

Get a textual representation of this object.

### GimpGgrGradient().decode

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L142)

```python
def decode(data):
```

Decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

### GimpGgrGradient().encode

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L159)

```python
def encode():
```

Encode this to a byte array.

### GimpGgrGradient().getColor

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L178)

```python
def getColor(percent):
```

Given a decimal percent (1.0 = 100%) retrieve...

the appropriate color for this point in the gradient.

### GimpGgrGradient().load

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L127)

```python
def load(fileName: BytesIO | str):
```

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

### GimpGgrGradient().save

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L168)

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

Single segment within a gradient

### GradientSegment().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L96)

```python
def __repr__(indent=''):
```

Get a textual representation of this object

### GradientSegment().decode

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L51)

```python
def decode(data):
```

decode a byte buffer

#### Arguments

- `data` - data buffer to decode

### GradientSegment().encode

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L74)

```python
def encode():
```

encode this to a byte array

### GradientSegment().getColor

[[find in source code]](../../gimpformats/GimpGgrGradient.py#L44)

```python
def getColor(percent):
```

given a decimal percent (1.0 = 100%) retrieve
the appropriate color for this point in the gradient
