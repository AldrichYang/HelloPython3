import re
yh = ' yang heng learn python '
print(yh.upper())
print(yh.lower())
# returns a string with whitespace removed from the start and end
print(yh.strip())
print(yh.split())
print(yh.join(['want', 'tobe']))
text = ("%d little pigs come out or I'll %s and %s and %s" %
        (3, 'huff', 'puff', 'blow down'))
# 注意：同样的语法，使用(),[],{}的输出效果都不一样，使用()是正常的
# text = ["%d little pigs come out or I'll %s and %s and %s" %
#         (3, 'huff', 'puff', 'blow down')]
# text = {"%d little pigs come out or I'll %s and %s and %s" %
#         (3, 'huff', 'puff', 'blow down')}
print(text)

uri = '/api/reserveAmount/get?userId=37350294'
print(uri.split('?'))
# print(uri.replace('?',''))
print(re.sub(r"(\?.*)",'',uri))
