A simple, cross-platform tool for playing Pandora.com radio with a QT GUI and a VLC backend

Install instructions:

Ubuntu/Debian
  - Download and install .deb file -> https://github.com/JeffHoogland/qAndora/blob/master/Compiled-Packages/qandora.deb?raw=true
  - Launch qAndora.desktop or run qAndora in terminal

Windows
  - Install VLC http://www.videolan.org/
  - Download zip file -> https://github.com/JeffHoogland/qAndora/blob/master/Compiled-Packages/windows.zip?raw=true
  - Extract the contents
  - Run qAndora.exe
  - Optional: For global multimedia key support install: http://sourceforge.net/projects/pyhook/

Nokia N900/Fremantle
  - Install python-gst0.10
  - Download and extract qandora-n900.tar.gz -> https://github.com/JeffHoogland/qAndora/blob/master/Compiled-Packages/qandora-n900.tar.gz
  - Run qAndora.py: python qAndora.py

Nokia N9/Harmattan
  - Download and install .deb file for python-gst0.10 -> http://mirror.lxer.com/harmattan/url/http/mirror.thecust.net/harmattan-dev.nokia.com/pool/harmattan/free/g/gst0.10-python/python-gst0.10_0.10.21-1maemo2+0m6_armel.deb
  - Download and install .deb file for qAndora -> https://github.com/JeffHoogland/qAndora/blob/master/Compiled-Packages/qandora-mobile.deb?raw=true
  - Launch qAndora from home screen

Other OS
  - Install PySide, VLC, and GIT
  - Clone sources: git clone https://github.com/JeffHoogland/qAndora.git
  - Run qAndora.py: python qAndora.py

TODO List:
- Add/remove/edit stations
- Add validation that the pandora login works instead of assuming it does
- hot keys: http://i.imgur.com/ea9qQwN.png
- Add preference option to change between VLC and Gst backends
