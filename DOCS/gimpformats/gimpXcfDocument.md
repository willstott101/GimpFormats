# gimpXcfDocument

> Auto-generated documentation for [gimpformats.gimpXcfDocument](../../gimpformats/gimpXcfDocument.py) module.

Pure python implementation of the gimp xcf file format.

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / gimpXcfDocument
    - [GimpDocument](#gimpdocument)
        - [GimpDocument().\_\_delitem\_\_](#gimpdocument__delitem__)
        - [GimpDocument().\_\_getitem\_\_](#gimpdocument__getitem__)
        - [GimpDocument().\_\_len\_\_](#gimpdocument__len__)
        - [GimpDocument().\_\_repr\_\_](#gimpdocument__repr__)
        - [GimpDocument().\_\_setitem\_\_](#gimpdocument__setitem__)
        - [GimpDocument().addLayer](#gimpdocumentaddlayer)
        - [GimpDocument().appendLayer](#gimpdocumentappendlayer)
        - [GimpDocument().decode](#gimpdocumentdecode)
        - [GimpDocument().deleteLayer](#gimpdocumentdeletelayer)
        - [GimpDocument().encode](#gimpdocumentencode)
        - [GimpDocument().forceFullyLoaded](#gimpdocumentforcefullyloaded)
        - [GimpDocument().getLayer](#gimpdocumentgetlayer)
        - [GimpDocument().image](#gimpdocumentimage)
        - [GimpDocument().insertLayer](#gimpdocumentinsertlayer)
        - [GimpDocument().layers](#gimpdocumentlayers)
        - [GimpDocument().load](#gimpdocumentload)
        - [GimpDocument().newLayer](#gimpdocumentnewlayer)
        - [GimpDocument().newLayerFromClipboard](#gimpdocumentnewlayerfromclipboard)
        - [GimpDocument().save](#gimpdocumentsave)
        - [GimpDocument().saveNew](#gimpdocumentsavenew)
        - [GimpDocument().setLayer](#gimpdocumentsetlayer)
    - [blendModeLookup](#blendmodelookup)
    - [flattenAll](#flattenall)
    - [flattenLayerOrGroup](#flattenlayerorgroup)
    - [renderMaskWOffset](#rendermaskwoffset)
    - [renderWOffset](#renderwoffset)

Currently supports:
 Loading xcf files
 Getting image hierarchy and info
 Getting image for each layer (PIL image)
Currently not supporting:
 Saving
 Programatically alter documents (add layer, etc)
 Rendering a final, compositied image

## GimpDocument

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L31)

```python
class GimpDocument(GimpIOBase):
    def __init__(fileName=None):
```

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

### GimpDocument().\_\_delitem\_\_

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L329)

```python
def __delitem__(index: int) -> None:
```

Make this class act like this class is an array of layers...

Delete a layer at an index.

### GimpDocument().\_\_getitem\_\_

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L315)

```python
def __getitem__(index: int) -> GimpLayer:
```

Make this class act like this class is an array of layers...

Get the layer at an index.

### GimpDocument().\_\_len\_\_

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L308)

```python
def __len__() -> int:
```

Make this class act like this class is an array of layers...

Get the len.

### GimpDocument().\_\_repr\_\_

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L377)

```python
def __repr__(indent='') -> str:
```

Get a textual representation of this object.

### GimpDocument().\_\_setitem\_\_

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L322)

```python
def __setitem__(index: int, layer) -> None:
```

Make this class act like this class is an array of layers...

Set a layer at an index.

### GimpDocument().addLayer

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L281)

```python
def addLayer(layer: GimpLayer):
```

Append a layer object to the document.

#### Arguments

- `layer` - the new layer to append

### GimpDocument().appendLayer

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L288)

```python
def appendLayer(layer: GimpLayer):
```

Append a layer object to the document.

#### Arguments

- `layer` - the new layer to append

### GimpDocument().decode

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L91)

```python
def decode(data: bytes, index: int = 0) -> int:
```

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

- `Exception` - "Not a valid GIMP file"

#### Returns

- `int` - offset

### GimpDocument().deleteLayer

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L303)

```python
def deleteLayer(index: int) -> None:
```

Delete a layer.

### GimpDocument().encode

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L160)

```python
def encode():
```

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

### GimpDocument().forceFullyLoaded

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L205)

```python
def forceFullyLoaded():
```

Make sure everything is fully loaded from the file.

### GimpDocument().getLayer

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L237)

```python
def getLayer(index: int):
```

Return a given layer.

### GimpDocument().image

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L340)

```python
@property
def image():
```

Get a final, compiled image.

### GimpDocument().insertLayer

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L295)

```python
def insertLayer(layer: GimpLayer, index: int = -1):
```

Insert a layer object at a specific position.

#### Arguments

- `layer` - the new layer to insert
- `index` - where to insert the new layer (default=top)

### GimpDocument().layers

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L216)

```python
@property
def layers():
```

Decode the image's layers if necessary.

TODO: need to do the same thing with self.Channels

### GimpDocument().load

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L83)

```python
def load(fileName: BytesIO | str):
```

Load a gimp xcf and decode the file. See decode for more on this process.

#### Arguments

- `fileName` - can be a file name or a file-like object

### GimpDocument().newLayer

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L247)

```python
def newLayer(name: str, image: Image.Image, index: int = -1) -> GimpLayer:
```

Create a new layer based on a PIL image.

#### Arguments

- `name` *str* - a name for the new layer
- `image` *Image.Image* - pil image
- `index` *int, optional* - where to insert the new layer (default=top). Defaults to -1.

#### Returns

- `GimpLayer` - newly created GimpLayer object

### GimpDocument().newLayerFromClipboard

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L263)

```python
def newLayerFromClipboard(
    name: str = 'pasted',
    index: int = -1,
) -> GimpLayer | None:
```

Create a new image from the system clipboard.

NOTE: requires pillow PIL implementation
NOTE: only works on OSX and Windows

#### Arguments

- `name` *str* - a name for the new layer
- `index` *int, optional* - where to insert the new layer (default=top). Defaults to -1.

#### Returns

- `GimpLayer` - newly created GimpLayer object

### GimpDocument().save

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L368)

```python
def save(filename: str | BytesIO = None):
```

Save this gimp image to a file.

### GimpDocument().saveNew

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L373)

```python
def saveNew(filename=None):
```

Save a new gimp image to a file.

### GimpDocument().setLayer

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L241)

```python
def setLayer(index, layer):
```

Assign to a given layer.

## blendModeLookup

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L399)

```python
def blendModeLookup(
    blendmode: int,
    blendLookup: dict[(int, BlendType)],
    default: BlendType = BlendType.NORMAL,
):
```

Get the blendmode from a lookup table.

## flattenAll

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L540)

```python
def flattenAll(
    layers: list[GimpLayer],
    imageDimensions: tuple[(int, int)],
    ignoreHidden: bool = True,
) -> Image.Image:
```

Flatten a list of layers and groups.

Note the bottom layer is at the end of the list

#### Arguments

- `layers` *list[GimpLayer]* - A list of layers and groups
imageDimensions (tuple[int, int]): size of the image been flattened. Defaults to None.
- `ignoreHidden` *bool, optional* - ignore layers that are hidden. Defaults
to True.

#### Returns

- `PIL.Image` - Flattened image

## flattenLayerOrGroup

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L409)

```python
def flattenLayerOrGroup(
    layerOrGroup: list[GimpLayer] | GimpLayer,
    imageDimensions: tuple[(int, int)],
    flattenedSoFar: Image.Image | None = None,
    ignoreHidden: bool = True,
) -> Image.Image:
```

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

## renderMaskWOffset

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L585)

```python
def renderMaskWOffset(
    image: Image.Image,
    size: tuple[(int, int)],
    offsets: tuple[(int, int)] = (0, 0),
) -> Image.Image:
```

Render an image with offset and alpha to a given size.

#### Arguments

- `image` *Image.Image* - pil image to draw
size (tuple[int, int]): width, height as a tuple
- `alpha` *float, optional* - alpha transparency. Defaults to 1.0.
offsets (tuple[int, int], optional): x, y offsets as a tuple.
Defaults to (0, 0).

#### Returns

- `Image.Image` - new image

## renderWOffset

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L565)

```python
def renderWOffset(
    image: Image.Image,
    size: tuple[(int, int)],
    offsets: tuple[(int, int)] = (0, 0),
) -> Image.Image:
```

Render an image with offset and alpha to a given size.

#### Arguments

- `image` *Image.Image* - pil image to draw
size (tuple[int, int]): width, height as a tuple
- `alpha` *float, optional* - alpha transparency. Defaults to 1.0.
offsets (tuple[int, int], optional): x, y offsets as a tuple.
Defaults to (0, 0).

#### Returns

- `Image.Image` - new image
