# Gimpgtptoolpreset

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpgtptoolpreset

> Auto-generated documentation for [gimpformats.GimpGtpToolPreset](../../../gimpformats/GimpGtpToolPreset.py) module.

- [Gimpgtptoolpreset](#gimpgtptoolpreset)
  - [GimpGtpToolPreset](#gimpgtptoolpreset)
    - [GimpGtpToolPreset().__repr__](#gimpgtptoolpreset()__repr__)
    - [GimpGtpToolPreset().__str__](#gimpgtptoolpreset()__str__)
    - [GimpGtpToolPreset().decode](#gimpgtptoolpreset()decode)
    - [GimpGtpToolPreset().encode](#gimpgtptoolpreset()encode)
    - [GimpGtpToolPreset().load](#gimpgtptoolpreset()load)
    - [GimpGtpToolPreset().save](#gimpgtptoolpreset()save)
  - [ParenFileValue](#parenfilevalue)
    - [ParenFileValue().__repr__](#parenfilevalue()__repr__)
    - [ParenFileValue().__str__](#parenfilevalue()__str__)
  - [parenFileDecode](#parenfiledecode)
  - [parenFileEncode](#parenfileencode)
  - [walkTree](#walktree)

## GimpGtpToolPreset

[Show source in GimpGtpToolPreset.py:122](../../../gimpformats/GimpGtpToolPreset.py#L122)

Pure python implementation of the gimp gtp tool preset format.

#### Signature

```python
class GimpGtpToolPreset:
    def __init__(self, fileName: BytesIO | str | None = None) -> None: ...
```

### GimpGtpToolPreset().__repr__

[Show source in GimpGtpToolPreset.py:163](../../../gimpformats/GimpGtpToolPreset.py#L163)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: int = 0) -> str: ...
```

### GimpGtpToolPreset().__str__

[Show source in GimpGtpToolPreset.py:159](../../../gimpformats/GimpGtpToolPreset.py#L159)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpGtpToolPreset().decode

[Show source in GimpGtpToolPreset.py:140](../../../gimpformats/GimpGtpToolPreset.py#L140)

Decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - ignored

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int: ...
```

### GimpGtpToolPreset().encode

[Show source in GimpGtpToolPreset.py:149](../../../gimpformats/GimpGtpToolPreset.py#L149)

Encode to bytes.

#### Signature

```python
def encode(self) -> bytes: ...
```

### GimpGtpToolPreset().load

[Show source in GimpGtpToolPreset.py:132](../../../gimpformats/GimpGtpToolPreset.py#L132)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str) -> None: ...
```

### GimpGtpToolPreset().save

[Show source in GimpGtpToolPreset.py:153](../../../gimpformats/GimpGtpToolPreset.py#L153)

Save this gimp tool preset to a file.

#### Signature

```python
def save(self, tofileName: str | BytesIO | None = None) -> None: ...
```



## ParenFileValue

[Show source in GimpGtpToolPreset.py:12](../../../gimpformats/GimpGtpToolPreset.py#L12)

A parentheses-based file format.

(possibly "scheme" language?)

#### Signature

```python
class ParenFileValue:
    def __init__(
        self, name: str | None = None, value: str = "", children=None
    ) -> None: ...
```

### ParenFileValue().__repr__

[Show source in GimpGtpToolPreset.py:57](../../../gimpformats/GimpGtpToolPreset.py#L57)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### ParenFileValue().__str__

[Show source in GimpGtpToolPreset.py:53](../../../gimpformats/GimpGtpToolPreset.py#L53)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```



## parenFileDecode

[Show source in GimpGtpToolPreset.py:75](../../../gimpformats/GimpGtpToolPreset.py#L75)

Decode a parentheses-based file format.

(possibly "scheme" language?)

#### Signature

```python
def parenFileDecode(data: bytes) -> list[ParenFileValue]: ...
```

#### See also

- [ParenFileValue](#parenfilevalue)



## parenFileEncode

[Show source in GimpGtpToolPreset.py:108](../../../gimpformats/GimpGtpToolPreset.py#L108)

Encode a values tree to a buffer.

#### Signature

```python
def parenFileEncode(values: list[ParenFileValue]) -> str: ...
```

#### See also

- [ParenFileValue](#parenfilevalue)



## walkTree

[Show source in GimpGtpToolPreset.py:84](../../../gimpformats/GimpGtpToolPreset.py#L84)

Walk the tree.

#### Signature

```python
def walkTree(items: list[brackettree.RoundNode]) -> list[ParenFileValue]: ...
```

#### See also

- [ParenFileValue](#parenfilevalue)