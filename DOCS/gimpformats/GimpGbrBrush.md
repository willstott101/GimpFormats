# GimpGbrBrush

> Auto-generated documentation for [gimpformats.GimpGbrBrush](../../gimpformats/GimpGbrBrush.py) module.

Pure python implementation of the gimp gbr brush format.

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

[[find in source code]](../../gimpformats/GimpGbrBrush.py#L14)

```python
class GimpGbrBrush():
    def __init__(fileName=None):
```

Pure python implementation of the gimp gbr brush format.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/gbr.txt

### GimpGbrBrush().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpGbrBrush.py#L132)

```python
def __repr__(indent=''):
```

Get a textual representation of this object.

### GimpGbrBrush().decode

[[find in source code]](../../gimpformats/GimpGbrBrush.py#L51)

```python
def decode(data: bytes, index: int = 0) -> int:
```

Decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

### GimpGbrBrush().encode

[[find in source code]](../../gimpformats/GimpGbrBrush.py#L81)

```python
def encode() -> bytearray:
```

encode this object to byte array

### GimpGbrBrush().image

[[find in source code]](../../gimpformats/GimpGbrBrush.py#L102)

```python
@property
def image() -> PIL.Image.Image | None:
```

get a final, compiled image.

### GimpGbrBrush().load

[[find in source code]](../../gimpformats/GimpGbrBrush.py#L36)

```python
def load(fileName: BytesIO | str):
```

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

### GimpGbrBrush().save

[[find in source code]](../../gimpformats/GimpGbrBrush.py#L109)

```python
def save(tofileName: str, toExtension: str | None = None):
```

save this gimp image to a file.

### GimpGbrBrush().size

[[find in source code]](../../gimpformats/GimpGbrBrush.py#L97)

```python
@property
def size() -> tuple[(int, int)]:
```

Get the size.
