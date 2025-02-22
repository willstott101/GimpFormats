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

[Show source in enums.py:206](../../../gimpformats/enums.py#L206)

#### Signature

```python
class AllProps(Enum): ...
```



## ChannelProperties

[Show source in enums.py:174](../../../gimpformats/enums.py#L174)

#### Signature

```python
class ChannelProperties(Enum): ...
```



## ColorMode

[Show source in enums.py:7](../../../gimpformats/enums.py#L7)

#### Signature

```python
class ColorMode(Enum): ...
```



## CompositeMode

[Show source in enums.py:20](../../../gimpformats/enums.py#L20)

#### Signature

```python
class CompositeMode(Enum): ...
```



## CompositeSpace

[Show source in enums.py:27](../../../gimpformats/enums.py#L27)

#### Signature

```python
class CompositeSpace(Enum): ...
```



## CompressionMode

[Show source in enums.py:45](../../../gimpformats/enums.py#L45)

#### Signature

```python
class CompressionMode(Enum): ...
```



## GeneralProperties

[Show source in enums.py:141](../../../gimpformats/enums.py#L141)

#### Signature

```python
class GeneralProperties(Enum): ...
```



## GimpBlendMode

[Show source in enums.py:52](../../../gimpformats/enums.py#L52)

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

[Show source in enums.py:156](../../../gimpformats/enums.py#L156)

#### Signature

```python
class ImageProperties(Enum): ...
```



## LayerProperties

[Show source in enums.py:185](../../../gimpformats/enums.py#L185)

#### Signature

```python
class LayerProperties(Enum): ...
```



## TagColor

[Show source in enums.py:33](../../../gimpformats/enums.py#L33)

#### Signature

```python
class TagColor(Enum): ...
```



## Units

[Show source in enums.py:13](../../../gimpformats/enums.py#L13)

#### Signature

```python
class Units(Enum): ...
```



## merge_to

[Show source in enums.py:135](../../../gimpformats/enums.py#L135)

#### Signature

```python
def merge_to(src: Enum, dest: Enum): ...
```