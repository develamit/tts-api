tts-api
=======

tts-api is an API for Google Translate's text-to-speech functionality.

Google Translate imposes a 100 character limit on input text; tts-api accepts text of arbitrary length. 

tts-api:
* splits input text into <100 character segments on word boundaries. In the future, it may be helpful to
split on clause boundaries or other natural pauses.
* strips the initial silence from the retrieved .mp3's.
* concatenates the .mp3's and redirects the request to the file.


Dependencies
------------

* python 2.7
* tornado
* sox

Installation:

  sudo apt-get install python-pip sox libsox-fmt-mp3
  sudo pip install tornado



Running tts-api
---------------

  python app.py
  
This project requires an HTTP server to serve the .mp3's.
For Nginx:
* set 127.0.0.1:8007 as an upstream frontend
* set the location of /static/ to /your/path/to/tts-api
