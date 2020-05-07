<a name=".gimpformats"></a>
## gimpformats

gimpformats

Forked from https://github.com/TheHeadlessSourceMan/gimpFormats

A pure python implementation of the GIMP XCF image format.

Use this to interact with GIMP image formats

<a name=".gimpformats.binaryIO"></a>
## gimpformats.binaryIO

Base binary I/O helper.

Does boilerplate things like reading the next uint32 from the document

<a name=".gimpformats.binaryIO.IO"></a>
### IO

```python
class IO()
```

Class to handle i/o to a byte buffer or file-like object

<a name=".gimpformats.binaryIO.IO.__init__"></a>
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

<a name=".gimpformats.binaryIO.IO.data"></a>
#### data

```python
 | @data.setter
 | data(data)
```

set data

<a name=".gimpformats.binaryIO.IO.beginContext"></a>
#### beginContext

```python
 | beginContext(newIndex)
```

Start a new context where the index can be changed all you want,
and when endContext() is called, it will be restored to the current position

<a name=".gimpformats.binaryIO.IO.endContext"></a>
#### endContext

```python
 | endContext()
```

Restore the index to the previous location where it was when beginContext() was called

<a name=".gimpformats.binaryIO.IO.bool"></a>
#### bool

```python
 | @bool.setter
 | bool(ioBool)
```

set bool

<a name=".gimpformats.binaryIO.IO.bool8"></a>
#### bool8

```python
 | @bool8.setter
 | bool8(ioBool)
```

set a bool8

<a name=".gimpformats.binaryIO.IO.bool16"></a>
#### bool16

```python
 | @bool16.setter
 | bool16(ioBool)
```

set bool16

<a name=".gimpformats.binaryIO.IO.bool32"></a>
#### bool32

```python
 | @bool32.setter
 | bool32(ioBool)
```

set bool32

<a name=".gimpformats.binaryIO.IO.bool64"></a>
#### bool64

```python
 | @bool64.setter
 | bool64(ioBool)
```

set bool64

<a name=".gimpformats.binaryIO.IO.byte"></a>
#### byte

```python
 | @byte.setter
 | byte(byte)
```

set byte

<a name=".gimpformats.binaryIO.IO.unsignedByte"></a>
#### unsignedByte

```python
 | @unsignedByte.setter
 | unsignedByte(byte)
```

set unsigned byte

<a name=".gimpformats.binaryIO.IO.word"></a>
#### word

```python
 | @word.setter
 | word(word)
```

set a word

<a name=".gimpformats.binaryIO.IO.unsignedWord"></a>
#### unsignedWord

```python
 | @unsignedWord.setter
 | unsignedWord(unsignedWord)
```

set an unsigned word

<a name=".gimpformats.binaryIO.IO.dword"></a>
#### dword

```python
 | @dword.setter
 | dword(dword)
```

set a dword

<a name=".gimpformats.binaryIO.IO.unsignedDword"></a>
#### unsignedDword

```python
 | @unsignedDword.setter
 | unsignedDword(unsignedDword)
```

set an unsigned dword

<a name=".gimpformats.binaryIO.IO.i8"></a>
#### i8

```python
 | @i8.setter
 | i8(i8)
```

set an int8

<a name=".gimpformats.binaryIO.IO.u8"></a>
#### u8

```python
 | @u8.setter
 | u8(u8)
```

set an unsigned int

<a name=".gimpformats.binaryIO.IO.i16"></a>
#### i16

```python
 | @i16.setter
 | i16(i16)
```

set an int16

<a name=".gimpformats.binaryIO.IO.u16"></a>
#### u16

```python
 | @u16.setter
 | u16(u16)
```

set an unint16

<a name=".gimpformats.binaryIO.IO.i32"></a>
#### i32

```python
 | @i32.setter
 | i32(i32)
```

set an int32

<a name=".gimpformats.binaryIO.IO.u32"></a>
#### u32

```python
 | @u32.setter
 | u32(u32)
```

set a unint32

<a name=".gimpformats.binaryIO.IO.i64"></a>
#### i64

```python
 | @i64.setter
 | i64(i64)
```

set an int64

<a name=".gimpformats.binaryIO.IO.u64"></a>
#### u64

```python
 | @u64.setter
 | u64(u64)
```

set a uint64

<a name=".gimpformats.binaryIO.IO.float32"></a>
#### float32

```python
 | @float32.setter
 | float32(float32)
```

set a float32

<a name=".gimpformats.binaryIO.IO.float64"></a>
#### float64

```python
 | @float64.setter
 | float64(float64)
```

set a float64

<a name=".gimpformats.binaryIO.IO.u8be"></a>
#### u8be

```python
 | @u8be.setter
 | u8be(u8be)
```

set the uint8

<a name=".gimpformats.binaryIO.IO.u8le"></a>
#### u8le

```python
 | @u8le.setter
 | u8le(u8le)
```

