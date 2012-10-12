#!/usr/bin/env python

import inspect, os, errno, markup
path =  os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+'/www/img/' # script directory
print path

counter = 1
el = len(os.listdir(path))

for f in os.listdir(path):
	if f[0] is ".":
		continue
	page = markup.page()
	page.init(charset="UTF-8")
	from markup import oneliner as e
	if counter+1 == el:
		page.a(e.img(src='img/'+f, width=1024), href='index1.html')
	else:
		page.a(e.img(src='img/'+f, width=1024), href='index'+str(counter+1)+'.html')
	final = open('www/index'+str(counter)+'.html','w')
	counter = counter + 1
	final.write(str(page))
	final.close()
	

