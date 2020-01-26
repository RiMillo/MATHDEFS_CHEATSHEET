#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

filename = '/home/e74177/PhD/MATHDEFS_CHEATSHEET/mathdefs.sty'
outfile = '/home/e74177/PhD/MATHDEFS_CHEATSHEET/table.tex'
with open(filename, 'r') as f:
    with open(outfile, 'w') as fo:

        line = f.readline()
        while line:
            if line[:11] == '\\newcommand':
                cmd = None
                nb = None
                expr = None
                # print(line)
                # break
                # line = re.escape(line)
                match = re.search(r'\\newcommand{(.+)}\[(.+)\]{(.+)}', line)
                if match:
                    cmd, nb, expr = match.groups()
                else:
                    match = re.search(r'\\newcommand{(.+)}{(.+)}', line)
                    if match:
                        cmd, expr = match.groups()
                        print('One',cmd, expr)
                    else:
                        match = re.search(r'\\newcommand{(.+)}\[(.+)\]', line)
                        if match:
                            cmd, nb = match.groups()
                            # print 'Two'
                            print('Two',cmd, nb)
                        else:
                            print(line)
                # print(cmd, nb, expr)
                if nb is None:
                    nb = 0
                out = '$ {cmd} $ & {nb} & \\verb|{cmd}| & \\verb|{expr}| \\\\'.format(cmd=cmd,
                                                                                     nb=nb,
                                                                                     expr=expr)
                fo.write(out+'\n')
            line = f.readline()
