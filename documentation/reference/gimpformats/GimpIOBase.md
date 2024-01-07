# Gimpiobase

[Gimpformats Index](../README.md#gimpformats-index) /
[Gimpformats](./index.md#gimpformats) /
Gimpiobase

> Auto-generated documentation for [gimpformats.GimpIOBase](../../../gimpformats/GimpIOBase.py) module.

- [Gimpiobase](#gimpiobase)
  - [GimpIOBase](#gimpiobase)
    - [GimpIOBase().__repr__](#gimpiobase()__repr__)
    - [GimpIOBase().activeVector](#gimpiobase()activevector)
    - [GimpIOBase().doc](#gimpiobase()doc)
    - [GimpIOBase().expanded](#gimpiobase()expanded)
    - [GimpIOBase().expanded](#gimpiobase()expanded-1)
    - [GimpIOBase().getBlendMode](#gimpiobase()getblendmode)
    - [GimpIOBase().getCompositeModes](#gimpiobase()getcompositemodes)
    - [GimpIOBase().getCompositeSpaces](#gimpiobase()getcompositespaces)
    - [GimpIOBase().getCompression](#gimpiobase()getcompression)
    - [GimpIOBase().getTagColours](#gimpiobase()gettagcolours)
    - [GimpIOBase().getUnits](#gimpiobase()getunits)
    - [GimpIOBase().pointerSize](#gimpiobase()pointersize)
    - [GimpIOBase().root](#gimpiobase()root)
    - [GimpIOBase().tattoo](#gimpiobase()tattoo)
    - [GimpIOBase().tattoo](#gimpiobase()tattoo-1)
  - [GimpUserUnits](#gimpuserunits)
    - [GimpUserUnits().__repr__](#gimpuserunits()__repr__)
    - [GimpUserUnits().decode](#gimpuserunits()decode)
    - [GimpUserUnits().encode](#gimpuserunits()encode)

## GimpIOBase

[Show source in GimpIOBase.py:12](../../../gimpformats/GimpIOBase.py#L12)

A specialized binary file base for Gimp files.

#### Signature

```python
class GimpIOBase:
    def __init__(self, parent): ...
```

### GimpIOBase().__repr__

[Show source in GimpIOBase.py:680](../../../gimpformats/GimpIOBase.py#L680)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: str = ""): ...
```

### GimpIOBase().activeVector

[Show source in GimpIOBase.py:296](../../../gimpformats/GimpIOBase.py#L296)

Get the vector that is currently active.

#### Signature

```python
@property
def activeVector(self): ...
```

### GimpIOBase().doc

[Show source in GimpIOBase.py:223](../../../gimpformats/GimpIOBase.py#L223)

Get the main document object.

#### Signature

```python
@property
def doc(self): ...
```

### GimpIOBase().expanded

[Show source in GimpIOBase.py:301](../../../gimpformats/GimpIOBase.py#L301)

Is the group layer expanded.

#### Signature

```python
@property
def expanded(self) -> bool: ...
```

### GimpIOBase().expanded

[Show source in GimpIOBase.py:306](../../../gimpformats/GimpIOBase.py#L306)

Is the group layer expanded.

#### Signature

```python
@expanded.setter
def expanded(self, expanded): ...
```

### GimpIOBase().getBlendMode

[Show source in GimpIOBase.py:173](../../../gimpformats/GimpIOBase.py#L173)

Return the blend mode as a string.

#### Signature

```python
def getBlendMode(self) -> str: ...
```

### GimpIOBase().getCompositeModes

[Show source in GimpIOBase.py:189](../../../gimpformats/GimpIOBase.py#L189)

Return the composite mode as a string.

#### Signature

```python
def getCompositeModes(self): ...
```

### GimpIOBase().getCompositeSpaces

[Show source in GimpIOBase.py:193](../../../gimpformats/GimpIOBase.py#L193)

Return the composite spaces as a string.

#### Signature

```python
def getCompositeSpaces(self): ...
```

### GimpIOBase().getCompression

[Show source in GimpIOBase.py:177](../../../gimpformats/GimpIOBase.py#L177)

Return the compression as a string.

#### Signature

```python
def getCompression(self) -> str: ...
```

### GimpIOBase().getTagColours

[Show source in GimpIOBase.py:185](../../../gimpformats/GimpIOBase.py#L185)

Return the tag colours as a string.

#### Signature

```python
def getTagColours(self): ...
```

### GimpIOBase().getUnits

[Show source in GimpIOBase.py:181](../../../gimpformats/GimpIOBase.py#L181)

Return the units as a string.

#### Signature

```python
def getUnits(self) -> str: ...
```

### GimpIOBase().pointerSize

[Show source in GimpIOBase.py:197](../../../gimpformats/GimpIOBase.py#L197)

Determine the size of the "pointer" datatype based on the document version.

NOTE: prior to version 11, it was 32-bit,
 since then it is 64-bit, thus supporting
 larger image files

#### Signature

```python
@property
def pointerSize(self) -> int: ...
```

### GimpIOBase().root

[Show source in GimpIOBase.py:231](../../../gimpformats/GimpIOBase.py#L231)

Get the root of the file object tree (Which is the same as self.doc).

#### Signature

```python
@property
def root(self): ...
```

### GimpIOBase().tattoo

[Show source in GimpIOBase.py:236](../../../gimpformats/GimpIOBase.py#L236)

Gimp nomenclature for the item's unique id.

#### Signature

```python
@property
def tattoo(self): ...
```

### GimpIOBase().tattoo

[Show source in GimpIOBase.py:241](../../../gimpformats/GimpIOBase.py#L241)

Gimp nomenclature for the item's unique id.

#### Signature

```python
@tattoo.setter
def tattoo(self, tattoo): ...
```



## GimpUserUnits

[Show source in GimpIOBase.py:763](../../../gimpformats/GimpIOBase.py#L763)

User-defined measurement units.

#### Signature

```python
class GimpUserUnits:
    def __init__(self): ...
```

### GimpUserUnits().__repr__

[Show source in GimpIOBase.py:807](../../../gimpformats/GimpIOBase.py#L807)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: str = ""): ...
```

### GimpUserUnits().decode

[Show source in GimpIOBase.py:775](../../../gimpformats/GimpIOBase.py#L775)

Decode a byte buffer.

#### Arguments

- `data` *bytes* - data buffer to decode
- `index` *int, optional* - index within the buffer to start at]. Defaults to 0.

#### Returns

- `int` - offset

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int: ...
```

### GimpUserUnits().encode

[Show source in GimpIOBase.py:795](../../../gimpformats/GimpIOBase.py#L795)

Convert this object to raw bytes.

#### Signature

```python
def encode(self): ...
```