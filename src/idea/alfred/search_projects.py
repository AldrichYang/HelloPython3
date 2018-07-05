import sys

# import sys
#
# query = "{query}"
#
# sys.stdout.write(query)
import os
import json

PROJECT_PATH = u'/Users/user/Idea_workspace/'

query = "invt"
result = ['dir1', 'dir2', 'dir3']


def search(query):
    return json.dumps(result)


sys.stdout.write(search(query))
sys.stdout.write(json.dumps({'items': [{'item': {'title': 'dir1'}}]}))
