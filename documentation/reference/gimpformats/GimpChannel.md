# Gimpchannel

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpchannel

> Auto-generated documentation for [gimpformats.GimpChannel](../../../gimpformats/GimpChannel.py) module.

- [Gimpchannel](#gimpchannel)
  - [GimpChannel](#gimpchannel)
    - [GimpChannel().__repr__](#gimpchannel()__repr__)
    - [GimpChannel().__str__](#gimpchannel()__str__)
    - [GimpChannel().decode](#gimpchannel()decode)
    - [GimpChannel().encode](#gimpchannel()encode)
    - [GimpChannel().forceFullyLoaded](#gimpchannel()forcefullyloaded)
    - [GimpChannel().image](#gimpchannel()image)
    - [GimpChannel().image](#gimpchannel()image-1)
    - [GimpChannel().imageHierarchy](#gimpchannel()imagehierarchy)

## GimpChannel

[Show source in GimpChannel.py:13](../../../gimpformats/GimpChannel.py#L13)

Represents a single channel or mask in a gimp image.

#### Signature

```python
class GimpChannel(GimpIOBase):
    def __init__(
        self, parent: GimpIOBase, name: str = "", image: Image.Image | None = None
    ) -> None: ...
```

### GimpChannel().__repr__

[Show source in GimpChannel.py:112](../../../gimpformats/GimpChannel.py#L112)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: int = 0) -> str: ...
```

### GimpChannel().__str__

[Show source in GimpChannel.py:108](../../../gimpformats/GimpChannel.py#L108)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpChannel().decode

[Show source in GimpChannel.py:37](../../../gimpformats/GimpChannel.py#L37)

Decode a byte buffer.

#### Arguments

----
 - `data` *bytes* - data to decode
 - `index` *int, optional* - index to start from. Defaults to 0.

#### Returns

-------
 - `int` - pointer

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int: ...
```

### GimpChannel().encode

[Show source in GimpChannel.py:59](../../../gimpformats/GimpChannel.py#L59)

Encode this object to a byte buffer.

#### Signature

```python
def encode(self) -> bytearray: ...
```

### GimpChannel().forceFullyLoaded

[Show source in GimpChannel.py:87](../../../gimpformats/GimpChannel.py#L87)

Make sure everything is fully loaded from the file.

#### Signature

```python
def forceFullyLoaded(self) -> None: ...
```

### GimpChannel().image

[Show source in GimpChannel.py:72](../../../gimpformats/GimpChannel.py#L72)

Get a final, compiled image.

#### Signature

```python
@property
def image(self) -> Image.Image | None: ...
```

### GimpChannel().image

[Show source in GimpChannel.py:77](../../../gimpformats/GimpChannel.py#L77)

Get a final, compiled image.

#### Signature

```python
@image.setter
def image(self, image: Image.Image) -> None: ...
```

### GimpChannel().imageHierarchy

[Show source in GimpChannel.py:93](../../../gimpformats/GimpChannel.py#L93)

Get the image hierarchy.

This is mainly used for decoding the image, so
not much use to you.

#### Signature

```python
@property
def imageHierarchy(self) -> GimpImageHierarchy: ...
```