set the uint8

<a name=".gimpformats.binaryIO.IO.i8le"></a>
#### i8le

```python
 | @i8le.setter
 | i8le(i8le)
```

set the int8

<a name=".gimpformats.binaryIO.IO.i8be"></a>
#### i8be

```python
 | @i8be.setter
 | i8be(i8be)
```

set the int8

<a name=".gimpformats.binaryIO.IO.u16be"></a>
#### u16be

```python
 | @u16be.setter
 | u16be(u16be)
```

set the uint16

<a name=".gimpformats.binaryIO.IO.u16le"></a>
#### u16le

```python
 | @u16le.setter
 | u16le(u16le)
```

set the uint16

<a name=".gimpformats.binaryIO.IO.i16le"></a>
#### i16le

```python
 | @i16le.setter
 | i16le(i16le)
```

set the int16

<a name=".gimpformats.binaryIO.IO.i16be"></a>
#### i16be

```python
 | @i16be.setter
 | i16be(i16be)
```

set the int16

<a name=".gimpformats.binaryIO.IO.u32be"></a>
#### u32be

```python
 | @u32be.setter
 | u32be(u32be)
```

set the uint32

<a name=".gimpformats.binaryIO.IO.u32le"></a>
#### u32le

```python
 | @u32le.setter
 | u32le(u32le)
```

set the uint32

<a name=".gimpformats.binaryIO.IO.i32le"></a>
#### i32le

```python
 | @i32le.setter
 | i32le(i32le)
```

set the int32

<a name=".gimpformats.binaryIO.IO.i32be"></a>
#### i32be

```python
 | @i32be.setter
 | i32be(i32be)
```

set the int32

<a name=".gimpformats.binaryIO.IO.u64be"></a>
#### u64be

```python
 | @u64be.setter
 | u64be(u64be)
```

set the uint64

<a name=".gimpformats.binaryIO.IO.u64le"></a>
#### u64le

```python
 | @u64le.setter
 | u64le(u64le)
```

set the uint64

<a name=".gimpformats.binaryIO.IO.i64le"></a>
#### i64le

```python
 | @i64le.setter
 | i64le(i64le)
```

set the int64

<a name=".gimpformats.binaryIO.IO.i64be"></a>
#### i64be

```python
 | @i64be.setter
 | i64be(i64be)
```

set the int64

<a name=".gimpformats.binaryIO.IO.float"></a>
#### float

```python
 | @float.setter
 | float(f)
```

set a float

<a name=".gimpformats.binaryIO.IO.double"></a>
#### double

```python
 | @double.setter
 | double(f)
```

set a double

<a name=".gimpformats.binaryIO.IO.float32be"></a>
#### float32be

```python
 | @float32be.setter
 | float32be(float32be)
```

set a 32 bit float

<a name=".gimpformats.binaryIO.IO.float32le"></a>
#### float32le

```python
 | @float32le.setter
 | float32le(float32le)
```

set a 32 bit float

<a name=".gimpformats.binaryIO.IO.float64be"></a>
#### float64be

```python
 | @float64be.setter
 | float64be(float64be)
```

set a 64 bit float

<a name=".gimpformats.binaryIO.IO.float64le"></a>
#### float64le

```python
 | @float64le.setter
 | float64le(float64le)
```

set a 64 bit float

<a name=".gimpformats.binaryIO.IO.getBytes"></a>
#### getBytes

```python
 | getBytes(nbytes)
```

grab some raw bytes and advance the index

<a name=".gimpformats.binaryIO.IO.addBytes"></a>
#### addBytes

```python
 | addBytes(ioBytes)
```

add some raw bytes and advance the index

alias for setBytes()

**Arguments**:

- `bytes`: can be a string, bytearray, or another IO object

<a name=".gimpformats.binaryIO.IO.setBytes"></a>
#### setBytes

```python
 | setBytes(ioBytes)
```

add some raw bytes and advance the index

alias for addBytes()

**Arguments**:

- `ioBytes`: can be a string, bytearray, or another IO object

<a name=".gimpformats.binaryIO.IO.sz754"></a>
#### sz754

```python
 | @sz754.setter
 | sz754(sz754)
```

set sz754

<a name=".gimpformats.binaryIO.IO.sz754A"></a>
#### sz754A

```python
 | @sz754A.setter
 | sz754A(sz754)
```

set sz754A

<a name=".gimpformats.binaryIO.IO.sz754W"></a>
#### sz754W

```python
 | @sz754W.setter
 | sz754W(sz754)
```

set sz754W

<a name=".gimpformats.binaryIO.IO.sz754U"></a>
#### sz754U

```python
 | @sz754U.setter
 | sz754U(sz754)
```

set sz754U

<a name=".gimpformats.binaryIO.IO.textLine"></a>
#### textLine

```python
 | @textLine.setter
 | textLine(text)
```

Set a sequence of chars until the next new line char

