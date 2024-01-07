# Gimpxcfdocument

[Gimpformats Index](../README.md#gimpformats-index) /
[Gimpformats](./index.md#gimpformats) /
Gimpxcfdocument

> Auto-generated documentation for [gimpformats.gimpXcfDocument](../../../gimpformats/gimpXcfDocument.py) module.

- [Gimpxcfdocument](#gimpxcfdocument)
  - [GimpDocument](#gimpdocument)
    - [GimpDocument().__delitem__](#gimpdocument()__delitem__)
    - [GimpDocument().__getitem__](#gimpdocument()__getitem__)
    - [GimpDocument().__len__](#gimpdocument()__len__)
    - [GimpDocument().__repr__](#gimpdocument()__repr__)
    - [GimpDocument().__setitem__](#gimpdocument()__setitem__)
    - [GimpDocument().addLayer](#gimpdocument()addlayer)
    - [GimpDocument().appendLayer](#gimpdocument()appendlayer)
    - [GimpDocument().decode](#gimpdocument()decode)
    - [GimpDocument().deleteLayer](#gimpdocument()deletelayer)
    - [GimpDocument().encode](#gimpdocument()encode)
    - [GimpDocument().forceFullyLoaded](#gimpdocument()forcefullyloaded)
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
  - [blendModeLookup](#blendmodelookup)
  - [flattenAll](#flattenall)
  - [flattenLayerOrGroup](#flattenlayerorgroup)
  - [renderMaskWOffset](#rendermaskwoffset)
  - [renderWOffset](#renderwoffset)

## GimpDocument

[Show source in gimpXcfDocument.py:30](../../../gimpformats/gimpXcfDocument.py#L30)

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
    def __init__(self, fileName=None): ...
```

### GimpDocument().__delitem__

[Show source in gimpXcfDocument.py:328](../../../gimpformats/gimpXcfDocument.py#L328)

Make this class act like this class is an array of layers...

Delete a layer at an index.

#### Signature

```python
def __delitem__(self, index: int) -> None: ...
```

### GimpDocument().__getitem__

[Show source in gimpXcfDocument.py:314](../../../gimpformats/gimpXcfDocument.py#L314)

Make this class act like this class is an array of layers...

Get the layer at an index.

#### Signature

```python
def __getitem__(self, index: int) -> GimpLayer: ...
```

### GimpDocument().__len__

[Show source in gimpXcfDocument.py:307](../../../gimpformats/gimpXcfDocument.py#L307)

Make this class act like this class is an array of layers...

Get the len.

#### Signature

```python
def __len__(self) -> int: ...
```

### GimpDocument().__repr__

[Show source in gimpXcfDocument.py:386](../../../gimpformats/gimpXcfDocument.py#L386)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent="") -> str: ...
```

### GimpDocument().__setitem__

[Show source in gimpXcfDocument.py:321](../../../gimpformats/gimpXcfDocument.py#L321)

Make this class act like this class is an array of layers...

Set a layer at an index.

#### Signature

```python
def __setitem__(self, index: int, layer) -> None: ...
```

### GimpDocument().addLayer

[Show source in gimpXcfDocument.py:280](../../../gimpformats/gimpXcfDocument.py#L280)

Append a layer object to the document.

#### Arguments

- `layer` - the new layer to append

#### Signature

```python
def addLayer(self, layer: GimpLayer): ...
```

### GimpDocument().appendLayer

[Show source in gimpXcfDocument.py:287](../../../gimpformats/gimpXcfDocument.py#L287)

Append a layer object to the document.

#### Arguments

- `layer` - the new layer to append

#### Signature

```python
def appendLayer(self, layer: GimpLayer): ...
```

### GimpDocument().decode

[Show source in gimpXcfDocument.py:90](../../../gimpformats/gimpXcfDocument.py#L90)

Decode a byte buffer.

Steps:
Create a new IO buffer (array of binary values)
Check that the file is a valid gimp xcf
Grab the file version
Grab other attributes as outlined in the spec
Get precision data using the class and ioBuf buffer
List of properties
Get the layers and add the pointers to them
Get the channels and add the pointers to them
Return the offset

#### Arguments

- `data` *bytes* - data buffer to decode
- `index` *int, optional* - index within the buffer to start at]. Defaults to 0.

#### Raises

- `RuntimeError` - "Not a valid GIMP file"

#### Returns

- `int` - offset

#### Signature

```python
def decode(self, data: bytes, index: int = 0) -> int: ...
```

### GimpDocument().deleteLayer

[Show source in gimpXcfDocument.py:302](../../../gimpformats/gimpXcfDocument.py#L302)

Delete a layer.

#### Signature

```python
def deleteLayer(self, index: int) -> None: ...
```

### GimpDocument().encode

[Show source in gimpXcfDocument.py:159](../../../gimpformats/gimpXcfDocument.py#L159)

Encode to a byte array.

Steps:
Create a new IO buffer (array of binary values)
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
def encode(self): ...
```

### GimpDocument().forceFullyLoaded

[Show source in gimpXcfDocument.py:204](../../../gimpformats/gimpXcfDocument.py#L204)

Make sure everything is fully loaded from the file.

#### Signature

```python
def forceFullyLoaded(self): ...
```

### GimpDocument().getLayer

[Show source in gimpXcfDocument.py:236](../../../gimpformats/gimpXcfDocument.py#L236)

Return a given layer.

#### Signature

```python
def getLayer(self, index: int): ...
```

### GimpDocument().image

[Show source in gimpXcfDocument.py:339](../../../gimpformats/gimpXcfDocument.py#L339)

Get a final, compiled image.

#### Signature

```python
@property
def image(self): ...
```

### GimpDocument().insertLayer

[Show source in gimpXcfDocument.py:294](../../../gimpformats/gimpXcfDocument.py#L294)

Insert a layer object at a specific position.

#### Arguments

- `layer` - the new layer to insert
- `index` - where to insert the new layer (default=top)

#### Signature

```python
def insertLayer(self, layer: GimpLayer, index: int = -1): ...
```

### GimpDocument().layers

[Show source in gimpXcfDocument.py:215](../../../gimpformats/gimpXcfDocument.py#L215)

Decode the image's layers if necessary.

TODO: need to do the same thing with self.Channels

#### Signature

```python
@property
def layers(self): ...
```

### GimpDocument().load

[Show source in gimpXcfDocument.py:82](../../../gimpformats/gimpXcfDocument.py#L82)

Load a gimp xcf and decode the file. See decode for more on this process.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str): ...
```

### GimpDocument().newLayer

[Show source in gimpXcfDocument.py:246](../../../gimpformats/gimpXcfDocument.py#L246)

Create a new layer based on a PIL image.

#### Arguments

- `name` *str* - a name for the new layer
- [GimpDocument().image](#gimpdocumentimage) *Image.Image* - pil image
- `index` *int, optional* - where to insert the new layer (default=top). Defaults to -1.

#### Returns

- `GimpLayer` - newly created GimpLayer object

#### Signature

```python
def newLayer(self, name: str, image: Image.Image, index: int = -1) -> GimpLayer: ...
```

### GimpDocument().newLayerFromClipboard

[Show source in gimpXcfDocument.py:262](../../../gimpformats/gimpXcfDocument.py#L262)

Create a new image from the system clipboard.

NOTE: requires pillow PIL implementation
NOTE: only works on OSX and Windows

#### Arguments

- `name` *str* - a name for the new layer
- `index` *int, optional* - where to insert the new layer (default=top). Defaults to -1.

#### Returns

- `GimpLayer` - newly created GimpLayer object

#### Signature

```python
def newLayerFromClipboard(
    self, name: str = "pasted", index: int = -1
) -> GimpLayer | None: ...
```

### GimpDocument().save

[Show source in gimpXcfDocument.py:367](../../../gimpformats/gimpXcfDocument.py#L367)

Save this gimp image to a file.

#### Signature

```python
def save(self, filename: str | BytesIO = None): ...
```

### GimpDocument().saveNew

[Show source in gimpXcfDocument.py:377](../../../gimpformats/gimpXcfDocument.py#L377)

Save a new gimp image to a file.

#### Signature

```python
def saveNew(self, filename=None): ...
```

### GimpDocument().setLayer

[Show source in gimpXcfDocument.py:240](../../../gimpformats/gimpXcfDocument.py#L240)

Assign to a given layer.

#### Signature

```python
def setLayer(self, index, layer): ...
```



## blendModeLookup

[Show source in gimpXcfDocument.py:408](../../../gimpformats/gimpXcfDocument.py#L408)

Get the blendmode from a lookup table.

#### Signature

```python
def blendModeLookup(
    blendmode: int,
    blendLookup: dict[int, BlendType],
    default: BlendType = BlendType.NORMAL,
): ...
```



## flattenAll

[Show source in gimpXcfDocument.py:553](../../../gimpformats/gimpXcfDocument.py#L553)

Flatten a list of layers and groups.

Note the bottom layer is at the end of the list

#### Arguments

- `layers` *list[GimpLayer]* - A list of layers and groups
imageDimensions (tuple[int, int]): size of the image been flattened. Defaults to None.
- `ignoreHidden` *bool, optional* - ignore layers that are hidden. Defaults
to True.

#### Returns

- `PIL.Image` - Flattened image

#### Signature

```python
def flattenAll(
    layers: list[GimpLayer], imageDimensions: tuple[int, int], ignoreHidden: bool = True
) -> Image.Image: ...
```



## flattenLayerOrGroup

[Show source in gimpXcfDocument.py:418](../../../gimpformats/gimpXcfDocument.py#L418)

Flatten a layer or group on to an image of what has already been	flattened.

#### Arguments

- `layerOrGroup` *Layer,Group* - A layer or a group of layers
imageDimensions (tuple[int, int]): size of the image
- `flattenedSoFar` *PIL.Image, optional* - the image of what has already
been flattened. Defaults to None.
- `ignoreHidden` *bool, optional* - ignore layers that are hidden. Defaults
to True.

#### Returns

- `PIL.Image` - Flattened image

#### Signature

```python
def flattenLayerOrGroup(
    layerOrGroup: list[GimpLayer] | GimpLayer,
    imageDimensions: tuple[int, int],
    flattenedSoFar: Image.Image | None = None,
    ignoreHidden: bool = True,
) -> Image.Image: ...
```



## renderMaskWOffset

[Show source in gimpXcfDocument.py:598](../../../gimpformats/gimpXcfDocument.py#L598)

Render an image with offset and alpha to a given size.

#### Arguments

- `image` *Image.Image* - pil image to draw
size (tuple[int, int]): width, height as a tuple
- `alpha` *float, optional* - alpha transparency. Defaults to 1.0.
offsets (tuple[int, int], optional): x, y offsets as a tuple.
Defaults to (0, 0).

#### Returns

- `Image.Image` - new image

#### Signature

```python
def renderMaskWOffset(
    image: Image.Image, size: tuple[int, int], offsets: tuple[int, int] = (0, 0)
) -> Image.Image: ...
```



## renderWOffset

[Show source in gimpXcfDocument.py:578](../../../gimpformats/gimpXcfDocument.py#L578)

Render an image with offset and alpha to a given size.

#### Arguments

- `image` *Image.Image* - pil image to draw
size (tuple[int, int]): width, height as a tuple
- `alpha` *float, optional* - alpha transparency. Defaults to 1.0.
offsets (tuple[int, int], optional): x, y offsets as a tuple.
Defaults to (0, 0).

#### Returns

- `Image.Image` - new image

#### Signature

```python
def renderWOffset(
    image: Image.Image, size: tuple[int, int], offsets: tuple[int, int] = (0, 0)
) -> Image.Image: ...
```