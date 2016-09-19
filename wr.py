import re
from datetime import datetime

def urlify(s):
	s = re.sub(r"[^\w\s]", '', s)
	s = re.sub(r"\s+", '-', s)
	return s

title = raw_input('title: ')
time=str(datetime.now())

content='''---
layout:      post
title:       %s
date:        %s
update_date: 
summary:     
categories:  blog
permalink:   /blog/%s/
---

'''%(title, time[:10],urlify(title))

f = open('blog/'+urlify(title)+'.md','w')
f.write(content)
f.close
