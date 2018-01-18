# -*- coding: utf-8 -*-
#Needed to select a random element from list
import random

#Initialize and fill list
alist = []
alist.append(23453)
alist.append("A String")
alist.append(2341.674)
alist.append('c')

#Initialize and fill map
amap = {}
amap['me'] = "Nicholas Biegel"
amap['you'] = "Michael Lewis"

#Print out list, map, and others
print(alist)
print(random.choice(alist))
print(amap)
print(amap['me'])