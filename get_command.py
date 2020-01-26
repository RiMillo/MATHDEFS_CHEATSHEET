#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Write in outname a file with all the commands defined in mathdefs.
# Such a file is used in vimtex for autocompletion

import re

filename = './mathdefs.sty'
outname = './mathdefs'
fi = open(filename, 'r')
fo = open(outname, 'w')
for line in fi.readlines():
    if re.search('newcommand', line):
        line = line.replace("\\","")
        ins_curly_brackets = re.search(r'{(.*?)}',line).group(1)
        fo.write(ins_curly_brackets+'\n')
     # if newcommand
# for
fi.close()
fo.close()
