# Gimpparasites

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpparasites

> Auto-generated documentation for [gimpformats.GimpParasites](../../../gimpformats/GimpParasites.py) module.

- [Gimpparasites](#gimpparasites)
  - [GimpParasite](#gimpparasite)
    - [GimpParasite().__repr__](#gimpparasite()__repr__)
    - [GimpParasite().__str__](#gimpparasite()__str__)
    - [GimpParasite().decode](#gimpparasite()decode)
    - [GimpParasite().encode](#gimpparasite()encode)

## GimpParasite

[Show source in GimpParasites.py:48](../../../gimpformats/GimpParasites.py#L48)

Parasites are arbitrary (meta)data strings that can be attached to a document tree item.

They are used to store things like last-used plugin settings, gamma adjuetments, etc.

Format of known parasites:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/parasites.txt

#### Signature

```python
class GimpParasite:
    def __init__(self) -> None: ...
```

### GimpParasite().__repr__

[Show source in GimpParasites.py:92](../../../gimpformats/GimpParasites.py#L92)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: int = 0) -> str: ...
```

### GimpParasite().__str__

[Show source in GimpParasites.py:88](../../../gimpformats/GimpParasites.py#L88)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpParasite().decode

[Show source in GimpParasites.py:62](../../../gimpformats/GimpParasites.py#L62)

Decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int: ...
```

### GimpParasite().encode

[Show source in GimpParasites.py:75](../../../gimpformats/GimpParasites.py#L75)

Encode a byte buffer.

#### Arguments

- `data` - data buffer to encode
- `index` - index within the buffer to start at

#### Signature

```python
def encode(self) -> bytearray: ...
```