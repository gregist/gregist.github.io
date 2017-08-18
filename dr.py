'''create a drawing post'''

import re
from datetime import datetime
from datetime import timedelta

INPUT = input('title: ').split('|')
def urlify(string):
    '''urlify'''
    string = re.sub(r"[^\w\s]", '', string)
    string = re.sub(r"\s+", '-', string)
    return string

# INPUT = '!2016-07-02-motif'.split('|')
# INPUT = 'motif jdf|test'.split('|')

def generator(input):
    if input[0][0] == '!':
        lines = []
        title = input[0].split('-')[-1]
        file = '_posts/'+input[0][1:]+'.md'
        with open(file, 'r') as fr:
            cont = fr.read()
        cont = cont.replace(title, title+' 1', 2).replace(title+'.png', title+'-1.png')
        file1 = '_posts/'+input[0][1:]+'-1.md'
        print(file+'>>>'+file1)
        return [file1, cont]
    else:
        title = input[0]
        context = input[1] if len(input) > 1 else ''
        time = datetime.now()
        while title[0] == '`':
            time = time - timedelta(hours=24)
            title = title[1:]
        time = str(time)
        cont = '''---
layout:     post
title:      %s
date:       %s
summary:    
categories: drawing
---
![%s](/images/diary/%s.png \"%s\")
''' % (title, time[:19], title, urlify(title), context)
        file = '_posts/'+time[:10]+'-'+urlify(title)+'.md'
        print('>>>'+file)
        return [file, cont]

para = generator(INPUT)

with open(para[0], 'w') as fw:
    fw.write(para[1])
    # print('done!')
