import inspect, os, errno, markup
path =  os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+'/www/img/' # script directory
print path

for f in os.listdir(path):
	page = markup.page()
	page.init(charset="UTF-8")

	page.img(src=f, width=1024, height=768)
	print page

