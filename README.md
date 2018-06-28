# prism-markdown-extension

## Install

```bash
pip3 install markdown-prism
```

## Usage

```python
from markdown import markdown
from markdown_prism import PrismCodeExtension

text = '''
`sudo pip3 install markdown-prism`
'''
html = markdown(text, extensions=[PrismCodeExtension()])
print(html)
```

then link prism.js and prism css in your html