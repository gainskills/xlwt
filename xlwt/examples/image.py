#!/usr/bin/env python
# -*- coding: windows-1251 -*-
# Copyright (C) 2005 Kiseliov Roman

__rev_id__ = """$Id$"""


from pyExcelerator import *

w = Workbook()
ws = w.add_sheet('Image')
ws.insert_bitmap('python.bmp', 2, 2)
ws.insert_bitmap('python.bmp', 10, 2)

w.save('image.xls')