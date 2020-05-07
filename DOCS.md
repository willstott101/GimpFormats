<a name=".gimpformats"></a>
## gimpformats

gimpformats

Forked from https://github.com/TheHeadlessSourceMan/gimpFormats

A pure python implementation of the GIMP XCF image format.

Use this to interact with GIMP image formats

<a name=".gimpformats.BinaryIO"></a>
## gimpformats.BinaryIO

Base binary I/O helper.

Does boilerplate things like reading the next uint32 from the document

<a name=".gimpformats.BinaryIO.IO"></a>
### IO

```python
class IO()
```

Class to handle i/o to a byte buffer or file-like object

<a name=".gimpformats.BinaryIO.IO.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(data=None, idx=0, littleEndian=False, boolSize=8, stringEncoding='U')
```

**Arguments**:

- `data`: can be a data buffer or a file-like object
- `idx`: start reading/writing the data at the given index
- `littleEndian`: whether the default is big-endian or little-endian
- `boolSize`: how many default bits to use for a bool (8,16,32,or 64)
- `stringEncoding`: default string encoding A=Ascii, U=UTF-8, W-Unicode wide

<a name=".gimpformats.BinaryIO.IO.data"></a>
#### data

```python
 | @data.setter
 | data(data)
```

set data

<a name=".gimpformats.BinaryIO.IO.beginContext"></a>
#### beginContext

```python
 | beginContext(newIndex)
```

Start a new context where the index can be changed all you want,
and when endContext() is called, it will be restored to the current position

<a name=".gimpformats.BinaryIO.IO.endContext"></a>
#### endContext

```python
 | endContext()
```

Restore the index to the previous location where it was when beginContext() was called

<a name=".gimpformats.BinaryIO.IO.bool"></a>
#### bool

```python
 | @bool.setter
 | bool(ioBool)
```

set bool

<a name=".gimpformats.BinaryIO.IO.bool8"></a>
#### bool8

```python
 | @bool8.setter
 | bool8(ioBool)
```

set a bool8

<a name=".gimpformats.BinaryIO.IO.bool16"></a>
#### bool16

```python
 | @bool16.setter
 | bool16(ioBool)
```

set bool16

<a name=".gimpformats.BinaryIO.IO.bool32"></a>
#### bool32

```python
 | @bool32.setter
 | bool32(ioBool)
```

set bool32

<a name=".gimpformats.BinaryIO.IO.bool64"></a>
#### bool64

```python
 | @bool64.setter
 | bool64(ioBool)
```

set bool64

<a name=".gimpformats.BinaryIO.IO.byte"></a>
#### byte

```python
 | @byte.setter
 | byte(byte)
```

set byte

<a name=".gimpformats.BinaryIO.IO.unsignedByte"></a>
#### unsignedByte

```python
 | @unsignedByte.setter
 | unsignedByte(byte)
```

set unsigned byte

<a name=".gimpformats.BinaryIO.IO.word"></a>
#### word

```python
 | @word.setter
 | word(word)
```

set a word

<a name=".gimpformats.BinaryIO.IO.unsignedWord"></a>
#### unsignedWord

```python
 | @unsignedWord.setter
 | unsignedWord(unsignedWord)
```

set an unsigned word

<a name=".gimpformats.BinaryIO.IO.dword"></a>
#### dword

```python
 | @dword.setter
 | dword(dword)
```

set a dword

<a name=".gimpformats.BinaryIO.IO.unsignedDword"></a>
#### unsignedDword

```python
 | @unsignedDword.setter
 | unsignedDword(unsignedDword)
```

set an unsigned dword

<a name=".gimpformats.BinaryIO.IO.i8"></a>
#### i8

```python
 | @i8.setter
 | i8(i8)
```

set an int8

<a name=".gimpformats.BinaryIO.IO.u8"></a>
#### u8

```python
 | @u8.setter
 | u8(u8)
```

set an unsigned int

<a name=".gimpformats.BinaryIO.IO.i16"></a>
#### i16

```python
 | @i16.setter
 | i16(i16)
