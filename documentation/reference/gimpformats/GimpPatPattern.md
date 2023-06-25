# Gimppatpattern

[Gimpformats Index](../README.md#gimpformats-index) /
[Gimpformats](./index.md#gimpformats) /
Gimppatpattern

> Auto-generated documentation for [gimpformats.GimpPatPattern](../../../gimpformats/GimpPatPattern.py) module.

- [Gimppatpattern](#gimppatpattern)
  - [GimpPatPattern](#gimppatpattern)
    - [GimpPatPattern().__repr__](#gimppatpattern()__repr__)
    - [GimpPatPattern().decode](#gimppatpattern()decode)
    - [GimpPatPattern().encode](#gimppatpattern()encode)
    - [GimpPatPattern().image](#gimppatpattern()image)
    - [GimpPatPattern().image](#gimppatpattern()image-1)
    - [GimpPatPattern().load](#gimppatpattern()load)
    - [GimpPatPattern().save](#gimppatpattern()save)
    - [GimpPatPattern().size](#gimppatpattern()size)

## GimpPatPattern

[Show source in GimpPatPattern.py:14](../../../gimpformats/GimpPatPattern.py#L14)

Pure python implementation of a gimp pattern file.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/pat.txt

#### Signature

```python
class GimpPatPattern:
    def __init__(self, fileName: BytesIO | str = None):
        ...
```

### GimpPatPattern().__repr__

[Show source in GimpPatPattern.py:138](../../../gimpformats/GimpPatPattern.py#L138)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self):
    ...
```

### GimpPatPattern().decode

[Show source in GimpPatPattern.py:49](../../../gimpformats/GimpPatPattern.py#L49)

Decode a byte buffer.

#### Arguments

- `data` *bytes* - data to decode
- `index` *int, optional* - index to start from. Defaults to 0.

#### Raises

- `RuntimeError` - "File format error.  Magic value mismatch."

#### Returns

- `int` - pointer

#### Signature

```python
def decode(self, data: bytes, index: int = 0):
    ...
```

### GimpPatPattern().encode

[Show source in GimpPatPattern.py:78](../../../gimpformats/GimpPatPattern.py#L78)

Encode to a byte buffer.

#### Signature

```python
def encode(self):
    ...
```

### GimpPatPattern().image

[Show source in GimpPatPattern.py:100](../../../gimpformats/GimpPatPattern.py#L100)

Get a final, compiled image.

#### Signature

```python
@property
def image(self):
    ...
```

### GimpPatPattern().image

[Show source in GimpPatPattern.py:111](../../../gimpformats/GimpPatPattern.py#L111)

#### Signature

```python
@image.setter
def image(self, image):
    ...
```

### GimpPatPattern().load

[Show source in GimpPatPattern.py:41](../../../gimpformats/GimpPatPattern.py#L41)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str):
    ...
```

### GimpPatPattern().save

[Show source in GimpPatPattern.py:116](../../../gimpformats/GimpPatPattern.py#L116)

Save this gimp image to a file.

#### Signature

```python
def save(self, tofileName=None, toExtension=None):
    ...
```

### GimpPatPattern().size

[Show source in GimpPatPattern.py:95](../../../gimpformats/GimpPatPattern.py#L95)

The size of the pattern.

#### Signature

```python
@property
def size(self):
    ...
```


