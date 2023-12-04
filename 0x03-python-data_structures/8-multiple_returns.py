#!/usr/bin/python3
def multiple_returnes(sentence):
    return (len(sentence), sentence[0] if len(sentence) > 0 else None)
