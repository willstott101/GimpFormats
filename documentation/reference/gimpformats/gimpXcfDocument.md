# Gimpxcfdocument

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Gimpxcfdocument

> Auto-generated documentation for [gimpformats.gimpXcfDocument](../../../gimpformats/gimpXcfDocument.py) module.

- [Gimpxcfdocument](#gimpxcfdocument)
  - [BlendType](#blendtype)
  - [GimpDocument](#gimpdocument)
    - [GimpDocument().__delitem__](#gimpdocument()__delitem__)
    - [GimpDocument().__getitem__](#gimpdocument()__getitem__)
    - [GimpDocument().__len__](#gimpdocument()__len__)
    - [GimpDocument().__repr__](#gimpdocument()__repr__)
    - [GimpDocument().__setitem__](#gimpdocument()__setitem__)
    - [GimpDocument().__str__](#gimpdocument()__str__)
    - [GimpDocument().addLayer](#gimpdocument()addlayer)
    - [GimpDocument().appendLayer](#gimpdocument()appendlayer)
    - [GimpDocument().decode](#gimpdocument()decode)
    - [GimpDocument().deleteLayer](#gimpdocument()deletelayer)
    - [GimpDocument().encode](#gimpdocument()encode)
    - [GimpDocument().forceFullyLoaded](#gimpdocument()forcefullyloaded)
    - [GimpDocument().full_repr](#gimpdocument()full_repr)
    - [GimpDocument().getLayer](#gimpdocument()getlayer)
    - [GimpDocument().image](#gimpdocument()image)
    - [GimpDocument().insertLayer](#gimpdocument()insertlayer)
    - [GimpDocument().layers](#gimpdocument()layers)
    - [GimpDocument().load](#gimpdocument()load)
    - [GimpDocument().newLayer](#gimpdocument()newlayer)
    - [GimpDocument().newLayerFromClipboard](#gimpdocument()newlayerfromclipboard)
    - [GimpDocument().save](#gimpdocument()save)
    - [GimpDocument().saveNew](#gimpdocument()savenew)
    - [GimpDocument().setLayer](#gimpdocument()setlayer)
  - [applyMask](#applymask)
  - [blendModeLookup](#blendmodelookup)
  - [blendWithFlattened](#blendwithflattened)
  - [flattenAll](#flattenall)
  - [flattenLayerOrGroup](#flattenlayerorgroup)
  - [renderLayerOrGroup](#renderlayerorgroup)

## BlendType

[Show source in gimpXcfDocument.py:442](../../../gimpformats/gimpXcfDocument.py#L442)

Gimp xcf blend types.

#### Signature

```python
class BlendType(Enum): ...
```



## GimpDocument

[Show source in gimpXcfDocument.py:35](../../../gimpformats/gimpXcfDocument.py#L35)

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

### GimpDocument().__delitem__

[Show source in gimpXcfDocument.py:344](../../../gimpformats/gimpXcfDocument.py#L344)

Make this class act like this class is an array of layers...

Delete a layer at an index.

#### Signature

```python
def __delitem__(self, index: int) -> None: ...
```

### GimpDocument().__getitem__

[Show source in gimpXcfDocument.py:330](../../../gimpformats/gimpXcfDocument.py#L330)

Make this class act like this class is an array of layers...

Get the layer at an index.

#### Signature

```python
def __getitem__(self, index: int) -> GimpLayer: ...
```

#### See also

- [GimpLayer](./GimpLayer.md#gimplayer)

### GimpDocument().__len__

[Show source in gimpXcfDocument.py:323](../../../gimpformats/gimpXcfDocument.py#L323)

Make this class act like this class is an array of layers...

Get the len.

#### Signature

```python
def __len__(self) -> int: ...
```

### GimpDocument().__repr__

[Show source in gimpXcfDocument.py:405](../../../gimpformats/gimpXcfDocument.py#L405)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self) -> str: ...
```

### GimpDocument().__setitem__

[Show source in gimpXcfDocument.py:337](../../../gimpformats/gimpXcfDocument.py#L337)

Make this class act like this class is an array of layers...

Set a layer at an index.

#### Signature

```python
def __setitem__(self, index: int, layer: GimpLayer) -> None: ...
```

#### See also

- [GimpLayer](./GimpLayer.md#gimplayer)

### GimpDocument().__str__

[Show source in gimpXcfDocument.py:401](../../../gimpformats/gimpXcfDocument.py#L401)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpDocument().addLayer

[Show source in gimpXcfDocument.py:296](../../../gimpformats/gimpXcfDocument.py#L296)

Append a layer object to the document.

#### Arguments

- `layer` - the new layer to append

#### Signature

```python
def addLayer(self, layer: GimpLayer) -> None: ...
```

#### See also

- [GimpLayer](./GimpLayer.md#gimplayer)

### GimpDocument().appendLayer

[Show source in gimpXcfDocument.py:303](../../../gimpformats/gimpXcfDocument.py#L303)

Append a layer object to the document.

#### Arguments

- `layer` - the new layer to append

#### Signature

```python
def appendLayer(self, layer: GimpLayer) -> None: ...
```

#### See also

- [GimpLayer](./GimpLayer.md#gimplayer)

### GimpDocument().decode

[Show source in gimpXcfDocument.py:95](../../../gimpformats/gimpXcfDocument.py#L95)

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
 - `data` *bytes* - data buffer to decode
 - `index` *int, optional* - index within the buffer to start at]. Defaults to 0.

#### Raises

------
 - `RuntimeError` - "Not a valid GIMP file"

#### Returns

-------
 - `int` - offset

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int: ...
```

### GimpDocument().deleteLayer

[Show source in gimpXcfDocument.py:318](../../../gimpformats/gimpXcfDocument.py#L318)

Delete a layer.

#### Signature

```python
def deleteLayer(self, index: int) -> None: ...
```

### GimpDocument().encode

[Show source in gimpXcfDocument.py:169](../../../gimpformats/gimpXcfDocument.py#L169)

Encode to bytes.

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

[Show source in gimpXcfDocument.py:214](../../../gimpformats/gimpXcfDocument.py#L214)

Make sure everything is fully loaded from the file.

#### Signature

```python
def forceFullyLoaded(self) -> None: ...
```

### GimpDocument().full_repr

[Show source in gimpXcfDocument.py:413](../../../gimpformats/gimpXcfDocument.py#L413)

Get a textual representation of this object.

#### Signature

```python
def full_repr(self, indent: int = 0) -> str: ...
```

### GimpDocument().getLayer

[Show source in gimpXcfDocument.py:246](../../../gimpformats/gimpXcfDocument.py#L246)

Return a given layer.

#### Signature

```python
def getLayer(self, index: int) -> GimpLayer: ...
```

#### See also

- [GimpLayer](./GimpLayer.md#gimplayer)

### GimpDocument().image

[Show source in gimpXcfDocument.py:351](../../../gimpformats/gimpXcfDocument.py#L351)

Generates a final, compiled image by processing layers and groups.

#### Signature

```python
@property
def image(self) -> Image.Image: ...
```

### GimpDocument().insertLayer

[Show source in gimpXcfDocument.py:310](../../../gimpformats/gimpXcfDocument.py#L310)

Insert a layer object at a specific position.

#### Arguments

- `layer` - the new layer to insert
- `index` - where to insert the new layer (default=top)

#### Signature

```python
def insertLayer(self, layer: GimpLayer, index: int = -1) -> None: ...
```

#### See also

- [GimpLayer](./GimpLayer.md#gimplayer)

### GimpDocument().layers

[Show source in gimpXcfDocument.py:225](../../../gimpformats/gimpXcfDocument.py#L225)

Decode the image's layers if necessary.

TODO: need to do the same thing with self.Channels

#### Signature

```python
@property
def layers(self) -> list[GimpLayer]: ...
```

#### See also

- [GimpLayer](./GimpLayer.md#gimplayer)

### GimpDocument().load

[Show source in gimpXcfDocument.py:87](../../../gimpformats/gimpXcfDocument.py#L87)

Load a gimp xcf and decode the file. See decode for more on this process.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str) -> None: ...
```

### GimpDocument().newLayer

[Show source in gimpXcfDocument.py:256](../../../gimpformats/gimpXcfDocument.py#L256)

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

[Show source in gimpXcfDocument.py:275](../../../gimpformats/gimpXcfDocument.py#L275)

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

### GimpDocument().save

[Show source in gimpXcfDocument.py:382](../../../gimpformats/gimpXcfDocument.py#L382)

Save this gimp image to a file.

#### Signature

```python
def save(self, filename: str | BytesIO | None = None) -> NoReturn: ...
```

### GimpDocument().saveNew

[Show source in gimpXcfDocument.py:392](../../../gimpformats/gimpXcfDocument.py#L392)

Save a new gimp image to a file.

#### Signature

```python
def saveNew(self, filename: str | None = None) -> NoReturn: ...
```

### GimpDocument().setLayer

[Show source in gimpXcfDocument.py:250](../../../gimpformats/gimpXcfDocument.py#L250)

Assign to a given layer.

#### Signature

```python
def setLayer(self, index: int, layer: GimpLayer) -> None: ...
```

#### See also

- [GimpLayer](./GimpLayer.md#gimplayer)



## applyMask

[Show source in gimpXcfDocument.py:600](../../../gimpformats/gimpXcfDocument.py#L600)

Apply a mask efficiently.

#### Signature

```python
def applyMask(
    image: Image.Image,
    mask: Image.Image | None,
    xOffset: int,
    yOffset: int,
    size: tuple[int, int],
) -> Image.Image: ...
```



## blendModeLookup

[Show source in gimpXcfDocument.py:626](../../../gimpformats/gimpXcfDocument.py#L626)

Look up the blend mode from the lookup table.

#### Signature

```python
def blendModeLookup(
    blend_mode: BlendMode, blendLookup: dict[BlendMode, BlendMode]
) -> BlendMode: ...
```



## blendWithFlattened

[Show source in gimpXcfDocument.py:615](../../../gimpformats/gimpXcfDocument.py#L615)

Optimized function to blend layers with existing flattened image.

#### Signature

```python
def blendWithFlattened(
    flattened: Image.Image | None, foreground: Image.Image, layer: GimpLayer
) -> Image.Image: ...
```

#### See also

- [GimpLayer](./GimpLayer.md#gimplayer)



## flattenAll

[Show source in gimpXcfDocument.py:578](../../../gimpformats/gimpXcfDocument.py#L578)

Optimized flattenAll to avoid excessive recursion.

#### Signature

```python
def flattenAll(
    layers: list[GimpLayer], imageDimensions: tuple[int, int], ignoreHidden: bool = True
) -> Image.Image | None: ...
```

#### See also

- [GimpLayer](./GimpLayer.md#gimplayer)



## flattenLayerOrGroup

[Show source in gimpXcfDocument.py:521](../../../gimpformats/gimpXcfDocument.py#L521)

Recursively flattens a layer or group, handling nested groups properly.

#### Signature

```python
def flattenLayerOrGroup(
    layerOrGroup: GimpLayer | list[GimpLayer],
    imageDimensions: tuple[int, int],
    flattenedSoFar: Image.Image | None = None,
    ignoreHidden: bool = True,
) -> Image.Image: ...
```



## renderLayerOrGroup

[Show source in gimpXcfDocument.py:590](../../../gimpformats/gimpXcfDocument.py#L590)

Optimized function to render a layer or group with reduced conversions.

#### Signature

```python
def renderLayerOrGroup(
    image: Image.Image, size: tuple[int, int], offsets: tuple[int, int] = (0, 0)
) -> Image.Image: ...
```