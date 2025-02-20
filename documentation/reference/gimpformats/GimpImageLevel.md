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

#### Signature

```python
class GimpImageLevel(GimpIOBase):
    def __init__(self, parent: Any) -> None: ...
```

#### See also

- [GimpIOBase](./GimpIOBase.md#gimpiobase)

### GimpImageLevel().__repr__

[Show source in GimpImageLevel.py:287](../../../gimpformats/GimpImageLevel.py#L287)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpImageLevel().__str__

[Show source in GimpImageLevel.py:283](../../../gimpformats/GimpImageLevel.py#L283)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpImageLevel()._encodeRLE

[Show source in GimpImageLevel.py:153](../../../gimpformats/GimpImageLevel.py#L153)

Encode image to RLE image data.

#### Signature

```python
def _encodeRLE(self, data: bytearray, bpp: int) -> bytearray: ...
```

### GimpImageLevel()._imgToTiles

[Show source in GimpImageLevel.py:248](../../../gimpformats/GimpImageLevel.py#L248)

Break an image into a series of tiles, each<=64x64.

#### Signature

```python
def _imgToTiles(self, image: Image.Image) -> list[Image.Image]: ...
```

### GimpImageLevel().bpp

[Show source in GimpImageLevel.py:228](../../../gimpformats/GimpImageLevel.py#L228)

Get bpp.

#### Signature

```python
@property
def bpp(self) -> int: ...
```

### GimpImageLevel().decode

[Show source in GimpImageLevel.py:30](../../../gimpformats/GimpImageLevel.py#L30)

Decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

#### Signature

```python
def decode(self, data: bytearray | bytes | None, index: int = 0) -> int: ...
```

### GimpImageLevel().encode

[Show source in GimpImageLevel.py:72](../../../gimpformats/GimpImageLevel.py#L72)

Encode this object to a byte buffer.

#### Signature

```python
def encode(self) -> bytearray: ...
```

### GimpImageLevel().image

[Show source in GimpImageLevel.py:259](../../../gimpformats/GimpImageLevel.py#L259)

Get a final, compiled image.

#### Signature

```python
@property
def image(self) -> Image.Image: ...
```

### GimpImageLevel().image

[Show source in GimpImageLevel.py:275](../../../gimpformats/GimpImageLevel.py#L275)

#### Signature

```python
@image.setter
def image(self, image: Image.Image) -> None: ...
```

### GimpImageLevel().mode

[Show source in GimpImageLevel.py:233](../../../gimpformats/GimpImageLevel.py#L233)

Get mode.

#### Signature

```python
@property
def mode(self) -> str: ...
```

### GimpImageLevel().tiles

[Show source in GimpImageLevel.py:239](../../../gimpformats/GimpImageLevel.py#L239)

Get tiles.

#### Signature

```python
@property
def tiles(self) -> list[Image.Image]: ...
```