# Gimpimagelevel

[Gimpformats Index](../README.md#gimpformats-index) /
[Gimpformats](./index.md#gimpformats) /
Gimpimagelevel

> Auto-generated documentation for [gimpformats.GimpImageLevel](../../../gimpformats/GimpImageLevel.py) module.

- [Gimpimagelevel](#gimpimagelevel)
  - [GimpImageLevel](#gimpimagelevel)
    - [GimpImageLevel().__repr__](#gimpimagelevel()__repr__)
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
    def __init__(self, parent):
        ...
```

### GimpImageLevel().__repr__

[Show source in GimpImageLevel.py:278](../../../gimpformats/GimpImageLevel.py#L278)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: str = ""):
    ...
```

### GimpImageLevel().bpp

[Show source in GimpImageLevel.py:223](../../../gimpformats/GimpImageLevel.py#L223)

Get bpp.

#### Signature

```python
@property
def bpp(self):
    ...
```

### GimpImageLevel().decode

[Show source in GimpImageLevel.py:31](../../../gimpformats/GimpImageLevel.py#L31)

Decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

#### Signature

```python
def decode(self, data: bytes, index: int = 0):
    ...
```

### GimpImageLevel().encode

[Show source in GimpImageLevel.py:70](../../../gimpformats/GimpImageLevel.py#L70)

Encode this object to a byte buffer.

#### Signature

```python
def encode(self):
    ...
```

### GimpImageLevel().image

[Show source in GimpImageLevel.py:254](../../../gimpformats/GimpImageLevel.py#L254)

Get a final, compiled image

#### Signature

```python
@property
def image(self) -> Image:
    ...
```

### GimpImageLevel().image

[Show source in GimpImageLevel.py:270](../../../gimpformats/GimpImageLevel.py#L270)

#### Signature

```python
@image.setter
def image(self, image: Image):
    ...
```

### GimpImageLevel().mode

[Show source in GimpImageLevel.py:228](../../../gimpformats/GimpImageLevel.py#L228)

Get mode.

#### Signature

```python
@property
def mode(self):
    ...
```

### GimpImageLevel().tiles

[Show source in GimpImageLevel.py:234](../../../gimpformats/GimpImageLevel.py#L234)

Get tiles.

#### Signature

```python
@property
def tiles(self):
    ...
```