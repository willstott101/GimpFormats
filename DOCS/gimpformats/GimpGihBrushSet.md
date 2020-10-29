# GimpGihBrushSet

> Auto-generated documentation for [gimpformats.GimpGihBrushSet](../../gimpformats/GimpGihBrushSet.py) module.

Gimp Image Pipe Format

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

[[find in source code]](../../gimpformats/GimpGihBrushSet.py#L14)

```python
class GimpGihBrushSet():
    def __init__(fileName=None):
```

Gimp Image Pipe Format

The gih format is use to store a series of brushes, and some extra info
for how to use them.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/gih.txt

### GimpGihBrushSet().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpGihBrushSet.py#L97)

```python
def __repr__(indent=''):
```

Get a textual representation of this object

### GimpGihBrushSet().decode

[[find in source code]](../../gimpformats/GimpGihBrushSet.py#L48)

```python
def decode(data, index=0):
```

decode a byte buffer

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

### GimpGihBrushSet().encode

[[find in source code]](../../gimpformats/GimpGihBrushSet.py#L73)

```python
def encode():
```

encode this object to a byte array

### GimpGihBrushSet().load

[[find in source code]](../../gimpformats/GimpGihBrushSet.py#L32)

```python
def load(fileName: Union[(BytesIO, str)]):
```

load a gimp file

#### Arguments

- `fileName` - can be a file name or a file-like object

### GimpGihBrushSet().save

[[find in source code]](../../gimpformats/GimpGihBrushSet.py#L89)

```python
def save(tofileName=None):
```

save this gimp image to a file
