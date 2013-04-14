#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image
import os
def makeThumbnails(instance, **kwargs):
    im = Image.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                    "static/media/" + instance.image.name).replace("/", "\\"))
    im = im.resize((273, 375), Image.ANTIALIAS)
    im.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
        "static/media/" + instance.image.name).replace("/", "\\"))