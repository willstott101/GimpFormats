# Gimpxcfdocument

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpxcfdocument

> Auto-generated documentation for [gimpformats.gimpXcfDocument](../../../gimpformats/gimpXcfDocument.py) module.

- [Gimpxcfdocument](#gimpxcfdocument)
  - [GimpDocument](#gimpdocument)
    - [GimpDocument().__repr__](#gimpdocument()__repr__)
    - [GimpDocument().__str__](#gimpdocument()__str__)
    - [GimpDocument()._render](#gimpdocument()_render)
    - [GimpDocument().decode](#gimpdocument()decode)
    - [GimpDocument().deleteRawLayer](#gimpdocument()deleterawlayer)
    - [GimpDocument().encode](#gimpdocument()encode)
    - [GimpDocument().forceFullyLoaded](#gimpdocument()forcefullyloaded)
    - [GimpDocument().full_repr](#gimpdocument()full_repr)
    - [GimpDocument().getLayer](#gimpdocument()getlayer)
    - [GimpDocument().image](#gimpdocument()image)
    - [GimpDocument().insertRawLayer](#gimpdocument()insertrawlayer)
    - [GimpDocument().iterablePointerDecoder](#gimpdocument()iterablepointerdecoder)
    - [GimpDocument().load](#gimpdocument()load)
    - [GimpDocument().newLayer](#gimpdocument()newlayer)
    - [GimpDocument().raw_layers](#gimpdocument()raw_layers)
    - [GimpDocument().render](#gimpdocument()render)
    - [GimpDocument().save](#gimpdocument()save)
    - [GimpDocument().saveNew](#gimpdocument()savenew)
    - [GimpDocument().setRawLayer](#gimpdocument()setrawlayer)
    - [GimpDocument().walkTree](#gimpdocument()walktree)
  - [GimpGroup](#gimpgroup)
    - [GimpGroup().__repr__](#gimpgroup()__repr__)
    - [GimpGroup().add_layer](#gimpgroup()add_layer)
    - [GimpGroup().get_group](#gimpgroup()get_group)
  - [applyMask](#applymask)
  - [blendModeLookup](#blendmodelookup)
  - [make_thumbnail](#make_thumbnail)
  - [pil2np](#pil2np)

## GimpDocument

[Show source in gimpXcfDocument.py:60](../../../gimpformats/gimpXcfDocument.py#L60)

Pure python implementation of the gimp file format.

Has a series of attributes including the following:
self._layers = None
self._layerPtr = []
self._channels = []
self._channelPtr = []
self.version = None
self.width = 0
self.height = 0
self.baseColorMode = 0
self.precision = None # Precision object
self._data = None

The image structure always starts at offset 0 in the XCF file.

byte[9]     "gimp xcf " File type identification
byte[4]     version     XCF version
byte        0            Zero marks the end of the version tag.
uint32      width        Width of canvas
uint32      height       Height of canvas
uint32      base_type    Color mode of the image; one of
       0: RGB color; 1: Grayscale; 2: Indexed color
uint32      precision    Image precision; this field is only present for
      XCF 4 or over (since GIMP 2.10.0).
property-list        Image properties
,-----------------   Repeat once for each layer, topmost layer first:
| pointer lptr       Pointer to the layer structure.
`--
pointer   0           Zero marks the end of the array of layer pointers.
,------------------  Repeat once for each channel, in no particular order:
| pointer cptr       Pointer to the channel structure.
`--
pointer   0           Zero marks the end of the array of channel pointers.
,------------------  Repeat once for each path, in no particular order:
| pointer cptr       Pointer to the vectors structure.
`--
pointer   0           Zero marks the end of the array of vectors pointers.

#### Signature

```python
class GimpDocument(GimpIOBase):
    def __init__(self, fileName: BytesIO | str | None = None) -> None: ...
```

#### See also

- [GimpIOBase](./GimpIOBase.md#gimpiobase)

### GimpDocument().__repr__

[Show source in gimpXcfDocument.py:437](../../../gimpformats/gimpXcfDocument.py#L437)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpDocument().__str__

[Show source in gimpXcfDocument.py:433](../../../gimpformats/gimpXcfDocument.py#L433)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpDocument()._render

[Show source in gimpXcfDocument.py:481](../../../gimpformats/gimpXcfDocument.py#L481)

Perform the full project render over the current project.

#### Returns

Type: *PIL.Image*
The fully composited image

#### Signature

```python
def _render(self, current_group: GimpGroup) -> np.ndarray: ...
```

#### See also

- [GimpGroup](#gimpgroup)

### GimpDocument().decode

[Show source in gimpXcfDocument.py:176](../../../gimpformats/gimpXcfDocument.py#L176)

Decode the XCF Header to a GimpDocument.

:param bytearray | bytes data: raw bytes representing the GimpDocument/XCF

#### Arguments

- `index` *int* - An optional start index, only set this if you know what you're doing :)

Note that this decode function is somewhat lazy with what is decoded. For example,
for the layers, the pointers and basic layer info is decoded, in addition to the
pointers to the image_hierarchy and masks. However, the actual image data is not loaded.

Image data will be fetched when when calling descendants `.image` method as
appropriate

byte[9]     "gimp xcf "
byte[4]     version
byte        0
uint32      width
uint32      height
uint32      base_type
uint32      precision
property-list        Image properties
,-----------------
| pointer lptr       layer structure.
`--
pointer   0
,------------------
| pointer cptr       channel structure.
`--
pointer   0
,------------------
| pointer cptr       vectors structure.
`--
pointer   0

#### Signature

```python
def decode(self, data: bytearray | bytes, index: int = 0) -> int: ...
```

### GimpDocument().deleteRawLayer

[Show source in gimpXcfDocument.py:378](../../../gimpformats/gimpXcfDocument.py#L378)

Delete a layer.

#### Signature

```python
def deleteRawLayer(self, index: int) -> None: ...
```

### GimpDocument().encode

[Show source in gimpXcfDocument.py:241](../../../gimpformats/gimpXcfDocument.py#L241)

Encode to bytearray.

Similarly to decode, we must start by constructing the XCF header, though we must
then add the bytes returned when calling descendants `.encode` method as
appropriate

byte[9]     "gimp xcf "
byte[4]     version
byte        0
uint32      width
uint32      height
uint32      base_type
uint32      precision
property-list        Image properties
,-----------------
| pointer lptr       layer structure.
`--
pointer   0
,------------------
| pointer cptr       channel structure.
`--
pointer   0
,------------------
| pointer cptr       vectors structure.
`--
pointer   0

#### Signature

```python
def encode(self) -> bytearray: ...
```

### GimpDocument().forceFullyLoaded

[Show source in gimpXcfDocument.py:303](../../../gimpformats/gimpXcfDocument.py#L303)

Make sure everything is fully loaded from the file.

#### Signature

```python
def forceFullyLoaded(self) -> None: ...
```

### GimpDocument().full_repr

[Show source in gimpXcfDocument.py:445](../../../gimpformats/gimpXcfDocument.py#L445)

Get a textual representation of this object.

#### Signature

```python
def full_repr(self, indent: int = 0) -> str: ...
```

### GimpDocument().getLayer

[Show source in gimpXcfDocument.py:335](../../../gimpformats/gimpXcfDocument.py#L335)

Return a given layer.

#### Signature

```python
def getLayer(self, index: int) -> GimpLayer | GimpGroup: ...
```

### GimpDocument().image

[Show source in gimpXcfDocument.py:405](../../../gimpformats/gimpXcfDocument.py#L405)

Generates a final, compiled image by processing layers and groups.

#### Signature

```python
@property
def image(self) -> Image.Image: ...
```

### GimpDocument().insertRawLayer

[Show source in gimpXcfDocument.py:370](../../../gimpformats/gimpXcfDocument.py#L370)

Insert a layer object at a specific position.

#### Arguments

- `layer` - the new layer to insert
- `index` - where to insert the new layer (default=top)

#### Signature

```python
def insertRawLayer(self, layer: GimpLayer, index: int = -1) -> None: ...
```

#### See also

- [GimpLayer](./GimpLayer.md#gimplayer)

### GimpDocument().iterablePointerDecoder

[Show source in gimpXcfDocument.py:146](../../../gimpformats/gimpXcfDocument.py#L146)

Iterate over a pointer as defined in the spec. This method is responsible for
returning a list of int pointers (representing indexes in the XCF), and a list of types
representing the data.

EG.

,-----------------
| pointer lptr       layer structure.
`--
pointer   0

#### Arguments

- `ioBuf` *IO* - The raw buffer representing the XCF doc
- `obj` *T* - create instances of this type (and decode into this)

#### Returns

Type: *tuple[list[int], list[T]]*
list of int pointers (representing indexes
in the XCF), and a list of types representing the data.

#### Signature

```python
def iterablePointerDecoder(
    self, ioBuf: IO, cls: type[T]
) -> tuple[list[int], list[T]]: ...
```

#### See also

- [IO](./binaryiotools.md#io)
- [T](#t)

### GimpDocument().load

[Show source in gimpXcfDocument.py:137](../../../gimpformats/gimpXcfDocument.py#L137)

Load a gimp xcf and decode the file. See decode for more on this process.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str) -> None: ...
```

### GimpDocument().newLayer

[Show source in gimpXcfDocument.py:351](../../../gimpformats/gimpXcfDocument.py#L351)

Create a new layer based on a PIL image.

#### Arguments

----
 - `name` *str* - a name for the new layer
 - [GimpDocument().image](#gimpdocumentimage) *Image.Image* - pil image
 - `index` *int, optional* - where to insert the new layer (default=top). Defaults to -1.

#### Returns

-------
 - `GimpLayer` - newly created GimpLayer object

#### Signature

```python
def newLayer(self, name: str, image: Image.Image, index: int = -1) -> GimpLayer: ...
```

#### See also

- [GimpLayer](./GimpLayer.md#gimplayer)

### GimpDocument().raw_layers

[Show source in gimpXcfDocument.py:314](../../../gimpformats/gimpXcfDocument.py#L314)

Decode the image's layers if necessary.

TODO: need to do the same thing with self.Channels

#### Signature

```python
@property
def raw_layers(self) -> list[GimpLayer]: ...
```

#### See also

- [GimpLayer](./GimpLayer.md#gimplayer)

### GimpDocument().render

[Show source in gimpXcfDocument.py:473](../../../gimpformats/gimpXcfDocument.py#L473)

Perform the full project render over the current project.

#### Returns

Type: *PIL.Image*
The fully composited image

#### Signature

```python
def render(self, root_group: GimpGroup) -> Image.Image: ...
```

#### See also

- [GimpGroup](#gimpgroup)

### GimpDocument().save

[Show source in gimpXcfDocument.py:414](../../../gimpformats/gimpXcfDocument.py#L414)

Save this gimp image to a file.

#### Signature

```python
def save(self, filename: str | BytesIO | None = None) -> NoReturn: ...
```

### GimpDocument().saveNew

[Show source in gimpXcfDocument.py:424](../../../gimpformats/gimpXcfDocument.py#L424)

Save a new gimp image to a file.

#### Signature

```python
def saveNew(self, filename: str | None = None) -> NoReturn: ...
```

### GimpDocument().setRawLayer

[Show source in gimpXcfDocument.py:345](../../../gimpformats/gimpXcfDocument.py#L345)

Assign to a given layer.

#### Signature

```python
def setRawLayer(self, index: int, layer: GimpLayer) -> None: ...
```

#### See also

- [GimpLayer](./GimpLayer.md#gimplayer)

### GimpDocument().walkTree

[Show source in gimpXcfDocument.py:382](../../../gimpformats/gimpXcfDocument.py#L382)

#### Signature

```python
def walkTree(self) -> GimpGroup: ...
```

#### See also

- [GimpGroup](#gimpgroup)



## GimpGroup

[Show source in gimpXcfDocument.py:36](../../../gimpformats/gimpXcfDocument.py#L36)

#### Signature

```python
class GimpGroup:
    def __init__(self, name: Any) -> None: ...
```

### GimpGroup().__repr__

[Show source in gimpXcfDocument.py:55](../../../gimpformats/gimpXcfDocument.py#L55)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpGroup().add_layer

[Show source in gimpXcfDocument.py:42](../../../gimpformats/gimpXcfDocument.py#L42)

#### Signature

```python
def add_layer(self, layer: GimpLayer | GimpGroup) -> None: ...
```

### GimpGroup().get_group

[Show source in gimpXcfDocument.py:45](../../../gimpformats/gimpXcfDocument.py#L45)

#### Signature

```python
def get_group(self, idx: int) -> GimpGroup: ...
```



## applyMask

[Show source in gimpXcfDocument.py:596](../../../gimpformats/gimpXcfDocument.py#L596)

Apply a grayscale Pillow mask to an RGBA NumPy image.

- Black areas in the mask (0) make corresponding image areas transparent.
- White areas (255) keep the image unchanged.
- Gray areas (0-255) result in partial transparency.

#### Signature

```python
def applyMask(
    im: np.ndarray, mask_im: Image.Image | None, offsets: tuple[int, int] = (0, 0)
) -> np.ndarray: ...
```



## blendModeLookup

[Show source in gimpXcfDocument.py:591](../../../gimpformats/gimpXcfDocument.py#L591)

Look up the blend mode from the lookup table.

#### Signature

```python
def blendModeLookup(blend_type: GimpBlendMode) -> BlendMode: ...
```



## make_thumbnail

[Show source in gimpXcfDocument.py:585](../../../gimpformats/gimpXcfDocument.py#L585)

#### Signature

```python
def make_thumbnail(image: Image.Image) -> None: ...
```



## pil2np

[Show source in gimpXcfDocument.py:579](../../../gimpformats/gimpXcfDocument.py#L579)

#### Signature

```python
def pil2np(image: Image.Image | None) -> np.ndarray: ...
```