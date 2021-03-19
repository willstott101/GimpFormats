# GimpPatPattern

> Auto-generated documentation for [gimpformats.GimpPatPattern](../../gimpformats/GimpPatPattern.py) module.

Pure python implementation of a gimp pattern file.

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / GimpPatPattern
    - [GimpPatPattern](#gimppatpattern)
        - [GimpPatPattern().\_\_repr\_\_](#gimppatpattern__repr__)
        - [GimpPatPattern().decode](#gimppatpatterndecode)
        - [GimpPatPattern().encode](#gimppatpatternencode)
        - [GimpPatPattern().image](#gimppatpatternimage)
        - [GimpPatPattern().image](#gimppatpatternimage)
        - [GimpPatPattern().load](#gimppatpatternload)
        - [GimpPatPattern().save](#gimppatpatternsave)
        - [GimpPatPattern().size](#gimppatpatternsize)

## GimpPatPattern

[[find in source code]](../../gimpformats/GimpPatPattern.py#L12)

```python
class GimpPatPattern():
    def __init__(fileName=None):
```

Pure python implementation of a gimp pattern file.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/pat.txt

### GimpPatPattern().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpPatPattern.py#L130)

```python
def __repr__(indent=''):
```

Get a textual representation of this object.

### GimpPatPattern().decode

[[find in source code]](../../gimpformats/GimpPatPattern.py#L49)

```python
def decode(data, index=0):
```

Decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

### GimpPatPattern().encode

[[find in source code]](../../gimpformats/GimpPatPattern.py#L70)

```python
def encode():
```

Encode to a byte buffer.

### GimpPatPattern().image

[[find in source code]](../../gimpformats/GimpPatPattern.py#L92)

```python
@property
def image():
```

Get a final, compiled image.

### GimpPatPattern().image

[[find in source code]](../../gimpformats/GimpPatPattern.py#L103)

```python
@image.setter
def image(image):
```

### GimpPatPattern().load

[[find in source code]](../../gimpformats/GimpPatPattern.py#L34)

```python
def load(fileName: BytesIO | str):
```

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

### GimpPatPattern().save

[[find in source code]](../../gimpformats/GimpPatPattern.py#L108)

```python
def save(tofileName=None, toExtension=None):
```

Save this gimp image to a file.

### GimpPatPattern().size

[[find in source code]](../../gimpformats/GimpPatPattern.py#L87)

```python
@property
def size():
```

The size of the pattern.