<a name=".gimpformats.binaryIO.IO.textLineA"></a>
#### textLineA

```python
 | @textLineA.setter
 | textLineA(text)
```

Set a sequence of chars until the next new line char in ascii

<a name=".gimpformats.binaryIO.IO.textLineW"></a>
#### textLineW

```python
 | @textLineW.setter
 | textLineW(text)
```

Set a sequence of chars until the next new line char in ucs-2

<a name=".gimpformats.binaryIO.IO.textLineU"></a>
#### textLineU

```python
 | @textLineU.setter
 | textLineU(text)
```

Set a sequence of chars until the next new line char in utf-8

<a name=".gimpformats.binaryIO.IO.cString"></a>
#### cString

```python
 | @cString.setter
 | cString(text)
```

Set a sequence of chars and add a null byte

<a name=".gimpformats.binaryIO.IO.cStringA"></a>
#### cStringA

```python
 | @cStringA.setter
 | cStringA(text)
```

Set a sequence of chars and add a null byte in ascii

<a name=".gimpformats.binaryIO.IO.cStringW"></a>
#### cStringW

```python
 | @cStringW.setter
 | cStringW(text)
```

Set a sequence of chars and add a null byte in ucs-2

<a name=".gimpformats.binaryIO.IO.cStringU"></a>
#### cStringU

```python
 | @cStringU.setter
 | cStringU(text)
```

Set a sequence of chars and add a null byte in utf-8

<a name=".gimpformats.gimpFormat"></a>
## gimpformats.gimpFormat

Pure python implementation of the gimp file formats

<a name=".gimpformats.gimpFormat.GimpFormatPlugin"></a>
### GimpFormatPlugin

```python
class GimpFormatPlugin()
```

Pure python implementation of the gimp file formats

<a name=".gimpformats.gimpFormat.showLayer"></a>
#### showLayer

```python
showLayer(iteration, l)
```

show a layer

<a name=".gimpformats.gimpFormat.saveLayer"></a>
#### saveLayer

```python
saveLayer(gimpDoc, l, filename)
```

save a layer

<a name=".gimpformats.gimpGbrBrush"></a>
## gimpformats.gimpGbrBrush

Pure python implementation of the gimp gbr brush format

<a name=".gimpformats.gimpGbrBrush.GimpGbrBrush"></a>
### GimpGbrBrush

```python
class GimpGbrBrush():
 |  GimpGbrBrush(filename=None)
```

Pure python implementation of the gimp gbr brush format

See:
	https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/gbr.txt

<a name=".gimpformats.gimpGbrBrush.GimpGbrBrush.load"></a>
#### load

```python
 | load(filename)
```

load a gimp file

**Arguments**:

- `filename`: can be a file name or a file-like object

<a name=".gimpformats.gimpGbrBrush.GimpGbrBrush._decode_"></a>
#### \_decode\_

```python
 | _decode_(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.gimpGbrBrush.GimpGbrBrush.toBytes"></a>
#### toBytes

```python
 | toBytes()
```

encode this object to byte array

<a name=".gimpformats.gimpGbrBrush.GimpGbrBrush.size"></a>
#### size

```python
 | @property
 | size()
```

Get the size

<a name=".gimpformats.gimpGbrBrush.GimpGbrBrush.image"></a>
#### image

```python
 | @property
 | image()
```

get a final, compiled image

<a name=".gimpformats.gimpGbrBrush.GimpGbrBrush.save"></a>
#### save

```python
 | save(toFilename=None, toExtension=None)
```

save this gimp image to a file

<a name=".gimpformats.gimpGbrBrush.GimpGbrBrush.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.gimpGgrGradient"></a>
## gimpformats.gimpGgrGradient

Gimp color gradient

<a name=".gimpformats.gimpGgrGradient.GradientSegment"></a>
### GradientSegment

```python
class GradientSegment():
 |  GradientSegment()
```

Single segment within a gradient

<a name=".gimpformats.gimpGgrGradient.GradientSegment.getColor"></a>
#### getColor

```python
 | getColor(percent)
```

given a decimal percent (1.0 = 100%) retrieve
the appropriate color for this point in the gradient

<a name=".gimpformats.gimpGgrGradient.GradientSegment._decode_"></a>
#### \_decode\_

```python
 | _decode_(data)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode

<a name=".gimpformats.gimpGgrGradient.GradientSegment.toBytes"></a>
#### toBytes

```python
 | toBytes()
```

encode this to a byte array

<a name=".gimpformats.gimpGgrGradient.GradientSegment.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.gimpGgrGradient.GimpGgrGradient"></a>
### GimpGgrGradient

```python
class GimpGgrGradient():
 |  GimpGgrGradient(filename=None)
```

Gimp color gradient

See:
	https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/ggr.txt

<a name=".gimpformats.gimpGgrGradient.GimpGgrGradient.load"></a>
#### load

```python
 | load(filename)
```

load a gimp file

