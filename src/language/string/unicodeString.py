# Regular Python strings are *not* unicode, they are just plain bytes.
# To create a unicode string, use the 'u' prefix on the string literal

ustring = u'A unicode \u018e string \xfe'
print(ustring)
# convert a unicode string to bytes with an encoding such as 'utf-8',
# call the ustring.encode('utf-8') method on the unicode string
s = ustring.encode('utf-8')
print(s)
# the unicode(s, encoding) function converts encoded plain bytes to a unicode string
# t = unicode(s, 'utf-8')
# print(t == ustring)
