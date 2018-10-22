# cinecanvas2srt
Simple CineCanvas DCP subtitle XML to SRT converter in Python 3

Usage:
```
$ python3 -m venv _py_env
$ py_env/bin/pip install -r requirements.txt
$ _py_env/bin/python3 cinecanvas-subs-to-srt.py cinecanvas_test.xml
```

That outputs converted SRT to stdout:

```
1
00:00:16,460 --> 00:00:19,416
It's funny you think about
the process of making the game, -

2
00:00:19,496 --> 00:00:22,456
and you're taking
an incredible amount of things.

3
00:00:22,572 --> 00:00:27,208
Thousands of great ideas.
You can't just have a hundred.

4
00:00:27,408 --> 00:00:31,684
You have to have thousands of ideas.
Or 10,000.
```
