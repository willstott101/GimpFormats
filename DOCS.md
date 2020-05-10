<a name=".gimpformats"></a>
## gimpformats

gimpformats

Forked from https://github.com/TheHeadlessSourceMan/gimpFormats

A pure python implementation of the GIMP XCF image format.

Use this to interact with GIMP image formats

<a name=".gimpformats.GimpChannel"></a>
## gimpformats.GimpChannel

Represents a single channel or mask in a gimp image

<a name=".gimpformats.GimpChannel.GimpChannel"></a>
### GimpChannel

```python
class GimpChannel(GimpIOBase):
 |  GimpChannel(parent, name='', image=None)
```

Represents a single channel or mask in a gimp image

<a name=".gimpformats.GimpChannel.GimpChannel.decode_"></a>
#### decode\_

```python
 | decode_(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.GimpChannel.GimpChannel.encode_"></a>
#### encode\_

```python
 | encode_()
```

encode this object to a byte buffer

<a name=".gimpformats.GimpChannel.GimpChannel.image"></a>
#### image

```python
 | @image.setter
 | image(image)
```

get a final, compiled image

<a name=".gimpformats.GimpChannel.GimpChannel.imageHierarchy"></a>
#### imageHierarchy

```python
 | @property
 | imageHierarchy()
```

Get the image hierarchy

This is mainly used for decoding the image, so
not much use to you.

<a name=".gimpformats.GimpChannel.GimpChannel.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.GimpGbrBrush"></a>
## gimpformats.GimpGbrBrush

Pure python implementation of the gimp gbr brush format

<a name=".gimpformats.GimpGbrBrush.GimpGbrBrush"></a>
### GimpGbrBrush

```python
class GimpGbrBrush():
 |  GimpGbrBrush(filename=None)
```

Pure python implementation of the gimp gbr brush format

See:
	https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/gbr.txt

<a name=".gimpformats.GimpGbrBrush.GimpGbrBrush.load"></a>
#### load

```python
 | load(filename)
