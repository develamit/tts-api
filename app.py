# -*- coding: utf-8 -*-
'''


'''
import urllib2
from urllib import quote_plus
import shutil
from os import urandom
import subprocess
from os.path import dirname, realpath, join
import tornado.web
import tornado.ioloop
from tornado.options import define, options
from text_segmenter import get_segments
from binascii import hexlify

class TTSHandler(tornado.web.RequestHandler):
    def get(self):
        joined_name = hexlify(urandom(16))

        # Set the user agent
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        base_url = 'http://translate.google.com/translate_tts?tl=en&q='

        # Split the text into <100 character segments
        text = self.get_argument("text", strip=True)
        segments = get_segments(text)
        segments = [quote_plus(s) for s in segments]

        trimmed_names = []
        for segment in segments:
            name = hexlify(urandom(16))
            #try:
            tts_response = opener.open(base_url + segment)
            raw_name = 'static/mp3/%s_r.mp3' % name
            trimmed_name = 'static/mp3/%s_t.mp3' % name

            raw_file = open(raw_name, 'w')
            raw_file.write(tts_response.read())
            raw_file.close()

            sox_call = ['sox',
                dirname(realpath(__file__)) + '/' + raw_name,
                dirname(realpath(__file__)) + '/'+ trimmed_name,
                'silence', '1', '0', '-40d']
            return_code = subprocess.call(sox_call)
            if return_code != 0:
                print 'error'

            trimmed_names.append(trimmed_name)


        # Cat the parts
        PATH = dirname(realpath(__file__)) + '/static/mp3/joined/'

        response_file_name = PATH + joined_name + '.mp3'
        with open(response_file_name, 'wb') as destination:
            for file_name in trimmed_names:
                with open(file_name, 'rb') as in_:
                    shutil.copyfileobj(in_, destination)

        self.redirect(response_file_name)


handlers = [
            (r"/tts", TTSHandler),
            ]


settings = dict(template_path=join(
    dirname(__file__), "templates"))
application = tornado.web.Application(handlers, **settings)
define("port", default=8007, help="run on the given port", type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()








