# GimpParasites

> Auto-generated documentation for [gimpformats.GimpParasites](../../gimpformats/GimpParasites.py) module.

Parasites are arbitrary (meta)data strings that can be attached to a document tree item

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / GimpParasites
    - [GimpParasite](#gimpparasite)
        - [GimpParasite().\_\_repr\_\_](#gimpparasite__repr__)
        - [GimpParasite().decode](#gimpparasitedecode)
        - [GimpParasite().encode](#gimpparasiteencode)

They are used to store things like last-used plugin settings, gamma adjuetments, etc.

Format of known parasites:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/parasites.txt

## GimpParasite

[[find in source code]](../../gimpformats/GimpParasites.py#L47)

```python
class GimpParasite():
    def __init__():
```

Parasites are arbitrary (meta)data strings that can be attached to a document tree item

They are used to store things like last-used plugin settings, gamma adjuetments, etc.

Format of known parasites:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/parasites.txt

### GimpParasite().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpParasites.py#L87)

```python
def __repr__(indent: str = '') -> str:
```

Get a textual representation of this object.

### GimpParasite().decode

[[find in source code]](../../gimpformats/GimpParasites.py#L61)

```python
def decode(data: bytes, index: int = 0) -> int:
```

Decode a byte buffer

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

### GimpParasite().encode

[[find in source code]](../../gimpformats/GimpParasites.py#L74)

```python
def encode():
```

Encode a byte buffer

#### Arguments

- `data` - data buffer to encode
- `index` - index within the buffer to start at
