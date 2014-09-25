#!/bin/bash

#Remove old data
rm Compiled-Packages/qandora.deb
rm -rf Compiled-Packages/qandora/opt/qAndora/*

#Move over new files
cp qAndora.py Compiled-Packages/qandora/opt/qAndora/
cp ui_*.py Compiled-Packages/qandora/opt/qAndora/
cp -a images Compiled-Packages/qandora/opt/qAndora/
cp -a playerVLC Compiled-Packages/qandora/opt/qAndora/

#Build new deb
cd Compiled-Packages/
dpkg --build qandora
