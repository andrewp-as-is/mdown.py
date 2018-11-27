#!/usr/bin/env python
import mdown


headers = ("header1", "header2")
matrix = (("cell11", "cell12"), ("cell21", "cell22"))
string = """header1|header2
-|-
cell11|cell12
cell21|cell22"""

assert string == mdown.table(headers, matrix)
