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

[Show source in gimpXcfDocument.py:57](../../../gimpformats/gimpXcfDocument.py#L57)

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

[Show source in gimpXcfDocument.py:373](../../../gimpformats/gimpXcfDocument.py#L373)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpDocument().__str__

[Show source in gimpXcfDocument.py:369](../../../gimpformats/gimpXcfDocument.py#L369)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpDocument()._render

[Show source in gimpXcfDocument.py:417](../../../gimpformats/gimpXcfDocument.py#L417)

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

[Show source in gimpXcfDocument.py:117](../../../gimpformats/gimpXcfDocument.py#L117)

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

[Show source in gimpXcfDocument.py:314](../../../gimpformats/gimpXcfDocument.py#L314)

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

[Show source in gimpXcfDocument.py:239](../../../gimpformats/gimpXcfDocument.py#L239)

Make sure everything is fully loaded from the file.

#### Signature

```python
def forceFullyLoaded(self) -> None: ...
```

### GimpDocument().full_repr

[Show source in gimpXcfDocument.py:381](../../../gimpformats/gimpXcfDocument.py#L381)

Get a textual representation of this object.

#### Signature

```python
def full_repr(self, indent: int = 0) -> str: ...
```

### GimpDocument().getLayer

[Show source in gimpXcfDocument.py:271](../../../gimpformats/gimpXcfDocument.py#L271)

Return a given layer.

#### Signature

```python
def getLayer(self, index: int) -> GimpLayer | GimpGroup: ...
```

### GimpDocument().image

[Show source in gimpXcfDocument.py:341](../../../gimpformats/gimpXcfDocument.py#L341)

Generates a final, compiled image by processing layers and groups.

#### Signature

```python
@property
def image(self) -> Image.Image: ...
```

### GimpDocument().insertRawLayer

[Show source in gimpXcfDocument.py:306](../../../gimpformats/gimpXcfDocument.py#L306)

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

[Show source in gimpXcfDocument.py:109](../../../gimpformats/gimpXcfDocument.py#L109)

Load a gimp xcf and decode the file. See decode for more on this process.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str) -> None: ...
```

### GimpDocument().newLayer

[Show source in gimpXcfDocument.py:287](../../../gimpformats/gimpXcfDocument.py#L287)

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

[Show source in gimpXcfDocument.py:250](../../../gimpformats/gimpXcfDocument.py#L250)

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

[Show source in gimpXcfDocument.py:409](../../../gimpformats/gimpXcfDocument.py#L409)

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

[Show source in gimpXcfDocument.py:350](../../../gimpformats/gimpXcfDocument.py#L350)

Save this gimp image to a file.

#### Signature

```python
def save(self, filename: str | BytesIO | None = None) -> NoReturn: ...
```

### GimpDocument().saveNew

[Show source in gimpXcfDocument.py:360](../../../gimpformats/gimpXcfDocument.py#L360)

Save a new gimp image to a file.

#### Signature

```python
def saveNew(self, filename: str | None = None) -> NoReturn: ...
```

### GimpDocument().setRawLayer

[Show source in gimpXcfDocument.py:281](../../../gimpformats/gimpXcfDocument.py#L281)

Assign to a given layer.

#### Signature

```python
def setRawLayer(self, index: int, layer: GimpLayer) -> None: ...
```

#### See also

- [GimpLayer](./GimpLayer.md#gimplayer)

### GimpDocument().walkTree

[Show source in gimpXcfDocument.py:318](../../../gimpformats/gimpXcfDocument.py#L318)

#### Signature

```python
def walkTree(self) -> GimpGroup: ...
```

#### See also

- [GimpGroup](#gimpgroup)



## GimpGroup

[Show source in gimpXcfDocument.py:33](../../../gimpformats/gimpXcfDocument.py#L33)

#### Signature

```python
class GimpGroup:
    def __init__(self, name: Any) -> None: ...
```

### GimpGroup().__repr__

[Show source in gimpXcfDocument.py:52](../../../gimpformats/gimpXcfDocument.py#L52)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpGroup().add_layer

[Show source in gimpXcfDocument.py:39](../../../gimpformats/gimpXcfDocument.py#L39)

#### Signature

```python
def add_layer(self, layer: GimpLayer | GimpGroup) -> None: ...
```

### GimpGroup().get_group

[Show source in gimpXcfDocument.py:42](../../../gimpformats/gimpXcfDocument.py#L42)

#### Signature

```python
def get_group(self, idx: int) -> GimpGroup: ...
```



## applyMask

[Show source in gimpXcfDocument.py:532](../../../gimpformats/gimpXcfDocument.py#L532)

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

[Show source in gimpXcfDocument.py:527](../../../gimpformats/gimpXcfDocument.py#L527)

Look up the blend mode from the lookup table.

#### Signature

```python
def blendModeLookup(blend_type: GimpBlendMode) -> BlendMode: ...
```



## make_thumbnail

[Show source in gimpXcfDocument.py:521](../../../gimpformats/gimpXcfDocument.py#L521)

#### Signature

```python
def make_thumbnail(image: Image.Image) -> None: ...
```



## pil2np

[Show source in gimpXcfDocument.py:515](../../../gimpformats/gimpXcfDocument.py#L515)

#### Signature

```python
def pil2np(image: Image.Image | None) -> np.ndarray: ...
```