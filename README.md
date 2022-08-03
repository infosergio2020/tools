# tools
this is my scripts


# to make .exe
1) you need install: tinyages, pyinstaller, PySimpleGUI and need download upx.exe and paste to disk C:\
2) if you need save dependencies --> pip freeze > requirements.txt
pyinstaller ..\gui_XML.py --key 123456 -n find_dup -F -w --upx-dir C:\ 