<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/mdown.svg?maxAge=3600)](https://pypi.org/project/mdown/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/mdown.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/mdown.py/actions)

### Installation
```bash
$ [sudo] pip install mdown
```

#### Examples
**header**
```python
>>> import mdown
>>> mdown.header("title", 6)
'###### Title'
```
**code**
```python
>>> mdown.code("$ [sudo] pip install readme_md", "bash")
# look Install section :)
```

**image**
```python
>>> mdown.image("https://domain.com/image.png", title="title text", alt="alt text")
'![alt text](https://domain.com/image.png "title text")'
```

**table**
```python
>>> mdown.table(("header1","header2"),(("cell11","cell12"), ("cell21","cell22")))
'header1|header2
-|-
cell11|cell12
cell21|cell22'
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
