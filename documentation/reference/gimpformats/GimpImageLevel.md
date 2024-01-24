# Gimpimagelevel

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpimagelevel

> Auto-generated documentation for [gimpformats.GimpImageLevel](../../../gimpformats/GimpImageLevel.py) module.

- [Gimpimagelevel](#gimpimagelevel)
  - [GimpImageLevel](#gimpimagelevel)
    - [GimpImageLevel().__repr__](#gimpimagelevel()__repr__)
    - [GimpImageLevel()._encodeRLE](#gimpimagelevel()_encoderle)
    - [GimpImageLevel()._imgToTiles](#gimpimagelevel()_imgtotiles)
    - [GimpImageLevel().bpp](#gimpimagelevel()bpp)
    - [GimpImageLevel().decode](#gimpimagelevel()decode)
    - [GimpImageLevel().encode](#gimpimagelevel()encode)
    - [GimpImageLevel().image](#gimpimagelevel()image)
    - [GimpImageLevel().image](#gimpimagelevel()image-1)
    - [GimpImageLevel().mode](#gimpimagelevel()mode)
    - [GimpImageLevel().tiles](#gimpimagelevel()tiles)

## GimpImageLevel

[Show source in GimpImageLevel.py:18](../../../gimpformats/GimpImageLevel.py#L18)

Gets packed pixels from a gimp image.

This represents a single level in an imageHierarchy

#### Signature

```python
class GimpImageLevel(GimpIOBase):
    def __init__(self, parent) -> None: ...
```

### GimpImageLevel().__repr__

[Show source in GimpImageLevel.py:279](../../../gimpformats/GimpImageLevel.py#L279)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: str = "") -> str: ...
```

### GimpImageLevel()._encodeRLE

[Show source in GimpImageLevel.py:149](../../../gimpformats/GimpImageLevel.py#L149)

Encode image to RLE image data.

#### Signature

```python
def _encodeRLE(self, data, bpp): ...
```

### GimpImageLevel()._imgToTiles

[Show source in GimpImageLevel.py:244](../../../gimpformats/GimpImageLevel.py#L244)

break an image into a series of tiles, each<=64x64.

#### Signature

```python
def _imgToTiles(self, image): ...
```

### GimpImageLevel().bpp

[Show source in GimpImageLevel.py:224](../../../gimpformats/GimpImageLevel.py#L224)

Get bpp.

#### Signature

```python
@property
def bpp(self): ...
```

### GimpImageLevel().decode

[Show source in GimpImageLevel.py:31](../../../gimpformats/GimpImageLevel.py#L31)

Decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

#### Signature

```python
def decode(self, data: bytes, index: int = 0): ...
```

### GimpImageLevel().encode

[Show source in GimpImageLevel.py:71](../../../gimpformats/GimpImageLevel.py#L71)

Encode this object to a byte buffer.

#### Signature

```python
def encode(self): ...
```

### GimpImageLevel().image

[Show source in GimpImageLevel.py:255](../../../gimpformats/GimpImageLevel.py#L255)

Get a final, compiled image.

#### Signature

```python
@property
def image(self) -> Image: ...
```

### GimpImageLevel().image

[Show source in GimpImageLevel.py:271](../../../gimpformats/GimpImageLevel.py#L271)

#### Signature

```python
@image.setter
def image(self, image: Image) -> None: ...
```

### GimpImageLevel().mode

[Show source in GimpImageLevel.py:229](../../../gimpformats/GimpImageLevel.py#L229)

Get mode.

#### Signature

```python
@property
def mode(self): ...
```

### GimpImageLevel().tiles

[Show source in GimpImageLevel.py:235](../../../gimpformats/GimpImageLevel.py#L235)

Get tiles.

#### Signature

```python
@property
def tiles(self): ...
```