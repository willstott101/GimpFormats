# Gimpiobase

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpiobase

> Auto-generated documentation for [gimpformats.GimpIOBase](../../../gimpformats/GimpIOBase.py) module.

- [Gimpiobase](#gimpiobase)
  - [BlendMode](#blendmode)
  - [ColorMode](#colormode)
  - [CompositeMode](#compositemode)
  - [CompositeSpace](#compositespace)
  - [CompressionMode](#compressionmode)
  - [GimpIOBase](#gimpiobase)
    - [GimpIOBase().__repr__](#gimpiobase()__repr__)
    - [GimpIOBase().__str__](#gimpiobase()__str__)
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
    - [GimpIOBase().pointerSize](#gimpiobase()pointersize)
    - [GimpIOBase().root](#gimpiobase()root)
    - [GimpIOBase().tattoo](#gimpiobase()tattoo)
    - [GimpIOBase().tattoo](#gimpiobase()tattoo-1)
  - [GimpUserUnits](#gimpuserunits)
    - [GimpUserUnits().__repr__](#gimpuserunits()__repr__)
    - [GimpUserUnits().__str__](#gimpuserunits()__str__)
    - [GimpUserUnits().decode](#gimpuserunits()decode)
    - [GimpUserUnits().encode](#gimpuserunits()encode)
  - [ImageProperties](#imageproperties)
  - [TagColor](#tagcolor)
  - [Units](#units)
  - [camel_to_pascal_with_spaces](#camel_to_pascal_with_spaces)

## BlendMode

[Show source in GimpIOBase.py:77](../../../gimpformats/GimpIOBase.py#L77)

#### Signature

```python
class BlendMode(Enum): ...
```



## ColorMode

[Show source in GimpIOBase.py:32](../../../gimpformats/GimpIOBase.py#L32)

#### Signature

```python
class ColorMode(Enum): ...
```



## CompositeMode

[Show source in GimpIOBase.py:45](../../../gimpformats/GimpIOBase.py#L45)

#### Signature

```python
class CompositeMode(Enum): ...
```



## CompositeSpace

[Show source in GimpIOBase.py:52](../../../gimpformats/GimpIOBase.py#L52)

#### Signature

```python
class CompositeSpace(Enum): ...
```



## CompressionMode

[Show source in GimpIOBase.py:70](../../../gimpformats/GimpIOBase.py#L70)

#### Signature

```python
class CompressionMode(Enum): ...
```



## GimpIOBase

[Show source in GimpIOBase.py:186](../../../gimpformats/GimpIOBase.py#L186)

#### Signature

```python
class GimpIOBase:
    def __init__(self, parent: GimpIOBase = None) -> None: ...
```

### GimpIOBase().__repr__

[Show source in GimpIOBase.py:717](../../../gimpformats/GimpIOBase.py#L717)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: int = 0) -> str: ...
```

### GimpIOBase().__str__

[Show source in GimpIOBase.py:713](../../../gimpformats/GimpIOBase.py#L713)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpIOBase()._colormapDecode

[Show source in GimpIOBase.py:345](../../../gimpformats/GimpIOBase.py#L345)

_colormapDecode_.

#### Arguments

- `data` - can be bytes or an IO object

decode colormap/palette

#### Signature

```python
def _colormapDecode(self, data: bytes | IO, index: int = 0) -> None: ...
```

### GimpIOBase()._guidelinesDecode

[Show source in GimpIOBase.py:293](../../../gimpformats/GimpIOBase.py#L293)

Decode guidelines.

#### Signature

```python
def _guidelinesDecode(self, data: bytes) -> None: ...
```

### GimpIOBase()._itemPathDecode

[Show source in GimpIOBase.py:303](../../../gimpformats/GimpIOBase.py#L303)

Decode item path.

#### Signature

```python
def _itemPathDecode(self, data: bytes) -> None: ...
```

### GimpIOBase()._parasitesDecode

[Show source in GimpIOBase.py:277](../../../gimpformats/GimpIOBase.py#L277)

Decode list of parasites.

#### Signature

```python
def _parasitesDecode(self, data: bytes) -> int: ...
```

### GimpIOBase()._parasitesEncode

[Show source in GimpIOBase.py:286](../../../gimpformats/GimpIOBase.py#L286)

Encode list of parasites.

#### Signature

```python
def _parasitesEncode(self) -> bytearray: ...
```

### GimpIOBase()._propertiesDecode

[Show source in GimpIOBase.py:691](../../../gimpformats/GimpIOBase.py#L691)

Decode a list of properties.

#### Signature

```python
def _propertiesDecode(self, ioBuf: IO) -> int: ...
```

### GimpIOBase()._propertiesEncode

[Show source in GimpIOBase.py:704](../../../gimpformats/GimpIOBase.py#L704)

Encode a list of properties.

#### Signature

```python
def _propertiesEncode(self) -> bytearray: ...
```

### GimpIOBase()._propertyDecode

[Show source in GimpIOBase.py:390](../../../gimpformats/GimpIOBase.py#L390)

Decode a single property.

Many properties are in the form
prop: one of PROP_
lengthOfData: 4
data: varies but is often ioBuf.32 or ioBuf.boolean

#### Signature

```python
def _propertyDecode(self, prop: int, data: bytes) -> int: ...
```

### GimpIOBase()._propertyEncode

[Show source in GimpIOBase.py:501](../../../gimpformats/GimpIOBase.py#L501)

Encode a single property.

Many properties are in the form
prop: one of PROP_
lengthOfData: 4
data: varies but is often ioBuf.32 or ioBuf.boolean

If the property is the same as the default, or not specified, returns empty array

#### Signature

```python
def _propertyEncode(self, prop: int) -> bytearray: ...
```

### GimpIOBase()._samplePointsDecode

[Show source in GimpIOBase.py:378](../../../gimpformats/GimpIOBase.py#L378)

Decode a series of points.

#### Signature

```python
def _samplePointsDecode(self, data: bytes) -> None: ...
```

### GimpIOBase()._userUnitsDecode

[Show source in GimpIOBase.py:372](../../../gimpformats/GimpIOBase.py#L372)

Decode a set of user-defined measurement units.

#### Signature

```python
def _userUnitsDecode(self, data: bytes) -> None: ...
```

### GimpIOBase()._vectorsDecode

[Show source in GimpIOBase.py:313](../../../gimpformats/GimpIOBase.py#L313)

Decode vectors.

#### Signature

```python
def _vectorsDecode(self, data: bytes) -> None: ...
```

### GimpIOBase().activeVector

[Show source in GimpIOBase.py:327](../../../gimpformats/GimpIOBase.py#L327)

Get the vector that is currently active.

#### Signature

```python
@property
def activeVector(self) -> GimpVector: ...
```

### GimpIOBase().doc

[Show source in GimpIOBase.py:255](../../../gimpformats/GimpIOBase.py#L255)

#### Signature

```python
@property
def doc(self) -> GimpIOBase: ...
```

### GimpIOBase().expanded

[Show source in GimpIOBase.py:332](../../../gimpformats/GimpIOBase.py#L332)

Is the group layer expanded.

#### Signature

```python
@property
def expanded(self) -> bool: ...
```

### GimpIOBase().expanded

[Show source in GimpIOBase.py:337](../../../gimpformats/GimpIOBase.py#L337)

Is the group layer expanded.

#### Signature

```python
@expanded.setter
def expanded(self, expanded: bool) -> None: ...
```

### GimpIOBase().pointerSize

[Show source in GimpIOBase.py:229](../../../gimpformats/GimpIOBase.py#L229)

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

[Show source in GimpIOBase.py:262](../../../gimpformats/GimpIOBase.py#L262)

Get the root of the file object tree (Which is the same as self.doc).

#### Signature

```python
@property
def root(self) -> GimpIOBase: ...
```

### GimpIOBase().tattoo

[Show source in GimpIOBase.py:267](../../../gimpformats/GimpIOBase.py#L267)

Gimp nomenclature for the item's unique id.

#### Signature

```python
@property
def tattoo(self) -> Any | None: ...
```

### GimpIOBase().tattoo

[Show source in GimpIOBase.py:272](../../../gimpformats/GimpIOBase.py#L272)

Gimp nomenclature for the item's unique id.

#### Signature

```python
@tattoo.setter
def tattoo(self, tattoo: Any | None) -> None: ...
```



## GimpUserUnits

[Show source in GimpIOBase.py:794](../../../gimpformats/GimpIOBase.py#L794)

User-defined measurement units.

#### Signature

```python
class GimpUserUnits:
    def __init__(self) -> None: ...
```

### GimpUserUnits().__repr__

[Show source in GimpIOBase.py:844](../../../gimpformats/GimpIOBase.py#L844)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: int = 0) -> str: ...
```

### GimpUserUnits().__str__

[Show source in GimpIOBase.py:840](../../../gimpformats/GimpIOBase.py#L840)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpUserUnits().decode

[Show source in GimpIOBase.py:806](../../../gimpformats/GimpIOBase.py#L806)

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

[Show source in GimpIOBase.py:828](../../../gimpformats/GimpIOBase.py#L828)

Convert this object to raw bytes.

#### Signature

```python
def encode(self) -> bytearray: ...
```



## ImageProperties

[Show source in GimpIOBase.py:142](../../../gimpformats/GimpIOBase.py#L142)

#### Signature

```python
class ImageProperties(Enum): ...
```



## TagColor

[Show source in GimpIOBase.py:58](../../../gimpformats/GimpIOBase.py#L58)

#### Signature

```python
class TagColor(Enum): ...
```



## Units

[Show source in GimpIOBase.py:38](../../../gimpformats/GimpIOBase.py#L38)

#### Signature

```python
class Units(Enum): ...
```



## camel_to_pascal_with_spaces

[Show source in GimpIOBase.py:22](../../../gimpformats/GimpIOBase.py#L22)

#### Signature

```python
def camel_to_pascal_with_spaces(val: str) -> str: ...
```