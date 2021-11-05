# utils

> Auto-generated documentation for [gimpformats.utils](../../gimpformats/utils.py) module.

- [Gimpformats](../README.md#gimpformats-index) / [Modules](../README.md#gimpformats-modules) / [gimpformats](index.md#gimpformats) / utils
    - [fileOpen](#fileopen)
    - [save](#save)

## fileOpen

[[find in source code]](../../gimpformats/utils.py#L6)

```python
def fileOpen(fileName: BytesIO | str) -> tuple[(str, bytes)]:
```

## save

[[find in source code]](../../gimpformats/utils.py#L18)

```python
def save(data: bytes, tofileName: BytesIO | str = None):
```

Save this gimp image to a file.
