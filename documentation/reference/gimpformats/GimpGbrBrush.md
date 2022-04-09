# Gimpgbrbrush

> Auto-generated documentation for [gimpformats.GimpGbrBrush](../../../gimpformats/GimpGbrBrush.py) module.

Pure python implementation of the gimp gbr brush format.

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../MODULES.md#gimpformats-modules) / [Gimpformats](index.md#gimpformats) / Gimpgbrbrush
    - [GimpGbrBrush](#gimpgbrbrush)
        - [GimpGbrBrush().\_\_repr\_\_](#gimpgbrbrush__repr__)
        - [GimpGbrBrush().decode](#gimpgbrbrushdecode)
        - [GimpGbrBrush().encode](#gimpgbrbrushencode)
        - [GimpGbrBrush().image](#gimpgbrbrushimage)
        - [GimpGbrBrush().load](#gimpgbrbrushload)
        - [GimpGbrBrush().save](#gimpgbrbrushsave)
        - [GimpGbrBrush().size](#gimpgbrbrushsize)

## GimpGbrBrush

[[find in source code]](../../../gimpformats/GimpGbrBrush.py#L15)

```python
class GimpGbrBrush():
    def __init__(fileName: str = None):
```

Pure python implementation of the gimp gbr brush format.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/gbr.txt

### GimpGbrBrush().\_\_repr\_\_

[[find in source code]](../../../gimpformats/GimpGbrBrush.py#L132)

```python
def __repr__(indent=''):
```

Get a textual representation of this object.

### GimpGbrBrush().decode

[[find in source code]](../../../gimpformats/GimpGbrBrush.py#L50)

```python
def decode(data: bytes, index: int = 0) -> int:
```

Decode a byte buffer.

#### Arguments

- `data` *bytes* - data buffer to decode
- `index` *int, optional* - index within the buffer to start at. Defaults to 0.

#### Raises

- `RuntimeError` - "unknown brush version"
- `RuntimeError` - "File format error.  Magic value mismatch"

#### Returns

- `int` - offset]

### GimpGbrBrush().encode

[[find in source code]](../../../gimpformats/GimpGbrBrush.py#L88)

```python
def encode() -> bytearray:
```

Encode this object to byte array.

### GimpGbrBrush().image

[[find in source code]](../../../gimpformats/GimpGbrBrush.py#L107)

```python
@property
def image() -> PIL.Image.Image | None:
```

Get a final, compiled image.

### GimpGbrBrush().load

[[find in source code]](../../../gimpformats/GimpGbrBrush.py#L42)

```python
def load(fileName: BytesIO | str):
```

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

### GimpGbrBrush().save

[[find in source code]](../../../gimpformats/GimpGbrBrush.py#L114)

```python
def save(tofileName: str, toExtension: str | None = None):
```

Save this gimp image to a file.

### GimpGbrBrush().size

[[find in source code]](../../../gimpformats/GimpGbrBrush.py#L102)

```python
@property
def size() -> tuple[int, int]:
```

Get the size.
