# Gimpgplpalette

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpgplpalette

> Auto-generated documentation for [gimpformats.GimpGplPalette](../../../gimpformats/GimpGplPalette.py) module.

- [Gimpgplpalette](#gimpgplpalette)
  - [GimpGplPalette](#gimpgplpalette)
    - [GimpGplPalette().__eq__](#gimpgplpalette()__eq__)
    - [GimpGplPalette().__repr__](#gimpgplpalette()__repr__)
    - [GimpGplPalette().__str__](#gimpgplpalette()__str__)
    - [GimpGplPalette().decode](#gimpgplpalette()decode)
    - [GimpGplPalette().encode](#gimpgplpalette()encode)
    - [GimpGplPalette().load](#gimpgplpalette()load)
    - [GimpGplPalette().save](#gimpgplpalette()save)

## GimpGplPalette

[Show source in GimpGplPalette.py:11](../../../gimpformats/GimpGplPalette.py#L11)

Pure python implementation of the gimp gpl palette format.

#### Signature

```python
class GimpGplPalette:
    def __init__(self, fileName: BytesIO | str | None = None) -> None: ...
```

### GimpGplPalette().__eq__

[Show source in GimpGplPalette.py:102](../../../gimpformats/GimpGplPalette.py#L102)

Perform a comparison.

#### Signature

```python
def __eq__(self, other: GimpGplPalette) -> bool: ...
```

### GimpGplPalette().__repr__

[Show source in GimpGplPalette.py:87](../../../gimpformats/GimpGplPalette.py#L87)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpGplPalette().__str__

[Show source in GimpGplPalette.py:83](../../../gimpformats/GimpGplPalette.py#L83)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpGplPalette().decode

[Show source in GimpGplPalette.py:37](../../../gimpformats/GimpGplPalette.py#L37)

Decode a byte buffer.

#### Arguments

----
 - `data` *str* - data buffer to decode

#### Raises

------
 - `RuntimeError` - File format error.  Magic value mismatch.

#### Signature

```python
def decode(self, data: str) -> None: ...
```

### GimpGplPalette().encode

[Show source in GimpGplPalette.py:66](../../../gimpformats/GimpGplPalette.py#L66)

Encode to a raw data stream.

#### Signature

```python
def encode(self) -> bytes: ...
```

### GimpGplPalette().load

[Show source in GimpGplPalette.py:29](../../../gimpformats/GimpGplPalette.py#L29)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str) -> None: ...
```

### GimpGplPalette().save

[Show source in GimpGplPalette.py:79](../../../gimpformats/GimpGplPalette.py#L79)

Save this gimp image to a file.

#### Signature

```python
def save(self, fileName: str | BytesIO) -> None: ...
```