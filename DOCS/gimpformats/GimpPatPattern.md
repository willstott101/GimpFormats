# GimpPatPattern

> Auto-generated documentation for [gimpformats.GimpPatPattern](../../gimpformats/GimpPatPattern.py) module.

Pure python implementation of a gimp pattern file

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / GimpPatPattern
    - [GimpPatPattern](#gimppatpattern)
        - [GimpPatPattern().\_\_repr\_\_](#gimppatpattern__repr__)
        - [GimpPatPattern().decode](#gimppatpatterndecode)
        - [GimpPatPattern().encode](#gimppatpatternencode)
        - [GimpPatPattern().image](#gimppatpatternimage)
        - [GimpPatPattern().image](#gimppatpatternimage)
        - [GimpPatPattern().load](#gimppatpatternload)
        - [GimpPatPattern().save](#gimppatpatternsave)
        - [GimpPatPattern().size](#gimppatpatternsize)

## GimpPatPattern

[[find in source code]](../../gimpformats/GimpPatPattern.py#L11)

```python
class GimpPatPattern():
    def __init__(fileName=None):
```

Pure python implementation of a gimp pattern file

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/pat.txt

### GimpPatPattern().\_\_repr\_\_

[[find in source code]](../../gimpformats/GimpPatPattern.py#L139)

```python
def __repr__(indent=''):
```

Get a textual representation of this object

### GimpPatPattern().decode

[[find in source code]](../../gimpformats/GimpPatPattern.py#L50)

```python
def decode(data, index=0):
```

decode a byte buffer

#### Arguments

- `data` - data buffer to decode
- `index` - index within the buffer to start at

### GimpPatPattern().encode

[[find in source code]](../../gimpformats/GimpPatPattern.py#L72)

```python
def encode():
```

encode to a byte buffer

### GimpPatPattern().image

[[find in source code]](../../gimpformats/GimpPatPattern.py#L98)

```python
@property
def image():
```

get a final, compiled image

### GimpPatPattern().image

[[find in source code]](../../gimpformats/GimpPatPattern.py#L112)

```python
@image.setter
def image(image):
```

### GimpPatPattern().load

[[find in source code]](../../gimpformats/GimpPatPattern.py#L34)

```python
def load(fileName: Union[(BytesIO, str)]):
```

load a gimp file

#### Arguments

- `fileName` - can be a file name or a file-like object

### GimpPatPattern().save

[[find in source code]](../../gimpformats/GimpPatPattern.py#L117)

```python
def save(tofileName=None, toExtension=None):
```

save this gimp image to a file

### GimpPatPattern().size

[[find in source code]](../../gimpformats/GimpPatPattern.py#L91)

```python
@property
def size():
```

the size of the pattern
