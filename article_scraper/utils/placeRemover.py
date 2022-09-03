import re

def clean(txt):
    txt = re.sub(r'([\w,\s]*)—', '', txt)
    return txt