```

load a gimp file

**Arguments**:

- `filename`: can be a file name or a file-like object

<a name=".gimpformats.GimpGbrBrush.GimpGbrBrush.decode_"></a>
#### decode\_

```python
 | decode_(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.GimpGbrBrush.GimpGbrBrush.encode_"></a>
#### encode\_

```python
 | encode_()
```

encode this object to byte array

<a name=".gimpformats.GimpGbrBrush.GimpGbrBrush.size"></a>
#### size

```python
 | @property
 | size()
```

Get the size

<a name=".gimpformats.GimpGbrBrush.GimpGbrBrush.image"></a>
#### image

```python
 | @property
 | image()
```

get a final, compiled image

<a name=".gimpformats.GimpGbrBrush.GimpGbrBrush.save"></a>
#### save

```python
 | save(toFilename=None, toExtension=None)
```

save this gimp image to a file

<a name=".gimpformats.GimpGbrBrush.GimpGbrBrush.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.GimpGgrGradient"></a>
## gimpformats.GimpGgrGradient

Gimp color gradient

<a name=".gimpformats.GimpGgrGradient.GradientSegment"></a>
### GradientSegment

```python
class GradientSegment():
 |  GradientSegment()
```

Single segment within a gradient

<a name=".gimpformats.GimpGgrGradient.GradientSegment.getColor"></a>
#### getColor

```python
 | getColor(percent)
```

given a decimal percent (1.0 = 100%) retrieve
the appropriate color for this point in the gradient

<a name=".gimpformats.GimpGgrGradient.GradientSegment.decode_"></a>
#### decode\_

```python
 | decode_(data)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode

<a name=".gimpformats.GimpGgrGradient.GradientSegment.encode_"></a>
#### encode\_

```python
 | encode_()
```

encode this to a byte array

<a name=".gimpformats.GimpGgrGradient.GradientSegment.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.GimpGgrGradient.GimpGgrGradient"></a>
### GimpGgrGradient

```python
class GimpGgrGradient():
 |  GimpGgrGradient(filename=None)
```

Gimp color gradient

See:
	https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/ggr.txt

<a name=".gimpformats.GimpGgrGradient.GimpGgrGradient.load"></a>
#### load

```python
 | load(filename)
```

load a gimp file

**Arguments**:

- `filename`: can be a file name or a file-like object

<a name=".gimpformats.GimpGgrGradient.GimpGgrGradient.decode_"></a>
#### decode\_

```python
 | decode_(data)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.GimpGgrGradient.GimpGgrGradient.encode_"></a>
#### encode\_

```python
 | encode_()
```

encode this to a byte array

<a name=".gimpformats.GimpGgrGradient.GimpGgrGradient.save"></a>
#### save

```python
 | save(toFilename=None)
```

save this gimp image to a file

<a name=".gimpformats.GimpGgrGradient.GimpGgrGradient.getColor"></a>
#### getColor

```python
 | getColor(percent)
```

given a decimal percent (1.0 = 100%) retrieve
the appropriate color for this point in the gradient

<a name=".gimpformats.GimpGgrGradient.GimpGgrGradient.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.GimpGihBrushSet"></a>
## gimpformats.GimpGihBrushSet

Gimp Image Pipe Format

The gih format is use to store a series of brushes, and some extra info
for how to use them.

<a name=".gimpformats.GimpGihBrushSet.GimpGihBrushSet"></a>
### GimpGihBrushSet

```python
class GimpGihBrushSet():
 |  GimpGihBrushSet(filename=None)
```

Gimp Image Pipe Format

The gih format is use to store a series of brushes, and some extra info
for how to use them.

See:
	https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/gih.txt

<a name=".gimpformats.GimpGihBrushSet.GimpGihBrushSet.load"></a>
#### load

```python
 | load(filename)
```

load a gimp file

**Arguments**:

- `filename`: can be a file name or a file-like object

<a name=".gimpformats.GimpGihBrushSet.GimpGihBrushSet.decode_"></a>
#### decode\_

```python
 | decode_(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.GimpGihBrushSet.GimpGihBrushSet.encode_"></a>
#### encode\_

```python
 | encode_()
```

encode this object to a byte array

<a name=".gimpformats.GimpGihBrushSet.GimpGihBrushSet.save"></a>
#### save

```python
 | save(toFilename=None)
```

save this gimp image to a file

<a name=".gimpformats.GimpGihBrushSet.GimpGihBrushSet.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.GimpGpbBrush"></a>
## gimpformats.GimpGpbBrush

Pure python implementation of the OLD gimp gpb brush format

<a name=".gimpformats.GimpGpbBrush.GimpGpbBrush"></a>
### GimpGpbBrush

```python
class GimpGpbBrush():
 |  GimpGpbBrush(filename)
```

Pure python implementation of the OLD gimp gpb brush format

See:
	https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/vbr.txt

<a name=".gimpformats.GimpGpbBrush.GimpGpbBrush.load"></a>
#### load

```python
 | load(filename)
```

load a gimp file

**Arguments**:

- `filename`: can be a file name or a file-like object

<a name=".gimpformats.GimpGpbBrush.GimpGpbBrush.decode_"></a>
#### decode\_

```python
 | decode_(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.GimpGpbBrush.GimpGpbBrush.encode_"></a>
#### encode\_

```python
 | encode_()
```

encode this object to a byte array

<a name=".gimpformats.GimpGpbBrush.GimpGpbBrush.save"></a>
#### save

```python
 | save(toFilename=None)
```

save this gimp image to a file

<a name=".gimpformats.GimpGpbBrush.GimpGpbBrush.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.GimpGplPalette"></a>
## gimpformats.GimpGplPalette

Pure python implementation of the gimp gpl palette format

<a name=".gimpformats.GimpGplPalette.GimpGplPalette"></a>
### GimpGplPalette

```python
class GimpGplPalette():
 |  GimpGplPalette(filename=None)
```

Pure python implementation of the gimp gpl palette format

<a name=".gimpformats.GimpGplPalette.GimpGplPalette.load"></a>
#### load

```python
 | load(filename)
```

load a gimp file

**Arguments**:

- `filename`: can be a file name or a file-like object

<a name=".gimpformats.GimpGplPalette.GimpGplPalette.decode_"></a>
#### decode\_

```python
 | decode_(data)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode

<a name=".gimpformats.GimpGplPalette.GimpGplPalette.encode_"></a>
#### encode\_

```python
 | encode_()
```

encode to a raw data stream

<a name=".gimpformats.GimpGplPalette.GimpGplPalette.save"></a>
#### save

```python
 | save(toFilename=None, toExtension=None)
```

save this gimp image to a file

<a name=".gimpformats.GimpGplPalette.GimpGplPalette.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.GimpGplPalette.GimpGplPalette.__eq__"></a>
#### \_\_eq\_\_

```python
 | __eq__(other)
```

perform a comparison

<a name=".gimpformats.GimpGtpToolPreset"></a>
## gimpformats.GimpGtpToolPreset

Pure python implementation of the gimp gtp tool preset format

<a name=".gimpformats.GimpGtpToolPreset.ParenFileValue"></a>
### ParenFileValue

```python
class ParenFileValue():
 |  ParenFileValue(name=None, value="", children=None)
```

A parentheses-based file format
(possibly "scheme" language?)

<a name=".gimpformats.GimpGtpToolPreset.ParenFileValue.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__()
```

Get a textual representation of this object

<a name=".gimpformats.GimpGtpToolPreset.parenFileDecode"></a>
#### parenFileDecode

```python
parenFileDecode(data)
```

Decode a parentheses-based file format
(possibly "scheme" language?)

<a name=".gimpformats.GimpGtpToolPreset.walkTree"></a>
#### walkTree

```python
walkTree(items)
```

walk the tree

<a name=".gimpformats.GimpGtpToolPreset.parenFileEncode"></a>
#### parenFileEncode

```python
parenFileEncode(values)
```

encode a values tree to a buffer

<a name=".gimpformats.GimpGtpToolPreset.GimpGtpToolPreset"></a>
### GimpGtpToolPreset

```python
class GimpGtpToolPreset():
 |  GimpGtpToolPreset(filename=None)
```

Pure python implementation of the gimp gtp tool preset format

<a name=".gimpformats.GimpGtpToolPreset.GimpGtpToolPreset.load"></a>
#### load

```python
 | load(filename)
```

load a gimp file

**Arguments**:

- `filename`: can be a file name or a file-like object

<a name=".gimpformats.GimpGtpToolPreset.GimpGtpToolPreset.decode_"></a>
#### decode\_

```python
 | decode_(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode

<a name=".gimpformats.GimpGtpToolPreset.GimpGtpToolPreset.encode_"></a>
#### encode\_

```python
 | encode_()
```

encode to a byte array

<a name=".gimpformats.GimpGtpToolPreset.GimpGtpToolPreset.save"></a>
#### save

```python
 | save(toFilename=None, toExtension=None)
```

save this gimp tool preset to a file

<a name=".gimpformats.GimpGtpToolPreset.GimpGtpToolPreset.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.GimpImageHierarch"></a>
## gimpformats.GimpImageHierarch

Gets packed pixels from a gimp image

NOTE: This was originally designed to be a hierarchy, like
	an image pyramid, through in practice they only use the
	top level of the pyramid (64x64) and ignore the rest.

<a name=".gimpformats.GimpImageHierarch.GimpImageHierarchy"></a>
### GimpImageHierarchy

```python
class GimpImageHierarchy(GimpIOBase):
 |  GimpImageHierarchy(parent, image=None)
```

Gets packed pixels from a gimp image

NOTE: This was originally designed to be a hierarchy, like
	an image pyramid, through in practice they only use the
	top level of the pyramid (64x64) and ignore the rest.

<a name=".gimpformats.GimpImageHierarch.GimpImageHierarchy.decode_"></a>
#### decode\_

```python
 | decode_(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.GimpImageHierarch.GimpImageHierarchy.encode_"></a>
#### encode\_

```python
 | encode_()
```

encode this object to a byte buffer

<a name=".gimpformats.GimpImageHierarch.GimpImageHierarchy.levels"></a>
#### levels

```python
 | @property
 | levels()
```

Get the levels within this hierarchy

Presently hierarchy is not really used by gimp,
so this returns an array of one item

<a name=".gimpformats.GimpImageHierarch.GimpImageHierarchy.image"></a>
#### image

```python
 | @image.setter
 | image(image)
```

set the image

<a name=".gimpformats.GimpImageHierarch.GimpImageHierarchy.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.GimpImageLevel"></a>
## gimpformats.GimpImageLevel

Gets packed pixels from a gimp image

This represents a single level in an imageHierarchy

<a name=".gimpformats.GimpImageLevel.GimpImageLevel"></a>
### GimpImageLevel

```python
class GimpImageLevel(GimpIOBase):
 |  GimpImageLevel(parent)
```

Gets packed pixels from a gimp image

This represents a single level in an imageHierarchy

<a name=".gimpformats.GimpImageLevel.GimpImageLevel.decode_"></a>
#### decode\_

```python
 | decode_(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.GimpImageLevel.GimpImageLevel.encode_"></a>
#### encode\_

```python
 | encode_()
```

encode this object to a byte buffer

<a name=".gimpformats.GimpImageLevel.GimpImageLevel.bpp"></a>
#### bpp

```python
 | @property
 | bpp()
```

get bpp

<a name=".gimpformats.GimpImageLevel.GimpImageLevel.mode"></a>
#### mode

```python
 | @property
 | mode()
```

get mode

<a name=".gimpformats.GimpImageLevel.GimpImageLevel.tiles"></a>
#### tiles

```python
 | @property
 | tiles()
```

get tiles

<a name=".gimpformats.GimpImageLevel.GimpImageLevel.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.GimpIOBase"></a>
## gimpformats.GimpIOBase

A specialized binary file base for Gimp files

<a name=".gimpformats.GimpIOBase.GimpIOBase"></a>
### GimpIOBase

```python
class GimpIOBase():
 |  GimpIOBase(parent)
```

A specialized binary file base for Gimp files

<a name=".gimpformats.GimpIOBase.GimpIOBase.getBlendMode"></a>
#### getBlendMode

```python
 | getBlendMode()
```

return the blend mode as a string

<a name=".gimpformats.GimpIOBase.GimpIOBase.getCompression"></a>
#### getCompression

```python
 | getCompression()
```

return the compression as a string

<a name=".gimpformats.GimpIOBase.GimpIOBase.getUnits"></a>
#### getUnits

```python
 | getUnits()
```

return the units as a string

<a name=".gimpformats.GimpIOBase.GimpIOBase.getTagColours"></a>
#### getTagColours

```python
 | getTagColours()
```

return the tag colours as a string

<a name=".gimpformats.GimpIOBase.GimpIOBase.getCompositeModes"></a>
#### getCompositeModes

```python
 | getCompositeModes()
```

return the composite mode as a string

<a name=".gimpformats.GimpIOBase.GimpIOBase.getCompositeSpaces"></a>
#### getCompositeSpaces

```python
 | getCompositeSpaces()
```

return the composite spaces as a string

<a name=".gimpformats.GimpIOBase.GimpIOBase._POINTER_SIZE_"></a>
#### \_POINTER\_SIZE\_

```python
 | @property
 | _POINTER_SIZE_()
```

Determine the size of the "pointer" datatype
based on the document version

NOTE: prior to version 11, it was 32-bit,
	since then it is 64-bit, thus supporting
	larger image files

<a name=".gimpformats.GimpIOBase.GimpIOBase.doc"></a>
#### doc

```python
 | @property
 | doc()
```

Get the main document object

<a name=".gimpformats.GimpIOBase.GimpIOBase.root"></a>
#### root

```python
 | @property
 | root()
```

Get the root of the file object tree
(Which is the same as self.doc)

<a name=".gimpformats.GimpIOBase.GimpIOBase.tattoo"></a>
#### tattoo

```python
 | @tattoo.setter
 | tattoo(tattoo)
```

This is the gimp nomenclature for the item's unique id

<a name=".gimpformats.GimpIOBase.GimpIOBase._parasitesDecode_"></a>
#### \_parasitesDecode\_

```python
 | _parasitesDecode_(data)
```

decode list of parasites

<a name=".gimpformats.GimpIOBase.GimpIOBase._parasitesEncode_"></a>
#### \_parasitesEncode\_

```python
 | _parasitesEncode_()
```

encode list of parasites

<a name=".gimpformats.GimpIOBase.GimpIOBase._guidelinesDecode_"></a>
#### \_guidelinesDecode\_

```python
 | _guidelinesDecode_(data)
```

decode guidelines

<a name=".gimpformats.GimpIOBase.GimpIOBase._itemPathDecode_"></a>
#### \_itemPathDecode\_

```python
 | _itemPathDecode_(data)
```

decode item path

<a name=".gimpformats.GimpIOBase.GimpIOBase._vectorsDecode_"></a>
#### \_vectorsDecode\_

```python
 | _vectorsDecode_(data)
```

decode vectors

<a name=".gimpformats.GimpIOBase.GimpIOBase.activeVector"></a>
#### activeVector

```python
 | @property
 | activeVector()
```

get the vector that is currently active

<a name=".gimpformats.GimpIOBase.GimpIOBase.expanded"></a>
#### expanded

```python
 | @expanded.setter
 | expanded(expanded)
```

is the group layer expanded

<a name=".gimpformats.GimpIOBase.GimpIOBase._colormapDecode_"></a>
#### \_colormapDecode\_

```python
 | _colormapDecode_(data, index=None)
```

**Arguments**:

- `data`: can be bytes or an IO object

decode colormap/palette

<a name=".gimpformats.GimpIOBase.GimpIOBase._userUnitsDecode_"></a>
#### \_userUnitsDecode\_

```python
 | _userUnitsDecode_(data)
```

decode a set of user-defined measurement units

<a name=".gimpformats.GimpIOBase.GimpIOBase._samplePointsDecode_"></a>
#### \_samplePointsDecode\_

```python
 | _samplePointsDecode_(data)
```

decode a series of points

<a name=".gimpformats.GimpIOBase.GimpIOBase._propertyDecode_"></a>
#### \_propertyDecode\_

```python
 | _propertyDecode_(propertyType, data)
```

decode a single property

Many properties are in the form
propertyType: one of PROP_
lengthOfData: 4
data: varies but is often io.32 or io.bool

<a name=".gimpformats.GimpIOBase.GimpIOBase._propertyEncode_"></a>
#### \_propertyEncode\_

```python
 | _propertyEncode_(propertyType)
```

encode a single property

Many properties are in the form
propertyType: one of PROP_
lengthOfData: 4
data: varies but is often io.32 or io.bool

If the property is the same as the default, or not specified, returns empty array

<a name=".gimpformats.GimpIOBase.GimpIOBase._propertiesDecode_"></a>
#### \_propertiesDecode\_

```python
 | _propertiesDecode_(io)
```

decode a list of properties

<a name=".gimpformats.GimpIOBase.GimpIOBase._propertiesEncode_"></a>
#### \_propertiesEncode\_

```python
 | _propertiesEncode_()
```

encode a list of properties

<a name=".gimpformats.GimpIOBase.GimpIOBase.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.GimpIOBase.GimpUserUnits"></a>
### GimpUserUnits

```python
class GimpUserUnits():
 |  GimpUserUnits()
```

user-defined measurement units

<a name=".gimpformats.GimpIOBase.GimpUserUnits.decode_"></a>
#### decode\_

```python
 | decode_(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.GimpIOBase.GimpUserUnits.encode_"></a>
#### encode\_

```python
 | encode_()
```

convert this object to raw bytes

<a name=".gimpformats.GimpIOBase.GimpUserUnits.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.GimpLayer"></a>
## gimpformats.GimpLayer

Represents a single layer in a gimp image

<a name=".gimpformats.GimpLayer.GimpLayer"></a>
### GimpLayer

```python
class GimpLayer(GimpIOBase):
 |  GimpLayer(parent, name=None, image=None)
```

Represents a single layer in a gimp image

<a name=".gimpformats.GimpLayer.GimpLayer.decode_"></a>
#### decode\_

```python
 | decode_(data, index=0)
```

decode a byte buffer

Steps:
Create a new IO buffer (array of binary values)
Grab attributes as outlined in the spec
List of properties
Get the image hierarchy and mask pointers
Return the offset

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.GimpLayer.GimpLayer.encode_"></a>
#### encode\_

```python
 | encode_()
```

encode to byte array

Steps:
Create a new IO buffer (array of binary values)
Set attributes as outlined in the spec
List of properties
Set the image hierarchy and mask pointers
Return the data

<a name=".gimpformats.GimpLayer.GimpLayer.mask"></a>
#### mask

```python
 | @property
 | mask()
```

Get the layer mask

<a name=".gimpformats.GimpLayer.GimpLayer.image"></a>
#### image

```python
 | @image.setter
 | image(image)
```

set the layer image

NOTE: resets layer width, height, and colorMode

<a name=".gimpformats.GimpLayer.GimpLayer.imageHierarchy"></a>
#### imageHierarchy

```python
 | @property
 | imageHierarchy()
```

Get the image hierarchy objects

This is mainly needed for deciphering image, and therefore,
of little use to you, the user.

NOTE: can return None if it has been fully read into an image

<a name=".gimpformats.GimpLayer.GimpLayer.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.GimpParasites"></a>
## gimpformats.GimpParasites

Parasites are arbitrary (meta)data strings that can be attached to a document tree item

They are used to store things like last-used plugin settings, gamma adjuetments, etc.

Format of known parasites:
	https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/parasites.txt

<a name=".gimpformats.GimpParasites.GimpParasite"></a>
### GimpParasite

```python
class GimpParasite():
 |  GimpParasite()
```

Parasites are arbitrary (meta)data strings that can be attached to a document tree item

They are used to store things like last-used plugin settings, gamma adjuetments, etc.

Format of known parasites:
	https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/parasites.txt

<a name=".gimpformats.GimpParasites.GimpParasite.decode_"></a>
#### decode\_

```python
 | decode_(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.GimpParasites.GimpParasite.encode_"></a>
#### encode\_

```python
 | encode_()
```

encode a byte buffer

**Arguments**:

- `data`: data buffer to encode
- `index`: index within the buffer to start at

<a name=".gimpformats.GimpParasites.GimpParasite.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.GimpPatPattern"></a>
## gimpformats.GimpPatPattern

Pure python implementation of a gimp pattern file

<a name=".gimpformats.GimpPatPattern.GimpPatPattern"></a>
### GimpPatPattern

```python
class GimpPatPattern():
 |  GimpPatPattern(filename=None)
```

Pure python implementation of a gimp pattern file

See:
	https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/pat.txt

<a name=".gimpformats.GimpPatPattern.GimpPatPattern.load"></a>
#### load

```python
 | load(filename)
```

load a gimp file

**Arguments**:

- `filename`: can be a file name or a file-like object

<a name=".gimpformats.GimpPatPattern.GimpPatPattern.decode_"></a>
#### decode\_

```python
 | decode_(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.GimpPatPattern.GimpPatPattern.encode_"></a>
#### encode\_

```python
 | encode_()
```

encode to a byte buffer

<a name=".gimpformats.GimpPatPattern.GimpPatPattern.size"></a>
#### size

```python
 | @property
 | size()
```

the size of the pattern

<a name=".gimpformats.GimpPatPattern.GimpPatPattern.save"></a>
#### save

```python
 | save(toFilename=None, toExtension=None)
```

save this gimp image to a file

<a name=".gimpformats.GimpPatPattern.GimpPatPattern.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.GimpPrecision"></a>
## gimpformats.GimpPrecision

Since the precision code is so unusual, I decided to create a class
to parse it.

<a name=".gimpformats.GimpPrecision.Precision"></a>
### Precision

```python
class Precision():
 |  Precision()
```

Since the precision code is so unusual, I decided to create a class
to parse it.

<a name=".gimpformats.GimpPrecision.Precision.decode_"></a>
#### decode\_

```python
 | decode_(gimpVersion, io)
```

decode the precision code from the file

<a name=".gimpformats.GimpPrecision.Precision.encode_"></a>
#### encode\_

```python
 | encode_(gimpVersion, io)
```

encode this to the file

NOTE: will not mess with development versions 5 or 6

<a name=".gimpformats.GimpPrecision.Precision.requiredGimpVersion"></a>
#### requiredGimpVersion

```python
 | requiredGimpVersion()
```

return the lowest gimp version that supports this precision

<a name=".gimpformats.GimpVbrBrush"></a>
## gimpformats.GimpVbrBrush

Pure python implementation of the gimp vbr brush format

<a name=".gimpformats.GimpVbrBrush.GimpVbrBrush"></a>
### GimpVbrBrush

```python
class GimpVbrBrush():
 |  GimpVbrBrush(filename=None)
```

Pure python implementation of the gimp vbr brush format

See:
	https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/vbr.txt

<a name=".gimpformats.GimpVbrBrush.GimpVbrBrush.load"></a>
#### load

```python
 | load(filename)
```

load a gimp file

**Arguments**:

- `filename`: can be a file name or a file-like object

<a name=".gimpformats.GimpVbrBrush.GimpVbrBrush.image"></a>
#### image

```python
 | @property
 | image()
```

this parametric brush converted to a useable PIL image

<a name=".gimpformats.GimpVbrBrush.GimpVbrBrush.decode_"></a>
#### decode\_

```python
 | decode_(data)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode

<a name=".gimpformats.GimpVbrBrush.GimpVbrBrush.encode_"></a>
#### encode\_

```python
 | encode_()
```

encode to a raw data stream

<a name=".gimpformats.GimpVbrBrush.GimpVbrBrush.save"></a>
#### save

```python
 | save(toFilename=None, toExtension=None)
```

save this gimp image to a file

<a name=".gimpformats.GimpVbrBrush.GimpVbrBrush.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.GimpVbrBrush.GimpVbrBrush.__eq__"></a>
#### \_\_eq\_\_

```python
 | __eq__(other)
```

perform a comparison

<a name=".gimpformats.GimpVectors"></a>
## gimpformats.GimpVectors

Stuff related to vectors/paths within a gimp document

<a name=".gimpformats.GimpVectors.GimpVector"></a>
### GimpVector

```python
class GimpVector()
```

A gimp brush stroke vector

<a name=".gimpformats.GimpVectors.GimpVector.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(parent)
```

GimpIOBase.__init__(self, parent)

<a name=".gimpformats.GimpVectors.GimpVector.decode_"></a>
#### decode\_

```python
 | decode_(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.GimpVectors.GimpVector.encode_"></a>
#### encode\_

```python
 | encode_()
```

encode to binary data

<a name=".gimpformats.GimpVectors.GimpVector.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.GimpVectors.GimpStroke"></a>
### GimpStroke

```python
class GimpStroke()
```

A single stroke within a vector

<a name=".gimpformats.GimpVectors.GimpStroke.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(parent)
```

GimpIOBase.__init__(self, parent)

<a name=".gimpformats.GimpVectors.GimpStroke.decode_"></a>
#### decode\_

```python
 | decode_(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.GimpVectors.GimpStroke.encode_"></a>
#### encode\_

```python
 | encode_()
```

encode to binary data

<a name=".gimpformats.GimpVectors.GimpStroke.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.GimpVectors.GimpPoint"></a>
### GimpPoint

```python
class GimpPoint()
```

A single point within a stroke

<a name=".gimpformats.GimpVectors.GimpPoint.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(parent)
```

GimpIOBase.__init__(self, parent)

<a name=".gimpformats.GimpVectors.GimpPoint.decode_"></a>
#### decode\_

```python
 | decode_(data, index=0, numFloatsPerPoint=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at
- `numFloatsPerPoint`: required so we know
how many different brush dynamic measurements are
inside each point

<a name=".gimpformats.GimpVectors.GimpPoint.encode_"></a>
#### encode\_

```python
 | encode_()
```

encode to binary data

<a name=".gimpformats.GimpVectors.GimpPoint.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.gimpXcfDocument"></a>
## gimpformats.gimpXcfDocument

Pure python implementation of the gimp xcf file format

Currently supports:
	Loading xcf files
	Getting image hierarchy and info
	Getting image for each layer (PIL image)
Currently not supporting:
	Saving
	Programatically alter documents (add layer, etc)
	Rendering a final, compositied image

<a name=".gimpformats.gimpXcfDocument.GimpDocument"></a>
### GimpDocument

```python
class GimpDocument(GimpIOBase):
 |  GimpDocument(fileName=None)
```

Pure python implementation of the gimp file format

Has a series of attributes including the following:
self._layers = None
self._layerPtr = []
self._channels = []
self._channelPtr = []
self.version = None
self.width = 0
self.height = 0
self.baseColorMode = 0
self.precision = None # Precision object
self._data = None

See:
	https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/xcf.txt

<a name=".gimpformats.gimpXcfDocument.GimpDocument.load"></a>
#### load

```python
 | load(fileName)
```

Load a gimp xcf and decode the file. See decode for more on this
process

**Arguments**:

- `filename`: can be a file name or a file-like object

<a name=".gimpformats.gimpXcfDocument.GimpDocument.decode_"></a>
#### decode\_

```python
 | decode_(data, index=0)
```

decode a byte buffer

Steps:
Create a new IO buffer (array of binary values)
Check that the file is a valid gimp xcf
Grab the file version
Grab other attributes as outlined in the spec
Get precision data using the class and io buffer
List of properties
Get the layers and add the pointers to them
Get the channels and add the pointers to them
Return the offset

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.gimpXcfDocument.GimpDocument.encode_"></a>
#### encode\_

```python
 | encode_()
```

encode to a byte array

Steps:
Create a new IO buffer (array of binary values)
The file is a valid gimp xcf
Set the file version
Set other attributes as outlined in the spec
Set precision data using the class and io buffer
List of properties
Set the layers and add the pointers to them
Set the channels and add the pointers to them
Return the data

<a name=".gimpformats.gimpXcfDocument.GimpDocument.layers"></a>
#### layers

```python
 | @property
 | layers()
```

Decode the image's layers if necessary

TODO: need to do the same thing with self.Channels

<a name=".gimpformats.gimpXcfDocument.GimpDocument.getLayer"></a>
#### getLayer

```python
 | getLayer(index)
```

return a given layer

<a name=".gimpformats.gimpXcfDocument.GimpDocument.setLayer"></a>
#### setLayer

```python
 | setLayer(_index, _l)
```

assign to a given layer

<a name=".gimpformats.gimpXcfDocument.GimpDocument.newLayer"></a>
#### newLayer

```python
 | newLayer(name, image, index=-1)
```

create a new layer based on a PIL image

**Arguments**:

- `name`: a name for the new layer
- `index`: where to insert the new layer (default=top)

**Returns**:

newly created GimpLayer object

<a name=".gimpformats.gimpXcfDocument.GimpDocument.newLayerFromClipboard"></a>
#### newLayerFromClipboard

```python
 | newLayerFromClipboard(name='pasted', index=-1)
```

Create a new image from the system clipboard.

**Arguments**:

- `name`: a name for the new layer (default="pasted")
- `index`: where to insert the new layer (default=top)

**Returns**:

newly created GimpLayer object

NOTE: requires pillow PIL implementation
NOTE: only works on OSX and Windows

<a name=".gimpformats.gimpXcfDocument.GimpDocument.addLayer"></a>
#### addLayer

```python
 | addLayer(l)
```

append a layer object to the document

**Arguments**:

- `layer`: the new layer to append

<a name=".gimpformats.gimpXcfDocument.GimpDocument.appendLayer"></a>
#### appendLayer

```python
 | appendLayer(l)
```

append a layer object to the document

**Arguments**:

- `layer`: the new layer to append

<a name=".gimpformats.gimpXcfDocument.GimpDocument.insertLayer"></a>
#### insertLayer

```python
 | insertLayer(l, index=-1)
```

insert a layer object at a specific position

**Arguments**:

- `layer`: the new layer to insert
- `index`: where to insert the new layer (default=top)

<a name=".gimpformats.gimpXcfDocument.GimpDocument.deleteLayer"></a>
#### deleteLayer

```python
 | deleteLayer(index)
```

delete a layer

<a name=".gimpformats.gimpXcfDocument.GimpDocument.image"></a>
#### image

```python
 | @property
 | image()
```

get a final, compiled image

<a name=".gimpformats.gimpXcfDocument.GimpDocument.save"></a>
#### save

```python
 | save(toFilename=None)
```

save this gimp image to a file

<a name=".gimpformats.gimpXcfDocument.GimpDocument.saveNew"></a>
#### saveNew

```python
 | saveNew(toFilename=None)
```

save a new gimp image to a file

<a name=".gimpformats.gimpXcfDocument.GimpDocument.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.gimpXcfDocument.blendModeLookup"></a>
#### blendModeLookup

```python
blendModeLookup(blendmode, blendLookup, default=BlendType.NORMAL)
```

Get the blendmode from a lookup table

<a name=".gimpformats.gimpXcfDocument.rasterImageOffset"></a>
#### rasterImageOffset

```python
rasterImageOffset(image, size, offsets=(0, 0))
```

Rasterise an image with offset to a given size

<a name=".gimpformats.gimpXcfDocument.flattenLayerOrGroup"></a>
#### flattenLayerOrGroup

```python
flattenLayerOrGroup(layerOrGroup, imageDimensions, flattenedSoFar=None, ignoreHidden=True)
```

Flatten a layer or group on to an image of what has already been
flattened

**Arguments**:

- `layerOrGroup` _Layer|Group_ - A layer or a group of layers
  imageDimensions ((int, int)): size of the image
- `flattenedSoFar` _PIL.Image, optional_ - the image of what has already
  been flattened. Defaults to None.
- `ignoreHidden` _bool, optional_ - ignore layers that are hidden. Defaults
  to True.

**Returns**:

- `PIL.Image` - Flattened image

<a name=".gimpformats.gimpXcfDocument.flattenAll"></a>
#### flattenAll

```python
flattenAll(layers, imageDimensions, ignoreHidden=True)
```

Flatten a list of layers and groups

Note the bottom layer is at the end of the list

**Arguments**:

- `layers` _[Layer|Group]_ - A list of layers and groups
  imageDimensions ((int, int)): size of the image
  been flattened. Defaults to None.
- `ignoreHidden` _bool, optional_ - ignore layers that are hidden. Defaults
  to True.

**Returns**:

- `PIL.Image` - Flattened image

<a name=".gimpformats.gimpXcfDocument.showLayer"></a>
#### showLayer

```python
showLayer(image, l)
```

show a layer

<a name=".gimpformats.gimpXcfDocument.saveLayer"></a>
#### saveLayer

```python
saveLayer(gimpDoc, l, fileName)
```

save a layer

<a name=".make"></a>
## make

Makefile for python. Run one of the following subcommands:

install: Poetry install
build: Building docs, requirements.txt, setup.py, poetry build