```

set an int16

<a name=".gimpformats.BinaryIO.IO.u16"></a>
#### u16

```python
 | @u16.setter
 | u16(u16)
```

set an unint16

<a name=".gimpformats.BinaryIO.IO.i32"></a>
#### i32

```python
 | @i32.setter
 | i32(i32)
```

set an int32

<a name=".gimpformats.BinaryIO.IO.u32"></a>
#### u32

```python
 | @u32.setter
 | u32(u32)
```

set a unint32

<a name=".gimpformats.BinaryIO.IO.i64"></a>
#### i64

```python
 | @i64.setter
 | i64(i64)
```

set an int64

<a name=".gimpformats.BinaryIO.IO.u64"></a>
#### u64

```python
 | @u64.setter
 | u64(u64)
```

set a uint64

<a name=".gimpformats.BinaryIO.IO.float32"></a>
#### float32

```python
 | @float32.setter
 | float32(float32)
```

set a float32

<a name=".gimpformats.BinaryIO.IO.float64"></a>
#### float64

```python
 | @float64.setter
 | float64(float64)
```

set a float64

<a name=".gimpformats.BinaryIO.IO.u8be"></a>
#### u8be

```python
 | @u8be.setter
 | u8be(u8be)
```

set the uint8

<a name=".gimpformats.BinaryIO.IO.u8le"></a>
#### u8le

```python
 | @u8le.setter
 | u8le(u8le)
```

set the uint8

<a name=".gimpformats.BinaryIO.IO.i8le"></a>
#### i8le

```python
 | @i8le.setter
 | i8le(i8le)
```

set the int8

<a name=".gimpformats.BinaryIO.IO.i8be"></a>
#### i8be

```python
 | @i8be.setter
 | i8be(i8be)
```

set the int8

<a name=".gimpformats.BinaryIO.IO.u16be"></a>
#### u16be

```python
 | @u16be.setter
 | u16be(u16be)
```

set the uint16

<a name=".gimpformats.BinaryIO.IO.u16le"></a>
#### u16le

```python
 | @u16le.setter
 | u16le(u16le)
```

set the uint16

<a name=".gimpformats.BinaryIO.IO.i16le"></a>
#### i16le

```python
 | @i16le.setter
 | i16le(i16le)
```

set the int16

<a name=".gimpformats.BinaryIO.IO.i16be"></a>
#### i16be

```python
 | @i16be.setter
 | i16be(i16be)
```

set the int16

<a name=".gimpformats.BinaryIO.IO.u32be"></a>
#### u32be

```python
 | @u32be.setter
 | u32be(u32be)
```

set the uint32

<a name=".gimpformats.BinaryIO.IO.u32le"></a>
#### u32le

```python
 | @u32le.setter
 | u32le(u32le)
```

set the uint32

<a name=".gimpformats.BinaryIO.IO.i32le"></a>
#### i32le

```python
 | @i32le.setter
 | i32le(i32le)
```

set the int32

<a name=".gimpformats.BinaryIO.IO.i32be"></a>
#### i32be

```python
 | @i32be.setter
 | i32be(i32be)
```

set the int32

<a name=".gimpformats.BinaryIO.IO.u64be"></a>
#### u64be

```python
 | @u64be.setter
 | u64be(u64be)
```

set the uint64

<a name=".gimpformats.BinaryIO.IO.u64le"></a>
#### u64le

```python
 | @u64le.setter
 | u64le(u64le)
```

set the uint64

<a name=".gimpformats.BinaryIO.IO.i64le"></a>
#### i64le

```python
 | @i64le.setter
 | i64le(i64le)
```

set the int64

<a name=".gimpformats.BinaryIO.IO.i64be"></a>
#### i64be

```python
 | @i64be.setter
 | i64be(i64be)
```

set the int64

<a name=".gimpformats.BinaryIO.IO.float"></a>
#### float

```python
 | @float.setter
 | float(f)
