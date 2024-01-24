# Gimpgtptoolpreset

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpgtptoolpreset

> Auto-generated documentation for [gimpformats.GimpGtpToolPreset](../../../gimpformats/GimpGtpToolPreset.py) module.

- [Gimpgtptoolpreset](#gimpgtptoolpreset)
  - [GimpGtpToolPreset](#gimpgtptoolpreset)
    - [GimpGtpToolPreset().__repr__](#gimpgtptoolpreset()__repr__)
    - [GimpGtpToolPreset().decode](#gimpgtptoolpreset()decode)
    - [GimpGtpToolPreset().encode](#gimpgtptoolpreset()encode)
    - [GimpGtpToolPreset().load](#gimpgtptoolpreset()load)
    - [GimpGtpToolPreset().save](#gimpgtptoolpreset()save)
  - [ParenFileValue](#parenfilevalue)
    - [ParenFileValue().__repr__](#parenfilevalue()__repr__)
  - [parenFileDecode](#parenfiledecode)
  - [parenFileEncode](#parenfileencode)
  - [walkTree](#walktree)

## GimpGtpToolPreset

[Show source in GimpGtpToolPreset.py:117](../../../gimpformats/GimpGtpToolPreset.py#L117)

Pure python implementation of the gimp gtp tool preset format.

#### Signature

```python
class GimpGtpToolPreset:
    def __init__(self, fileName: BytesIO | str | None = None) -> None: ...
```

### GimpGtpToolPreset().__repr__

[Show source in GimpGtpToolPreset.py:154](../../../gimpformats/GimpGtpToolPreset.py#L154)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: str = "") -> str: ...
```

### GimpGtpToolPreset().decode

[Show source in GimpGtpToolPreset.py:135](../../../gimpformats/GimpGtpToolPreset.py#L135)

Decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - ignored

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int: ...
```

### GimpGtpToolPreset().encode

[Show source in GimpGtpToolPreset.py:144](../../../gimpformats/GimpGtpToolPreset.py#L144)

Encode to bytes.

#### Signature

```python
def encode(self) -> bytes: ...
```

### GimpGtpToolPreset().load

[Show source in GimpGtpToolPreset.py:127](../../../gimpformats/GimpGtpToolPreset.py#L127)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str) -> None: ...
```

### GimpGtpToolPreset().save

[Show source in GimpGtpToolPreset.py:148](../../../gimpformats/GimpGtpToolPreset.py#L148)

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

[Show source in GimpGtpToolPreset.py:52](../../../gimpformats/GimpGtpToolPreset.py#L52)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```



## parenFileDecode

[Show source in GimpGtpToolPreset.py:70](../../../gimpformats/GimpGtpToolPreset.py#L70)

Decode a parentheses-based file format.

(possibly "scheme" language?)

#### Signature

```python
def parenFileDecode(data: bytes) -> list[ParenFileValue]: ...
```

#### See also

- [ParenFileValue](#parenfilevalue)



## parenFileEncode

[Show source in GimpGtpToolPreset.py:103](../../../gimpformats/GimpGtpToolPreset.py#L103)

Encode a values tree to a buffer.

#### Signature

```python
def parenFileEncode(values: list[ParenFileValue]) -> str: ...
```

#### See also

- [ParenFileValue](#parenfilevalue)



## walkTree

[Show source in GimpGtpToolPreset.py:79](../../../gimpformats/GimpGtpToolPreset.py#L79)

Walk the tree.

#### Signature

```python
def walkTree(items: list[brackettree.RoundNode]) -> list[ParenFileValue]: ...
```

#### See also

- [ParenFileValue](#parenfilevalue)