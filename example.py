#!/usr/bin/env python3

import os
from mako.template import Template

DIR_PATH = os.path.dirname(os.path.realpath(__file__))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


persons = [Person("Orwell", 39),
           Person("Melville", 65),
           Person("Hemingway", 20)]

template_file = os.path.join(DIR_PATH, "template.txt")
template = Template(filename=template_file)
print(template.render(persons=persons))
