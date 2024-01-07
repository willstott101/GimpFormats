# Gimpvbrbrush

[Gimpformats Index](../README.md#gimpformats-index) /
[Gimpformats](./index.md#gimpformats) /
Gimpvbrbrush

> Auto-generated documentation for [gimpformats.GimpVbrBrush](../../../gimpformats/GimpVbrBrush.py) module.

- [Gimpvbrbrush](#gimpvbrbrush)
  - [GimpVbrBrush](#gimpvbrbrush)
    - [GimpVbrBrush().__eq__](#gimpvbrbrush()__eq__)
    - [GimpVbrBrush().__repr__](#gimpvbrbrush()__repr__)
    - [GimpVbrBrush().decode](#gimpvbrbrush()decode)
    - [GimpVbrBrush().encode](#gimpvbrbrush()encode)
    - [GimpVbrBrush().image](#gimpvbrbrush()image)
    - [GimpVbrBrush().load](#gimpvbrbrush()load)
    - [GimpVbrBrush().save](#gimpvbrbrush()save)

## GimpVbrBrush

[Show source in GimpVbrBrush.py:10](../../../gimpformats/GimpVbrBrush.py#L10)

Pure python implementation of the gimp vbr brush format.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/vbr.txt

#### Signature

```python
class GimpVbrBrush:
    def __init__(self, fileName: BytesIO | str | None = None): ...
```

### GimpVbrBrush().__eq__

[Show source in GimpVbrBrush.py:139](../../../gimpformats/GimpVbrBrush.py#L139)

Perform a comparison.

#### Signature

```python
def __eq__(self, other): ...
```

### GimpVbrBrush().__repr__

[Show source in GimpVbrBrush.py:123](../../../gimpformats/GimpVbrBrush.py#L123)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self): ...
```

### GimpVbrBrush().decode

[Show source in GimpVbrBrush.py:50](../../../gimpformats/GimpVbrBrush.py#L50)

Decode a byte buffer.

#### Arguments

- `dataIn` - data buffer to decode

#### Signature

```python
def decode(self, dataIn: bytes): ...
```

### GimpVbrBrush().encode

[Show source in GimpVbrBrush.py:78](../../../gimpformats/GimpVbrBrush.py#L78)

Encode to a raw data stream.

#### Signature

```python
def encode(self) -> bytes: ...
```

### GimpVbrBrush().image

[Show source in GimpVbrBrush.py:45](../../../gimpformats/GimpVbrBrush.py#L45)

This parametric brush converted to a useable PIL image.

#### Signature

```python
@property
def image(self): ...
```

### GimpVbrBrush().load

[Show source in GimpVbrBrush.py:37](../../../gimpformats/GimpVbrBrush.py#L37)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str): ...
```

### GimpVbrBrush().save

[Show source in GimpVbrBrush.py:101](../../../gimpformats/GimpVbrBrush.py#L101)

Save this gimp image to a file.

#### Signature

```python
def save(self, tofileName=None, toExtension=None): ...
```