**Arguments**:

- `filename`: can be a file name or a file-like object

<a name=".gimpformats.gimpGgrGradient.GimpGgrGradient._decode_"></a>
#### \_decode\_

```python
 | _decode_(data)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.gimpGgrGradient.GimpGgrGradient.toBytes"></a>
#### toBytes

```python
 | toBytes()
```

encode this to a byte array

<a name=".gimpformats.gimpGgrGradient.GimpGgrGradient.save"></a>
#### save

```python
 | save(toFilename=None)
```

save this gimp image to a file

<a name=".gimpformats.gimpGgrGradient.GimpGgrGradient.getColor"></a>
#### getColor

```python
 | getColor(percent)
```

given a decimal percent (1.0 = 100%) retrieve
the appropriate color for this point in the gradient

<a name=".gimpformats.gimpGgrGradient.GimpGgrGradient.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.gimpGihBrushSet"></a>
## gimpformats.gimpGihBrushSet

Gimp Image Pipe Format

The gih format is use to store a series of brushes, and some extra info
for how to use them.

<a name=".gimpformats.gimpGihBrushSet.GimpGihBrushSet"></a>
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

<a name=".gimpformats.gimpGihBrushSet.GimpGihBrushSet.load"></a>
#### load

```python
 | load(filename)
```

load a gimp file

**Arguments**:

- `filename`: can be a file name or a file-like object

<a name=".gimpformats.gimpGihBrushSet.GimpGihBrushSet._decode_"></a>
#### \_decode\_

```python
 | _decode_(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.gimpGihBrushSet.GimpGihBrushSet.toBytes"></a>
#### toBytes

```python
 | toBytes()
```

encode this object to a byte array

<a name=".gimpformats.gimpGihBrushSet.GimpGihBrushSet.save"></a>
#### save

```python
 | save(toFilename=None)
```

save this gimp image to a file

<a name=".gimpformats.gimpGihBrushSet.GimpGihBrushSet.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.gimpGpbBrush"></a>
## gimpformats.gimpGpbBrush

Pure python implementation of the OLD gimp gpb brush format

<a name=".gimpformats.gimpGpbBrush.GimpGpbBrush"></a>
### GimpGpbBrush

```python
class GimpGpbBrush():
 |  GimpGpbBrush(filename)
```

Pure python implementation of the OLD gimp gpb brush format

See:
	https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/vbr.txt

<a name=".gimpformats.gimpGpbBrush.GimpGpbBrush.load"></a>
#### load

```python
 | load(filename)
```

load a gimp file

**Arguments**:

- `filename`: can be a file name or a file-like object

<a name=".gimpformats.gimpGpbBrush.GimpGpbBrush._decode_"></a>
#### \_decode\_

```python
 | _decode_(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.gimpGpbBrush.GimpGpbBrush.toBytes"></a>
#### toBytes

```python
 | toBytes()
```

encode this object to a byte array

<a name=".gimpformats.gimpGpbBrush.GimpGpbBrush.save"></a>
#### save

```python
 | save(toFilename=None)
```

save this gimp image to a file

<a name=".gimpformats.gimpGpbBrush.GimpGpbBrush.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.gimpGplPalette"></a>
## gimpformats.gimpGplPalette

Pure python implementation of the gimp gpl palette format

<a name=".gimpformats.gimpGplPalette.GimpGplPalette"></a>
### GimpGplPalette

```python
class GimpGplPalette():
 |  GimpGplPalette(filename=None)
```

Pure python implementation of the gimp gpl palette format

<a name=".gimpformats.gimpGplPalette.GimpGplPalette.load"></a>
#### load

```python
 | load(filename)
```

load a gimp file

**Arguments**:

- `filename`: can be a file name or a file-like object

<a name=".gimpformats.gimpGplPalette.GimpGplPalette._decode_"></a>
#### \_decode\_

```python
 | _decode_(data)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode

<a name=".gimpformats.gimpGplPalette.GimpGplPalette.toBytes"></a>
#### toBytes

```python
 | toBytes()
```

encode to a raw data stream

<a name=".gimpformats.gimpGplPalette.GimpGplPalette.save"></a>
#### save

```python
 | save(toFilename=None, toExtension=None)
```

save this gimp image to a file

<a name=".gimpformats.gimpGplPalette.GimpGplPalette.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.gimpGplPalette.GimpGplPalette.__eq__"></a>
#### \_\_eq\_\_

```python
 | __eq__(other)
```

perform a comparison

<a name=".gimpformats.gimpGtpToolPreset"></a>
## gimpformats.gimpGtpToolPreset

Pure python implementation of the gimp gtp tool preset format

<a name=".gimpformats.gimpGtpToolPreset.ParenFileValue"></a>
### ParenFileValue

```python
class ParenFileValue():
 |  ParenFileValue(name=None, value="", children=None)
```

A parentheses-based file format
(possibly "scheme" language?)

<a name=".gimpformats.gimpGtpToolPreset.ParenFileValue.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__()
```

Get a textual representation of this object

<a name=".gimpformats.gimpGtpToolPreset.parenFileDecode"></a>
#### parenFileDecode

```python
parenFileDecode(data)
```

Decode a parentheses-based file format
(possibly "scheme" language?)

<a name=".gimpformats.gimpGtpToolPreset.walkTree"></a>
#### walkTree

```python
walkTree(items)
```

walk the tree

<a name=".gimpformats.gimpGtpToolPreset.parenFileEncode"></a>
#### parenFileEncode

```python
parenFileEncode(values)
```

encode a values tree to a buffer

<a name=".gimpformats.gimpGtpToolPreset.GimpGtpToolPreset"></a>
### GimpGtpToolPreset

```python
class GimpGtpToolPreset():
 |  GimpGtpToolPreset(filename=None)
```

Pure python implementation of the gimp gtp tool preset format

<a name=".gimpformats.gimpGtpToolPreset.GimpGtpToolPreset.load"></a>
#### load

```python
 | load(filename)
```

load a gimp file

**Arguments**:

- `filename`: can be a file name or a file-like object

<a name=".gimpformats.gimpGtpToolPreset.GimpGtpToolPreset._decode_"></a>
#### \_decode\_

```python
 | _decode_(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode

<a name=".gimpformats.gimpGtpToolPreset.GimpGtpToolPreset.toBytes"></a>
#### toBytes

```python
 | toBytes()
```

encode to a byte array

<a name=".gimpformats.gimpGtpToolPreset.GimpGtpToolPreset.save"></a>
#### save

```python
 | save(toFilename=None, toExtension=None)
```

save this gimp tool preset to a file

<a name=".gimpformats.gimpGtpToolPreset.GimpGtpToolPreset.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.gimpImageInternals"></a>
## gimpformats.gimpImageInternals

Contains stuff around the internal image storage mechanism
of gimp files.

Generally speaking, the user should not care about anything
in this file.

<a name=".gimpformats.gimpImageInternals.GimpChannel"></a>
### GimpChannel

```python
class GimpChannel(GimpIOBase):
 |  GimpChannel(parent, name='', image=None)
```

Represents a single channel or mask in a gimp image

<a name=".gimpformats.gimpImageInternals.GimpChannel.fromBytes"></a>
#### fromBytes

```python
 | fromBytes(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.gimpImageInternals.GimpChannel.toBytes"></a>
#### toBytes

```python
 | toBytes()
```

encode this object to a byte buffer

<a name=".gimpformats.gimpImageInternals.GimpChannel.image"></a>
#### image

```python
 | @image.setter
 | image(image)
```

get a final, compiled image

<a name=".gimpformats.gimpImageInternals.GimpChannel.imageHierarchy"></a>
#### imageHierarchy

```python
 | @property
 | imageHierarchy()
```

Get teh image hierarchy

This is mainly used for decoding the image, so
not much use to you.

<a name=".gimpformats.gimpImageInternals.GimpChannel.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.gimpImageInternals.GimpImageHierarchy"></a>
### GimpImageHierarchy

```python
class GimpImageHierarchy(GimpIOBase):
 |  GimpImageHierarchy(parent, image=None)
```

Gets packed pixels from a gimp image

NOTE: This was originally designed to be a hierarchy, like
	an image pyramid, through in practice they only use the
	top level of the pyramid (64x64) and ignore the rest.

<a name=".gimpformats.gimpImageInternals.GimpImageHierarchy.fromBytes"></a>
#### fromBytes

```python
 | fromBytes(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.gimpImageInternals.GimpImageHierarchy.toBytes"></a>
#### toBytes

```python
 | toBytes()
```

encode this object to a byte buffer

<a name=".gimpformats.gimpImageInternals.GimpImageHierarchy.levels"></a>
#### levels

```python
 | @property
 | levels()
```

Get the levels within this hierarchy

Presently hierarchy is not really used by gimp,
so this returns an array of one item

<a name=".gimpformats.gimpImageInternals.GimpImageHierarchy.image"></a>
#### image

```python
 | @image.setter
 | image(image)
```

set the image

<a name=".gimpformats.gimpImageInternals.GimpImageHierarchy.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.gimpImageInternals.GimpImageLevel"></a>
### GimpImageLevel

```python
class GimpImageLevel(GimpIOBase):
 |  GimpImageLevel(parent)
```

Gets packed pixels from a gimp image

This represents a single level in an imageHierarchy

<a name=".gimpformats.gimpImageInternals.GimpImageLevel.fromBytes"></a>
#### fromBytes

```python
 | fromBytes(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.gimpImageInternals.GimpImageLevel.toBytes"></a>
#### toBytes

```python
 | toBytes()
```

encode this object to a byte buffer

<a name=".gimpformats.gimpImageInternals.GimpImageLevel.bpp"></a>
#### bpp

```python
 | @property
 | bpp()
```

get bpp

<a name=".gimpformats.gimpImageInternals.GimpImageLevel.mode"></a>
#### mode

```python
 | @property
 | mode()
```

get mode

<a name=".gimpformats.gimpImageInternals.GimpImageLevel.tiles"></a>
#### tiles

```python
 | @property
 | tiles()
```

get tiles

<a name=".gimpformats.gimpImageInternals.GimpImageLevel.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.gimpIOBase"></a>
## gimpformats.gimpIOBase

A specialized binary file base for Gimp files

<a name=".gimpformats.gimpIOBase.GimpIOBase"></a>
### GimpIOBase

```python
class GimpIOBase():
 |  GimpIOBase(parent)
```

A specialized binary file base for Gimp files

<a name=".gimpformats.gimpIOBase.GimpIOBase.getBlendMode"></a>
#### getBlendMode

```python
 | getBlendMode()
```

return the blend mode as a string

<a name=".gimpformats.gimpIOBase.GimpIOBase.getCompression"></a>
#### getCompression

```python
 | getCompression()
```

return the compression as a string

<a name=".gimpformats.gimpIOBase.GimpIOBase.getUnits"></a>
#### getUnits

```python
 | getUnits()
```

return the units as a string

<a name=".gimpformats.gimpIOBase.GimpIOBase.getTagColours"></a>
#### getTagColours

```python
 | getTagColours()
```

return the tag colours as a string

<a name=".gimpformats.gimpIOBase.GimpIOBase.getCompositeModes"></a>
#### getCompositeModes

```python
 | getCompositeModes()
```

return the composite mode as a string

<a name=".gimpformats.gimpIOBase.GimpIOBase.getCompositeSpaces"></a>
#### getCompositeSpaces

```python
 | getCompositeSpaces()
```

return the composite spaces as a string

<a name=".gimpformats.gimpIOBase.GimpIOBase._POINTER_SIZE_"></a>
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

<a name=".gimpformats.gimpIOBase.GimpIOBase.doc"></a>
#### doc

```python
 | @property
 | doc()
```

Get the main document object

<a name=".gimpformats.gimpIOBase.GimpIOBase.root"></a>
#### root

```python
 | @property
 | root()
```

Get the root of the file object tree
(Which is the same as self.doc)

<a name=".gimpformats.gimpIOBase.GimpIOBase.tattoo"></a>
#### tattoo

```python
 | @tattoo.setter
 | tattoo(tattoo)
```

This is the gimp nomenclature for the item's unique id

<a name=".gimpformats.gimpIOBase.GimpIOBase._parasitesDecode_"></a>
#### \_parasitesDecode\_

```python
 | _parasitesDecode_(data)
```

decode list of parasites

<a name=".gimpformats.gimpIOBase.GimpIOBase._parasitesEncode_"></a>
#### \_parasitesEncode\_

```python
 | _parasitesEncode_()
```

encode list of parasites

<a name=".gimpformats.gimpIOBase.GimpIOBase._guidelinesDecode_"></a>
#### \_guidelinesDecode\_

```python
 | _guidelinesDecode_(data)
```

decode guidelines

<a name=".gimpformats.gimpIOBase.GimpIOBase._itemPathDecode_"></a>
#### \_itemPathDecode\_

```python
 | _itemPathDecode_(data)
```

decode item path

<a name=".gimpformats.gimpIOBase.GimpIOBase.activeVector"></a>
#### activeVector

```python
 | @property
 | activeVector()
```

get the vector that is currently active

<a name=".gimpformats.gimpIOBase.GimpIOBase.expanded"></a>
#### expanded

```python
 | @expanded.setter
 | expanded(expanded)
```

is the group layer expanded

<a name=".gimpformats.gimpIOBase.GimpIOBase._colormapDecode_"></a>
#### \_colormapDecode\_

```python
 | _colormapDecode_(data, index=None)
```

**Arguments**:

- `data`: can be bytes or an IO object

decode colormap/palette

<a name=".gimpformats.gimpIOBase.GimpIOBase._userUnitsDecode_"></a>
#### \_userUnitsDecode\_

```python
 | _userUnitsDecode_(data)
```

decode a set of user-defined measurement units

<a name=".gimpformats.gimpIOBase.GimpIOBase._samplePointsDecode_"></a>
#### \_samplePointsDecode\_

```python
 | _samplePointsDecode_(data)
```

decode a series of points

<a name=".gimpformats.gimpIOBase.GimpIOBase._propertyDecode_"></a>
#### \_propertyDecode\_

```python
 | _propertyDecode_(propertyType, data)
```

decode a single property

Many properties are in the form
propertyType: one of PROP_
lengthOfData: 4
data: varies but is often io.32 or io.bool

<a name=".gimpformats.gimpIOBase.GimpIOBase._propertyEncode_"></a>
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

<a name=".gimpformats.gimpIOBase.GimpIOBase._propertiesDecode_"></a>
#### \_propertiesDecode\_

```python
 | _propertiesDecode_(io)
```

decode a list of properties

<a name=".gimpformats.gimpIOBase.GimpIOBase._propertiesEncode_"></a>
#### \_propertiesEncode\_

```python
 | _propertiesEncode_()
```

encode a list of properties

<a name=".gimpformats.gimpIOBase.GimpIOBase.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.gimpIOBase.GimpUserUnits"></a>
### GimpUserUnits

```python
class GimpUserUnits():
 |  GimpUserUnits()
```

user-defined measurement units

<a name=".gimpformats.gimpIOBase.GimpUserUnits.fromBytes"></a>
#### fromBytes

```python
 | fromBytes(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.gimpIOBase.GimpUserUnits.toBytes"></a>
#### toBytes

```python
 | toBytes()
```

convert this object to raw bytes

<a name=".gimpformats.gimpIOBase.GimpUserUnits.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.gimpParasites"></a>
## gimpformats.gimpParasites

Parasites are arbitrary (meta)data strings that can be attached to a document tree item

They are used to store things like last-used plugin settings, gamma adjuetments, etc.

Format of known parasites:
	https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/parasites.txt

<a name=".gimpformats.gimpParasites.GimpParasite"></a>
### GimpParasite

```python
class GimpParasite():
 |  GimpParasite()
```

Parasites are arbitrary (meta)data strings that can be attached to a document tree item

They are used to store things like last-used plugin settings, gamma adjuetments, etc.

Format of known parasites:
	https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/parasites.txt

<a name=".gimpformats.gimpParasites.GimpParasite.fromBytes"></a>
#### fromBytes

```python
 | fromBytes(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.gimpParasites.GimpParasite.toBytes"></a>
#### toBytes

```python
 | toBytes()
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.gimpParasites.GimpParasite.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.gimpPatPattern"></a>
## gimpformats.gimpPatPattern

Pure python implementation of a gimp pattern file

<a name=".gimpformats.gimpPatPattern.GimpPatPattern"></a>
### GimpPatPattern

```python
class GimpPatPattern():
 |  GimpPatPattern(filename=None)
```

Pure python implementation of a gimp pattern file

See:
	https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/pat.txt

<a name=".gimpformats.gimpPatPattern.GimpPatPattern.load"></a>
#### load

```python
 | load(filename)
```

load a gimp file

**Arguments**:

- `filename`: can be a file name or a file-like object

<a name=".gimpformats.gimpPatPattern.GimpPatPattern._decode_"></a>
#### \_decode\_

```python
 | _decode_(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.gimpPatPattern.GimpPatPattern.toBytes"></a>
#### toBytes

```python
 | toBytes()
```

encode to a byte buffer

<a name=".gimpformats.gimpPatPattern.GimpPatPattern.size"></a>
#### size

```python
 | @property
 | size()
```

the size of the pattern

<a name=".gimpformats.gimpPatPattern.GimpPatPattern.save"></a>
#### save

```python
 | save(toFilename=None, toExtension=None)
```

save this gimp image to a file

<a name=".gimpformats.gimpPatPattern.GimpPatPattern.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.gimpVbrBrush"></a>
## gimpformats.gimpVbrBrush

Pure python implementation of the gimp vbr brush format

<a name=".gimpformats.gimpVbrBrush.GimpVbrBrush"></a>
### GimpVbrBrush

```python
class GimpVbrBrush():
 |  GimpVbrBrush(filename=None)
```

Pure python implementation of the gimp vbr brush format

See:
	https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/vbr.txt

<a name=".gimpformats.gimpVbrBrush.GimpVbrBrush.load"></a>
#### load

```python
 | load(filename)
```

load a gimp file

**Arguments**:

- `filename`: can be a file name or a file-like object

<a name=".gimpformats.gimpVbrBrush.GimpVbrBrush.image"></a>
#### image

```python
 | @property
 | image()
```

this parametric brush converted to a useable PIL image

<a name=".gimpformats.gimpVbrBrush.GimpVbrBrush._decode_"></a>
#### \_decode\_

```python
 | _decode_(data)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode

<a name=".gimpformats.gimpVbrBrush.GimpVbrBrush.toBytes"></a>
#### toBytes

```python
 | toBytes()
```

encode to a raw data stream

<a name=".gimpformats.gimpVbrBrush.GimpVbrBrush.save"></a>
#### save

```python
 | save(toFilename=None, toExtension=None)
```

save this gimp image to a file

<a name=".gimpformats.gimpVbrBrush.GimpVbrBrush.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.gimpVbrBrush.GimpVbrBrush.__eq__"></a>
#### \_\_eq\_\_

```python
 | __eq__(other)
```

perform a comparison

<a name=".gimpformats.gimpVectors"></a>
## gimpformats.gimpVectors

Stuff related to vectors/paths within a gimp document

<a name=".gimpformats.gimpVectors.GimpVector"></a>
### GimpVector

```python
class GimpVector(GimpIOBase):
 |  GimpVector(parent)
```

A gimp brush stroke vector

<a name=".gimpformats.gimpVectors.GimpVector.fromBytes"></a>
#### fromBytes

```python
 | fromBytes(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.gimpVectors.GimpVector.toBytes"></a>
#### toBytes

```python
 | toBytes()
```

encode to binary data

<a name=".gimpformats.gimpVectors.GimpVector.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.gimpVectors.GimpStroke"></a>
### GimpStroke

```python
class GimpStroke(GimpIOBase):
 |  GimpStroke(parent)
```

A single stroke within a vector

<a name=".gimpformats.gimpVectors.GimpStroke.fromBytes"></a>
#### fromBytes

```python
 | fromBytes(data, index=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at

<a name=".gimpformats.gimpVectors.GimpStroke.toBytes"></a>
#### toBytes

```python
 | toBytes()
```

encode to binary data

<a name=".gimpformats.gimpVectors.GimpStroke.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.gimpVectors.GimpPoint"></a>
### GimpPoint

```python
class GimpPoint(GimpIOBase):
 |  GimpPoint(parent)
```

A single point within a stroke

<a name=".gimpformats.gimpVectors.GimpPoint.fromBytes"></a>
#### fromBytes

```python
 | fromBytes(data, index=0, numFloatsPerPoint=0)
```

decode a byte buffer

**Arguments**:

- `data`: data buffer to decode
- `index`: index within the buffer to start at
- `numFloatsPerPoint`: required so we know
how many different brush dynamic measurements are
inside each point

<a name=".gimpformats.gimpVectors.GimpPoint.toBytes"></a>
#### toBytes

```python
 | toBytes()
```

encode to binary data

<a name=".gimpformats.gimpVectors.GimpPoint.__repr__"></a>
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

<a name=".gimpformats.gimpXcfDocument.GimpLayer"></a>
### GimpLayer

```python
class GimpLayer(GimpIOBase):
 |  GimpLayer(parent, name=None, image=None)
```

Represents a single layer in a gimp image

<a name=".gimpformats.gimpXcfDocument.GimpLayer._decode_"></a>
#### \_decode\_

```python
 | _decode_(data, index=0)
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

<a name=".gimpformats.gimpXcfDocument.GimpLayer.toBytes"></a>
#### toBytes

```python
 | toBytes()
```

encode to byte array

Steps:
Create a new IO buffer (array of binary values)
Set attributes as outlined in the spec
List of properties
Set the image hierarchy and mask pointers
Return the data

<a name=".gimpformats.gimpXcfDocument.GimpLayer.mask"></a>
#### mask

```python
 | @property
 | mask()
```

Get the layer mask

<a name=".gimpformats.gimpXcfDocument.GimpLayer.image"></a>
#### image

```python
 | @image.setter
 | image(image)
```

set the layer image

NOTE: resets layer width, height, and colorMode

<a name=".gimpformats.gimpXcfDocument.GimpLayer.imageHierarchy"></a>
#### imageHierarchy

```python
 | @property
 | imageHierarchy()
```

Get the image hierarchy objects

This is mainly needed for deciphering image, and therefore,
of little use to you, the user.

NOTE: can return None if it has been fully read into an image

<a name=".gimpformats.gimpXcfDocument.GimpLayer.__repr__"></a>
#### \_\_repr\_\_

```python
 | __repr__(indent='')
```

Get a textual representation of this object

<a name=".gimpformats.gimpXcfDocument.Precision"></a>
### Precision

```python
class Precision():
 |  Precision()
```

Since the precision code is so unusual, I decided to create a class
to parse it.

<a name=".gimpformats.gimpXcfDocument.Precision.decode"></a>
#### decode

```python
 | decode(gimpVersion, io)
```

decode the precision code from the file

<a name=".gimpformats.gimpXcfDocument.Precision.encode"></a>
#### encode

```python
 | encode(gimpVersion, io)
```

encode this to the file

NOTE: will not mess with development versions 5 or 6

<a name=".gimpformats.gimpXcfDocument.Precision.requiredGimpVersion"></a>
#### requiredGimpVersion

```python
 | requiredGimpVersion()
```

return the lowest gimp version that supports this precision

<a name=".gimpformats.gimpXcfDocument.GimpDocument"></a>
### GimpDocument

```python
class GimpDocument(GimpIOBase):
 |  GimpDocument(fileName=None)
```

Pure python implementation of the gimp file format

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

<a name=".gimpformats.gimpXcfDocument.GimpDocument._decode_"></a>
#### \_decode\_

```python
 | _decode_(data, index=0)
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

<a name=".gimpformats.gimpXcfDocument.GimpDocument.toBytes"></a>
#### toBytes

```python
 | toBytes()
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

