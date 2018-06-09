# -*- coding: utf-8 -*-
__author__ = 'Сергі Полунець'
__versions__ = "v.3.6.5-64"
import os
names = "PogodaPC"
scripts = "PogodaPC"
icons = "PogodaPC"
num = 2
path = '"C:/Program Files (x86)/Windows Kits/10/Redist/ucrt/DLLs/x64"'
pathQt = 'C:/Python36-64/Lib/site-packages/PyQt5/Qt/bin'
if str(num) == "1":
    pacs = "--onefile --console"
elif str(num) == "2":
    pacs = "--windowed"
elif str(num) == "3":
    pacs = "--onefile --windowed"
else:
    pacs = "--console"
os.system("pyinstaller.exe {0} --icon={1}.ico {2}.py --name={3} --paths={4} --paths={5} ".format(pacs, icons, scripts, names, path ,pathQt))
#os.system("del /a " + "{0}.spec".format(names))
