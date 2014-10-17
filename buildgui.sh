#!/bin/bash
rm ui_*.py
rm ui_*.pyc
pyside-uic UI-Layouts/qAndora.ui > ui_qAndora.py
pyside-uic UI-Layouts/qAndora-mobile.ui > ui_qAndora_mobile.py
pyside-uic UI-Layouts/qLogin.ui > ui_qLogin.py
pyside-uic UI-Layouts/qPreferences.ui > ui_qPreferences.py
