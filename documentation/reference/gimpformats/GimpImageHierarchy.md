# Gimpimagehierarchy

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpimagehierarchy

> Auto-generated documentation for [gimpformats.GimpImageHierarchy](../../../gimpformats/GimpImageHierarchy.py) module.

- [Gimpimagehierarchy](#gimpimagehierarchy)
  - [GimpImageHierarchy](#gimpimagehierarchy)
    - [GimpImageHierarchy().__repr__](#gimpimagehierarchy()__repr__)
    - [GimpImageHierarchy().__str__](#gimpimagehierarchy()__str__)
    - [GimpImageHierarchy().decode](#gimpimagehierarchy()decode)
    - [GimpImageHierarchy().encode](#gimpimagehierarchy()encode)
    - [GimpImageHierarchy().image](#gimpimagehierarchy()image)
    - [GimpImageHierarchy().image](#gimpimagehierarchy()image-1)
    - [GimpImageHierarchy().levels](#gimpimagehierarchy()levels)

## GimpImageHierarchy

[Show source in GimpImageHierarchy.py:16](../../../gimpformats/GimpImageHierarchy.py#L16)

Represents packed pixels from a GIMP image hierarchy.

Note that the XCF docs say this was originally designed as a hierarchy,
but currently only the top level (lptr) is used

uint32      width   Width of the pixel array
uint32      height  Height of the pixel array
uint32      bpp     Number of bytes per pixel; this depends on the
    color mode and image precision (fields 'base_type'
    and 'precision' of the image header). For
    instance, some combination values:
    3: RGB color without alpha in 8-bit precision
    4: RGB color with alpha in 8-bit precision
    6: RGB color without alpha in 16-bit precision
    16: RGB color with alpha in 32-bit precision
    1: Grayscale without alpha in 8-bit precision
    4: Grayscale with alpha in 16-bit precision
    1: Indexed without alpha (always 8-bit)
    2: Indexed with alpha (always 8-bit)
    And so on.

pointer     lptr    Pointer to the "level" structure
,--------   ------  Repeat zero or more times
| pointer   dlevel  Pointer to an unused level structure (dummy level)
`--
pointer     0       Zero marks the end of the list of level pointers.
.

#### Signature

```python
class GimpImageHierarchy(GimpIOBase):
    def __init__(self, parent, image: Image.Image | None = None) -> None: ...
```

#### See also

- [GimpIOBase](./GimpIOBase.md#gimpiobase)

### GimpImageHierarchy().__repr__

[Show source in GimpImageHierarchy.py:141](../../../gimpformats/GimpImageHierarchy.py#L141)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpImageHierarchy().__str__

[Show source in GimpImageHierarchy.py:137](../../../gimpformats/GimpImageHierarchy.py#L137)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpImageHierarchy().decode

[Show source in GimpImageHierarchy.py:58](../../../gimpformats/GimpImageHierarchy.py#L58)

Decode packed pixels from a byte buffer.

#### Signature

```python
def decode(self, data: bytearray, index: int = 0) -> int: ...
```

### GimpImageHierarchy().encode

[Show source in GimpImageHierarchy.py:88](../../../gimpformats/GimpImageHierarchy.py#L88)

Encode packed pixels data into a byte buffer.

#### Signature

```python
def encode(self, offset: int = 0) -> bytearray: ...
```

### GimpImageHierarchy().image

[Show source in GimpImageHierarchy.py:122](../../../gimpformats/GimpImageHierarchy.py#L122)

Get a final, compiled image.

#### Signature

```python
@property
def image(self) -> Image.Image | None: ...
```

### GimpImageHierarchy().image

[Show source in GimpImageHierarchy.py:127](../../../gimpformats/GimpImageHierarchy.py#L127)

Set the image.

#### Signature

```python
@image.setter
def image(self, image: Image.Image) -> None: ...
```

### GimpImageHierarchy().levels

[Show source in GimpImageHierarchy.py:108](../../../gimpformats/GimpImageHierarchy.py#L108)

Get the levels within this hierarchy.

Presently hierarchy is not really used by gimp,
so this returns an array of one item

#### Signature

```python
@property
def levels(self) -> list[GimpImageLevel]: ...
```

#### See also

- [GimpImageLevel](./GimpImageLevel.md#gimpimagelevel)