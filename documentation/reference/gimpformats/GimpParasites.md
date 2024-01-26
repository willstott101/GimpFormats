# Gimpparasites

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpparasites

> Auto-generated documentation for [gimpformats.GimpParasites](../../../gimpformats/GimpParasites.py) module.

- [Gimpparasites](#gimpparasites)
  - [GimpParasite](#gimpparasite)
    - [GimpParasite().__repr__](#gimpparasite()__repr__)
    - [GimpParasite().__str__](#gimpparasite()__str__)
    - [GimpParasite().decode](#gimpparasite()decode)
    - [GimpParasite().encode](#gimpparasite()encode)
  - [repr_indent_lines](#repr_indent_lines)

## GimpParasite

[Show source in GimpParasites.py:46](../../../gimpformats/GimpParasites.py#L46)

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

[Show source in GimpParasites.py:90](../../../gimpformats/GimpParasites.py#L90)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: int = 0) -> str: ...
```

### GimpParasite().__str__

[Show source in GimpParasites.py:86](../../../gimpformats/GimpParasites.py#L86)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpParasite().decode

[Show source in GimpParasites.py:60](../../../gimpformats/GimpParasites.py#L60)

Decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int: ...
```

### GimpParasite().encode

[Show source in GimpParasites.py:73](../../../gimpformats/GimpParasites.py#L73)

Encode a byte buffer.

#### Arguments

- `data` - data buffer to encode
- `index` - index within the buffer to start at

#### Signature

```python
def encode(self): ...
```



## repr_indent_lines

[Show source in GimpParasites.py:99](../../../gimpformats/GimpParasites.py#L99)

#### Signature

```python
def repr_indent_lines(indent: int, lines: list[str]): ...
```