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

[Show source in GimpGtpToolPreset.py:118](../../../gimpformats/GimpGtpToolPreset.py#L118)

Pure python implementation of the gimp gtp tool preset format.

#### Signature

```python
class GimpGtpToolPreset:
    def __init__(self, fileName=None):
        ...
```

### GimpGtpToolPreset().__repr__

[Show source in GimpGtpToolPreset.py:164](../../../gimpformats/GimpGtpToolPreset.py#L164)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent=""):
    ...
```

### GimpGtpToolPreset().decode

[Show source in GimpGtpToolPreset.py:135](../../../gimpformats/GimpGtpToolPreset.py#L135)

Decode a byte buffer.

#### Arguments

- `data` - data buffer to decode
- `index` - ignored

#### Signature

```python
def decode(self, data: bytes, index: int = 0):
    ...
```

### GimpGtpToolPreset().encode

[Show source in GimpGtpToolPreset.py:144](../../../gimpformats/GimpGtpToolPreset.py#L144)

Encode to a byte array.

#### Signature

```python
def encode(self):
    ...
```

### GimpGtpToolPreset().load

[Show source in GimpGtpToolPreset.py:127](../../../gimpformats/GimpGtpToolPreset.py#L127)

Load a gimp file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str):
    ...
```

### GimpGtpToolPreset().save

[Show source in GimpGtpToolPreset.py:148](../../../gimpformats/GimpGtpToolPreset.py#L148)

Save this gimp tool preset to a file.

#### Signature

```python
def save(self, tofileName=None, toExtension=None):
    ...
```



## ParenFileValue

[Show source in GimpGtpToolPreset.py:13](../../../gimpformats/GimpGtpToolPreset.py#L13)

A parentheses-based file format.

(possibly "scheme" language?)

#### Signature

```python
class ParenFileValue:
    def __init__(self, name: str = None, value: str = "", children=None):
        ...
```

### ParenFileValue().__repr__

[Show source in GimpGtpToolPreset.py:52](../../../gimpformats/GimpGtpToolPreset.py#L52)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self):
    ...
```



## parenFileDecode

[Show source in GimpGtpToolPreset.py:70](../../../gimpformats/GimpGtpToolPreset.py#L70)

Decode a parentheses-based file format.

(possibly "scheme" language?)

#### Signature

```python
def parenFileDecode(data: bytes):
    ...
```



## parenFileEncode

[Show source in GimpGtpToolPreset.py:104](../../../gimpformats/GimpGtpToolPreset.py#L104)

Encode a values tree to a buffer.

#### Signature

```python
def parenFileEncode(values):
    ...
```



## walkTree

[Show source in GimpGtpToolPreset.py:80](../../../gimpformats/GimpGtpToolPreset.py#L80)

Walk the tree.

#### Signature

```python
def walkTree(items):
    ...
```


