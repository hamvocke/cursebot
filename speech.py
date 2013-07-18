#!/usr/bin/python

from pygsr import Pygsr
speech = Pygsr()
speech.record(3)
phrase, complete_response = speech.speech_to_text('de_DE')
print phrase
