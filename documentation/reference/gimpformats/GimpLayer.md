# Gimplayer

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimplayer

> Auto-generated documentation for [gimpformats.GimpLayer](../../../gimpformats/GimpLayer.py) module.

- [Gimplayer](#gimplayer)
  - [GimpLayer](#gimplayer)
    - [GimpLayer().__repr__](#gimplayer()__repr__)
    - [GimpLayer().decode](#gimplayer()decode)
    - [GimpLayer().encode](#gimplayer()encode)
    - [GimpLayer().forceFullyLoaded](#gimplayer()forcefullyloaded)
    - [GimpLayer().image](#gimplayer()image)
    - [GimpLayer().image](#gimplayer()image-1)
    - [GimpLayer().imageHierarchy](#gimplayer()imagehierarchy)
    - [GimpLayer().imageHierarchy](#gimplayer()imagehierarchy-1)
    - [GimpLayer().mask](#gimplayer()mask)

## GimpLayer

[Show source in GimpLayer.py:13](../../../gimpformats/GimpLayer.py#L13)

Represents a single layer in a gimp image.

#### Signature

```python
class GimpLayer(GimpIOBase):
    def __init__(
        self, parent, name: str | None = None, image: Image | None = None
    ) -> None: ...
```

### GimpLayer().__repr__

[Show source in GimpLayer.py:184](../../../gimpformats/GimpLayer.py#L184)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: str = "") -> str: ...
```

### GimpLayer().decode

[Show source in GimpLayer.py:48](../../../gimpformats/GimpLayer.py#L48)

Decode a byte buffer.

Steps:
Create a new IO buffer (array of binary values)
Grab attributes as outlined in the spec
List of properties
Get the image hierarchy and mask pointers
Return the offset

#### Arguments

----
 - `data` *bytes* - data buffer to decode
 - `index` *int, optional* - index within the buffer to start at]. Defaults to 0.

#### Returns

-------
 - `int` - offset

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int: ...
```

### GimpLayer().encode

[Show source in GimpLayer.py:84](../../../gimpformats/GimpLayer.py#L84)

Encode to byte array.

Steps:
Create a new IO buffer (array of binary values)
Set attributes as outlined in the spec
List of properties
Set the image hierarchy and mask pointers
Return the data

#### Signature

```python
def encode(self): ...
```

### GimpLayer().forceFullyLoaded

[Show source in GimpLayer.py:176](../../../gimpformats/GimpLayer.py#L176)

Make sure everything is fully loaded from the file.

#### Signature

```python
def forceFullyLoaded(self) -> None: ...
```

### GimpLayer().image

[Show source in GimpLayer.py:127](../../../gimpformats/GimpLayer.py#L127)

Get the layer image.

NOTE: can return None!

#### Signature

```python
@property
def image(self) -> Image | None: ...
```

### GimpLayer().image

[Show source in GimpLayer.py:137](../../../gimpformats/GimpLayer.py#L137)

Set the layer image.

NOTE: resets layer width, height, and colorMode

#### Signature

```python
@image.setter
def image(self, image: Image) -> None: ...
```

### GimpLayer().imageHierarchy

[Show source in GimpLayer.py:154](../../../gimpformats/GimpLayer.py#L154)

Get the image hierarchy objects.

This is mainly needed for deciphering image, and therefore,
of little use to you, the user.

NOTE: can return None if it has been fully read into an image

#### Signature

```python
@property
def imageHierarchy(self) -> GimpImageHierarchy: ...
```

### GimpLayer().imageHierarchy

[Show source in GimpLayer.py:171](../../../gimpformats/GimpLayer.py#L171)

Set the image hierarchy.

#### Signature

```python
@imageHierarchy.setter
def imageHierarchy(self, imgHierarchy) -> None: ...
```

### GimpLayer().mask

[Show source in GimpLayer.py:118](../../../gimpformats/GimpLayer.py#L118)

Get the layer mask.

#### Signature

```python
@property
def mask(self): ...
```