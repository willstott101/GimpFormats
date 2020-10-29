# GimpGpbBrush

> Auto-generated documentation for [gimpformats.GimpGpbBrush](../../gimpformats/GimpGpbBrush.py) module.

Pure python implementation of the OLD gimp gpb brush format

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / GimpGpbBrush
    - [GimpGpbBrush](#gimpgpbbrush)
        - [GimpGpbBrush().\_\_repr\_\_](#gimpgpbbrush__repr__)
        - [GimpGpbBrush().decode](#gimpgpbbrushdecode)
        - [GimpGpbBrush().encode](#gimpgpbbrushencode)
        - [GimpGpbBrush().load](#gimpgpbbrushload)
        - [GimpGpbBrush().save](#gimpgpbbrushsave)

## GimpGpbBrush

[[find in source code]](../../gimpformats/GimpGpbBrush.py#L12)

```python
class GimpGpbBrush():
    def __init__(fileName: Union[(BytesIO, str)]):
```

Pure python implementation of the OLD gimp gpb brush format

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/vbr.txt

### GimpGpbBrush().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpGpbBrush.py#L67)

```python
def __repr__(indent=''):
```

Get a textual representation of this object

### GimpGpbBrush().decode

[[find in source code]](../../gimpformats/GimpGpbBrush.py#L43)

```python
def decode(data, index=0):
```

decode a byte buffer

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

### GimpGpbBrush().encode

[[find in source code]](../../gimpformats/GimpGpbBrush.py#L54)

```python
def encode():
```

encode this object to a byte array

### GimpGpbBrush().load

[[find in source code]](../../gimpformats/GimpGpbBrush.py#L27)

```python
def load(fileName: Union[(BytesIO, str)]):
```

load a gimp file

#### Arguments

- `fileName` - can be a file name or a file-like object

### GimpGpbBrush().save

[[find in source code]](../../gimpformats/GimpGpbBrush.py#L61)

```python
def save(tofileName=None):
```

save this gimp image to a file
