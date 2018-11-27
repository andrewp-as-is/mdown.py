#!/usr/bin/env python
import mdown

image = "https://domain.com/image.png"
string = '![alt text](https://domain.com/image.png "title text")'
assert string == mdown.image(image, title="title text", alt="alt text")

md = mdown.image(image, title="title text", alt="")
string = '![](https://domain.com/image.png "title text")'
assert string == mdown.image(image, title="title text", alt="")
