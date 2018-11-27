[![](https://img.shields.io/pypi/pyversions/mdown.svg?longCache=True)](https://pypi.org/pypi/mdown/)
[![](https://img.shields.io/pypi/v/mdown.svg?maxAge=3600)](https://pypi.org/pypi/mdown/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mdown.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mdown.py/)

#### Install
```bash
$ [sudo] pip install mdown
```

#### Functions
function|description
-|-
`mdown.code(code, language=None)`|return string with markdown code block
`mdown.header(title, lvl)`|return string with markdown header
`mdown.image(url, link='', title='', alt='')`|return string with markdown image
`mdown.table(headers, matrix)`|return string with markdown table (one-line cells only)

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

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>