# Gimpgtptoolpreset

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpgtptoolpreset

> Auto-generated documentation for [gimpformats.GimpGtpToolPreset](../../../gimpformats/GimpGtpToolPreset.py) module.

- [Gimpgtptoolpreset](#gimpgtptoolpreset)
  - [GimpGtpToolPreset](#gimpgtptoolpreset)
    - [GimpGtpToolPreset().__repr__](#gimpgtptoolpreset()__repr__)
    - [GimpGtpToolPreset().__str__](#gimpgtptoolpreset()__str__)
    - [GimpGtpToolPreset().decode](#gimpgtptoolpreset()decode)
    - [GimpGtpToolPreset().encode](#gimpgtptoolpreset()encode)
    - [GimpGtpToolPreset().full_repr](#gimpgtptoolpreset()full_repr)
    - [GimpGtpToolPreset().load](#gimpgtptoolpreset()load)
    - [GimpGtpToolPreset().save](#gimpgtptoolpreset()save)
  - [ParenFileValue](#parenfilevalue)
    - [ParenFileValue().__repr__](#parenfilevalue()__repr__)
    - [ParenFileValue().__str__](#parenfilevalue()__str__)
    - [ParenFileValue().full_repr](#parenfilevalue()full_repr)
  - [parenFileDecode](#parenfiledecode)
  - [parenFileEncode](#parenfileencode)
  - [walkTree](#walktree)

## GimpGtpToolPreset

[Show source in GimpGtpToolPreset.py:116](../../../gimpformats/GimpGtpToolPreset.py#L116)

Pure python implementation of the gimp gtp tool preset format.

#### Signature

```python
class GimpGtpToolPreset:
    def __init__(self, fileName: BytesIO | str | None = None) -> None: ...
```

### GimpGtpToolPreset().__repr__

[Show source in GimpGtpToolPreset.py:155](../../../gimpformats/GimpGtpToolPreset.py#L155)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpGtpToolPreset().__str__

[Show source in GimpGtpToolPreset.py:151](../../../gimpformats/GimpGtpToolPreset.py#L151)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpGtpToolPreset().decode

[Show source in GimpGtpToolPreset.py:134](../../../gimpformats/GimpGtpToolPreset.py#L134)

Decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - ignored

#### Signature

```python
def decode(self, data: bytearray | bytes, index: int = 0) -> int: ...
```

### GimpGtpToolPreset().encode

[Show source in GimpGtpToolPreset.py:143](../../../gimpformats/GimpGtpToolPreset.py#L143)

Encode to bytearray.

#### Signature

```python
def encode(self) -> bytes: ...
```

### GimpGtpToolPreset().full_repr

[Show source in GimpGtpToolPreset.py:159](../../../gimpformats/GimpGtpToolPreset.py#L159)

Get a textual representation of this object.

#### Signature

```python
def full_repr(self, indent: int = 0) -> str: ...
```

### GimpGtpToolPreset().load

[Show source in GimpGtpToolPreset.py:126](../../../gimpformats/GimpGtpToolPreset.py#L126)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str) -> None: ...
```

### GimpGtpToolPreset().save

[Show source in GimpGtpToolPreset.py:147](../../../gimpformats/GimpGtpToolPreset.py#L147)

Save this gimp image to a file.

#### Signature

```python
def save(self, tofileName: str | BytesIO) -> None: ...
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

[Show source in GimpGtpToolPreset.py:43](../../../gimpformats/GimpGtpToolPreset.py#L43)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### ParenFileValue().__str__

[Show source in GimpGtpToolPreset.py:39](../../../gimpformats/GimpGtpToolPreset.py#L39)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### ParenFileValue().full_repr

[Show source in GimpGtpToolPreset.py:51](../../../gimpformats/GimpGtpToolPreset.py#L51)

Get a textual representation of this object.

#### Signature

```python
def full_repr(self) -> str: ...
```



## parenFileDecode

[Show source in GimpGtpToolPreset.py:69](../../../gimpformats/GimpGtpToolPreset.py#L69)

Decode a parentheses-based file format.

(possibly "scheme" language?)

#### Signature

```python
def parenFileDecode(data: bytearray) -> list[ParenFileValue]: ...
```

#### See also

- [ParenFileValue](#parenfilevalue)



## parenFileEncode

[Show source in GimpGtpToolPreset.py:102](../../../gimpformats/GimpGtpToolPreset.py#L102)

Encode a values tree to a buffer.

#### Signature

```python
def parenFileEncode(values: list[ParenFileValue]) -> str: ...
```

#### See also

- [ParenFileValue](#parenfilevalue)



## walkTree

[Show source in GimpGtpToolPreset.py:78](../../../gimpformats/GimpGtpToolPreset.py#L78)

Walk the tree.

#### Signature

```python
def walkTree(items: list[brackettree.RoundNode]) -> list[ParenFileValue]: ...
```

#### See also

- [ParenFileValue](#parenfilevalue)