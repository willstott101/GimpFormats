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
  - [blendModeLookup](#blendmodelookup-1)
  - [flattenAll](#flattenall)
  - [flattenLayerOrGroup](#flattenlayerorgroup)
  - [renderLayerOrGroup](#renderlayerorgroup)
  - [renderMaskWOffset](#rendermaskwoffset)

## BlendType

[Show source in gimpXcfDocument.py:439](../../../gimpformats/gimpXcfDocument.py#L439)

#### Signature

```python
class BlendType(Enum): ...
```



## GimpDocument

[Show source in gimpXcfDocument.py:33](../../../gimpformats/gimpXcfDocument.py#L33)

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
    def __init__(self, fileName=None) -> None: ...
```

### GimpDocument().__delitem__

[Show source in gimpXcfDocument.py:339](../../../gimpformats/gimpXcfDocument.py#L339)

Make this class act like this class is an array of layers...

Delete a layer at an index.

#### Signature

```python
def __delitem__(self, index: int) -> None: ...
```

### GimpDocument().__getitem__

[Show source in gimpXcfDocument.py:325](../../../gimpformats/gimpXcfDocument.py#L325)

Make this class act like this class is an array of layers...

Get the layer at an index.

#### Signature

```python
def __getitem__(self, index: int) -> GimpLayer: ...
```

### GimpDocument().__len__

[Show source in gimpXcfDocument.py:318](../../../gimpformats/gimpXcfDocument.py#L318)

Make this class act like this class is an array of layers...

Get the len.

#### Signature

```python
def __len__(self) -> int: ...
```

### GimpDocument().__repr__

[Show source in gimpXcfDocument.py:401](../../../gimpformats/gimpXcfDocument.py#L401)

Get a textual representation of this object.

#### Signature

```python
def __repr__(self, indent: int = 0) -> str: ...
```

### GimpDocument().__setitem__

[Show source in gimpXcfDocument.py:332](../../../gimpformats/gimpXcfDocument.py#L332)

Make this class act like this class is an array of layers...

Set a layer at an index.

#### Signature

```python
def __setitem__(self, index: int, layer) -> None: ...
```

### GimpDocument().__str__

[Show source in gimpXcfDocument.py:397](../../../gimpformats/gimpXcfDocument.py#L397)

Get a textual representation of this object.

#### Signature

```python
def __str__(self) -> str: ...
```

### GimpDocument().addLayer

[Show source in gimpXcfDocument.py:291](../../../gimpformats/gimpXcfDocument.py#L291)

Append a layer object to the document.

#### Arguments

- `layer` - the new layer to append

#### Signature

```python
def addLayer(self, layer: GimpLayer) -> None: ...
```

### GimpDocument().appendLayer

[Show source in gimpXcfDocument.py:298](../../../gimpformats/gimpXcfDocument.py#L298)

Append a layer object to the document.

#### Arguments

- `layer` - the new layer to append

#### Signature

```python
def appendLayer(self, layer: GimpLayer) -> None: ...
```

### GimpDocument().decode

[Show source in gimpXcfDocument.py:93](../../../gimpformats/gimpXcfDocument.py#L93)

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

[Show source in gimpXcfDocument.py:313](../../../gimpformats/gimpXcfDocument.py#L313)

Delete a layer.

#### Signature

```python
def deleteLayer(self, index: int) -> None: ...
```

### GimpDocument().encode

[Show source in gimpXcfDocument.py:166](../../../gimpformats/gimpXcfDocument.py#L166)

Encode to bytes.

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

[Show source in gimpXcfDocument.py:211](../../../gimpformats/gimpXcfDocument.py#L211)

Make sure everything is fully loaded from the file.

#### Signature

```python
def forceFullyLoaded(self) -> None: ...
```

### GimpDocument().getLayer

[Show source in gimpXcfDocument.py:243](../../../gimpformats/gimpXcfDocument.py#L243)

Return a given layer.

#### Signature

```python
def getLayer(self, index: int): ...
```

### GimpDocument().image

[Show source in gimpXcfDocument.py:350](../../../gimpformats/gimpXcfDocument.py#L350)

Get a final, compiled image.

#### Signature

```python
@property
def image(self): ...
```

### GimpDocument().insertLayer

[Show source in gimpXcfDocument.py:305](../../../gimpformats/gimpXcfDocument.py#L305)

Insert a layer object at a specific position.

#### Arguments

- `layer` - the new layer to insert
- `index` - where to insert the new layer (default=top)

#### Signature

```python
def insertLayer(self, layer: GimpLayer, index: int = -1) -> None: ...
```

### GimpDocument().layers

[Show source in gimpXcfDocument.py:222](../../../gimpformats/gimpXcfDocument.py#L222)

Decode the image's layers if necessary.

TODO: need to do the same thing with self.Channels

#### Signature

```python
@property
def layers(self): ...
```

### GimpDocument().load

[Show source in gimpXcfDocument.py:85](../../../gimpformats/gimpXcfDocument.py#L85)

Load a gimp xcf and decode the file. See decode for more on this process.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def load(self, fileName: BytesIO | str) -> None: ...
```

### GimpDocument().newLayer

[Show source in gimpXcfDocument.py:253](../../../gimpformats/gimpXcfDocument.py#L253)

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

### GimpDocument().newLayerFromClipboard

[Show source in gimpXcfDocument.py:271](../../../gimpformats/gimpXcfDocument.py#L271)

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

[Show source in gimpXcfDocument.py:378](../../../gimpformats/gimpXcfDocument.py#L378)

Save this gimp image to a file.

#### Signature

```python
def save(self, filename: str | BytesIO | None = None) -> NoReturn: ...
```

### GimpDocument().saveNew

[Show source in gimpXcfDocument.py:388](../../../gimpformats/gimpXcfDocument.py#L388)

Save a new gimp image to a file.

#### Signature

```python
def saveNew(self, filename=None) -> NoReturn: ...
```

### GimpDocument().setLayer

[Show source in gimpXcfDocument.py:247](../../../gimpformats/gimpXcfDocument.py#L247)

Assign to a given layer.

#### Signature

```python
def setLayer(self, index, layer) -> None: ...
```



## blendModeLookup

[Show source in gimpXcfDocument.py:430](../../../gimpformats/gimpXcfDocument.py#L430)

Get the blendmode from a lookup table.

#### Signature

```python
def blendModeLookup(
    blendmode: int,
    blendLookup: dict[int, BlendType],
    default: BlendType = BlendType.NORMAL,
): ...
```

#### See also

- [BlendType](#blendtype)



## blendModeLookup

[Show source in gimpXcfDocument.py:613](../../../gimpformats/gimpXcfDocument.py#L613)

#### Signature

```python
def blendModeLookup(blend_mode, blendLookup): ...
```



## flattenAll

[Show source in gimpXcfDocument.py:585](../../../gimpformats/gimpXcfDocument.py#L585)

#### Signature

```python
def flattenAll(
    layers: list[GimpLayer], imageDimensions: tuple[int, int], ignoreHidden: bool = True
) -> Image.Image: ...
```



## flattenLayerOrGroup

[Show source in gimpXcfDocument.py:516](../../../gimpformats/gimpXcfDocument.py#L516)

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

[Show source in gimpXcfDocument.py:596](../../../gimpformats/gimpXcfDocument.py#L596)

#### Signature

```python
def renderLayerOrGroup(
    image: Image.Image, size: tuple[int, int], offsets: tuple[int, int] = (0, 0)
) -> Image.Image: ...
```



## renderMaskWOffset

[Show source in gimpXcfDocument.py:604](../../../gimpformats/gimpXcfDocument.py#L604)

#### Signature

```python
def renderMaskWOffset(
    image: Image.Image, size: tuple[int, int], offsets: tuple[int, int] = (0, 0)
) -> Image.Image: ...
```