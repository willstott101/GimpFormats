# Binaryiotools

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Binaryiotools

> Auto-generated documentation for [gimpformats.binaryiotools](../../../gimpformats/binaryiotools.py) module.

- [Binaryiotools](#binaryiotools)
  - [IO](#io)
    - [IO().__getitem__](#io()__getitem__)
    - [IO().__len__](#io()__len__)
    - [IO()._read](#io()_read)
    - [IO()._readUntil](#io()_readuntil)
    - [IO()._sz754](#io()_sz754)
    - [IO()._sz754set](#io()_sz754set)
    - [IO()._write](#io()_write)
    - [IO().addbytearray](#io()addbytearray)
    - [IO().beginContext](#io()begincontext)
    - [IO().bool16](#io()bool16)
    - [IO().bool16](#io()bool16-1)
    - [IO().bool32](#io()bool32)
    - [IO().bool32](#io()bool32-1)
    - [IO().bool64](#io()bool64)
    - [IO().bool64](#io()bool64-1)
    - [IO().bool8](#io()bool8)
    - [IO().bool8](#io()bool8-1)
    - [IO().boolean](#io()boolean)
    - [IO().boolean](#io()boolean-1)
    - [IO().byte](#io()byte)
    - [IO().byte](#io()byte-1)
    - [IO().cString](#io()cstring)
    - [IO().cString](#io()cstring-1)
    - [IO().cStringA](#io()cstringa)
    - [IO().cStringA](#io()cstringa-1)
    - [IO().cStringU](#io()cstringu)
    - [IO().cStringU](#io()cstringu-1)
    - [IO().cStringW](#io()cstringw)
    - [IO().cStringW](#io()cstringw-1)
    - [IO().data](#io()data)
    - [IO().data](#io()data-1)
    - [IO().double](#io()double)
    - [IO().double](#io()double-1)
    - [IO().dword](#io()dword)
    - [IO().dword](#io()dword-1)
    - [IO().endContext](#io()endcontext)
    - [IO().float32](#io()float32)
    - [IO().float32](#io()float32-1)
    - [IO().float32be](#io()float32be)
    - [IO().float32be](#io()float32be-1)
    - [IO().float32le](#io()float32le)
    - [IO().float32le](#io()float32le-1)
    - [IO().float64](#io()float64)
    - [IO().float64](#io()float64-1)
    - [IO().float64be](#io()float64be)
    - [IO().float64be](#io()float64be-1)
    - [IO().float64le](#io()float64le)
    - [IO().float64le](#io()float64le-1)
    - [IO().floating](#io()floating)
    - [IO().floating](#io()floating-1)
    - [IO().getbytearray](#io()getbytearray)
    - [IO().i16](#io()i16)
    - [IO().i16](#io()i16-1)
    - [IO().i16be](#io()i16be)
    - [IO().i16be](#io()i16be-1)
    - [IO().i16le](#io()i16le)
    - [IO().i16le](#io()i16le-1)
    - [IO().i32](#io()i32)
    - [IO().i32](#io()i32-1)
    - [IO().i32be](#io()i32be)
    - [IO().i32be](#io()i32be-1)
    - [IO().i32le](#io()i32le)
    - [IO().i32le](#io()i32le-1)
    - [IO().i64](#io()i64)
    - [IO().i64](#io()i64-1)
    - [IO().i64be](#io()i64be)
    - [IO().i64be](#io()i64be-1)
    - [IO().i64le](#io()i64le)
    - [IO().i64le](#io()i64le-1)
    - [IO().i8](#io()i8)
    - [IO().i8](#io()i8-1)
    - [IO().i8be](#io()i8be)
    - [IO().i8be](#io()i8be-1)
    - [IO().i8le](#io()i8le)
    - [IO().i8le](#io()i8le-1)
    - [IO().index](#io()index)
    - [IO().index](#io()index-1)
    - [IO().qword](#io()qword)
    - [IO().qword](#io()qword-1)
    - [IO().setbytearray](#io()setbytearray)
    - [IO().sz754](#io()sz754)
    - [IO().sz754](#io()sz754-1)
    - [IO().sz754A](#io()sz754a)
    - [IO().sz754A](#io()sz754a-1)
    - [IO().sz754U](#io()sz754u)
    - [IO().sz754U](#io()sz754u-1)
    - [IO().sz754W](#io()sz754w)
    - [IO().sz754W](#io()sz754w-1)
    - [IO().textLine](#io()textline)
    - [IO().textLine](#io()textline-1)
    - [IO().textLineA](#io()textlinea)
    - [IO().textLineA](#io()textlinea-1)
    - [IO().textLineU](#io()textlineu)
    - [IO().textLineU](#io()textlineu-1)
    - [IO().textLineW](#io()textlinew)
    - [IO().textLineW](#io()textlinew-1)
    - [IO().u16](#io()u16)
    - [IO().u16](#io()u16-1)
    - [IO().u16be](#io()u16be)
    - [IO().u16be](#io()u16be-1)
    - [IO().u16le](#io()u16le)
    - [IO().u16le](#io()u16le-1)
    - [IO().u32](#io()u32)
    - [IO().u32](#io()u32-1)
    - [IO().u32be](#io()u32be)
    - [IO().u32be](#io()u32be-1)
    - [IO().u32le](#io()u32le)
    - [IO().u32le](#io()u32le-1)
    - [IO().u64](#io()u64)
    - [IO().u64](#io()u64-1)
    - [IO().u64be](#io()u64be)
    - [IO().u64be](#io()u64be-1)
    - [IO().u64le](#io()u64le)
    - [IO().u64le](#io()u64le-1)
    - [IO().u8](#io()u8)
    - [IO().u8](#io()u8-1)
    - [IO().u8be](#io()u8be)
    - [IO().u8be](#io()u8be-1)
    - [IO().u8le](#io()u8le)
    - [IO().u8le](#io()u8le-1)
    - [IO().unsignedByte](#io()unsignedbyte)
    - [IO().unsignedByte](#io()unsignedbyte-1)
    - [IO().unsignedDword](#io()unsigneddword)
    - [IO().unsignedDword](#io()unsigneddword-1)
    - [IO().unsignedQword](#io()unsignedqword)
    - [IO().unsignedQword](#io()unsignedqword-1)
    - [IO().unsignedWord](#io()unsignedword)
    - [IO().unsignedWord](#io()unsignedword-1)
    - [IO().word](#io()word)
    - [IO().word](#io()word-1)

## IO

[Show source in binaryiotools.py:40](../../../gimpformats/binaryiotools.py#L40)

Class to handle i/o to a byte buffer or file-like object.

#### Signature

```python
class IO:
    def __init__(
        self,
        data: bytearray | bytes | None = None,
        idx: int = 0,
        littleEndian: bool = False,
        boolSize: int = 8,
        stringEncoding: str = "U",
    ) -> None: ...
```

### IO().__getitem__

[Show source in binaryiotools.py:72](../../../gimpformats/binaryiotools.py#L72)

Get data at a specific idx.

#### Signature

```python
def __getitem__(self, idx: int): ...
```

### IO().__len__

[Show source in binaryiotools.py:68](../../../gimpformats/binaryiotools.py#L68)

Length of data.

#### Signature

```python
def __len__(self) -> int: ...
```

### IO()._read

[Show source in binaryiotools.py:121](../../../gimpformats/binaryiotools.py#L121)

General formatted read.

#### Signature

```python
def _read(self, size: int, fmt: str) -> Any: ...
```

### IO()._readUntil

[Show source in binaryiotools.py:763](../../../gimpformats/binaryiotools.py#L763)

Read a sequence of chars in a set encoding until a set char.

#### Arguments

- `until` - must be within the ascii character set
- `encoding` - one of A (ascii), U (UTF-8) or W (UCS-2)

#### Signature

```python
def _readUntil(self, until: str, encoding: str = "A") -> str: ...
```

### IO()._sz754

[Show source in binaryiotools.py:695](../../../gimpformats/binaryiotools.py#L695)

Read the next string conforming to IEEE 754 and advance the index.

Note, string format is:
 uint32   n+1  Number of bytearray that follow, including the zero byte
 byte[n]  ...  String data in Unicode, encoded using UTF-8
 byte     0    Zero marks the end of the string.
or simply uint32=0 for empty string

#### Signature

```python
def _sz754(self, encoding: str) -> str: ...
```

### IO()._sz754set

[Show source in binaryiotools.py:717](../../../gimpformats/binaryiotools.py#L717)

_sz754set.

#### Signature

```python
def _sz754set(self, sz754: Any, _encoding: str) -> None: ...
```

### IO()._write

[Show source in binaryiotools.py:111](../../../gimpformats/binaryiotools.py#L111)

General formatted write.

#### Signature

```python
def _write(self, size: int, fmt: str, data: Any) -> None: ...
```

### IO().addbytearray

[Show source in binaryiotools.py:664](../../../gimpformats/binaryiotools.py#L664)

Add some raw bytearray and advance the index.

alias for setbytearray()

#### Arguments

- `bytearray` - can be a string, bytearray, or another IO object

#### Signature

```python
def addbytearray(self, iobytearray: Any) -> None: ...
```

### IO().beginContext

[Show source in binaryiotools.py:100](../../../gimpformats/binaryiotools.py#L100)

Start a new context where the index can be changed all you want...

and when endContext() is called, it will be restored to the current position

#### Signature

```python
def beginContext(self, newIndex: int) -> None: ...
```

### IO().bool16

[Show source in binaryiotools.py:178](../../../gimpformats/binaryiotools.py#L178)

Get bool16.

#### Signature

```python
@property
def bool16(self) -> bool: ...
```

### IO().bool16

[Show source in binaryiotools.py:183](../../../gimpformats/binaryiotools.py#L183)

Set bool16.

#### Signature

```python
@bool16.setter
def bool16(self, ioBool: bool) -> None: ...
```

### IO().bool32

[Show source in binaryiotools.py:188](../../../gimpformats/binaryiotools.py#L188)

Get bool32.

#### Signature

```python
@property
def bool32(self) -> bool: ...
```

### IO().bool32

[Show source in binaryiotools.py:193](../../../gimpformats/binaryiotools.py#L193)

Set bool32.

#### Signature

```python
@bool32.setter
def bool32(self, ioBool: bool) -> None: ...
```

### IO().bool64

[Show source in binaryiotools.py:198](../../../gimpformats/binaryiotools.py#L198)

Get bool64.

#### Signature

```python
@property
def bool64(self) -> bool: ...
```

### IO().bool64

[Show source in binaryiotools.py:203](../../../gimpformats/binaryiotools.py#L203)

Set bool64.

#### Signature

```python
@bool64.setter
def bool64(self, ioBool: bool) -> None: ...
```

### IO().bool8

[Show source in binaryiotools.py:168](../../../gimpformats/binaryiotools.py#L168)

Get bool8.

#### Signature

```python
@property
def bool8(self) -> bool: ...
```

### IO().bool8

[Show source in binaryiotools.py:173](../../../gimpformats/binaryiotools.py#L173)

Set a bool8.

#### Signature

```python
@bool8.setter
def bool8(self, ioBool: bool) -> None: ...
```

### IO().boolean

[Show source in binaryiotools.py:141](../../../gimpformats/binaryiotools.py#L141)

Return bool.

#### Signature

```python
@property
def boolean(self) -> bool: ...
```

### IO().boolean

[Show source in binaryiotools.py:154](../../../gimpformats/binaryiotools.py#L154)

Set bool.

#### Signature

```python
@boolean.setter
def boolean(self, ioBool: bool) -> None: ...
```

### IO().byte

[Show source in binaryiotools.py:208](../../../gimpformats/binaryiotools.py#L208)

Get byte.

#### Signature

```python
@property
def byte(self) -> Any: ...
```

### IO().byte

[Show source in binaryiotools.py:213](../../../gimpformats/binaryiotools.py#L213)

Set byte.

#### Signature

```python
@byte.setter
def byte(self, byte: Any) -> None: ...
```

### IO().cString

[Show source in binaryiotools.py:852](../../../gimpformats/binaryiotools.py#L852)

Read a sequence of chars until the next null byte.

#### Signature

```python
@property
def cString(self) -> str: ...
```

### IO().cString

[Show source in binaryiotools.py:857](../../../gimpformats/binaryiotools.py#L857)

Set a sequence of chars and add a null byte.

#### Signature

```python
@cString.setter
def cString(self, text: str) -> None: ...
```

### IO().cStringA

[Show source in binaryiotools.py:863](../../../gimpformats/binaryiotools.py#L863)

Read a sequence of chars until the next null byte in ascii.

#### Signature

```python
@property
def cStringA(self) -> str: ...
```

### IO().cStringA

[Show source in binaryiotools.py:868](../../../gimpformats/binaryiotools.py#L868)

Set a sequence of chars and add a null byte in ascii.

#### Signature

```python
@cStringA.setter
def cStringA(self, text: str) -> None: ...
```

### IO().cStringU

[Show source in binaryiotools.py:885](../../../gimpformats/binaryiotools.py#L885)

Read a sequence of chars until the next null byte in utf-8.

#### Signature

```python
@property
def cStringU(self) -> str: ...
```

### IO().cStringU

[Show source in binaryiotools.py:890](../../../gimpformats/binaryiotools.py#L890)

Set a sequence of chars and add a null byte in utf-8.

#### Signature

```python
@cStringU.setter
def cStringU(self, text: str) -> None: ...
```

### IO().cStringW

[Show source in binaryiotools.py:874](../../../gimpformats/binaryiotools.py#L874)

Read a sequence of chars until the next null byte in ucs-2.

#### Signature

```python
@property
def cStringW(self) -> str: ...
```

### IO().cStringW

[Show source in binaryiotools.py:879](../../../gimpformats/binaryiotools.py#L879)

Set a sequence of chars and add a null byte in ucs-2.

#### Signature

```python
@cStringW.setter
def cStringW(self, text: str) -> None: ...
```

### IO().data

[Show source in binaryiotools.py:76](../../../gimpformats/binaryiotools.py#L76)

Return data.

#### Signature

```python
@property
def data(self) -> bytearray: ...
```

### IO().data

[Show source in binaryiotools.py:83](../../../gimpformats/binaryiotools.py#L83)

Set data.

#### Signature

```python
@data.setter
def data(self, data: bytearray) -> None: ...
```

### IO().double

[Show source in binaryiotools.py:608](../../../gimpformats/binaryiotools.py#L608)

Get a double.

#### Signature

```python
@property
def double(self) -> float: ...
```

### IO().double

[Show source in binaryiotools.py:613](../../../gimpformats/binaryiotools.py#L613)

Set a double.

#### Signature

```python
@double.setter
def double(self, floating: float) -> None: ...
```

### IO().dword

[Show source in binaryiotools.py:248](../../../gimpformats/binaryiotools.py#L248)

Get a dword.

#### Signature

```python
@property
def dword(self) -> Any: ...
```

### IO().dword

[Show source in binaryiotools.py:253](../../../gimpformats/binaryiotools.py#L253)

Set a dword.

#### Signature

```python
@dword.setter
def dword(self, dword: Any) -> None: ...
```

### IO().endContext

[Show source in binaryiotools.py:107](../../../gimpformats/binaryiotools.py#L107)

Restore the index to the previous location where it was when	beginContext() was called.

#### Signature

```python
def endContext(self) -> None: ...
```

### IO().float32

[Show source in binaryiotools.py:408](../../../gimpformats/binaryiotools.py#L408)

Get a float32.

#### Signature

```python
@property
def float32(self) -> float: ...
```

### IO().float32

[Show source in binaryiotools.py:415](../../../gimpformats/binaryiotools.py#L415)

Set a float32.

#### Signature

```python
@float32.setter
def float32(self, float32: float) -> None: ...
```

### IO().float32be

[Show source in binaryiotools.py:618](../../../gimpformats/binaryiotools.py#L618)

Read the next 32 bit float and advance the index.

#### Signature

```python
@property
def float32be(self) -> float: ...
```

### IO().float32be

[Show source in binaryiotools.py:623](../../../gimpformats/binaryiotools.py#L623)

Set a 32 bit float.

#### Signature

```python
@float32be.setter
def float32be(self, float32be: float) -> None: ...
```

### IO().float32le

[Show source in binaryiotools.py:628](../../../gimpformats/binaryiotools.py#L628)

Read the next 32 bit float and advance the index.

#### Signature

```python
@property
def float32le(self) -> float: ...
```

### IO().float32le

[Show source in binaryiotools.py:633](../../../gimpformats/binaryiotools.py#L633)

Set a 32 bit float.

#### Signature

```python
@float32le.setter
def float32le(self, float32le: float) -> None: ...
```

### IO().float64

[Show source in binaryiotools.py:423](../../../gimpformats/binaryiotools.py#L423)

Get a float64.

#### Signature

```python
@property
def float64(self) -> float: ...
```

### IO().float64

[Show source in binaryiotools.py:430](../../../gimpformats/binaryiotools.py#L430)

Set a float64.

#### Signature

```python
@float64.setter
def float64(self, float64: float) -> None: ...
```

### IO().float64be

[Show source in binaryiotools.py:638](../../../gimpformats/binaryiotools.py#L638)

Read the next 64 bit float and advance the index.

#### Signature

```python
@property
def float64be(self) -> float: ...
```

### IO().float64be

[Show source in binaryiotools.py:643](../../../gimpformats/binaryiotools.py#L643)

Set a 64 bit float.

#### Signature

```python
@float64be.setter
def float64be(self, float64be: float) -> None: ...
```

### IO().float64le

[Show source in binaryiotools.py:648](../../../gimpformats/binaryiotools.py#L648)

Read the next 64 bit float and advance the index.

#### Signature

```python
@property
def float64le(self) -> float: ...
```

### IO().float64le

[Show source in binaryiotools.py:653](../../../gimpformats/binaryiotools.py#L653)

Set a 64 bit float.

#### Signature

```python
@float64le.setter
def float64le(self, float64le: float) -> None: ...
```

### IO().floating

[Show source in binaryiotools.py:598](../../../gimpformats/binaryiotools.py#L598)

Get a float.

#### Signature

```python
@property
def floating(self) -> float: ...
```

### IO().floating

[Show source in binaryiotools.py:603](../../../gimpformats/binaryiotools.py#L603)

Set a float.

#### Signature

```python
@floating.setter
def floating(self, floating: float) -> None: ...
```

### IO().getbytearray

[Show source in binaryiotools.py:658](../../../gimpformats/binaryiotools.py#L658)

Grab some raw bytearray and advance the index.

#### Signature

```python
def getbytearray(self, nbytearray: int): ...
```

### IO().i16

[Show source in binaryiotools.py:318](../../../gimpformats/binaryiotools.py#L318)

Get an int16.

#### Signature

```python
@property
def i16(self) -> int: ...
```

### IO().i16

[Show source in binaryiotools.py:325](../../../gimpformats/binaryiotools.py#L325)

Set an int16.

#### Signature

```python
@i16.setter
def i16(self, i16: int) -> None: ...
```

### IO().i16be

[Show source in binaryiotools.py:508](../../../gimpformats/binaryiotools.py#L508)

Read the next signed int16 and advance the index.

#### Signature

```python
@property
def i16be(self) -> int: ...
```

### IO().i16be

[Show source in binaryiotools.py:513](../../../gimpformats/binaryiotools.py#L513)

Set the int16.

#### Signature

```python
@i16be.setter
def i16be(self, i16be: int) -> None: ...
```

### IO().i16le

[Show source in binaryiotools.py:498](../../../gimpformats/binaryiotools.py#L498)

Read the next signed int16 and advance the index.

#### Signature

```python
@property
def i16le(self) -> int: ...
```

### IO().i16le

[Show source in binaryiotools.py:503](../../../gimpformats/binaryiotools.py#L503)

Set the int16.

#### Signature

```python
@i16le.setter
def i16le(self, i16le: int) -> None: ...
```

### IO().i32

[Show source in binaryiotools.py:348](../../../gimpformats/binaryiotools.py#L348)

Get an int32.

#### Signature

```python
@property
def i32(self) -> int: ...
```

### IO().i32

[Show source in binaryiotools.py:355](../../../gimpformats/binaryiotools.py#L355)

Set an int32.

#### Signature

```python
@i32.setter
def i32(self, i32: int) -> None: ...
```

### IO().i32be

[Show source in binaryiotools.py:548](../../../gimpformats/binaryiotools.py#L548)

Read the next signed int32 and advance the index.

#### Signature

```python
@property
def i32be(self) -> int: ...
```

### IO().i32be

[Show source in binaryiotools.py:553](../../../gimpformats/binaryiotools.py#L553)

Set the int32.

#### Signature

```python
@i32be.setter
def i32be(self, i32be: int) -> None: ...
```

### IO().i32le

[Show source in binaryiotools.py:538](../../../gimpformats/binaryiotools.py#L538)

Read the next signed int32 and advance the index.

#### Signature

```python
@property
def i32le(self) -> int: ...
```

### IO().i32le

[Show source in binaryiotools.py:543](../../../gimpformats/binaryiotools.py#L543)

Set the int32.

#### Signature

```python
@i32le.setter
def i32le(self, i32le: int) -> None: ...
```

### IO().i64

[Show source in binaryiotools.py:378](../../../gimpformats/binaryiotools.py#L378)

Get an int64.

#### Signature

```python
@property
def i64(self) -> int: ...
```

### IO().i64

[Show source in binaryiotools.py:385](../../../gimpformats/binaryiotools.py#L385)

Set an int64.

#### Signature

```python
@i64.setter
def i64(self, i64: int) -> None: ...
```

### IO().i64be

[Show source in binaryiotools.py:588](../../../gimpformats/binaryiotools.py#L588)

Read the next signed int64 and advance the index.

#### Signature

```python
@property
def i64be(self) -> int: ...
```

### IO().i64be

[Show source in binaryiotools.py:593](../../../gimpformats/binaryiotools.py#L593)

Set the int64.

#### Signature

```python
@i64be.setter
def i64be(self, i64be: int) -> None: ...
```

### IO().i64le

[Show source in binaryiotools.py:578](../../../gimpformats/binaryiotools.py#L578)

Read the next signed int64 and advance the index.

#### Signature

```python
@property
def i64le(self) -> int: ...
```

### IO().i64le

[Show source in binaryiotools.py:583](../../../gimpformats/binaryiotools.py#L583)

Set the int64.

#### Signature

```python
@i64le.setter
def i64le(self, i64le: int) -> None: ...
```

### IO().i8

[Show source in binaryiotools.py:288](../../../gimpformats/binaryiotools.py#L288)

Get an int8.

#### Signature

```python
@property
def i8(self) -> int: ...
```

### IO().i8

[Show source in binaryiotools.py:295](../../../gimpformats/binaryiotools.py#L295)

Set an int8.

#### Signature

```python
@i8.setter
def i8(self, i8: int) -> None: ...
```

### IO().i8be

[Show source in binaryiotools.py:468](../../../gimpformats/binaryiotools.py#L468)

Read the next signed int8 and advance the index.

#### Signature

```python
@property
def i8be(self) -> int: ...
```

### IO().i8be

[Show source in binaryiotools.py:473](../../../gimpformats/binaryiotools.py#L473)

Set the int8.

#### Signature

```python
@i8be.setter
def i8be(self, i8be: int) -> None: ...
```

### IO().i8le

[Show source in binaryiotools.py:458](../../../gimpformats/binaryiotools.py#L458)

Read the next signed int8 and advance the index.

#### Signature

```python
@property
def i8le(self) -> int: ...
```

### IO().i8le

[Show source in binaryiotools.py:463](../../../gimpformats/binaryiotools.py#L463)

Set the int8.

#### Signature

```python
@i8le.setter
def i8le(self, i8le: int) -> None: ...
```

### IO().index

[Show source in binaryiotools.py:90](../../../gimpformats/binaryiotools.py#L90)

Return data.

#### Signature

```python
@property
def index(self) -> int: ...
```

### IO().index

[Show source in binaryiotools.py:95](../../../gimpformats/binaryiotools.py#L95)

Set index.

#### Signature

```python
@index.setter
def index(self, index: int) -> None: ...
```

### IO().qword

[Show source in binaryiotools.py:268](../../../gimpformats/binaryiotools.py#L268)

Get a qword.

#### Signature

```python
@property
def qword(self) -> Any: ...
```

### IO().qword

[Show source in binaryiotools.py:273](../../../gimpformats/binaryiotools.py#L273)

Set a qword.

#### Signature

```python
@qword.setter
def qword(self, qword: Any) -> None: ...
```

### IO().setbytearray

[Show source in binaryiotools.py:673](../../../gimpformats/binaryiotools.py#L673)

Add some raw bytearray and advance the index.

alias for addbytearray()

#### Arguments

- `iobytearray` - can be a string, bytearray, or another IO object

#### Signature

```python
def setbytearray(self, iobytearray: Any) -> None: ...
```

### IO().sz754

[Show source in binaryiotools.py:723](../../../gimpformats/binaryiotools.py#L723)

sz754.

#### Signature

```python
@property
def sz754(self) -> Any: ...
```

### IO().sz754

[Show source in binaryiotools.py:728](../../../gimpformats/binaryiotools.py#L728)

Set sz754.

#### Signature

```python
@sz754.setter
def sz754(self, sz754: Any) -> None: ...
```

### IO().sz754A

[Show source in binaryiotools.py:733](../../../gimpformats/binaryiotools.py#L733)

sz754A.

#### Signature

```python
@property
def sz754A(self) -> Any: ...
```

### IO().sz754A

[Show source in binaryiotools.py:738](../../../gimpformats/binaryiotools.py#L738)

Set sz754A.

#### Signature

```python
@sz754A.setter
def sz754A(self, sz754: Any) -> None: ...
```

### IO().sz754U

[Show source in binaryiotools.py:753](../../../gimpformats/binaryiotools.py#L753)

sz754U.

#### Signature

```python
@property
def sz754U(self) -> Any: ...
```

### IO().sz754U

[Show source in binaryiotools.py:758](../../../gimpformats/binaryiotools.py#L758)

Set sz754U.

#### Signature

```python
@sz754U.setter
def sz754U(self, sz754: Any) -> None: ...
```

### IO().sz754W

[Show source in binaryiotools.py:743](../../../gimpformats/binaryiotools.py#L743)

sz754W.

#### Signature

```python
@property
def sz754W(self) -> Any: ...
```

### IO().sz754W

[Show source in binaryiotools.py:748](../../../gimpformats/binaryiotools.py#L748)

Set sz754W.

#### Signature

```python
@sz754W.setter
def sz754W(self, sz754: Any) -> None: ...
```

### IO().textLine

[Show source in binaryiotools.py:792](../../../gimpformats/binaryiotools.py#L792)

Read a sequence of chars until the next new line char.

#### Signature

```python
@property
def textLine(self) -> str: ...
```

### IO().textLine

[Show source in binaryiotools.py:800](../../../gimpformats/binaryiotools.py#L800)

Set a sequence of chars until the next new line char.

#### Signature

```python
@textLine.setter
def textLine(self, text: str) -> None: ...
```

### IO().textLineA

[Show source in binaryiotools.py:807](../../../gimpformats/binaryiotools.py#L807)

Read a sequence of chars until the next new line char in ascii.

#### Signature

```python
@property
def textLineA(self) -> str: ...
```

### IO().textLineA

[Show source in binaryiotools.py:815](../../../gimpformats/binaryiotools.py#L815)

Set a sequence of chars until the next new line char in ascii.

#### Signature

```python
@textLineA.setter
def textLineA(self, text: str) -> None: ...
```

### IO().textLineU

[Show source in binaryiotools.py:837](../../../gimpformats/binaryiotools.py#L837)

Read a sequence of chars until the next new line char in utf-8.

#### Signature

```python
@property
def textLineU(self) -> str: ...
```

### IO().textLineU

[Show source in binaryiotools.py:845](../../../gimpformats/binaryiotools.py#L845)

Set a sequence of chars until the next new line char in utf-8.

#### Signature

```python
@textLineU.setter
def textLineU(self, text: str) -> None: ...
```

### IO().textLineW

[Show source in binaryiotools.py:822](../../../gimpformats/binaryiotools.py#L822)

Read a sequence of chars until the next new line char in ucs-2.

#### Signature

```python
@property
def textLineW(self) -> str: ...
```

### IO().textLineW

[Show source in binaryiotools.py:830](../../../gimpformats/binaryiotools.py#L830)

Set a sequence of chars until the next new line char in ucs-2.

#### Signature

```python
@textLineW.setter
def textLineW(self, text: str) -> None: ...
```

### IO().u16

[Show source in binaryiotools.py:333](../../../gimpformats/binaryiotools.py#L333)

Get an uint16.

#### Signature

```python
@property
def u16(self) -> int: ...
```

### IO().u16

[Show source in binaryiotools.py:340](../../../gimpformats/binaryiotools.py#L340)

Set an unint16.

#### Signature

```python
@u16.setter
def u16(self, u16: int) -> None: ...
```

### IO().u16be

[Show source in binaryiotools.py:478](../../../gimpformats/binaryiotools.py#L478)

Read the next uint16 and advance the index.

#### Signature

```python
@property
def u16be(self) -> int: ...
```

### IO().u16be

[Show source in binaryiotools.py:483](../../../gimpformats/binaryiotools.py#L483)

Set the uint16.

#### Signature

```python
@u16be.setter
def u16be(self, u16be: int) -> None: ...
```

### IO().u16le

[Show source in binaryiotools.py:488](../../../gimpformats/binaryiotools.py#L488)

Read the next uint16 and advance the index.

#### Signature

```python
@property
def u16le(self) -> int: ...
```

### IO().u16le

[Show source in binaryiotools.py:493](../../../gimpformats/binaryiotools.py#L493)

Set the uint16.

#### Signature

```python
@u16le.setter
def u16le(self, u16le: int) -> None: ...
```

### IO().u32

[Show source in binaryiotools.py:363](../../../gimpformats/binaryiotools.py#L363)

Get a uint32.

#### Signature

```python
@property
def u32(self) -> int: ...
```

### IO().u32

[Show source in binaryiotools.py:370](../../../gimpformats/binaryiotools.py#L370)

Set a unint32.

#### Signature

```python
@u32.setter
def u32(self, u32: int) -> None: ...
```

### IO().u32be

[Show source in binaryiotools.py:518](../../../gimpformats/binaryiotools.py#L518)

Read the next uint32 and advance the index.

#### Signature

```python
@property
def u32be(self) -> int: ...
```

### IO().u32be

[Show source in binaryiotools.py:523](../../../gimpformats/binaryiotools.py#L523)

Set the uint32.

#### Signature

```python
@u32be.setter
def u32be(self, u32be: int) -> None: ...
```

### IO().u32le

[Show source in binaryiotools.py:528](../../../gimpformats/binaryiotools.py#L528)

Read the next uint32 and advance the index.

#### Signature

```python
@property
def u32le(self) -> int: ...
```

### IO().u32le

[Show source in binaryiotools.py:533](../../../gimpformats/binaryiotools.py#L533)

Set the uint32.

#### Signature

```python
@u32le.setter
def u32le(self, u32le: int) -> None: ...
```

### IO().u64

[Show source in binaryiotools.py:393](../../../gimpformats/binaryiotools.py#L393)

Get a uint64.

#### Signature

```python
@property
def u64(self) -> int: ...
```

### IO().u64

[Show source in binaryiotools.py:400](../../../gimpformats/binaryiotools.py#L400)

Set a uint64.

#### Signature

```python
@u64.setter
def u64(self, u64: int) -> None: ...
```

### IO().u64be

[Show source in binaryiotools.py:558](../../../gimpformats/binaryiotools.py#L558)

Read the next uint64 and advance the index.

#### Signature

```python
@property
def u64be(self) -> int: ...
```

### IO().u64be

[Show source in binaryiotools.py:563](../../../gimpformats/binaryiotools.py#L563)

Set the uint64.

#### Signature

```python
@u64be.setter
def u64be(self, u64be: int) -> None: ...
```

### IO().u64le

[Show source in binaryiotools.py:568](../../../gimpformats/binaryiotools.py#L568)

Read the next uint64 and advance the index.

#### Signature

```python
@property
def u64le(self) -> int: ...
```

### IO().u64le

[Show source in binaryiotools.py:573](../../../gimpformats/binaryiotools.py#L573)

Set the uint64.

#### Signature

```python
@u64le.setter
def u64le(self, u64le: int) -> None: ...
```

### IO().u8

[Show source in binaryiotools.py:303](../../../gimpformats/binaryiotools.py#L303)

Get an unsigned int.

#### Signature

```python
@property
def u8(self) -> int: ...
```

### IO().u8

[Show source in binaryiotools.py:310](../../../gimpformats/binaryiotools.py#L310)

Set an unsigned int.

#### Signature

```python
@u8.setter
def u8(self, u8: int) -> None: ...
```

### IO().u8be

[Show source in binaryiotools.py:438](../../../gimpformats/binaryiotools.py#L438)

Read the next uint8 and advance the index.

#### Signature

```python
@property
def u8be(self) -> int: ...
```

### IO().u8be

[Show source in binaryiotools.py:443](../../../gimpformats/binaryiotools.py#L443)

Set the uint8.

#### Signature

```python
@u8be.setter
def u8be(self, u8be: int) -> None: ...
```

### IO().u8le

[Show source in binaryiotools.py:448](../../../gimpformats/binaryiotools.py#L448)

Read the next uint8 and advance the index.

#### Signature

```python
@property
def u8le(self) -> int: ...
```

### IO().u8le

[Show source in binaryiotools.py:453](../../../gimpformats/binaryiotools.py#L453)

Set the uint8.

#### Signature

```python
@u8le.setter
def u8le(self, u8le: int) -> None: ...
```

### IO().unsignedByte

[Show source in binaryiotools.py:218](../../../gimpformats/binaryiotools.py#L218)

Get unsigned byte.

#### Signature

```python
@property
def unsignedByte(self) -> Any: ...
```

### IO().unsignedByte

[Show source in binaryiotools.py:223](../../../gimpformats/binaryiotools.py#L223)

Set unsigned byte.

#### Signature

```python
@unsignedByte.setter
def unsignedByte(self, byte: Any) -> None: ...
```

### IO().unsignedDword

[Show source in binaryiotools.py:258](../../../gimpformats/binaryiotools.py#L258)

Get a unsigned dword.

#### Signature

```python
@property
def unsignedDword(self) -> Any: ...
```

### IO().unsignedDword

[Show source in binaryiotools.py:263](../../../gimpformats/binaryiotools.py#L263)

Set an unsigned dword.

#### Signature

```python
@unsignedDword.setter
def unsignedDword(self, unsignedDword: Any) -> None: ...
```

### IO().unsignedQword

[Show source in binaryiotools.py:278](../../../gimpformats/binaryiotools.py#L278)

Get an unsigned qword.

#### Signature

```python
@property
def unsignedQword(self) -> Any: ...
```

### IO().unsignedQword

[Show source in binaryiotools.py:283](../../../gimpformats/binaryiotools.py#L283)

Set an unsigned qword.

#### Signature

```python
@unsignedQword.setter
def unsignedQword(self, unsignedQword: Any) -> None: ...
```

### IO().unsignedWord

[Show source in binaryiotools.py:238](../../../gimpformats/binaryiotools.py#L238)

Get an unsigned word.

#### Signature

```python
@property
def unsignedWord(self) -> Any: ...
```

### IO().unsignedWord

[Show source in binaryiotools.py:243](../../../gimpformats/binaryiotools.py#L243)

Set an unsigned word.

#### Signature

```python
@unsignedWord.setter
def unsignedWord(self, unsignedWord: Any) -> None: ...
```

### IO().word

[Show source in binaryiotools.py:228](../../../gimpformats/binaryiotools.py#L228)

Get a word.

#### Signature

```python
@property
def word(self) -> Any: ...
```

### IO().word

[Show source in binaryiotools.py:233](../../../gimpformats/binaryiotools.py#L233)

Set a word.

#### Signature

```python
@word.setter
def word(self, word: Any) -> None: ...
```