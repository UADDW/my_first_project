# -*- coding: utf-8 -*-
"""
Package my_first_project
=======================================

A 'hello world' example.
"""
__version__ = "0.0.0"


def hello(who='world'):
    """'Hello world' method.

    :param str who: whom to say hello to
    :returns: a string
    """
    result = "Hello " + who
    return result

# eof

print(hello())
print('Can you hear me?')
