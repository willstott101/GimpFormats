# Gimpimagehierarchy

[Gimpformats Index](../README.md#gimpformats-index) /
[Gimpformats](./index.md#gimpformats) /
Gimpimagehierarchy

> Auto-generated documentation for [gimpformats.GimpImageHierarchy](../../../gimpformats/GimpImageHierarchy.py) module.

- [Gimpimagehierarchy](#gimpimagehierarchy)
  - [GimpImageHierarchy](#gimpimagehierarchy)
    - [GimpImageHierarchy().__repr__](#gimpimagehierarchy()__repr__)
    - [GimpImageHierarchy().decode](#gimpimagehierarchy()decode)
    - [GimpImageHierarchy().encode](#gimpimagehierarchy()encode)
    - [GimpImageHierarchy().image](#gimpimagehierarchy()image)
    - [GimpImageHierarchy().image](#gimpimagehierarchy()image-1)
    - [GimpImageHierarchy().levels](#gimpimagehierarchy()levels)

## GimpImageHierarchy

[Show source in GimpImageHierarchy.py:15](../../../gimpformats/GimpImageHierarchy.py#L15)

Gets packed pixels from a gimp image

NOTE: This was originally designed to be a hierarchy, like
 an image pyramid, through in practice they only use the
 top level of the pyramid (64x64) and ignore the rest.

#### Signature

```python
class GimpImageHierarchy(GimpIOBase):
    def __init__(self, parent, image: Image.Image | None = None):
        ...
```

### GimpImageHierarchy().__repr__

[Show source in GimpImageHierarchy.py:116](../../../gimpformats/GimpImageHierarchy.py#L116)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: str = ""):
    ...
```

### GimpImageHierarchy().decode

[Show source in GimpImageHierarchy.py:35](../../../gimpformats/GimpImageHierarchy.py#L35)

decode a byte buffer

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

#### Signature

```python
def decode(self, data: bytes, index: int = 0):
    ...
```

### GimpImageHierarchy().encode

[Show source in GimpImageHierarchy.py:67](../../../gimpformats/GimpImageHierarchy.py#L67)

Encode this object to a byte buffer.

#### Signature

```python
def encode(self):
    ...
```

### GimpImageHierarchy().image

[Show source in GimpImageHierarchy.py:98](../../../gimpformats/GimpImageHierarchy.py#L98)

Get a final, compiled image.

#### Signature

```python
@property
def image(self) -> Image.Image | None:
    ...
```

### GimpImageHierarchy().image

[Show source in GimpImageHierarchy.py:105](../../../gimpformats/GimpImageHierarchy.py#L105)

Set the image.

#### Signature

```python
@image.setter
def image(self, image: Image.Image):
    ...
```

### GimpImageHierarchy().levels

[Show source in GimpImageHierarchy.py:84](../../../gimpformats/GimpImageHierarchy.py#L84)

Get the levels within this hierarchy.

Presently hierarchy is not really used by gimp,
so this returns an array of one item

#### Signature

```python
@property
def levels(self):
    ...
```


