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

[Show source in GimpGbrBrush.py:15](../../../gimpformats/GimpGbrBrush.py#L15)

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

[Show source in GimpGbrBrush.py:132](../../../gimpformats/GimpGbrBrush.py#L132)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent=""):
    ...
```

### GimpGbrBrush().decode

[Show source in GimpGbrBrush.py:50](../../../gimpformats/GimpGbrBrush.py#L50)

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

[Show source in GimpGbrBrush.py:88](../../../gimpformats/GimpGbrBrush.py#L88)

Encode this object to byte array.

#### Signature

```python
def encode(self) -> bytearray:
    ...
```

### GimpGbrBrush().image

[Show source in GimpGbrBrush.py:107](../../../gimpformats/GimpGbrBrush.py#L107)

Get a final, compiled image.

#### Signature

```python
@property
def image(self) -> PIL.Image.Image | None:
    ...
```

### GimpGbrBrush().load

[Show source in GimpGbrBrush.py:42](../../../gimpformats/GimpGbrBrush.py#L42)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str):
    ...
```

### GimpGbrBrush().save

[Show source in GimpGbrBrush.py:114](../../../gimpformats/GimpGbrBrush.py#L114)

Save this gimp image to a file.

#### Signature

```python
def save(self, tofileName: str, toExtension: str | None = None):
    ...
```

### GimpGbrBrush().size

[Show source in GimpGbrBrush.py:102](../../../gimpformats/GimpGbrBrush.py#L102)

Get the size.

#### Signature

```python
@property
def size(self) -> tuple[int, int]:
    ...
```


