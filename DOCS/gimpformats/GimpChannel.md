# GimpChannel

> Auto-generated documentation for [gimpformats.GimpChannel](../../gimpformats/GimpChannel.py) module.

Represents a single channel or mask in a gimp image.

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / GimpChannel
    - [GimpChannel](#gimpchannel)
        - [GimpChannel().\_\_repr\_\_](#gimpchannel__repr__)
        - [GimpChannel().decode](#gimpchanneldecode)
        - [GimpChannel().encode](#gimpchannelencode)
        - [GimpChannel().image](#gimpchannelimage)
        - [GimpChannel().image](#gimpchannelimage)
        - [GimpChannel().imageHierarchy](#gimpchannelimagehierarchy)

## GimpChannel

[[find in source code]](../../gimpformats/GimpChannel.py#L14)

```python
class GimpChannel(GimpIOBase):
    def __init__(parent, name: str = '', image: Image.Image | None = None):
```

Represents a single channel or mask in a gimp image.

### GimpChannel().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpChannel.py#L94)

```python
def __repr__(indent: str = '') -> str:
```

Get a textual representation of this object.

### GimpChannel().decode

[[find in source code]](../../gimpformats/GimpChannel.py#L28)

```python
def decode(data: bytearray, index: int = 0) -> int:
```

Decode a byte buffer.

#### Arguments

- `data` *bytearray* - data to decode
- `index` *int, optional* - index to start from. Defaults to 0.

#### Returns

- `int` - pointer

### GimpChannel().encode

[[find in source code]](../../gimpformats/GimpChannel.py#L48)

```python
def encode() -> bytearray:
```

Encode this object to a byte buffer.

### GimpChannel().image

[[find in source code]](../../gimpformats/GimpChannel.py#L61)

```python
@property
def image() -> Image.Image | None:
```

Get a final, compiled image.

### GimpChannel().image

[[find in source code]](../../gimpformats/GimpChannel.py#L66)

```python
@image.setter
def image(image: Image.Image):
```

Get a final, compiled image.

### GimpChannel().imageHierarchy

[[find in source code]](../../gimpformats/GimpChannel.py#L82)

```python
@property
def imageHierarchy():
```

Get the image hierarchy.

This is mainly used for decoding the image, so
not much use to you.
