# Gimpvbrbrush

> Auto-generated documentation for [gimpformats.GimpVbrBrush](../../../gimpformats/GimpVbrBrush.py) module.

Pure python implementation of the gimp vbr brush format.

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../MODULES.md#gimpformats-modules) / [Gimpformats](index.md#gimpformats) / Gimpvbrbrush
    - [GimpVbrBrush](#gimpvbrbrush)
        - [GimpVbrBrush().\_\_eq\_\_](#gimpvbrbrush__eq__)
        - [GimpVbrBrush().\_\_repr\_\_](#gimpvbrbrush__repr__)
        - [GimpVbrBrush().decode](#gimpvbrbrushdecode)
        - [GimpVbrBrush().encode](#gimpvbrbrushencode)
        - [GimpVbrBrush().image](#gimpvbrbrushimage)
        - [GimpVbrBrush().load](#gimpvbrbrushload)
        - [GimpVbrBrush().save](#gimpvbrbrushsave)

## GimpVbrBrush

[[find in source code]](../../../gimpformats/GimpVbrBrush.py#L11)

```python
class GimpVbrBrush():
    def __init__(fileName: BytesIO | str | None = None):
```

Pure python implementation of the gimp vbr brush format.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/vbr.txt

### GimpVbrBrush().\_\_eq\_\_

[[find in source code]](../../../gimpformats/GimpVbrBrush.py#L140)

```python
def __eq__(other):
```

Perform a comparison.

### GimpVbrBrush().\_\_repr\_\_

[[find in source code]](../../../gimpformats/GimpVbrBrush.py#L124)

```python
def __repr__():
```

Get a textual representation of this object.

### GimpVbrBrush().decode

[[find in source code]](../../../gimpformats/GimpVbrBrush.py#L51)

```python
def decode(dataIn: bytes):
```

Decode a byte buffer.

#### Arguments

- `dataIn` - data buffer to decode

### GimpVbrBrush().encode

[[find in source code]](../../../gimpformats/GimpVbrBrush.py#L79)

```python
def encode() -> bytes:
```

Encode to a raw data stream.

### GimpVbrBrush().image

[[find in source code]](../../../gimpformats/GimpVbrBrush.py#L46)

```python
@property
def image():
```

This parametric brush converted to a useable PIL image.

### GimpVbrBrush().load

[[find in source code]](../../../gimpformats/GimpVbrBrush.py#L38)

```python
def load(fileName: BytesIO | str):
```

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

### GimpVbrBrush().save

[[find in source code]](../../../gimpformats/GimpVbrBrush.py#L102)

```python
def save(tofileName=None, toExtension=None):
```

Save this gimp image to a file.
