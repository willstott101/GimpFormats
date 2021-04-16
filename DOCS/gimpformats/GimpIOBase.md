# GimpIOBase

> Auto-generated documentation for [gimpformats.GimpIOBase](../../gimpformats/GimpIOBase.py) module.

A specialized binary file base for Gimp files.

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / GimpIOBase
    - [GimpIOBase](#gimpiobase)
        - [GimpIOBase().\_\_repr\_\_](#gimpiobase__repr__)
        - [GimpIOBase().activeVector](#gimpiobaseactivevector)
        - [GimpIOBase().doc](#gimpiobasedoc)
        - [GimpIOBase().expanded](#gimpiobaseexpanded)
        - [GimpIOBase().expanded](#gimpiobaseexpanded)
        - [GimpIOBase().getBlendMode](#gimpiobasegetblendmode)
        - [GimpIOBase().getCompositeModes](#gimpiobasegetcompositemodes)
        - [GimpIOBase().getCompositeSpaces](#gimpiobasegetcompositespaces)
        - [GimpIOBase().getCompression](#gimpiobasegetcompression)
        - [GimpIOBase().getTagColours](#gimpiobasegettagcolours)
        - [GimpIOBase().getUnits](#gimpiobasegetunits)
        - [GimpIOBase().root](#gimpiobaseroot)
        - [GimpIOBase().tattoo](#gimpiobasetattoo)
        - [GimpIOBase().tattoo](#gimpiobasetattoo)
    - [GimpUserUnits](#gimpuserunits)
        - [GimpUserUnits().\_\_repr\_\_](#gimpuserunits__repr__)
        - [GimpUserUnits().decode](#gimpuserunitsdecode)
        - [GimpUserUnits().encode](#gimpuserunitsencode)

## GimpIOBase

[[find in source code]](../../gimpformats/GimpIOBase.py#L13)

```python
class GimpIOBase():
    def __init__(parent):
```

A specialized binary file base for Gimp files.

### GimpIOBase().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpIOBase.py#L681)

```python
def __repr__(indent: str = ''):
```

Get a textual representation of this object.

### GimpIOBase().activeVector

[[find in source code]](../../gimpformats/GimpIOBase.py#L296)

```python
@property
def activeVector():
```

Get the vector that is currently active.

### GimpIOBase().doc

[[find in source code]](../../gimpformats/GimpIOBase.py#L223)

```python
@property
def doc():
```

Get the main document object.

### GimpIOBase().expanded

[[find in source code]](../../gimpformats/GimpIOBase.py#L301)

```python
@property
def expanded() -> bool:
```

Is the group layer expanded.

### GimpIOBase().expanded

[[find in source code]](../../gimpformats/GimpIOBase.py#L306)

```python
@expanded.setter
def expanded(expanded):
```

Is the group layer expanded.

### GimpIOBase().getBlendMode

[[find in source code]](../../gimpformats/GimpIOBase.py#L173)

```python
def getBlendMode() -> str:
```

Return the blend mode as a string.

### GimpIOBase().getCompositeModes

[[find in source code]](../../gimpformats/GimpIOBase.py#L189)

```python
def getCompositeModes():
```

Return the composite mode as a string.

### GimpIOBase().getCompositeSpaces

[[find in source code]](../../gimpformats/GimpIOBase.py#L193)

```python
def getCompositeSpaces():
```

Return the composite spaces as a string.

### GimpIOBase().getCompression

[[find in source code]](../../gimpformats/GimpIOBase.py#L177)

```python
def getCompression() -> str:
```

Return the compression as a string.

### GimpIOBase().getTagColours

[[find in source code]](../../gimpformats/GimpIOBase.py#L185)

```python
def getTagColours():
```

Return the tag colours as a string.

### GimpIOBase().getUnits

[[find in source code]](../../gimpformats/GimpIOBase.py#L181)

```python
def getUnits() -> str:
```

Return the units as a string.

### GimpIOBase().root

[[find in source code]](../../gimpformats/GimpIOBase.py#L231)

```python
@property
def root():
```

Get the root of the file object tree (Which is the same as self.doc).

### GimpIOBase().tattoo

[[find in source code]](../../gimpformats/GimpIOBase.py#L236)

```python
@property
def tattoo():
```

Gimp nomenclature for the item's unique id.

### GimpIOBase().tattoo

[[find in source code]](../../gimpformats/GimpIOBase.py#L241)

```python
@tattoo.setter
def tattoo(tattoo):
```

Gimp nomenclature for the item's unique id.

## GimpUserUnits

[[find in source code]](../../gimpformats/GimpIOBase.py#L780)

```python
class GimpUserUnits():
    def __init__():
```

User-defined measurement units.

### GimpUserUnits().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpIOBase.py#L820)

```python
def __repr__(indent: str = ''):
```

Get a textual representation of this object.

### GimpUserUnits().decode

[[find in source code]](../../gimpformats/GimpIOBase.py#L792)

```python
def decode(data: bytearray, index: int = 0) -> int:
```

Decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

### GimpUserUnits().encode

[[find in source code]](../../gimpformats/GimpIOBase.py#L808)

```python
def encode():
```

Convert this object to raw bytes.
