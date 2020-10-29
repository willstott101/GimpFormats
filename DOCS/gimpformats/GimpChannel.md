# GimpChannel

> Auto-generated documentation for [gimpformats.GimpChannel](../../gimpformats/GimpChannel.py) module.

Represents a single channel or mask in a gimp image

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / GimpChannel
    - [GimpChannel](#gimpchannel)
        - [GimpChannel().\_\_repr\_\_](#gimpchannel__repr__)
        - [GimpChannel().decode](#gimpchanneldecode)
        - [GimpChannel().encode](#gimpchannelencode)
        - [GimpChannel().image](#gimpchannelimage)
        - [GimpChannel().image](#gimpchannelimage)
        - [GimpChannel().imageHierarchy](#gimpchannelimagehierarchy)

## GimpChannel

[[find in source code]](../../gimpformats/GimpChannel.py#L12)

```python
class GimpChannel(GimpIOBase):
    def __init__(parent, name: str = '', image: Optional[Image.Image] = None):
```

Represents a single channel or mask in a gimp image

### GimpChannel().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpChannel.py#L99)

```python
def __repr__(indent: str = '') -> str:
```

Get a textual representation of this object

### GimpChannel().decode

[[find in source code]](../../gimpformats/GimpChannel.py#L27)

```python
def decode(data: bytearray, index: int = 0):
```

decode a byte buffer

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

### GimpChannel().encode

[[find in source code]](../../gimpformats/GimpChannel.py#L44)

```python
def encode():
```

encode this object to a byte buffer

### GimpChannel().image

[[find in source code]](../../gimpformats/GimpChannel.py#L59)

```python
@property
def image() -> Optional[Image.Image]:
```

get a final, compiled image

### GimpChannel().image

[[find in source code]](../../gimpformats/GimpChannel.py#L66)

```python
@image.setter
def image(image: Image.Image):
```

get a final, compiled image

### GimpChannel().imageHierarchy

[[find in source code]](../../gimpformats/GimpChannel.py#L86)

```python
@property
def imageHierarchy():
```

Get the image hierarchy

This is mainly used for decoding the image, so
not much use to you.
