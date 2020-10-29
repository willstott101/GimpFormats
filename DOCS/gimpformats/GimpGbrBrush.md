# GimpGbrBrush

> Auto-generated documentation for [gimpformats.GimpGbrBrush](../../gimpformats/GimpGbrBrush.py) module.

Pure python implementation of the gimp gbr brush format

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / GimpGbrBrush
    - [GimpGbrBrush](#gimpgbrbrush)
        - [GimpGbrBrush().\_\_repr\_\_](#gimpgbrbrush__repr__)
        - [GimpGbrBrush().decode](#gimpgbrbrushdecode)
        - [GimpGbrBrush().encode](#gimpgbrbrushencode)
        - [GimpGbrBrush().image](#gimpgbrbrushimage)
        - [GimpGbrBrush().load](#gimpgbrbrushload)
        - [GimpGbrBrush().save](#gimpgbrbrushsave)
        - [GimpGbrBrush().size](#gimpgbrbrushsize)

## GimpGbrBrush

[[find in source code]](../../gimpformats/GimpGbrBrush.py#L12)

```python
class GimpGbrBrush():
    def __init__(fileName=None):
```

Pure python implementation of the gimp gbr brush format

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/gbr.txt

### GimpGbrBrush().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpGbrBrush.py#L126)

```python
def __repr__(indent=''):
```

Get a textual representation of this object

### GimpGbrBrush().decode

[[find in source code]](../../gimpformats/GimpGbrBrush.py#L51)

```python
def decode(data: bytes, index: int = 0):
```

decode a byte buffer

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

### GimpGbrBrush().encode

[[find in source code]](../../gimpformats/GimpGbrBrush.py#L77)

```python
def encode():
```

encode this object to byte array

### GimpGbrBrush().image

[[find in source code]](../../gimpformats/GimpGbrBrush.py#L98)

```python
@property
def image():
```

get a final, compiled image

### GimpGbrBrush().load

[[find in source code]](../../gimpformats/GimpGbrBrush.py#L35)

```python
def load(fileName: Union[(BytesIO, str)]):
```

load a gimp file

#### Arguments

- `fileName` - can be a file name or a file-like object

### GimpGbrBrush().save

[[find in source code]](../../gimpformats/GimpGbrBrush.py#L105)

```python
def save(tofileName=None, toExtension=None):
```

save this gimp image to a file

### GimpGbrBrush().size

[[find in source code]](../../gimpformats/GimpGbrBrush.py#L93)

```python
@property
def size():
```

Get the size
