#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# simple.py

import sys
from PyQt5.QtWidgets import (QApplication)

from SshManager import SshManager

app = QApplication(sys.argv)

sshManager = SshManager()
sshManager.show()

sys.exit(app.exec_())