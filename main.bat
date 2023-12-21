@echo off
python ./program/north_crawler.py
python ./program/north_corner.py
python ./program/cropped.py
python ./program/combine.py
python ./program/north_API.py
python ./program/north_PPTAuto.py
echo done
pause