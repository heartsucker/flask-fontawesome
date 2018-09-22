#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(__name__))

from example import create_app  # noqa

app = create_app()
app.run(host='127.0.0.1', port=8080, debug=True)