```

set a float

<a name=".gimpformats.BinaryIO.IO.double"></a>
#### double

```python
 | @double.setter
 | double(f)
```

set a double

<a name=".gimpformats.BinaryIO.IO.float32be"></a>
#### float32be

```python
 | @float32be.setter
 | float32be(float32be)
```

set a 32 bit float

<a name=".gimpformats.BinaryIO.IO.float32le"></a>
#### float32le

```python
 | @float32le.setter
 | float32le(float32le)
```

set a 32 bit float

<a name=".gimpformats.BinaryIO.IO.float64be"></a>
#### float64be

```python
 | @float64be.setter
 | float64be(float64be)
```

set a 64 bit float

<a name=".gimpformats.BinaryIO.IO.float64le"></a>
#### float64le

```python
 | @float64le.setter
 | float64le(float64le)
```

set a 64 bit float

<a name=".gimpformats.BinaryIO.IO.getBytes"></a>
#### getBytes

```python
 | getBytes(nbytes)
```

grab some raw bytes and advance the index

<a name=".gimpformats.BinaryIO.IO.addBytes"></a>
#### addBytes

```python
 | addBytes(ioBytes)
```

add some raw bytes and advance the index

alias for setBytes()

**Arguments**:

- `bytes`: can be a string, bytearray, or another IO object

<a name=".gimpformats.BinaryIO.IO.setBytes"></a>
#### setBytes

```python
 | setBytes(ioBytes)
```

add some raw bytes and advance the index

alias for addBytes()

**Arguments**:

- `ioBytes`: can be a string, bytearray, or another IO object

<a name=".gimpformats.BinaryIO.IO.sz754"></a>
#### sz754

```python
 | @sz754.setter
 | sz754(sz754)
```

set sz754

<a name=".gimpformats.BinaryIO.IO.sz754A"></a>
#### sz754A

```python
 | @sz754A.setter
 | sz754A(sz754)
```

set sz754A

<a name=".gimpformats.BinaryIO.IO.sz754W"></a>
#### sz754W

```python
 | @sz754W.setter
 | sz754W(sz754)
```

set sz754W

<a name=".gimpformats.BinaryIO.IO.sz754U"></a>
#### sz754U

```python
 | @sz754U.setter
 | sz754U(sz754)
```

set sz754U

<a name=".gimpformats.BinaryIO.IO.textLine"></a>
#### textLine

```python
 | @textLine.setter
 | textLine(text)
```

Set a sequence of chars until the next new line char

<a name=".gimpformats.BinaryIO.IO.textLineA"></a>
#### textLineA

```python
 | @textLineA.setter
 | textLineA(text)
```

Set a sequence of chars until the next new line char in ascii

<a name=".gimpformats.BinaryIO.IO.textLineW"></a>
#### textLineW

```python
 | @textLineW.setter
 | textLineW(text)
```

Set a sequence of chars until the next new line char in ucs-2

<a name=".gimpformats.BinaryIO.IO.textLineU"></a>
#### textLineU

```python
 | @textLineU.setter
 | textLineU(text)
```

Set a sequence of chars until the next new line char in utf-8

<a name=".gimpformats.BinaryIO.IO.cString"></a>
#### cString

```python
 | @cString.setter
 | cString(text)
```

Set a sequence of chars and add a null byte

<a name=".gimpformats.BinaryIO.IO.cStringA"></a>
#### cStringA

```python
 | @cStringA.setter
 | cStringA(text)
```

Set a sequence of chars and add a null byte in ascii

<a name=".gimpformats.BinaryIO.IO.cStringW"></a>
#### cStringW

```python
 | @cStringW.setter
 | cStringW(text)
```

Set a sequence of chars and add a null byte in ucs-2

<a name=".gimpformats.BinaryIO.IO.cStringU"></a>
#### cStringU

```python
 | @cStringU.setter
 | cStringU(text)
```

Set a sequence of chars and add a null byte in utf-8

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

