# Gimpgtptoolpreset

[Gimpformats Index](../README.md#gimpformats-index) /
[Gimpformats](./index.md#gimpformats) /
Gimpgtptoolpreset

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
    def __init__(self, fileName=None): ...
```

### GimpGtpToolPreset().__repr__

[Show source in GimpGtpToolPreset.py:163](../../../gimpformats/GimpGtpToolPreset.py#L163)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent=""): ...
```

### GimpGtpToolPreset().decode

[Show source in GimpGtpToolPreset.py:134](../../../gimpformats/GimpGtpToolPreset.py#L134)

Decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - ignored

#### Signature

```python
def decode(self, data: bytes, index: int = 0): ...
```

### GimpGtpToolPreset().encode

[Show source in GimpGtpToolPreset.py:143](../../../gimpformats/GimpGtpToolPreset.py#L143)

Encode to a byte array.

#### Signature

```python
def encode(self): ...
```

### GimpGtpToolPreset().load

[Show source in GimpGtpToolPreset.py:126](../../../gimpformats/GimpGtpToolPreset.py#L126)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str): ...
```

### GimpGtpToolPreset().save

[Show source in GimpGtpToolPreset.py:147](../../../gimpformats/GimpGtpToolPreset.py#L147)

Save this gimp tool preset to a file.

#### Signature

```python
def save(self, tofileName=None, toExtension=None): ...
```



## ParenFileValue

[Show source in GimpGtpToolPreset.py:12](../../../gimpformats/GimpGtpToolPreset.py#L12)

A parentheses-based file format.

(possibly "scheme" language?)

#### Signature

```python
class ParenFileValue:
    def __init__(self, name: str = None, value: str = "", children=None): ...
```

### ParenFileValue().__repr__

[Show source in GimpGtpToolPreset.py:51](../../../gimpformats/GimpGtpToolPreset.py#L51)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self): ...
```



## parenFileDecode

[Show source in GimpGtpToolPreset.py:69](../../../gimpformats/GimpGtpToolPreset.py#L69)

Decode a parentheses-based file format.

(possibly "scheme" language?)

#### Signature

```python
def parenFileDecode(data: bytes): ...
```



## parenFileEncode

[Show source in GimpGtpToolPreset.py:103](../../../gimpformats/GimpGtpToolPreset.py#L103)

Encode a values tree to a buffer.

#### Signature

```python
def parenFileEncode(values): ...
```



## walkTree

[Show source in GimpGtpToolPreset.py:79](../../../gimpformats/GimpGtpToolPreset.py#L79)

Walk the tree.

#### Signature

```python
def walkTree(items): ...
```