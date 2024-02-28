# Gimppatpattern

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimppatpattern

> Auto-generated documentation for [gimpformats.GimpPatPattern](../../../gimpformats/GimpPatPattern.py) module.

- [Gimppatpattern](#gimppatpattern)
  - [GimpPatPattern](#gimppatpattern)
    - [GimpPatPattern().__repr__](#gimppatpattern()__repr__)
    - [GimpPatPattern().__str__](#gimppatpattern()__str__)
    - [GimpPatPattern().decode](#gimppatpattern()decode)
    - [GimpPatPattern().encode](#gimppatpattern()encode)
    - [GimpPatPattern().image](#gimppatpattern()image)
    - [GimpPatPattern().image](#gimppatpattern()image-1)
    - [GimpPatPattern().load](#gimppatpattern()load)
    - [GimpPatPattern().save](#gimppatpattern()save)
    - [GimpPatPattern().size](#gimppatpattern()size)

## GimpPatPattern

[Show source in GimpPatPattern.py:13](../../../gimpformats/GimpPatPattern.py#L13)

Pure python implementation of a gimp pattern file.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/pat.txt

#### Signature

```python
class GimpPatPattern:
    def __init__(self, fileName: BytesIO | str | None = None) -> None: ...
```

### GimpPatPattern().__repr__

[Show source in GimpPatPattern.py:141](../../../gimpformats/GimpPatPattern.py#L141)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpPatPattern().__str__

[Show source in GimpPatPattern.py:137](../../../gimpformats/GimpPatPattern.py#L137)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpPatPattern().decode

[Show source in GimpPatPattern.py:50](../../../gimpformats/GimpPatPattern.py#L50)

Decode a byte buffer.

#### Arguments

----
 - `data` *bytes* - data to decode
 - `index` *int, optional* - index to start from. Defaults to 0.

#### Raises

------
 - `RuntimeError` - "File format error.  Magic value mismatch."

#### Returns

-------
 - `int` - pointer

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int: ...
```

### GimpPatPattern().encode

[Show source in GimpPatPattern.py:84](../../../gimpformats/GimpPatPattern.py#L84)

Encode to a byte buffer.

#### Signature

```python
def encode(self) -> bytearray: ...
```

### GimpPatPattern().image

[Show source in GimpPatPattern.py:106](../../../gimpformats/GimpPatPattern.py#L106)

Get a final, compiled image.

#### Signature

```python
@property
def image(self): ...
```

### GimpPatPattern().image

[Show source in GimpPatPattern.py:117](../../../gimpformats/GimpPatPattern.py#L117)

#### Signature

```python
@image.setter
def image(self, image: PIL.Image.Image) -> None: ...
```

### GimpPatPattern().load

[Show source in GimpPatPattern.py:42](../../../gimpformats/GimpPatPattern.py#L42)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str) -> None: ...
```

### GimpPatPattern().save

[Show source in GimpPatPattern.py:122](../../../gimpformats/GimpPatPattern.py#L122)

Save this gimp image to a file.

#### Signature

```python
def save(
    self, tofileName: str | BytesIO | None = None, toExtension: str | None = None
) -> None: ...
```

### GimpPatPattern().size

[Show source in GimpPatPattern.py:101](../../../gimpformats/GimpPatPattern.py#L101)

The size of the pattern.

#### Signature

```python
@property
def size(self): ...
```