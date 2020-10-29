# GimpVbrBrush

> Auto-generated documentation for [gimpformats.GimpVbrBrush](../../gimpformats/GimpVbrBrush.py) module.

Pure python implementation of the gimp vbr brush format

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / GimpVbrBrush
    - [GimpVbrBrush](#gimpvbrbrush)
        - [GimpVbrBrush().\_\_eq\_\_](#gimpvbrbrush__eq__)
        - [GimpVbrBrush().\_\_repr\_\_](#gimpvbrbrush__repr__)
        - [GimpVbrBrush().decode](#gimpvbrbrushdecode)
        - [GimpVbrBrush().encode](#gimpvbrbrushencode)
        - [GimpVbrBrush().image](#gimpvbrbrushimage)
        - [GimpVbrBrush().load](#gimpvbrbrushload)
        - [GimpVbrBrush().save](#gimpvbrbrushsave)

## GimpVbrBrush

[[find in source code]](../../gimpformats/GimpVbrBrush.py#L10)

```python
class GimpVbrBrush():
    def __init__(fileName: Union[(BytesIO, str, None)] = None):
```

Pure python implementation of the gimp vbr brush format

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/vbr.txt

### GimpVbrBrush().\_\_eq\_\_

[[find in source code]](../../gimpformats/GimpVbrBrush.py#L149)

```python
def __eq__(other):
```

perform a comparison

### GimpVbrBrush().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpVbrBrush.py#L131)

```python
def __repr__(indent=''):
```

Get a textual representation of this object

### GimpVbrBrush().decode

[[find in source code]](../../gimpformats/GimpVbrBrush.py#L56)

```python
def decode(data: bytes):
```

decode a byte buffer

#### Arguments

- `data` - data buffer to decode

### GimpVbrBrush().encode

[[find in source code]](../../gimpformats/GimpVbrBrush.py#L85)

```python
def encode():
```

encode to a raw data stream

### GimpVbrBrush().image

[[find in source code]](../../gimpformats/GimpVbrBrush.py#L49)

```python
@property
def image():
```

this parametric brush converted to a useable PIL image

### GimpVbrBrush().load

[[find in source code]](../../gimpformats/GimpVbrBrush.py#L33)

```python
def load(fileName: Union[(BytesIO, str)]):
```

load a gimp file

#### Arguments

- `fileName` - can be a file name or a file-like object

### GimpVbrBrush().save

[[find in source code]](../../gimpformats/GimpVbrBrush.py#L110)

```python
def save(tofileName=None, toExtension=None):
```

save this gimp image to a file
