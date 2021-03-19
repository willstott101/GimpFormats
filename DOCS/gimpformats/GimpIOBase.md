# GimpIOBase

> Auto-generated documentation for [gimpformats.GimpIOBase](../../gimpformats/GimpIOBase.py) module.

A specialized binary file base for Gimp files

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

[[find in source code]](../../gimpformats/GimpIOBase.py#L14)

```python
class GimpIOBase():
    def __init__(parent):
```

A specialized binary file base for Gimp files

### GimpIOBase().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpIOBase.py#L715)

```python
def __repr__(indent: str = ''):
```

Get a textual representation of this object

### GimpIOBase().activeVector

[[find in source code]](../../gimpformats/GimpIOBase.py#L318)

```python
@property
def activeVector():
```

get the vector that is currently active

### GimpIOBase().doc

[[find in source code]](../../gimpformats/GimpIOBase.py#L226)

```python
@property
def doc():
```

Get the main document object

### GimpIOBase().expanded

[[find in source code]](../../gimpformats/GimpIOBase.py#L325)

```python
@property
def expanded() -> bool:
```

is the group layer expanded

### GimpIOBase().expanded

[[find in source code]](../../gimpformats/GimpIOBase.py#L332)

```python
@expanded.setter
def expanded(expanded):
```

is the group layer expanded

### GimpIOBase().getBlendMode

[[find in source code]](../../gimpformats/GimpIOBase.py#L174)

```python
def getBlendMode() -> str:
```

return the blend mode as a string.

### GimpIOBase().getCompositeModes

[[find in source code]](../../gimpformats/GimpIOBase.py#L190)

```python
def getCompositeModes():
```

return the composite mode as a string.

### GimpIOBase().getCompositeSpaces

[[find in source code]](../../gimpformats/GimpIOBase.py#L194)

```python
def getCompositeSpaces():
```

return the composite spaces as a string.

### GimpIOBase().getCompression

[[find in source code]](../../gimpformats/GimpIOBase.py#L178)

```python
def getCompression() -> str:
```

return the compression as a string.

### GimpIOBase().getTagColours

[[find in source code]](../../gimpformats/GimpIOBase.py#L186)

```python
def getTagColours():
```

return the tag colours as a string.

### GimpIOBase().getUnits

[[find in source code]](../../gimpformats/GimpIOBase.py#L182)

```python
def getUnits() -> str:
```

return the units as a string.

### GimpIOBase().root

[[find in source code]](../../gimpformats/GimpIOBase.py#L236)

```python
@property
def root():
```

Get the root of the file object tree
(Which is the same as self.doc)

### GimpIOBase().tattoo

[[find in source code]](../../gimpformats/GimpIOBase.py#L244)

```python
@property
def tattoo():
```

This is the gimp nomenclature for the item's unique id

### GimpIOBase().tattoo

[[find in source code]](../../gimpformats/GimpIOBase.py#L251)

```python
@tattoo.setter
def tattoo(tattoo):
```

This is the gimp nomenclature for the item's unique id

## GimpUserUnits

[[find in source code]](../../gimpformats/GimpIOBase.py#L814)

```python
class GimpUserUnits():
    def __init__():
```

user-defined measurement units

### GimpUserUnits().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpIOBase.py#L859)

```python
def __repr__(indent: str = ''):
```

Get a textual representation of this object

### GimpUserUnits().decode

[[find in source code]](../../gimpformats/GimpIOBase.py#L828)

```python
def decode(data: bytearray, index: int = 0):
```

decode a byte buffer

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

### GimpUserUnits().encode

[[find in source code]](../../gimpformats/GimpIOBase.py#L845)

```python
def encode():
```

convert this object to raw bytes
