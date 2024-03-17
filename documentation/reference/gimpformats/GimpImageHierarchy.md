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

[Show source in GimpImageHierarchy.py:17](../../../gimpformats/GimpImageHierarchy.py#L17)

Represents packed pixels from a GIMP image hierarchy.

NOTE: Originally designed as a hierarchy, but currently only the top level (64x64) is used.

#### Signature

```python
class GimpImageHierarchy(GimpIOBase):
    def __init__(self, parent, image: Image.Image | None = None) -> None: ...
```

### GimpImageHierarchy().__repr__

[Show source in GimpImageHierarchy.py:113](../../../gimpformats/GimpImageHierarchy.py#L113)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: int = 0) -> str: ...
```

### GimpImageHierarchy().__str__

[Show source in GimpImageHierarchy.py:109](../../../gimpformats/GimpImageHierarchy.py#L109)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpImageHierarchy().decode

[Show source in GimpImageHierarchy.py:35](../../../gimpformats/GimpImageHierarchy.py#L35)

Decode packed pixels from a byte buffer.

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int: ...
```

### GimpImageHierarchy().encode

[Show source in GimpImageHierarchy.py:63](../../../gimpformats/GimpImageHierarchy.py#L63)

Encode packed pixels data into a byte buffer.

#### Signature

```python
def encode(self) -> bytearray: ...
```

### GimpImageHierarchy().image

[Show source in GimpImageHierarchy.py:94](../../../gimpformats/GimpImageHierarchy.py#L94)

Get a final, compiled image.

#### Signature

```python
@property
def image(self) -> Image.Image | None: ...
```

### GimpImageHierarchy().image

[Show source in GimpImageHierarchy.py:99](../../../gimpformats/GimpImageHierarchy.py#L99)

Set the image.

#### Signature

```python
@image.setter
def image(self, image: Image.Image) -> None: ...
```

### GimpImageHierarchy().levels

[Show source in GimpImageHierarchy.py:80](../../../gimpformats/GimpImageHierarchy.py#L80)

Get the levels within this hierarchy.

Presently hierarchy is not really used by gimp,
so this returns an array of one item

#### Signature

```python
@property
def levels(self) -> list[GimpImageLevel]: ...
```