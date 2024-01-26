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

[Show source in GimpGtpToolPreset.py:121](../../../gimpformats/GimpGtpToolPreset.py#L121)

Pure python implementation of the gimp gtp tool preset format.

#### Signature

```python
class GimpGtpToolPreset:
    def __init__(self, fileName: BytesIO | str | None = None) -> None: ...
```

### GimpGtpToolPreset().__repr__

[Show source in GimpGtpToolPreset.py:162](../../../gimpformats/GimpGtpToolPreset.py#L162)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: int = 0) -> str: ...
```

### GimpGtpToolPreset().__str__

[Show source in GimpGtpToolPreset.py:158](../../../gimpformats/GimpGtpToolPreset.py#L158)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpGtpToolPreset().decode

[Show source in GimpGtpToolPreset.py:139](../../../gimpformats/GimpGtpToolPreset.py#L139)

Decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - ignored

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int: ...
```

### GimpGtpToolPreset().encode

[Show source in GimpGtpToolPreset.py:148](../../../gimpformats/GimpGtpToolPreset.py#L148)

Encode to bytes.

#### Signature

```python
def encode(self) -> bytes: ...
```

### GimpGtpToolPreset().load

[Show source in GimpGtpToolPreset.py:131](../../../gimpformats/GimpGtpToolPreset.py#L131)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str) -> None: ...
```

### GimpGtpToolPreset().save

[Show source in GimpGtpToolPreset.py:152](../../../gimpformats/GimpGtpToolPreset.py#L152)

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

[Show source in GimpGtpToolPreset.py:56](../../../gimpformats/GimpGtpToolPreset.py#L56)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### ParenFileValue().__str__

[Show source in GimpGtpToolPreset.py:52](../../../gimpformats/GimpGtpToolPreset.py#L52)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```



## parenFileDecode

[Show source in GimpGtpToolPreset.py:74](../../../gimpformats/GimpGtpToolPreset.py#L74)

Decode a parentheses-based file format.

(possibly "scheme" language?)

#### Signature

```python
def parenFileDecode(data: bytes) -> list[ParenFileValue]: ...
```

#### See also

- [ParenFileValue](#parenfilevalue)



## parenFileEncode

[Show source in GimpGtpToolPreset.py:107](../../../gimpformats/GimpGtpToolPreset.py#L107)

Encode a values tree to a buffer.

#### Signature

```python
def parenFileEncode(values: list[ParenFileValue]) -> str: ...
```

#### See also

- [ParenFileValue](#parenfilevalue)



## walkTree

[Show source in GimpGtpToolPreset.py:83](../../../gimpformats/GimpGtpToolPreset.py#L83)

Walk the tree.

#### Signature

```python
def walkTree(items: list[brackettree.RoundNode]) -> list[ParenFileValue]: ...
```

#### See also

- [ParenFileValue](#parenfilevalue)