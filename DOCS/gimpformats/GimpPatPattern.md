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

[[find in source code]](../../gimpformats/GimpPatPattern.py#L14)

```python
class GimpPatPattern():
    def __init__(fileName: BytesIO | str = None):
```

Pure python implementation of a gimp pattern file.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/pat.txt

### GimpPatPattern().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpPatPattern.py#L138)

```python
def __repr__():
```

Get a textual representation of this object.

### GimpPatPattern().decode

[[find in source code]](../../gimpformats/GimpPatPattern.py#L49)

```python
def decode(data: bytes, index: int = 0):
```

Decode a byte buffer.

#### Arguments

- `data` *bytes* - data to decode
- `index` *int, optional* - index to start from. Defaults to 0.

#### Raises

- `RuntimeError` - "File format error.  Magic value mismatch."

#### Returns

- `int` - pointer

### GimpPatPattern().encode

[[find in source code]](../../gimpformats/GimpPatPattern.py#L78)

```python
def encode():
```

Encode to a byte buffer.

### GimpPatPattern().image

[[find in source code]](../../gimpformats/GimpPatPattern.py#L100)

```python
@property
def image():
```

Get a final, compiled image.

### GimpPatPattern().image

[[find in source code]](../../gimpformats/GimpPatPattern.py#L111)

```python
@image.setter
def image(image):
```

### GimpPatPattern().load

[[find in source code]](../../gimpformats/GimpPatPattern.py#L41)

```python
def load(fileName: BytesIO | str):
```

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

### GimpPatPattern().save

[[find in source code]](../../gimpformats/GimpPatPattern.py#L116)

```python
def save(tofileName=None, toExtension=None):
```

Save this gimp image to a file.

### GimpPatPattern().size

[[find in source code]](../../gimpformats/GimpPatPattern.py#L95)

```python
@property
def size():
```

The size of the pattern.
