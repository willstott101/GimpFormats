# GimpImageLevel

> Auto-generated documentation for [gimpformats.GimpImageLevel](../../gimpformats/GimpImageLevel.py) module.

Gets packed pixels from a gimp image.

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / GimpImageLevel
    - [GimpImageLevel](#gimpimagelevel)
        - [GimpImageLevel().\_\_repr\_\_](#gimpimagelevel__repr__)
        - [GimpImageLevel().bpp](#gimpimagelevelbpp)
        - [GimpImageLevel().decode](#gimpimageleveldecode)
        - [GimpImageLevel().encode](#gimpimagelevelencode)
        - [GimpImageLevel().image](#gimpimagelevelimage)
        - [GimpImageLevel().image](#gimpimagelevelimage)
        - [GimpImageLevel().mode](#gimpimagelevelmode)
        - [GimpImageLevel().tiles](#gimpimageleveltiles)

This represents a single level in an imageHierarchy

## GimpImageLevel

[[find in source code]](../../gimpformats/GimpImageLevel.py#L19)

```python
class GimpImageLevel(GimpIOBase):
    def __init__(parent):
```

Gets packed pixels from a gimp image.

This represents a single level in an imageHierarchy

### GimpImageLevel().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpImageLevel.py#L277)

```python
def __repr__(indent: str = ''):
```

Get a textual representation of this object.

### GimpImageLevel().bpp

[[find in source code]](../../gimpformats/GimpImageLevel.py#L222)

```python
@property
def bpp():
```

Get bpp.

### GimpImageLevel().decode

[[find in source code]](../../gimpformats/GimpImageLevel.py#L32)

```python
def decode(data: bytes, index: int = 0):
```

Decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

### GimpImageLevel().encode

[[find in source code]](../../gimpformats/GimpImageLevel.py#L69)

```python
def encode():
```

Encode this object to a byte buffer.

### GimpImageLevel().image

[[find in source code]](../../gimpformats/GimpImageLevel.py#L253)

```python
@property
def image() -> Image:
```

Get a final, compiled image

### GimpImageLevel().image

[[find in source code]](../../gimpformats/GimpImageLevel.py#L269)

```python
@image.setter
def image(image: Image):
```

### GimpImageLevel().mode

[[find in source code]](../../gimpformats/GimpImageLevel.py#L227)

```python
@property
def mode():
```

Get mode.

### GimpImageLevel().tiles

[[find in source code]](../../gimpformats/GimpImageLevel.py#L233)

```python
@property
def tiles():
```

Get tiles.
