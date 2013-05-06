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

* python 2.7.4
* tornado
* sox
* NLTK. NLTK is a big dependency. Currently I only use it for tokenization, which is wasteful as the text processed
by this app seldom require complex tokenization. However, I intend to change the segmentation from word boundaries to
more natural pauses, like cause boundaries (like this one), which would require NLTK for shallow parsing, etc.

Installation for Ubuntu 12.10/Mint 14
-------------------------------------

    sudo apt-get install python-pip sox python-nltk
    sudo pip install tornado


Running tts-api
---------------

Run the application server with:

    python app.py
  
This project requires an HTTP server to serve the .mp3's.
For Nginx:
* set `127.0.0.1:8007` as an upstream frontend
* set the location of `/static/` to `/your/path/to/tts-api`

To get the .mp3 for your text, send a `GET` request to `/tts` with your text as a parameter.

    http://127.0.0.1:8007/tts?text=your%20text%20here
    
Your request wil result in a redirect to the .mp3 (sorry, not much error handling right now).

If you run the application server without an HTTP server, the redirect will return 404. You can still find the
complete .mp3 in tts-api/static/mp3/joined.
