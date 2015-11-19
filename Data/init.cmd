@echo off
set arg1=%1
set arg2=%2
REM cd %~dp0
cd.
Python.2.7.10\pythonw.exe Data\MultiClip.py %arg1% %arg2%