from datetime import datetime
x = raw_input('post name:')
title = raw_input('title:')
f = open('_posts/'+x+'.md','w')
time=str(datetime.now())[:19]
f.write('---\nlayout:     post\ntitle:      '+title+'\ndate:       '+time+'\nsummary:    \ncategories: drawing\n---')
f.close
