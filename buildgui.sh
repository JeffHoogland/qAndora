#!/bin/bash
rm ui_*.py
rm ui_*.pyc
pyside-uic qAndora.ui > ui_qAndora.py
pyside-uic qLogin.ui > ui_qLogin.py
