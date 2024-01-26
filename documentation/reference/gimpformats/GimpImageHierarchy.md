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

Gets packed pixels from a gimp image.

NOTE: This was originally designed to be a hierarchy, like
 an image pyramid, through in practice they only use the
 top level of the pyramid (64x64) and ignore the rest.

#### Signature

```python
class GimpImageHierarchy(GimpIOBase):
    def __init__(self, parent, image: Image.Image | None = None) -> None: ...
```

### GimpImageHierarchy().__repr__

[Show source in GimpImageHierarchy.py:123](../../../gimpformats/GimpImageHierarchy.py#L123)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: int = 0) -> str: ...
```

### GimpImageHierarchy().__str__

[Show source in GimpImageHierarchy.py:119](../../../gimpformats/GimpImageHierarchy.py#L119)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpImageHierarchy().decode

[Show source in GimpImageHierarchy.py:36](../../../gimpformats/GimpImageHierarchy.py#L36)

decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

#### Signature

```python
def decode(self, data: bytes, index: int = 0): ...
```

### GimpImageHierarchy().encode

[Show source in GimpImageHierarchy.py:69](../../../gimpformats/GimpImageHierarchy.py#L69)

Encode this object to a byte buffer.

#### Signature

```python
def encode(self): ...
```

### GimpImageHierarchy().image

[Show source in GimpImageHierarchy.py:100](../../../gimpformats/GimpImageHierarchy.py#L100)

Get a final, compiled image.

#### Signature

```python
@property
def image(self) -> Image.Image | None: ...
```

### GimpImageHierarchy().image

[Show source in GimpImageHierarchy.py:107](../../../gimpformats/GimpImageHierarchy.py#L107)

Set the image.

#### Signature

```python
@image.setter
def image(self, image: Image.Image) -> None: ...
```

### GimpImageHierarchy().levels

[Show source in GimpImageHierarchy.py:86](../../../gimpformats/GimpImageHierarchy.py#L86)

Get the levels within this hierarchy.

Presently hierarchy is not really used by gimp,
so this returns an array of one item

#### Signature

```python
@property
def levels(self) -> list[GimpImageLevel]: ...
```