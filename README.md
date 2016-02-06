## ID Tech Hangout Source Codes

To use this you need to install Thrift and python virtualenv

run the followings

```
$ mkdir authpy
$ mkdir authrb
$ thrift -gen py -out authpy auth.thrift
$ thrift -gen rb -out authrb auth.thrift
$ virtualenv env
$ . env/bin/activate
$ pip install -r deps
```

To run the server simply run

```
$ python app.py
```

You can use pyclient to communicate from python and rbclient to communicate from ruby.

Presentation link:
https://docs.google.com/presentation/d/1oBNgrxyVLJJfxg26mc5tpBxOuc3vBfXAzXAe_dYKaNM/edit?usp=sharing

Youtube video
http://www.youtube.com/watch?v=hygZIml3VLo
