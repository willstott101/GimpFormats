# Gimpxcfdocument

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpxcfdocument

> Auto-generated documentation for [gimpformats.gimpXcfDocument](../../../gimpformats/gimpXcfDocument.py) module.

- [Gimpxcfdocument](#gimpxcfdocument)
  - [GimpDocument](#gimpdocument)
    - [GimpDocument().__repr__](#gimpdocument()__repr__)
    - [GimpDocument().__str__](#gimpdocument()__str__)
    - [GimpDocument()._render](#gimpdocument()_render)
    - [GimpDocument().addRawLayer](#gimpdocument()addrawlayer)
    - [GimpDocument().appendRawLayer](#gimpdocument()appendrawlayer)
    - [GimpDocument().decode](#gimpdocument()decode)
    - [GimpDocument().deleteRawLayer](#gimpdocument()deleterawlayer)
    - [GimpDocument().encode](#gimpdocument()encode)
    - [GimpDocument().forceFullyLoaded](#gimpdocument()forcefullyloaded)
    - [GimpDocument().full_repr](#gimpdocument()full_repr)
    - [GimpDocument().getLayer](#gimpdocument()getlayer)
    - [GimpDocument().image](#gimpdocument()image)
    - [GimpDocument().insertRawLayer](#gimpdocument()insertrawlayer)
    - [GimpDocument().load](#gimpdocument()load)
    - [GimpDocument().newLayer](#gimpdocument()newlayer)
    - [GimpDocument().newLayerFromClipboard](#gimpdocument()newlayerfromclipboard)
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

[Show source in gimpXcfDocument.py:58](../../../gimpformats/gimpXcfDocument.py#L58)

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

See:
 https://gitlab.gnome.org/GNOME/gimp/blob/master/devel-docs/xcf.txt

#### Signature

```python
class GimpDocument(GimpIOBase):
    def __init__(self, fileName: BytesIO | str | None = None) -> None: ...
```

#### See also

- [GimpIOBase](./GimpIOBase.md#gimpiobase)

### GimpDocument().__repr__

[Show source in gimpXcfDocument.py:406](../../../gimpformats/gimpXcfDocument.py#L406)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpDocument().__str__

[Show source in gimpXcfDocument.py:402](../../../gimpformats/gimpXcfDocument.py#L402)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpDocument()._render

[Show source in gimpXcfDocument.py:450](../../../gimpformats/gimpXcfDocument.py#L450)

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

### GimpDocument().addRawLayer

[Show source in gimpXcfDocument.py:325](../../../gimpformats/gimpXcfDocument.py#L325)

Append a layer object to the document.

#### Arguments

- `layer` - the new layer to append

#### Signature

```python
def addRawLayer(self, layer: GimpLayer) -> None: ...
```

#### See also

- [GimpLayer](./GimpLayer.md#gimplayer)

### GimpDocument().appendRawLayer

[Show source in gimpXcfDocument.py:332](../../../gimpformats/gimpXcfDocument.py#L332)

Append a layer object to the document.

#### Arguments

- `layer` - the new layer to append

#### Signature

```python
def appendRawLayer(self, layer: GimpLayer) -> None: ...
```

#### See also

- [GimpLayer](./GimpLayer.md#gimplayer)

### GimpDocument().decode

[Show source in gimpXcfDocument.py:118](../../../gimpformats/gimpXcfDocument.py#L118)

Decode a byte buffer.

Steps:
Create a new IO buffer
Check that the file is a valid gimp xcf
Grab the file version
Grab other attributes as outlined in the spec
Get precision data using the class and ioBuf buffer
List of properties
Get the layers and add the pointers to them
Get the channels and add the pointers to them
Return the offset

#### Arguments

----
 - `data` *bytearray* - data buffer to decode
 - `index` *int, optional* - index within the buffer to start at]. Defaults to 0.

#### Raises

------
 - `RuntimeError` - "Not a valid GIMP file"

#### Returns

-------
 - `int` - offset

#### Signature

```python
def decode(self, data: bytearray | bytes, index: int = 0) -> int: ...
```

### GimpDocument().deleteRawLayer

[Show source in gimpXcfDocument.py:347](../../../gimpformats/gimpXcfDocument.py#L347)

Delete a layer.

#### Signature

```python
def deleteRawLayer(self, index: int) -> None: ...
```

### GimpDocument().encode

[Show source in gimpXcfDocument.py:192](../../../gimpformats/gimpXcfDocument.py#L192)

Encode to bytearray.

Steps:
Create a new IO buffer
The file is a valid gimp xcf
Set the file version
Set other attributes as outlined in the spec
Set precision data using the class and ioBuf buffer
List of properties
Set the layers and add the pointers to them
Set the channels and add the pointers to them
Return the data

#### Signature

```python
def encode(self) -> bytearray: ...
```

### GimpDocument().forceFullyLoaded

[Show source in gimpXcfDocument.py:237](../../../gimpformats/gimpXcfDocument.py#L237)

Make sure everything is fully loaded from the file.

#### Signature

```python
def forceFullyLoaded(self) -> None: ...
```

### GimpDocument().full_repr

[Show source in gimpXcfDocument.py:414](../../../gimpformats/gimpXcfDocument.py#L414)

Get a textual representation of this object.

#### Signature

```python
def full_repr(self, indent: int = 0) -> str: ...
```

### GimpDocument().getLayer

[Show source in gimpXcfDocument.py:269](../../../gimpformats/gimpXcfDocument.py#L269)

Return a given layer.

#### Signature

```python
def getLayer(self, index: int) -> GimpLayer | GimpGroup: ...
```

### GimpDocument().image

[Show source in gimpXcfDocument.py:374](../../../gimpformats/gimpXcfDocument.py#L374)

Generates a final, compiled image by processing layers and groups.

#### Signature

```python
@property
def image(self) -> Image.Image: ...
```

### GimpDocument().insertRawLayer

[Show source in gimpXcfDocument.py:339](../../../gimpformats/gimpXcfDocument.py#L339)

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

### GimpDocument().load

[Show source in gimpXcfDocument.py:110](../../../gimpformats/gimpXcfDocument.py#L110)

Load a gimp xcf and decode the file. See decode for more on this process.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str) -> None: ...
```

### GimpDocument().newLayer

[Show source in gimpXcfDocument.py:285](../../../gimpformats/gimpXcfDocument.py#L285)

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

### GimpDocument().newLayerFromClipboard

[Show source in gimpXcfDocument.py:304](../../../gimpformats/gimpXcfDocument.py#L304)

Create a new image from the system clipboard.

NOTE: requires pillow PIL implementation
NOTE: only works on OSX and Windows

#### Arguments

----
 - `name` *str* - a name for the new layer
 - `index` *int, optional* - where to insert the new layer (default=top). Defaults to -1.

#### Returns

-------
 - `GimpLayer` - newly created GimpLayer object

#### Signature

```python
def newLayerFromClipboard(
    self, name: str = "pasted", index: int = -1
) -> GimpLayer | None: ...
```

### GimpDocument().raw_layers

[Show source in gimpXcfDocument.py:248](../../../gimpformats/gimpXcfDocument.py#L248)

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

[Show source in gimpXcfDocument.py:442](../../../gimpformats/gimpXcfDocument.py#L442)

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

[Show source in gimpXcfDocument.py:383](../../../gimpformats/gimpXcfDocument.py#L383)

Save this gimp image to a file.

#### Signature

```python
def save(self, filename: str | BytesIO | None = None) -> NoReturn: ...
```

### GimpDocument().saveNew

[Show source in gimpXcfDocument.py:393](../../../gimpformats/gimpXcfDocument.py#L393)

Save a new gimp image to a file.

#### Signature

```python
def saveNew(self, filename: str | None = None) -> NoReturn: ...
```

### GimpDocument().setRawLayer

[Show source in gimpXcfDocument.py:279](../../../gimpformats/gimpXcfDocument.py#L279)

Assign to a given layer.

#### Signature

```python
def setRawLayer(self, index: int, layer: GimpLayer) -> None: ...
```

#### See also

- [GimpLayer](./GimpLayer.md#gimplayer)

### GimpDocument().walkTree

[Show source in gimpXcfDocument.py:351](../../../gimpformats/gimpXcfDocument.py#L351)

#### Signature

```python
def walkTree(self) -> GimpGroup: ...
```

#### See also

- [GimpGroup](#gimpgroup)



## GimpGroup

[Show source in gimpXcfDocument.py:34](../../../gimpformats/gimpXcfDocument.py#L34)

#### Signature

```python
class GimpGroup:
    def __init__(self, name: Any) -> None: ...
```

### GimpGroup().__repr__

[Show source in gimpXcfDocument.py:53](../../../gimpformats/gimpXcfDocument.py#L53)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpGroup().add_layer

[Show source in gimpXcfDocument.py:40](../../../gimpformats/gimpXcfDocument.py#L40)

#### Signature

```python
def add_layer(self, layer: GimpLayer | GimpGroup) -> None: ...
```

### GimpGroup().get_group

[Show source in gimpXcfDocument.py:43](../../../gimpformats/gimpXcfDocument.py#L43)

#### Signature

```python
def get_group(self, idx: int) -> GimpGroup: ...
```



## applyMask

[Show source in gimpXcfDocument.py:566](../../../gimpformats/gimpXcfDocument.py#L566)

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

[Show source in gimpXcfDocument.py:561](../../../gimpformats/gimpXcfDocument.py#L561)

Look up the blend mode from the lookup table.

#### Signature

```python
def blendModeLookup(blend_type: GimpBlendMode) -> BlendMode: ...
```

#### See also

- [GimpBlendMode](./GimpIOBase.md#gimpblendmode)



## make_thumbnail

[Show source in gimpXcfDocument.py:555](../../../gimpformats/gimpXcfDocument.py#L555)

#### Signature

```python
def make_thumbnail(image: Image.Image) -> None: ...
```



## pil2np

[Show source in gimpXcfDocument.py:549](../../../gimpformats/gimpXcfDocument.py#L549)

#### Signature

```python
def pil2np(image: Image.Image | None) -> np.ndarray: ...
```