#!/bin/bash
rm ui_*.py
rm ui_*.pyc
pyside-uic qAndora.ui > ui_qAndora.py
pyside-uic qAndora-mobile.ui > ui_qAndora-mobile.py
pyside-uic qLogin.ui > ui_qLogin.py
pyside-uic qPreferences.ui > ui_qPreferences.py
