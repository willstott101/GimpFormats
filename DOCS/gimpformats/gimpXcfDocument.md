# gimpXcfDocument

> Auto-generated documentation for [gimpformats.gimpXcfDocument](../../gimpformats/gimpXcfDocument.py) module.

Pure python implementation of the gimp xcf file format

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / gimpXcfDocument
    - [GimpDocument](#gimpdocument)
        - [GimpDocument().\_\_repr\_\_](#gimpdocument__repr__)
        - [GimpDocument().addLayer](#gimpdocumentaddlayer)
        - [GimpDocument().appendLayer](#gimpdocumentappendlayer)
        - [GimpDocument().decode](#gimpdocumentdecode)
        - [GimpDocument().deleteLayer](#gimpdocumentdeletelayer)
        - [GimpDocument().encode](#gimpdocumentencode)
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
    - [rasterImageOffset](#rasterimageoffset)
    - [saveLayer](#savelayer)
    - [showLayer](#showlayer)

Currently supports:
 Loading xcf files
 Getting image hierarchy and info
 Getting image for each layer (PIL image)
Currently not supporting:
 Saving
 Programatically alter documents (add layer, etc)
 Rendering a final, compositied image

## GimpDocument

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L30)

```python
class GimpDocument(GimpIOBase):
    def __init__(fileName=None):
```

Pure python implementation of the gimp file format

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

### GimpDocument().\_\_repr\_\_

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L365)

```python
def __repr__(indent: str = ''):
```

Get a textual representation of this object

### GimpDocument().addLayer

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L266)

```python
def addLayer(lyr: GimpLayer):
```

append a layer object to the document

#### Arguments

- `layer` - the new layer to append

### GimpDocument().appendLayer

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L274)

```python
def appendLayer(l):
```

append a layer object to the document

#### Arguments

- `layer` - the new layer to append

### GimpDocument().decode

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L81)

```python
def decode(data: bytes, index: int = 0):
```

decode a byte buffer

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

- `data` - data buffer to decode
- `index` - index within the buffer to start at

### GimpDocument().deleteLayer

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L291)

```python
def deleteLayer(index: int) -> None:
```

delete a layer

### GimpDocument().encode

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L144)

```python
def encode():
```

encode to a byte array

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

### GimpDocument().getLayer

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L225)

```python
def getLayer(index: int):
```

return a given layer

### GimpDocument().image

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L314)

```python
@property
def image():
```

get a final, compiled image

### GimpDocument().insertLayer

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L282)

```python
def insertLayer(lyr: GimpLayer, index: int = -1):
```

insert a layer object at a specific position

#### Arguments

- `layer` - the new layer to insert
- `index` - where to insert the new layer (default=top)

### GimpDocument().layers

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L203)

```python
@property
def layers():
```

Decode the image's layers if necessary

TODO: need to do the same thing with self.Channels

### GimpDocument().load

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L64)

```python
def load(fileName: Union[(BytesIO, str)]):
```

Load a gimp xcf and decode the file. See decode for more on this
process

#### Arguments

- `fileName` - can be a file name or a file-like object

### GimpDocument().newLayer

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L239)

```python
def newLayer(name: str, image: Image.Image, index: int = -1):
```

create a new layer based on a PIL image

#### Arguments

- `name` - a name for the new layer
- `index` - where to insert the new layer (default=top)

#### Returns

newly created GimpLayer object

### GimpDocument().newLayerFromClipboard

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L252)

```python
def newLayerFromClipboard(name: str = 'pasted', index: int = -1):
```

Create a new image from the system clipboard.

#### Arguments

- `name` - a name for the new layer (default="pasted")
- `index` - where to insert the new layer (default=top)

#### Returns

newly created GimpLayer object

NOTE: requires pillow PIL implementation
NOTE: only works on OSX and Windows

### GimpDocument().save

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L344)

```python
def save(tofileName=None):
```

save this gimp image to a file

### GimpDocument().saveNew

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L355)

```python
def saveNew(tofileName=None):
```

save a new gimp image to a file

### GimpDocument().setLayer

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L231)

```python
def setLayer(_index, _l):
```

assign to a given layer

## blendModeLookup

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L387)

```python
def blendModeLookup(
    blendmode: int,
    blendLookup: dict[(int, BlendType)],
    default: BlendType = BlendType.NORMAL,
):
```

Get the blendmode from a lookup table

## flattenAll

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L460)

```python
def flattenAll(layers, imageDimensions, ignoreHidden=True):
```

Flatten a list of layers and groups

Note the bottom layer is at the end of the list

#### Arguments

- `layers` *[Layer|Group]* - A list of layers and groups
imageDimensions ((int, int)): size of the image
been flattened. Defaults to None.
- `ignoreHidden` *bool, optional* - ignore layers that are hidden. Defaults
to True.

#### Returns

- `PIL.Image` - Flattened image

## flattenLayerOrGroup

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L401)

```python
def flattenLayerOrGroup(
    layerOrGroup: Union[(list[GimpLayer], GimpLayer)],
    imageDimensions: tuple[(int, int)],
    flattenedSoFar: Optional[Image.Image] = None,
    ignoreHidden: bool = True,
) -> Image.Image:
```

Flatten a layer or group on to an image of what has already been
flattened

#### Arguments

- `layerOrGroup` *Layer|Group* - A layer or a group of layers
imageDimensions ((int, int)): size of the image
- `flattenedSoFar` *PIL.Image, optional* - the image of what has already
been flattened. Defaults to None.
- `ignoreHidden` *bool, optional* - ignore layers that are hidden. Defaults
to True.

#### Returns

- `PIL.Image` - Flattened image

## rasterImageOffset

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L395)

```python
def rasterImageOffset(
    image: Image.Image,
    size: tuple[(int, int)],
    offsets: tuple[(int, int)] = (0, 0),
):
```

Rasterise an image with offset to a given size

## saveLayer

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L540)

```python
def saveLayer(gimpDoc, l, fileName: Union[(BytesIO, str)]):
```

save a layer

## showLayer

[[find in source code]](../../gimpformats/gimpXcfDocument.py#L531)

```python
def showLayer(image, l):
```

show a layer
