@echo off
set arg1=%1
set arg2=%2
cd %~dp0
start Python.2.7.10\pythonw.exe mailPaste.py %arg1% %arg2%