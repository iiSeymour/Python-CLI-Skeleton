A simple line numbering program to demonstrate a good CLI with python.

    $ ./cli_skeleton.py -h
    usage: cli_skeleton.py [-h] [files [files ...]]

    positional arguments:
      files       input files

    optional arguments:
      -h, --help  show this help message and exit

### File Input

Handles file input as expected:

    $ ./cli_skeleton.py file
    1 The Zen of Python, by Tim Peters
    2
    3 Beautiful is better than ugly.
    4 Explicit is better than implicit.
    5 Simple is better than complex.
    6 Complex is better than complicated.
    7 Flat is better than nested.
    8 Sparse is better than dense.
    9 Readability counts.
    10 Special cases aren't special enough to break the rules.
    11 Although practicality beats purity.
    12 Errors should never pass silently.
    13 Unless explicitly silenced.
    14 In the face of ambiguity, refuse the temptation to guess.
    15 There should be one-- and preferably only one --obvious way to do it.
    16 Although that way may not be obvious at first unless you're Dutch.
    17 Now is better than never.
    18 Although never is often better than *right* now.
    19 If the implementation is hard to explain, it's a bad idea.
    20 If the implementation is easy to explain, it may be a good idea.
    21 Namespaces are one honking great idea -- let's do more of those!

### Standard Input

Standard Input is not a problem:

    $ python -m this | ./cli_skeleton.py
    1 The Zen of Python, by Tim Peters
    2
    3 Beautiful is better than ugly.
    4 Explicit is better than implicit.
    5 Simple is better than complex.
    6 Complex is better than complicated.
    7 Flat is better than nested.
    8 Sparse is better than dense.
    9 Readability counts.
    10 Special cases aren't special enough to break the rules.
    11 Although practicality beats purity.
    12 Errors should never pass silently.
    13 Unless explicitly silenced.
    14 In the face of ambiguity, refuse the temptation to guess.
    15 There should be one-- and preferably only one --obvious way to do it.
    16 Although that way may not be obvious at first unless you're Dutch.
    17 Now is better than never.
    18 Although never is often better than *right* now.
    19 If the implementation is hard to explain, it's a bad idea.
    20 If the implementation is easy to explain, it may be a good idea.
    21 Namespaces are one honking great idea -- let's do more of those!

### No input

Displays the help message on no input:

    $ ./cli_skeleton.py
    usage: cli_skeleton.py [-h] [files [files ...]]

    positional arguments:
      files       input files

    optional arguments:
      -h, --help  show this help message and exit
