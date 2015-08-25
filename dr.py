import re
from datetime import datetime

def urlify(s):
	s = re.sub(r"[^\w\s]", '', s)
	s = re.sub(r"\s+", '-', s)
	return s

title = raw_input('title: ')
time=str(datetime.now())

content='''---
layout:     post
title:      %s
date:       %s
summary:    
categories: drawing
---
![%s](/images/blog/%s.png \"\")
'''%(title, time[:19],title,urlify(title))

f = open('_posts/'+time[:10]+'-'+urlify(title)+'.md','w')
f.write(content)
f.close
