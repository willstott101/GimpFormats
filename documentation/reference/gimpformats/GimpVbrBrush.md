# Gimpvbrbrush

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpvbrbrush

> Auto-generated documentation for [gimpformats.GimpVbrBrush](../../../gimpformats/GimpVbrBrush.py) module.

- [Gimpvbrbrush](#gimpvbrbrush)
  - [GimpVbrBrush](#gimpvbrbrush)
    - [GimpVbrBrush().__eq__](#gimpvbrbrush()__eq__)
    - [GimpVbrBrush().__repr__](#gimpvbrbrush()__repr__)
    - [GimpVbrBrush().__str__](#gimpvbrbrush()__str__)
    - [GimpVbrBrush().decode](#gimpvbrbrush()decode)
    - [GimpVbrBrush().encode](#gimpvbrbrush()encode)
    - [GimpVbrBrush().image](#gimpvbrbrush()image)
    - [GimpVbrBrush().load](#gimpvbrbrush()load)
    - [GimpVbrBrush().save](#gimpvbrbrush()save)

## GimpVbrBrush

[Show source in GimpVbrBrush.py:11](../../../gimpformats/GimpVbrBrush.py#L11)

Pure python implementation of the gimp vbr brush format.

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/vbr.txt

#### Signature

```python
class GimpVbrBrush:
    def __init__(self, fileName: BytesIO | str | None = None) -> None: ...
```

### GimpVbrBrush().__eq__

[Show source in GimpVbrBrush.py:141](../../../gimpformats/GimpVbrBrush.py#L141)

Perform a comparison.

#### Signature

```python
def __eq__(self, other): ...
```

### GimpVbrBrush().__repr__

[Show source in GimpVbrBrush.py:125](../../../gimpformats/GimpVbrBrush.py#L125)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpVbrBrush().__str__

[Show source in GimpVbrBrush.py:121](../../../gimpformats/GimpVbrBrush.py#L121)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpVbrBrush().decode

[Show source in GimpVbrBrush.py:53](../../../gimpformats/GimpVbrBrush.py#L53)

Decode a byte buffer.

#### Arguments

- `dataIn` - data buffer to decode

#### Signature

```python
def decode(self, dataIn: bytes) -> None: ...
```

### GimpVbrBrush().encode

[Show source in GimpVbrBrush.py:83](../../../gimpformats/GimpVbrBrush.py#L83)

Encode to a raw data stream.

#### Signature

```python
def encode(self) -> bytes: ...
```

### GimpVbrBrush().image

[Show source in GimpVbrBrush.py:48](../../../gimpformats/GimpVbrBrush.py#L48)

Parametric brush converted to a useable PIL image.

#### Signature

```python
@property
def image(self) -> NoReturn: ...
```

### GimpVbrBrush().load

[Show source in GimpVbrBrush.py:40](../../../gimpformats/GimpVbrBrush.py#L40)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str) -> None: ...
```

### GimpVbrBrush().save

[Show source in GimpVbrBrush.py:106](../../../gimpformats/GimpVbrBrush.py#L106)

Save this gimp image to a file.

#### Signature

```python
def save(self, tofileName=None, toExtension=None) -> None: ...
```