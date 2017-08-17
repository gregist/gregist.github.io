'''create a drawing post'''

import re
from datetime import datetime
from datetime import timedelta


def urlify(string):
    '''urlify'''
    string = re.sub(r"[^\w\s]", '', string)
    string = re.sub(r"\s+", '-', string)
    return string

# INPUT = '~2016-07-17|'
INPUT = input('title: ').split('|')
TITLE = INPUT[0]
CONTEXT = INPUT[1] if len(INPUT) > 1 else ''

TIME = datetime.now()
while TITLE[:1] == '`':
    TIME = TIME - timedelta(hours=24)
    TITLE = TITLE[1:]
TIME = str(TIME)

print(TIME)

CONTENT = '''---
layout:     post
title:      %s
date:       %s
summary:    
categories: drawing
---
![%s](/images/diary/%s.png \"%s\")
''' % (TITLE, TIME[:19], TITLE, urlify(TITLE), CONTEXT)

with open('_posts/'+TIME[:10]+'-'+urlify(TITLE)+'.md', 'w') as flw:
    flw.write(CONTENT)
