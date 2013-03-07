# -*- coding: utf-8 -*-
'''
create routes

incoming should be full text string
need to segment string
save each mp3 to disk
cat mp3s
return path to mp3
delete mp3s at some point

'''
import urllib2
import urllib
import shutil
import os
import tornado.web
import tornado.ioloop
from tornado.options import define, options


class CheckHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('service minimally online')


class TTSHandler(tornado.web.RequestHandler):
    def get(self):
        text = self.get_argument("text", strip=True)


        with open(response_file_name, 'r') as response_file:
            self.write(response_file)




handlers = [
            (r"/check", CheckHandler),
            (r"/tts", TTSHandler),
            ]


settings = dict(template_path=os.path.join(
    os.path.dirname(__file__), "templates"))
application = tornado.web.Application(handlers, **settings)
define("port", default=8009, help="run on the given port", type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


base_url = 'http://translate.google.com/translate_tts?tl=en&q='



# Set the user agent
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

files = ['mp3/part1.mp3', 'mp3/part2.mp3', 'mp3/part3.mp3']

# Get the parts
response = opener.open(base_url + part1)
localFile = open('mp3/part1.mp3', 'w')
localFile.write(response.read())
localFile.close()

response = opener.open(base_url + part2)
localFile = open('mp3/part2.mp3', 'w')
localFile.write(response.read())
localFile.close()

response = opener.open(base_url + part3)
localFile = open('mp3/part3.mp3', 'w')
localFile.write(response.read())
localFile.close()

# Cat the parts
PATH = r'/home/gavin/dev/tts-api/mp3'

with open('mp3/merged.mp3', 'wb') as destination:
	for filename in files:
		with open(filename, 'rb') as in_:
		    shutil.copyfileobj(in_, destination)
