# GimpGpbBrush

> Auto-generated documentation for [gimpformats.GimpGpbBrush](../../gimpformats/GimpGpbBrush.py) module.

Pure python implementation of the OLD gimp gpb brush format.

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / GimpGpbBrush
    - [GimpGpbBrush](#gimpgpbbrush)
        - [GimpGpbBrush().\_\_repr\_\_](#gimpgpbbrush__repr__)
        - [GimpGpbBrush().decode](#gimpgpbbrushdecode)
        - [GimpGpbBrush().encode](#gimpgpbbrushencode)
        - [GimpGpbBrush().load](#gimpgpbbrushload)
        - [GimpGpbBrush().save](#gimpgpbbrushsave)

## GimpGpbBrush

[[find in source code]](../../gimpformats/GimpGpbBrush.py#L14)

```python
class GimpGpbBrush():
    def __init__(fileName: BytesIO | str):
```

Pure python implementation of the OLD gimp gpb brush format.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/vbr.txt

### GimpGpbBrush().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpGpbBrush.py#L79)

```python
def __repr__(indent=''):
```

Get a textual representation of this object.

### GimpGpbBrush().decode

[[find in source code]](../../gimpformats/GimpGpbBrush.py#L49)

```python
def decode(data: bytes, index: int = 0):
```

Decode a byte buffer.

#### Arguments

- `data` *bytes* - data to decode
- `index` *int, optional* - index to start from. Defaults to 0.

#### Returns

- `int` - pointer

### GimpGpbBrush().encode

[[find in source code]](../../gimpformats/GimpGpbBrush.py#L63)

```python
def encode():
```

Encode this object to a byte array.

### GimpGpbBrush().load

[[find in source code]](../../gimpformats/GimpGpbBrush.py#L34)

```python
def load(fileName: BytesIO | str):
```

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

### GimpGpbBrush().save

[[find in source code]](../../gimpformats/GimpGpbBrush.py#L70)

```python
def save(tofileName=None):
```

Save this gimp image to a file.
