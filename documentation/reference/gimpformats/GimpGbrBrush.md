# Gimpgbrbrush

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpgbrbrush

> Auto-generated documentation for [gimpformats.GimpGbrBrush](../../../gimpformats/GimpGbrBrush.py) module.

- [Gimpgbrbrush](#gimpgbrbrush)
  - [GimpGbrBrush](#gimpgbrbrush)
    - [GimpGbrBrush().__repr__](#gimpgbrbrush()__repr__)
    - [GimpGbrBrush().__str__](#gimpgbrbrush()__str__)
    - [GimpGbrBrush().decode](#gimpgbrbrush()decode)
    - [GimpGbrBrush().encode](#gimpgbrbrush()encode)
    - [GimpGbrBrush().image](#gimpgbrbrush()image)
    - [GimpGbrBrush().load](#gimpgbrbrush()load)
    - [GimpGbrBrush().save](#gimpgbrbrush()save)
    - [GimpGbrBrush().size](#gimpgbrbrush()size)

## GimpGbrBrush

[Show source in GimpGbrBrush.py:16](../../../gimpformats/GimpGbrBrush.py#L16)

Pure python implementation of the gimp gbr brush format.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/gbr.txt

#### Signature

```python
class GimpGbrBrush:
    def __init__(self, fileName: str | None = None) -> None: ...
```

### GimpGbrBrush().__repr__

[Show source in GimpGbrBrush.py:138](../../../gimpformats/GimpGbrBrush.py#L138)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: int = 0) -> str: ...
```

### GimpGbrBrush().__str__

[Show source in GimpGbrBrush.py:134](../../../gimpformats/GimpGbrBrush.py#L134)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpGbrBrush().decode

[Show source in GimpGbrBrush.py:52](../../../gimpformats/GimpGbrBrush.py#L52)

Decode a byte buffer.

#### Arguments

----
 - `data` *bytes* - data buffer to decode
 - `index` *int, optional* - index within the buffer to start at. Defaults to 0.

#### Raises

------
 - `RuntimeError` - "unknown brush version"
 - `RuntimeError` - "File format error.  Magic value mismatch"

#### Returns

-------
 - `int` - offset]

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int: ...
```

### GimpGbrBrush().encode

[Show source in GimpGbrBrush.py:94](../../../gimpformats/GimpGbrBrush.py#L94)

Encode this object to byte array.

#### Signature

```python
def encode(self) -> bytearray: ...
```

### GimpGbrBrush().image

[Show source in GimpGbrBrush.py:113](../../../gimpformats/GimpGbrBrush.py#L113)

Get a final, compiled image.

#### Signature

```python
@property
def image(self) -> PIL.Image.Image | None: ...
```

### GimpGbrBrush().load

[Show source in GimpGbrBrush.py:44](../../../gimpformats/GimpGbrBrush.py#L44)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str) -> None: ...
```

### GimpGbrBrush().save

[Show source in GimpGbrBrush.py:120](../../../gimpformats/GimpGbrBrush.py#L120)

Save this gimp image to a file.

#### Signature

```python
def save(self, tofileName: str, toExtension: str | None = None) -> None: ...
```

### GimpGbrBrush().size

[Show source in GimpGbrBrush.py:108](../../../gimpformats/GimpGbrBrush.py#L108)

Get the size.

#### Signature

```python
@property
def size(self) -> tuple[int, int]: ...
```