# GimpGihBrushSet

> Auto-generated documentation for [gimpformats.GimpGihBrushSet](../../gimpformats/GimpGihBrushSet.py) module.

Gimp Image Pipe Format.

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / GimpGihBrushSet
    - [GimpGihBrushSet](#gimpgihbrushset)
        - [GimpGihBrushSet().\_\_repr\_\_](#gimpgihbrushset__repr__)
        - [GimpGihBrushSet().decode](#gimpgihbrushsetdecode)
        - [GimpGihBrushSet().encode](#gimpgihbrushsetencode)
        - [GimpGihBrushSet().load](#gimpgihbrushsetload)
        - [GimpGihBrushSet().save](#gimpgihbrushsetsave)

The gih format is use to store a series of brushes, and some extra info
for how to use them.

## GimpGihBrushSet

[[find in source code]](../../gimpformats/GimpGihBrushSet.py#L17)

```python
class GimpGihBrushSet():
    def __init__(fileName: str = None):
```

Gimp Image Pipe Format.

The gih format is use to store a series of brushes, and some extra info
for how to use them.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/gih.txt

### GimpGihBrushSet().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpGihBrushSet.py#L94)

```python
def __repr__(indent=''):
```

Get a textual representation of this object.

### GimpGihBrushSet().decode

[[find in source code]](../../gimpformats/GimpGihBrushSet.py#L48)

```python
def decode(data: bytes, index: int = 0) -> int:
```

Decode a byte buffer.

#### Arguments

- `data` *bytes* - data buffer to decode
- `index` *int, optional* - index within the buffer to start at. Defaults to 0.

#### Returns

- `int` - offset

### GimpGihBrushSet().encode

[[find in source code]](../../gimpformats/GimpGihBrushSet.py#L76)

```python
def encode():
```

Encode this object to a byte array.

### GimpGihBrushSet().load

[[find in source code]](../../gimpformats/GimpGihBrushSet.py#L40)

```python
def load(fileName: BytesIO | str):
```

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

### GimpGihBrushSet().save

[[find in source code]](../../gimpformats/GimpGihBrushSet.py#L90)

```python
def save(tofileName: str):
```

Save this gimp image to a file.
