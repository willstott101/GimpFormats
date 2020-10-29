# GimpImageHierarchy

> Auto-generated documentation for [gimpformats.GimpImageHierarchy](../../gimpformats/GimpImageHierarchy.py) module.

Gets packed pixels from a gimp image

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / GimpImageHierarchy
    - [GimpImageHierarchy](#gimpimagehierarchy)
        - [GimpImageHierarchy().\_\_repr\_\_](#gimpimagehierarchy__repr__)
        - [GimpImageHierarchy().decode](#gimpimagehierarchydecode)
        - [GimpImageHierarchy().encode](#gimpimagehierarchyencode)
        - [GimpImageHierarchy().image](#gimpimagehierarchyimage)
        - [GimpImageHierarchy().image](#gimpimagehierarchyimage)
        - [GimpImageHierarchy().levels](#gimpimagehierarchylevels)

NOTE: This was originally designed to be a hierarchy, like
 an image pyramid, through in practice they only use the
 top level of the pyramid (64x64) and ignore the rest.

## GimpImageHierarchy

[[find in source code]](../../gimpformats/GimpImageHierarchy.py#L15)

```python
class GimpImageHierarchy(GimpIOBase):
    def __init__(parent, image: Optional[Image.Image] = None):
```

Gets packed pixels from a gimp image

NOTE: This was originally designed to be a hierarchy, like
 an image pyramid, through in practice they only use the
 top level of the pyramid (64x64) and ignore the rest.

### GimpImageHierarchy().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpImageHierarchy.py#L116)

```python
def __repr__(indent: str = ''):
```

Get a textual representation of this object

### GimpImageHierarchy().decode

[[find in source code]](../../gimpformats/GimpImageHierarchy.py#L34)

```python
def decode(data: bytearray, index: int = 0):
```

decode a byte buffer

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

### GimpImageHierarchy().encode

[[find in source code]](../../gimpformats/GimpImageHierarchy.py#L62)

```python
def encode():
```

encode this object to a byte buffer

### GimpImageHierarchy().image

[[find in source code]](../../gimpformats/GimpImageHierarchy.py#L94)

```python
@property
def image() -> Optional[Image.Image]:
```

get a final, compiled image

### GimpImageHierarchy().image

[[find in source code]](../../gimpformats/GimpImageHierarchy.py#L103)

```python
@image.setter
def image(image: Image.Image):
```

set the image

### GimpImageHierarchy().levels

[[find in source code]](../../gimpformats/GimpImageHierarchy.py#L79)

```python
@property
def levels():
```

Get the levels within this hierarchy

Presently hierarchy is not really used by gimp,
so this returns an array of one item
