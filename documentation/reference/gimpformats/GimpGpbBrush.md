# Gimpgpbbrush

[Gimpformats Index](../README.md#gimpformats-index) /
[Gimpformats](./index.md#gimpformats) /
Gimpgpbbrush

> Auto-generated documentation for [gimpformats.GimpGpbBrush](../../../gimpformats/GimpGpbBrush.py) module.

- [Gimpgpbbrush](#gimpgpbbrush)
  - [GimpGpbBrush](#gimpgpbbrush)
    - [GimpGpbBrush().__repr__](#gimpgpbbrush()__repr__)
    - [GimpGpbBrush().decode](#gimpgpbbrush()decode)
    - [GimpGpbBrush().encode](#gimpgpbbrush()encode)
    - [GimpGpbBrush().load](#gimpgpbbrush()load)
    - [GimpGpbBrush().save](#gimpgpbbrush()save)

## GimpGpbBrush

[Show source in GimpGpbBrush.py:13](../../../gimpformats/GimpGpbBrush.py#L13)

Pure python implementation of the OLD gimp gpb brush format.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/vbr.txt

#### Signature

```python
class GimpGpbBrush:
    def __init__(self, fileName: BytesIO | str):
        ...
```

### GimpGpbBrush().__repr__

[Show source in GimpGpbBrush.py:66](../../../gimpformats/GimpGpbBrush.py#L66)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent=""):
    ...
```

### GimpGpbBrush().decode

[Show source in GimpGpbBrush.py:41](../../../gimpformats/GimpGpbBrush.py#L41)

Decode a byte buffer.

#### Arguments

- `data` *bytes* - data to decode
- `index` *int, optional* - index to start from. Defaults to 0.

#### Returns

- `int` - pointer

#### Signature

```python
def decode(self, data: bytes, index: int = 0):
    ...
```

### GimpGpbBrush().encode

[Show source in GimpGpbBrush.py:55](../../../gimpformats/GimpGpbBrush.py#L55)

Encode this object to a byte array.

#### Signature

```python
def encode(self):
    ...
```

### GimpGpbBrush().load

[Show source in GimpGpbBrush.py:33](../../../gimpformats/GimpGpbBrush.py#L33)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str):
    ...
```

### GimpGpbBrush().save

[Show source in GimpGpbBrush.py:62](../../../gimpformats/GimpGpbBrush.py#L62)

Save this gimp image to a file.

#### Signature

```python
def save(self, tofileName=None):
    ...
```