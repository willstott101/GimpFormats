# Gimpgihbrushset

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpgihbrushset

> Auto-generated documentation for [gimpformats.GimpGihBrushSet](../../../gimpformats/GimpGihBrushSet.py) module.

- [Gimpgihbrushset](#gimpgihbrushset)
  - [GimpGihBrushSet](#gimpgihbrushset)
    - [GimpGihBrushSet().__repr__](#gimpgihbrushset()__repr__)
    - [GimpGihBrushSet().__str__](#gimpgihbrushset()__str__)
    - [GimpGihBrushSet().decode](#gimpgihbrushset()decode)
    - [GimpGihBrushSet().encode](#gimpgihbrushset()encode)
    - [GimpGihBrushSet().load](#gimpgihbrushset()load)
    - [GimpGihBrushSet().save](#gimpgihbrushset()save)

## GimpGihBrushSet

[Show source in GimpGihBrushSet.py:17](../../../gimpformats/GimpGihBrushSet.py#L17)

Gimp Image Pipe Format.

The gih format is use to store a series of brushes, and some extra info
for how to use them.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/gih.txt

#### Signature

```python
class GimpGihBrushSet:
    def __init__(self, fileName: str | None = None) -> None: ...
```

### GimpGihBrushSet().__repr__

[Show source in GimpGihBrushSet.py:103](../../../gimpformats/GimpGihBrushSet.py#L103)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: int = 0) -> str: ...
```

### GimpGihBrushSet().__str__

[Show source in GimpGihBrushSet.py:99](../../../gimpformats/GimpGihBrushSet.py#L99)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpGihBrushSet().decode

[Show source in GimpGihBrushSet.py:50](../../../gimpformats/GimpGihBrushSet.py#L50)

Decode a byte buffer.

#### Arguments

----
 - `data` *bytes* - data buffer to decode
 - `index` *int, optional* - index within the buffer to start at. Defaults to 0.

#### Returns

-------
 - `int` - offset

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int: ...
```

### GimpGihBrushSet().encode

[Show source in GimpGihBrushSet.py:81](../../../gimpformats/GimpGihBrushSet.py#L81)

Encode this object to bytes.

#### Signature

```python
def encode(self) -> bytes: ...
```

### GimpGihBrushSet().load

[Show source in GimpGihBrushSet.py:42](../../../gimpformats/GimpGihBrushSet.py#L42)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str) -> None: ...
```

### GimpGihBrushSet().save

[Show source in GimpGihBrushSet.py:95](../../../gimpformats/GimpGihBrushSet.py#L95)

Save this gimp image to a file.

#### Signature

```python
def save(self, tofileName: str) -> None: ...
```