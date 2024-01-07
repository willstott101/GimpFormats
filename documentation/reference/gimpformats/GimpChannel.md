# Gimpchannel

[Gimpformats Index](../README.md#gimpformats-index) /
[Gimpformats](./index.md#gimpformats) /
Gimpchannel

> Auto-generated documentation for [gimpformats.GimpChannel](../../../gimpformats/GimpChannel.py) module.

- [Gimpchannel](#gimpchannel)
  - [GimpChannel](#gimpchannel)
    - [GimpChannel().__repr__](#gimpchannel()__repr__)
    - [GimpChannel().decode](#gimpchannel()decode)
    - [GimpChannel().encode](#gimpchannel()encode)
    - [GimpChannel().forceFullyLoaded](#gimpchannel()forcefullyloaded)
    - [GimpChannel().image](#gimpchannel()image)
    - [GimpChannel().image](#gimpchannel()image-1)
    - [GimpChannel().imageHierarchy](#gimpchannel()imagehierarchy)

## GimpChannel

[Show source in GimpChannel.py:12](../../../gimpformats/GimpChannel.py#L12)

Represents a single channel or mask in a gimp image.

#### Signature

```python
class GimpChannel(GimpIOBase):
    def __init__(self, parent, name: str = "", image: Image.Image | None = None): ...
```

### GimpChannel().__repr__

[Show source in GimpChannel.py:101](../../../gimpformats/GimpChannel.py#L101)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: str = "") -> str: ...
```

### GimpChannel().decode

[Show source in GimpChannel.py:33](../../../gimpformats/GimpChannel.py#L33)

Decode a byte buffer.

#### Arguments

- `data` *bytes* - data to decode
- `index` *int, optional* - index to start from. Defaults to 0.

#### Returns

- `int` - pointer

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int: ...
```

### GimpChannel().encode

[Show source in GimpChannel.py:53](../../../gimpformats/GimpChannel.py#L53)

Encode this object to a byte buffer.

#### Signature

```python
def encode(self) -> bytearray: ...
```

### GimpChannel().forceFullyLoaded

[Show source in GimpChannel.py:81](../../../gimpformats/GimpChannel.py#L81)

Make sure everything is fully loaded from the file.

#### Signature

```python
def forceFullyLoaded(self): ...
```

### GimpChannel().image

[Show source in GimpChannel.py:66](../../../gimpformats/GimpChannel.py#L66)

Get a final, compiled image.

#### Signature

```python
@property
def image(self) -> Image.Image | None: ...
```

### GimpChannel().image

[Show source in GimpChannel.py:71](../../../gimpformats/GimpChannel.py#L71)

Get a final, compiled image.

#### Signature

```python
@image.setter
def image(self, image: Image.Image): ...
```

### GimpChannel().imageHierarchy

[Show source in GimpChannel.py:87](../../../gimpformats/GimpChannel.py#L87)

Get the image hierarchy.

This is mainly used for decoding the image, so
not much use to you.

#### Signature

```python
@property
def imageHierarchy(self): ...
```