#!/usr/bin/pyhon3
'''Module for lookup method.'''


def lookup(obj):
    '''Looks up object attribute and methods.
    Args:
        obj (object): the object to list.

    Returns:
        list: the list of attributes.
    '''
    return dir(obj)
