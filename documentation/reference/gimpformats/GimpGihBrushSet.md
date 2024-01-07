# Gimpgihbrushset

[Gimpformats Index](../README.md#gimpformats-index) /
[Gimpformats](./index.md#gimpformats) /
Gimpgihbrushset

> Auto-generated documentation for [gimpformats.GimpGihBrushSet](../../../gimpformats/GimpGihBrushSet.py) module.

- [Gimpgihbrushset](#gimpgihbrushset)
  - [GimpGihBrushSet](#gimpgihbrushset)
    - [GimpGihBrushSet().__repr__](#gimpgihbrushset()__repr__)
    - [GimpGihBrushSet().decode](#gimpgihbrushset()decode)
    - [GimpGihBrushSet().encode](#gimpgihbrushset()encode)
    - [GimpGihBrushSet().load](#gimpgihbrushset()load)
    - [GimpGihBrushSet().save](#gimpgihbrushset()save)

## GimpGihBrushSet

[Show source in GimpGihBrushSet.py:15](../../../gimpformats/GimpGihBrushSet.py#L15)

Gimp Image Pipe Format.

The gih format is use to store a series of brushes, and some extra info
for how to use them.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/gih.txt

#### Signature

```python
class GimpGihBrushSet:
    def __init__(self, fileName: str = None): ...
```

### GimpGihBrushSet().__repr__

[Show source in GimpGihBrushSet.py:92](../../../gimpformats/GimpGihBrushSet.py#L92)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent=""): ...
```

### GimpGihBrushSet().decode

[Show source in GimpGihBrushSet.py:46](../../../gimpformats/GimpGihBrushSet.py#L46)

Decode a byte buffer.

#### Arguments

- `data` *bytes* - data buffer to decode
- `index` *int, optional* - index within the buffer to start at. Defaults to 0.

#### Returns

- `int` - offset

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int: ...
```

### GimpGihBrushSet().encode

[Show source in GimpGihBrushSet.py:74](../../../gimpformats/GimpGihBrushSet.py#L74)

Encode this object to a byte array.

#### Signature

```python
def encode(self): ...
```

### GimpGihBrushSet().load

[Show source in GimpGihBrushSet.py:38](../../../gimpformats/GimpGihBrushSet.py#L38)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str): ...
```

### GimpGihBrushSet().save

[Show source in GimpGihBrushSet.py:88](../../../gimpformats/GimpGihBrushSet.py#L88)

Save this gimp image to a file.

#### Signature

```python
def save(self, tofileName: str): ...
```