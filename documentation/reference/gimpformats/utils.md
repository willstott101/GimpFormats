# Utils

[Gimpformats Index](../README.md#gimpformats-index) / [Gimpformats](./index.md#gimpformats) / Utils

> Auto-generated documentation for [gimpformats.utils](../../../gimpformats/utils.py) module.

- [Utils](#utils)
  - [fileOpen](#fileopen)
  - [repr_indent_lines](#repr_indent_lines)
  - [save](#save)

## fileOpen

[Show source in utils.py:9](../../../gimpformats/utils.py#L9)

Load a file.

#### Arguments

- `fileName` - can be a file name or a file-like object

#### Signature

```python
def fileOpen(file: BytesIO | str | Path) -> tuple[str, bytes]: ...
```



## repr_indent_lines

[Show source in utils.py:31](../../../gimpformats/utils.py#L31)

Represent lines with a given indentation (number of tabs).

#### Arguments

- `indent` *int* - number of tabs
:param list[str] lines: list of lines to represent

#### Returns

Type: *str*
indented lines

#### Signature

```python
def repr_indent_lines(indent: int, lines: list[str]) -> str: ...
```



## save

[Show source in utils.py:21](../../../gimpformats/utils.py#L21)

Save this gimp image to a file.

#### Signature

```python
def save(data: bytearray | bytes, file: BytesIO | str | Path) -> None: ...
```