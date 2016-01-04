'''create a drawing post'''

import re
from datetime import datetime

def urlify(string):
	string = re.sub(r"[^\w\s]", '', string)
	string = re.sub(r"\s+", '-', string)
	return string

TITLE = raw_input('title: ')
TIME = str(datetime.now())

CONTENT = '''---
layout:     post
title:      %s
date:       %s
summary:    
categories: drawing
---
![%s](/images/diary/%s.png \"\")
'''%(TITLE, TIME[:19], TITLE, urlify(TITLE))

with open('_posts/'+TIME[:10]+'-'+urlify(TITLE)+'.md', 'w') as flw:
    flw.write(CONTENT)

