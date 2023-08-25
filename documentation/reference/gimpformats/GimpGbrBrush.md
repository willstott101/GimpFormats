# Gimpgbrbrush

[Gimpformats Index](../README.md#gimpformats-index) /
[Gimpformats](./index.md#gimpformats) /
Gimpgbrbrush

> Auto-generated documentation for [gimpformats.GimpGbrBrush](../../../gimpformats/GimpGbrBrush.py) module.

- [Gimpgbrbrush](#gimpgbrbrush)
  - [GimpGbrBrush](#gimpgbrbrush)
    - [GimpGbrBrush().__repr__](#gimpgbrbrush()__repr__)
    - [GimpGbrBrush().decode](#gimpgbrbrush()decode)
    - [GimpGbrBrush().encode](#gimpgbrbrush()encode)
    - [GimpGbrBrush().image](#gimpgbrbrush()image)
    - [GimpGbrBrush().load](#gimpgbrbrush()load)
    - [GimpGbrBrush().save](#gimpgbrbrush()save)
    - [GimpGbrBrush().size](#gimpgbrbrush()size)

## GimpGbrBrush

[Show source in GimpGbrBrush.py:14](../../../gimpformats/GimpGbrBrush.py#L14)

Pure python implementation of the gimp gbr brush format.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/gbr.txt

#### Signature

```python
class GimpGbrBrush:
    def __init__(self, fileName: str = None):
        ...
```

### GimpGbrBrush().__repr__

[Show source in GimpGbrBrush.py:131](../../../gimpformats/GimpGbrBrush.py#L131)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent=""):
    ...
```

### GimpGbrBrush().decode

[Show source in GimpGbrBrush.py:49](../../../gimpformats/GimpGbrBrush.py#L49)

Decode a byte buffer.

#### Arguments

- `data` *bytes* - data buffer to decode
- `index` *int, optional* - index within the buffer to start at. Defaults to 0.

#### Raises

- `RuntimeError` - "unknown brush version"
- `RuntimeError` - "File format error.  Magic value mismatch"

#### Returns

- `int` - offset]

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int:
    ...
```

### GimpGbrBrush().encode

[Show source in GimpGbrBrush.py:87](../../../gimpformats/GimpGbrBrush.py#L87)

Encode this object to byte array.

#### Signature

```python
def encode(self) -> bytearray:
    ...
```

### GimpGbrBrush().image

[Show source in GimpGbrBrush.py:106](../../../gimpformats/GimpGbrBrush.py#L106)

Get a final, compiled image.

#### Signature

```python
@property
def image(self) -> PIL.Image.Image | None:
    ...
```

### GimpGbrBrush().load

[Show source in GimpGbrBrush.py:41](../../../gimpformats/GimpGbrBrush.py#L41)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str):
    ...
```

### GimpGbrBrush().save

[Show source in GimpGbrBrush.py:113](../../../gimpformats/GimpGbrBrush.py#L113)

Save this gimp image to a file.

#### Signature

```python
def save(self, tofileName: str, toExtension: str | None = None):
    ...
```

### GimpGbrBrush().size

[Show source in GimpGbrBrush.py:101](../../../gimpformats/GimpGbrBrush.py#L101)

Get the size.

#### Signature

```python
@property
def size(self) -> tuple[int, int]:
    ...
```