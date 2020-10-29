# GimpGplPalette

> Auto-generated documentation for [gimpformats.GimpGplPalette](../../gimpformats/GimpGplPalette.py) module.

Pure python implementation of the gimp gpl palette format

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / GimpGplPalette
    - [GimpGplPalette](#gimpgplpalette)
        - [GimpGplPalette().\_\_eq\_\_](#gimpgplpalette__eq__)
        - [GimpGplPalette().\_\_repr\_\_](#gimpgplpalette__repr__)
        - [GimpGplPalette().decode](#gimpgplpalettedecode)
        - [GimpGplPalette().encode](#gimpgplpaletteencode)
        - [GimpGplPalette().load](#gimpgplpaletteload)
        - [GimpGplPalette().save](#gimpgplpalettesave)

## GimpGplPalette

[[find in source code]](../../gimpformats/GimpGplPalette.py#L8)

```python
class GimpGplPalette():
    def __init__(fileName=None):
```

Pure python implementation of the gimp gpl palette format

### GimpGplPalette().\_\_eq\_\_

[[find in source code]](../../gimpformats/GimpGplPalette.py#L102)

```python
def __eq__(other):
```

perform a comparison

### GimpGplPalette().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpGplPalette.py#L87)

```python
def __repr__(indent=''):
```

Get a textual representation of this object

### GimpGplPalette().decode

[[find in source code]](../../gimpformats/GimpGplPalette.py#L34)

```python
def decode(data):
```

decode a byte buffer

#### Arguments

- `data` - data buffer to decode

### GimpGplPalette().encode

[[find in source code]](../../gimpformats/GimpGplPalette.py#L57)

```python
def encode():
```

encode to a raw data stream

### GimpGplPalette().load

[[find in source code]](../../gimpformats/GimpGplPalette.py#L18)

```python
def load(fileName: Union[(BytesIO, str)]):
```

load a gimp file

#### Arguments

- `fileName` - can be a file name or a file-like object

### GimpGplPalette().save

[[find in source code]](../../gimpformats/GimpGplPalette.py#L73)

```python
def save(tofileName=None, toExtension=None):
```

save this gimp image to a file
