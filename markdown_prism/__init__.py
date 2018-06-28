from markdown_prism.extension import PrismCodeExtension


def makeExtension(*args, **kwargs):
    return PrismCodeExtension(*args, **kwargs)