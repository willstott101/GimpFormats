# Native Convert

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Native Convert

> Auto-generated documentation for [gimpformats.native_convert](../../../gimpformats/native_convert.py) module.

- [Native Convert](#native-convert)
  - [convert_xcf_to_flat_image](#convert_xcf_to_flat_image)

## convert_xcf_to_flat_image

[Show source in native_convert.py:73](../../../gimpformats/native_convert.py#L73)

Convert an xcf file given by `xcf_path` to some flat image (such
as a jpg, png etc) given by `output_path`.

#### Arguments

- `xcf_path` *str* - path to a source xcf file
- `output_path` *str* - path to an output file (eg a png)

#### Signature

```python
def convert_xcf_to_flat_image(xcf_path: str, output_path: str) -> None: ...
```