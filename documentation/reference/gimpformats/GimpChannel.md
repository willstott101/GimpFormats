# Gimpchannel

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpchannel

> Auto-generated documentation for [gimpformats.GimpChannel](../../../gimpformats/GimpChannel.py) module.

- [Gimpchannel](#gimpchannel)
  - [GimpChannel](#gimpchannel)
    - [GimpChannel().__repr__](#gimpchannel()__repr__)
    - [GimpChannel().__str__](#gimpchannel()__str__)
    - [GimpChannel().decode](#gimpchannel()decode)
    - [GimpChannel().encode](#gimpchannel()encode)
    - [GimpChannel().image](#gimpchannel()image)
    - [GimpChannel().image](#gimpchannel()image-1)
    - [GimpChannel().imageHierarchy](#gimpchannel()imagehierarchy)

## GimpChannel

[Show source in GimpChannel.py:13](../../../gimpformats/GimpChannel.py#L13)

Represents a single channel or mask in a GIMP image.

#### Signature

```python
class GimpChannel(GimpIOBase):
    def __init__(
        self, parent: GimpIOBase, name: str = "", image: Image.Image | None = None
    ) -> None: ...
```

#### See also

- [GimpIOBase](./GimpIOBase.md#gimpiobase)

### GimpChannel().__repr__

[Show source in GimpChannel.py:99](../../../gimpformats/GimpChannel.py#L99)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: int = 0) -> str: ...
```

### GimpChannel().__str__

[Show source in GimpChannel.py:95](../../../gimpformats/GimpChannel.py#L95)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpChannel().decode

[Show source in GimpChannel.py:38](../../../gimpformats/GimpChannel.py#L38)

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
def decode(self, data: bytes | bytearray, index: int = 0) -> int: ...
```

### GimpChannel().encode

[Show source in GimpChannel.py:60](../../../gimpformats/GimpChannel.py#L60)

Encode this object to a byte buffer.

#### Signature

```python
def encode(self) -> bytearray: ...
```

### GimpChannel().image

[Show source in GimpChannel.py:71](../../../gimpformats/GimpChannel.py#L71)

Get the compiled image.

#### Signature

```python
@property
def image(self) -> Image.Image | None: ...
```

### GimpChannel().image

[Show source in GimpChannel.py:76](../../../gimpformats/GimpChannel.py#L76)

Set the compiled image.

#### Signature

```python
@image.setter
def image(self, image: Image.Image) -> None: ...
```

### GimpChannel().imageHierarchy

[Show source in GimpChannel.py:84](../../../gimpformats/GimpChannel.py#L84)

Get the image hierarchy.

#### Signature

```python
@property
def imageHierarchy(self) -> GimpImageHierarchy | None: ...
```