# GimpGtpToolPreset

> Auto-generated documentation for [gimpformats.GimpGtpToolPreset](../../gimpformats/GimpGtpToolPreset.py) module.

Pure python implementation of the gimp gtp tool preset format.

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / GimpGtpToolPreset
    - [GimpGtpToolPreset](#gimpgtptoolpreset)
        - [GimpGtpToolPreset().\_\_repr\_\_](#gimpgtptoolpreset__repr__)
        - [GimpGtpToolPreset().decode](#gimpgtptoolpresetdecode)
        - [GimpGtpToolPreset().encode](#gimpgtptoolpresetencode)
        - [GimpGtpToolPreset().load](#gimpgtptoolpresetload)
        - [GimpGtpToolPreset().save](#gimpgtptoolpresetsave)
    - [ParenFileValue](#parenfilevalue)
        - [ParenFileValue().\_\_repr\_\_](#parenfilevalue__repr__)
    - [parenFileDecode](#parenfiledecode)
    - [parenFileEncode](#parenfileencode)
    - [walkTree](#walktree)

## GimpGtpToolPreset

[[find in source code]](../../gimpformats/GimpGtpToolPreset.py#L118)

```python
class GimpGtpToolPreset():
    def __init__(fileName=None):
```

Pure python implementation of the gimp gtp tool preset format.

### GimpGtpToolPreset().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpGtpToolPreset.py#L164)

```python
def __repr__(indent=''):
```

Get a textual representation of this object.

### GimpGtpToolPreset().decode

[[find in source code]](../../gimpformats/GimpGtpToolPreset.py#L135)

```python
def decode(data: bytes, index: int = 0):
```

Decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - ignored

### GimpGtpToolPreset().encode

[[find in source code]](../../gimpformats/GimpGtpToolPreset.py#L144)

```python
def encode():
```

Encode to a byte array.

### GimpGtpToolPreset().load

[[find in source code]](../../gimpformats/GimpGtpToolPreset.py#L127)

```python
def load(fileName: BytesIO | str):
```

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

### GimpGtpToolPreset().save

[[find in source code]](../../gimpformats/GimpGtpToolPreset.py#L148)

```python
def save(tofileName=None, toExtension=None):
```

Save this gimp tool preset to a file.

## ParenFileValue

[[find in source code]](../../gimpformats/GimpGtpToolPreset.py#L13)

```python
class ParenFileValue():
    def __init__(name: str = None, value: str = '', children=None):
```

A parentheses-based file format.

(possibly "scheme" language?)

### ParenFileValue().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpGtpToolPreset.py#L52)

```python
def __repr__():
```

Get a textual representation of this object.

## parenFileDecode

[[find in source code]](../../gimpformats/GimpGtpToolPreset.py#L70)

```python
def parenFileDecode(data):
```

Decode a parentheses-based file format.

(possibly "scheme" language?)

## parenFileEncode

[[find in source code]](../../gimpformats/GimpGtpToolPreset.py#L104)

```python
def parenFileEncode(values):
```

Encode a values tree to a buffer.

## walkTree

[[find in source code]](../../gimpformats/GimpGtpToolPreset.py#L80)

```python
def walkTree(items):
```

Walk the tree.
