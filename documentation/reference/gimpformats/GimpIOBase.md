# Gimpiobase

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpiobase

> Auto-generated documentation for [gimpformats.GimpIOBase](../../../gimpformats/GimpIOBase.py) module.

- [Gimpiobase](#gimpiobase)
  - [GimpIOBase](#gimpiobase)
    - [GimpIOBase().__repr__](#gimpiobase()__repr__)
    - [GimpIOBase()._colormapDecode](#gimpiobase()_colormapdecode)
    - [GimpIOBase()._guidelinesDecode](#gimpiobase()_guidelinesdecode)
    - [GimpIOBase()._itemPathDecode](#gimpiobase()_itempathdecode)
    - [GimpIOBase()._parasitesDecode](#gimpiobase()_parasitesdecode)
    - [GimpIOBase()._parasitesEncode](#gimpiobase()_parasitesencode)
    - [GimpIOBase()._propertiesDecode](#gimpiobase()_propertiesdecode)
    - [GimpIOBase()._propertiesEncode](#gimpiobase()_propertiesencode)
    - [GimpIOBase()._propertyDecode](#gimpiobase()_propertydecode)
    - [GimpIOBase()._propertyEncode](#gimpiobase()_propertyencode)
    - [GimpIOBase()._samplePointsDecode](#gimpiobase()_samplepointsdecode)
    - [GimpIOBase()._userUnitsDecode](#gimpiobase()_userunitsdecode)
    - [GimpIOBase()._vectorsDecode](#gimpiobase()_vectorsdecode)
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

[Show source in GimpIOBase.py:13](../../../gimpformats/GimpIOBase.py#L13)

A specialized binary file base for Gimp files.

#### Signature

```python
class GimpIOBase:
    def __init__(self, parent: GimpIOBase) -> None: ...
```

### GimpIOBase().__repr__

[Show source in GimpIOBase.py:681](../../../gimpformats/GimpIOBase.py#L681)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: str = "") -> str: ...
```

### GimpIOBase()._colormapDecode

[Show source in GimpIOBase.py:315](../../../gimpformats/GimpIOBase.py#L315)

_colormapDecode_.

#### Arguments

- `data` - can be bytes or an IO object

decode colormap/palette

#### Signature

```python
def _colormapDecode(self, data: bytes | IO, index: int = 0) -> None: ...
```

### GimpIOBase()._guidelinesDecode

[Show source in GimpIOBase.py:263](../../../gimpformats/GimpIOBase.py#L263)

Decode guidelines.

#### Signature

```python
def _guidelinesDecode(self, data: bytes) -> None: ...
```

### GimpIOBase()._itemPathDecode

[Show source in GimpIOBase.py:273](../../../gimpformats/GimpIOBase.py#L273)

Decode item path.

#### Signature

```python
def _itemPathDecode(self, data: bytes) -> None: ...
```

### GimpIOBase()._parasitesDecode

[Show source in GimpIOBase.py:247](../../../gimpformats/GimpIOBase.py#L247)

Decode list of parasites.

#### Signature

```python
def _parasitesDecode(self, data: bytes) -> int: ...
```

### GimpIOBase()._parasitesEncode

[Show source in GimpIOBase.py:256](../../../gimpformats/GimpIOBase.py#L256)

Encode list of parasites.

#### Signature

```python
def _parasitesEncode(self) -> bytearray: ...
```

### GimpIOBase()._propertiesDecode

[Show source in GimpIOBase.py:659](../../../gimpformats/GimpIOBase.py#L659)

Decode a list of properties.

#### Signature

```python
def _propertiesDecode(self, ioBuf: IO) -> int: ...
```

### GimpIOBase()._propertiesEncode

[Show source in GimpIOBase.py:672](../../../gimpformats/GimpIOBase.py#L672)

Encode a list of properties.

#### Signature

```python
def _propertiesEncode(self) -> bytearray: ...
```

### GimpIOBase()._propertyDecode

[Show source in GimpIOBase.py:360](../../../gimpformats/GimpIOBase.py#L360)

Decode a single property.

Many properties are in the form
propertyType: one of PROP_
lengthOfData: 4
data: varies but is often ioBuf.32 or ioBuf.boolean

#### Signature

```python
def _propertyDecode(self, propertyType: int, data: bytes) -> int: ...
```

### GimpIOBase()._propertyEncode

[Show source in GimpIOBase.py:471](../../../gimpformats/GimpIOBase.py#L471)

Encode a single property.

Many properties are in the form
propertyType: one of PROP_
lengthOfData: 4
data: varies but is often ioBuf.32 or ioBuf.boolean

If the property is the same as the default, or not specified, returns empty array

#### Signature

```python
def _propertyEncode(self, propertyType: int) -> bytearray: ...
```

### GimpIOBase()._samplePointsDecode

[Show source in GimpIOBase.py:348](../../../gimpformats/GimpIOBase.py#L348)

Decode a series of points.

#### Signature

```python
def _samplePointsDecode(self, data: bytes) -> None: ...
```

### GimpIOBase()._userUnitsDecode

[Show source in GimpIOBase.py:342](../../../gimpformats/GimpIOBase.py#L342)

Decode a set of user-defined measurement units.

#### Signature

```python
def _userUnitsDecode(self, data: bytes) -> None: ...
```

### GimpIOBase()._vectorsDecode

[Show source in GimpIOBase.py:283](../../../gimpformats/GimpIOBase.py#L283)

Decode vectors.

#### Signature

```python
def _vectorsDecode(self, data: bytes) -> None: ...
```

### GimpIOBase().activeVector

[Show source in GimpIOBase.py:297](../../../gimpformats/GimpIOBase.py#L297)

Get the vector that is currently active.

#### Signature

```python
@property
def activeVector(self) -> GimpVector: ...
```

### GimpIOBase().doc

[Show source in GimpIOBase.py:224](../../../gimpformats/GimpIOBase.py#L224)

Get the main document object.

#### Signature

```python
@property
def doc(self) -> GimpIOBase: ...
```

### GimpIOBase().expanded

[Show source in GimpIOBase.py:302](../../../gimpformats/GimpIOBase.py#L302)

Is the group layer expanded.

#### Signature

```python
@property
def expanded(self) -> bool: ...
```

### GimpIOBase().expanded

[Show source in GimpIOBase.py:307](../../../gimpformats/GimpIOBase.py#L307)

Is the group layer expanded.

#### Signature

```python
@expanded.setter
def expanded(self, expanded: bool) -> None: ...
```

### GimpIOBase().getBlendMode

[Show source in GimpIOBase.py:174](../../../gimpformats/GimpIOBase.py#L174)

Return the blend mode as a string.

#### Signature

```python
def getBlendMode(self) -> str: ...
```

### GimpIOBase().getCompositeModes

[Show source in GimpIOBase.py:190](../../../gimpformats/GimpIOBase.py#L190)

Return the composite mode as a string.

#### Signature

```python
def getCompositeModes(self) -> str: ...
```

### GimpIOBase().getCompositeSpaces

[Show source in GimpIOBase.py:194](../../../gimpformats/GimpIOBase.py#L194)

Return the composite spaces as a string.

#### Signature

```python
def getCompositeSpaces(self) -> str: ...
```

### GimpIOBase().getCompression

[Show source in GimpIOBase.py:178](../../../gimpformats/GimpIOBase.py#L178)

Return the compression as a string.

#### Signature

```python
def getCompression(self) -> str: ...
```

### GimpIOBase().getTagColours

[Show source in GimpIOBase.py:186](../../../gimpformats/GimpIOBase.py#L186)

Return the tag colours as a string.

#### Signature

```python
def getTagColours(self) -> str: ...
```

### GimpIOBase().getUnits

[Show source in GimpIOBase.py:182](../../../gimpformats/GimpIOBase.py#L182)

Return the units as a string.

#### Signature

```python
def getUnits(self) -> str: ...
```

### GimpIOBase().pointerSize

[Show source in GimpIOBase.py:198](../../../gimpformats/GimpIOBase.py#L198)

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

[Show source in GimpIOBase.py:232](../../../gimpformats/GimpIOBase.py#L232)

Get the root of the file object tree (Which is the same as self.doc).

#### Signature

```python
@property
def root(self) -> GimpIOBase: ...
```

### GimpIOBase().tattoo

[Show source in GimpIOBase.py:237](../../../gimpformats/GimpIOBase.py#L237)

Gimp nomenclature for the item's unique id.

#### Signature

```python
@property
def tattoo(self) -> Any | None: ...
```

### GimpIOBase().tattoo

[Show source in GimpIOBase.py:242](../../../gimpformats/GimpIOBase.py#L242)

Gimp nomenclature for the item's unique id.

#### Signature

```python
@tattoo.setter
def tattoo(self, tattoo: Any | None) -> None: ...
```



## GimpUserUnits

[Show source in GimpIOBase.py:764](../../../gimpformats/GimpIOBase.py#L764)

User-defined measurement units.

#### Signature

```python
class GimpUserUnits:
    def __init__(self) -> None: ...
```

### GimpUserUnits().__repr__

[Show source in GimpIOBase.py:810](../../../gimpformats/GimpIOBase.py#L810)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: str = "") -> str: ...
```

### GimpUserUnits().decode

[Show source in GimpIOBase.py:776](../../../gimpformats/GimpIOBase.py#L776)

Decode a byte buffer.

#### Arguments

----
 - `data` *bytes* - data buffer to decode
 - `index` *int, optional* - index within the buffer to start at]. Defaults to 0.

#### Returns

-------
 - `int` - offset

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int: ...
```

### GimpUserUnits().encode

[Show source in GimpIOBase.py:798](../../../gimpformats/GimpIOBase.py#L798)

Convert this object to raw bytes.

#### Signature

```python
def encode(self): ...
```