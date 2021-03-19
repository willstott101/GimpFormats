# GimpLayer

> Auto-generated documentation for [gimpformats.GimpLayer](../../gimpformats/GimpLayer.py) module.

Represents a single layer in a gimp image

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / GimpLayer
    - [GimpLayer](#gimplayer)
        - [GimpLayer().\_\_repr\_\_](#gimplayer__repr__)
        - [GimpLayer().decode](#gimplayerdecode)
        - [GimpLayer().encode](#gimplayerencode)
        - [GimpLayer().image](#gimplayerimage)
        - [GimpLayer().image](#gimplayerimage)
        - [GimpLayer().imageHierarchy](#gimplayerimagehierarchy)
        - [GimpLayer().imageHierarchy](#gimplayerimagehierarchy)
        - [GimpLayer().mask](#gimplayermask)

## GimpLayer

[[find in source code]](../../gimpformats/GimpLayer.py#L15)

```python
class GimpLayer(GimpIOBase):
    def __init__(parent, name: str | None = None, image: Image | None = None):
```

Represents a single layer in a gimp image

### GimpLayer().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpLayer.py#L168)

```python
def __repr__(indent=''):
```

Get a textual representation of this object

### GimpLayer().decode

[[find in source code]](../../gimpformats/GimpLayer.py#L42)

```python
def decode(data: bytearray, index: int = 0):
```

Decode a byte buffer

Steps:
Create a new IO buffer (array of binary values)
Grab attributes as outlined in the spec
List of properties
Get the image hierarchy and mask pointers
Return the offset

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

### GimpLayer().encode

[[find in source code]](../../gimpformats/GimpLayer.py#L72)

```python
def encode():
```

Encode to byte array

Steps:
Create a new IO buffer (array of binary values)
Set attributes as outlined in the spec
List of properties
Set the image hierarchy and mask pointers
Return the data

### GimpLayer().image

[[find in source code]](../../gimpformats/GimpLayer.py#L114)

```python
@property
def image() -> Image:
```

Get the layer image

NOTE: can return None!

### GimpLayer().image

[[find in source code]](../../gimpformats/GimpLayer.py#L124)

```python
@image.setter
def image(image: Image):
```

Set the layer image

NOTE: resets layer width, height, and colorMode

### GimpLayer().imageHierarchy

[[find in source code]](../../gimpformats/GimpLayer.py#L141)

```python
@property
def imageHierarchy() -> GimpImageHierarchy:
```

Get the image hierarchy objects

This is mainly needed for deciphering image, and therefore,
of little use to you, the user.

NOTE: can return None if it has been fully read into an image

### GimpLayer().imageHierarchy

[[find in source code]](../../gimpformats/GimpLayer.py#L155)

```python
@imageHierarchy.setter
def imageHierarchy(imgHierarchy):
```

Set the image hierarchy.

### GimpLayer().mask

[[find in source code]](../../gimpformats/GimpLayer.py#L106)

```python
@property
def mask():
```

Get the layer mask
