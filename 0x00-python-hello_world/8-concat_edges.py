#!/usr/bin/python3

str_text = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"

str_text = str_text[39:-62] + str_text[107:-17] + str_text[:6]
print(str_text)
