# Gimpimagelevel

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpimagelevel

> Auto-generated documentation for [gimpformats.GimpImageLevel](../../../gimpformats/GimpImageLevel.py) module.

- [Gimpimagelevel](#gimpimagelevel)
  - [GimpImageLevel](#gimpimagelevel)
    - [GimpImageLevel().__repr__](#gimpimagelevel()__repr__)
    - [GimpImageLevel().__str__](#gimpimagelevel()__str__)
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

[Show source in GimpImageLevel.py:17](../../../gimpformats/GimpImageLevel.py#L17)

Gets packed pixels from a gimp image.

This represents a single level in an imageHierarchy

The level structure for the first level is laid out as follows:

uint32      width  Width of the pixel array
uint32      height Height of the pixel array
,----------------- Repeat for each of the ceil(width/64)*ceil(height/64) tiles
| pointer   tptr   Pointer to tile data
`--
pointer     0      Zero marks the end of the array of tile pointers.

#### Signature

```python
class GimpImageLevel(GimpIOBase):
    def __init__(self, parent: Any) -> None: ...
```

#### See also

- [GimpIOBase](./GimpIOBase.md#gimpiobase)

### GimpImageLevel().__repr__

[Show source in GimpImageLevel.py:310](../../../gimpformats/GimpImageLevel.py#L310)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpImageLevel().__str__

[Show source in GimpImageLevel.py:306](../../../gimpformats/GimpImageLevel.py#L306)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpImageLevel()._encodeRLE

[Show source in GimpImageLevel.py:174](../../../gimpformats/GimpImageLevel.py#L174)

Encode image to RLE image data.

#### Signature

```python
def _encodeRLE(self, data: bytearray, bpp: int) -> bytearray: ...
```

### GimpImageLevel()._imgToTiles

[Show source in GimpImageLevel.py:271](../../../gimpformats/GimpImageLevel.py#L271)

Break an image into a series of tiles, each<=64x64.

#### Signature

```python
def _imgToTiles(self, image: Image.Image) -> list[Image.Image]: ...
```

### GimpImageLevel().bpp

[Show source in GimpImageLevel.py:251](../../../gimpformats/GimpImageLevel.py#L251)

Get bpp.

#### Signature

```python
@property
def bpp(self) -> int: ...
```

### GimpImageLevel().decode

[Show source in GimpImageLevel.py:40](../../../gimpformats/GimpImageLevel.py#L40)

Decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

#### Signature

```python
def decode(self, data: bytearray | bytes | None, index: int = 0) -> int: ...
```

### GimpImageLevel().encode

[Show source in GimpImageLevel.py:84](../../../gimpformats/GimpImageLevel.py#L84)

Encode this object to a byte buffer.

#### Signature

```python
def encode(self, offset: int = 0) -> bytearray: ...
```

### GimpImageLevel().image

[Show source in GimpImageLevel.py:282](../../../gimpformats/GimpImageLevel.py#L282)

Get a final, compiled image.

#### Signature

```python
@property
def image(self) -> Image.Image: ...
```

### GimpImageLevel().image

[Show source in GimpImageLevel.py:298](../../../gimpformats/GimpImageLevel.py#L298)

#### Signature

```python
@image.setter
def image(self, image: Image.Image) -> None: ...
```

### GimpImageLevel().mode

[Show source in GimpImageLevel.py:256](../../../gimpformats/GimpImageLevel.py#L256)

Get mode.

#### Signature

```python
@property
def mode(self) -> str: ...
```

### GimpImageLevel().tiles

[Show source in GimpImageLevel.py:262](../../../gimpformats/GimpImageLevel.py#L262)

Get tiles.

#### Signature

```python
@property
def tiles(self) -> list[Image.Image]: ...
```