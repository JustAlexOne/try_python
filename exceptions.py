try:
    import chardet
except ImportError:
    chardet = None

if chardet:
    print("Good!")
else:
    print("Bad")

try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree