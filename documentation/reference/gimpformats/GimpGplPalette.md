# Gimpgplpalette

[Gimpformats Index](../README.md#gimpformats-index) /
[Gimpformats](./index.md#gimpformats) /
Gimpgplpalette

> Auto-generated documentation for [gimpformats.GimpGplPalette](../../../gimpformats/GimpGplPalette.py) module.

- [Gimpgplpalette](#gimpgplpalette)
  - [GimpGplPalette](#gimpgplpalette)
    - [GimpGplPalette().__eq__](#gimpgplpalette()__eq__)
    - [GimpGplPalette().__repr__](#gimpgplpalette()__repr__)
    - [GimpGplPalette().decode](#gimpgplpalette()decode)
    - [GimpGplPalette().encode](#gimpgplpalette()encode)
    - [GimpGplPalette().load](#gimpgplpalette()load)
    - [GimpGplPalette().save](#gimpgplpalette()save)

## GimpGplPalette

[Show source in GimpGplPalette.py:12](../../../gimpformats/GimpGplPalette.py#L12)

Pure python implementation of the gimp gpl palette format.

#### Signature

```python
class GimpGplPalette:
    def __init__(self, fileName: BytesIO | str | None = None):
        ...
```

### GimpGplPalette().__eq__

[Show source in GimpGplPalette.py:93](../../../gimpformats/GimpGplPalette.py#L93)

Perform a comparison.

#### Signature

```python
def __eq__(self, other: GimpGplPalette):
    ...
```

### GimpGplPalette().__repr__

[Show source in GimpGplPalette.py:78](../../../gimpformats/GimpGplPalette.py#L78)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self):
    ...
```

### GimpGplPalette().decode

[Show source in GimpGplPalette.py:36](../../../gimpformats/GimpGplPalette.py#L36)

Decode a byte buffer.

#### Arguments

- `data` *str* - data buffer to decode

#### Raises

- `RuntimeError` - File format error.  Magic value mismatch.

#### Signature

```python
def decode(self, data: str) -> None:
    ...
```

### GimpGplPalette().encode

[Show source in GimpGplPalette.py:61](../../../gimpformats/GimpGplPalette.py#L61)

Encode to a raw data stream.

#### Signature

```python
def encode(self):
    ...
```

### GimpGplPalette().load

[Show source in GimpGplPalette.py:28](../../../gimpformats/GimpGplPalette.py#L28)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str):
    ...
```

### GimpGplPalette().save

[Show source in GimpGplPalette.py:74](../../../gimpformats/GimpGplPalette.py#L74)

Save this gimp image to a file.

#### Signature

```python
def save(self, fileName: str | BytesIO):
    ...
```


