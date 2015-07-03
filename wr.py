import re
from datetime import datetime
def urlify(s):
	s = re.sub(r"[^\w\s]", '', s)
	s = re.sub(r"\s+", '-', s)
	return s
# x = raw_input('post name:')
title = raw_input('title: ')
time=str(datetime.now())
f = open('blog/'+urlify(title)+'.md','w')

f.write('---\nlayout:      post\ntitle:       '+title+'\ndate:        '+time[:10]+'\nupdate_date: \nsummary:     \npermalink:   /blog/'+urlify(title)+'/\n---\n\n')
f.close

g = open('blog.md','a')

g.write('\n'+'* ['+title+'](/'+'blog/'+urlify(title)+')')
g.close