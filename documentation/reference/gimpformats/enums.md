# Enums

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Enums

> Auto-generated documentation for [gimpformats.enums](../../../gimpformats/enums.py) module.

- [Enums](#enums)
  - [AllProps](#allprops)
  - [ChannelProperties](#channelproperties)
  - [ColorMode](#colormode)
  - [CompositeMode](#compositemode)
  - [CompositeSpace](#compositespace)
  - [CompressionMode](#compressionmode)
  - [GeneralProperties](#generalproperties)
  - [GimpBlendMode](#gimpblendmode)
  - [ImageProperties](#imageproperties)
  - [LayerProperties](#layerproperties)
  - [TagColor](#tagcolor)
  - [Units](#units)
  - [merge_to](#merge_to)

## AllProps

[Show source in enums.py:205](../../../gimpformats/enums.py#L205)

#### Signature

```python
class AllProps(Enum): ...
```



## ChannelProperties

[Show source in enums.py:173](../../../gimpformats/enums.py#L173)

#### Signature

```python
class ChannelProperties(Enum): ...
```



## ColorMode

[Show source in enums.py:6](../../../gimpformats/enums.py#L6)

#### Signature

```python
class ColorMode(Enum): ...
```



## CompositeMode

[Show source in enums.py:19](../../../gimpformats/enums.py#L19)

#### Signature

```python
class CompositeMode(Enum): ...
```



## CompositeSpace

[Show source in enums.py:26](../../../gimpformats/enums.py#L26)

#### Signature

```python
class CompositeSpace(Enum): ...
```



## CompressionMode

[Show source in enums.py:44](../../../gimpformats/enums.py#L44)

#### Signature

```python
class CompressionMode(Enum): ...
```



## GeneralProperties

[Show source in enums.py:140](../../../gimpformats/enums.py#L140)

#### Signature

```python
class GeneralProperties(Enum): ...
```



## GimpBlendMode

[Show source in enums.py:51](../../../gimpformats/enums.py#L51)

#### Attributes

- `NORMAL_LEGACY` - Since 'ancient times' 0-9: 'Normal (legacy)'

- `LIGHTEN_ONLY_LEGACY` - Since 'ancient times' 10-18: 'Lighten only (legacy)'

- `SOFT_LIGHT_LEGACY` - Since XCF 2 19: 'Soft light (legacy)'

- `GRAIN_EXTRACT_LEGACY` - Since XCF 2 20-22: 'Grain extract (legacy)'

- `OVERLAY` - Since XCF 9 23-27: 'Overlay'

- `NORMAL` - Since XCF 10 28-29: 'Normal'

- `MULTIPLY` - Since XCF 10 30-39: 'Multiply'

- `VALUE_HSV` - Since XCF 10 40-49: 'Value (HSV)'

- `LINEAR_LIGHT` - Since XCF 10 50-59: 'Linear light'

- `SPLIT` - Since XCF 10 60-61: 'Split'


#### Signature

```python
class GimpBlendMode(Enum): ...
```



## ImageProperties

[Show source in enums.py:155](../../../gimpformats/enums.py#L155)

#### Signature

```python
class ImageProperties(Enum): ...
```



## LayerProperties

[Show source in enums.py:184](../../../gimpformats/enums.py#L184)

#### Signature

```python
class LayerProperties(Enum): ...
```



## TagColor

[Show source in enums.py:32](../../../gimpformats/enums.py#L32)

#### Signature

```python
class TagColor(Enum): ...
```



## Units

[Show source in enums.py:12](../../../gimpformats/enums.py#L12)

#### Signature

```python
class Units(Enum): ...
```



## merge_to

[Show source in enums.py:134](../../../gimpformats/enums.py#L134)

#### Signature

```python
def merge_to(src: Enum, dest: Enum): ...
```