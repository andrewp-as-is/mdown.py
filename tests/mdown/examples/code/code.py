#!/usr/bin/env python
import mdown

string = """```bash
$ [sudo] pip install readme-md
```"""
assert string == mdown.code("$ [sudo] pip install readme-md", "bash")
