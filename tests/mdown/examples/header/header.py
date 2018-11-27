#!/usr/bin/env python
import mdown

string = '# Title'
assert string == mdown.header("Title", 1)

string = '###### Title'
assert string == mdown.header("Title", 6)
