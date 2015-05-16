from datetime import datetime
# x = raw_input('post name:')
title = raw_input('title:')
time=str(datetime.now())
f = open('_posts/'+time[:10]+'-'+title+'.md','w')

f.write('---\nlayout:     post\ntitle:      '+title+'\ndate:       '+time[:19]+'\nsummary:    \ncategories: drawing\n---')
f.close
