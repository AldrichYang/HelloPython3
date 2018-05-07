import sys
# help string for the built-in len() function; note that it's "len" not "len()",
# which is a call to the function, which we don't want
help(len)
help(sys)

# dir() is like help() but just gives a quick list of its defined symbols, or "attributes"
dir(sys)

# help string for the exit() function in the sys module
help(sys.exit)

# help string for the split() method for string objects.
# You can call help() with that object itself or an example of that object, plus its attribute.
#  For example, calling help('xyz'.split) is the same as calling help(str.split).
help('xyz'.split)

# help string for list objects
help(list)

# displays list object attributes, including its methods
dir(list)

# help string for the append() method for list objects
help(list.append)
