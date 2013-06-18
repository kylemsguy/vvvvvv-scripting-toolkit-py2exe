@echo off

echo Deleting old archive...
if exist vvvvvv-scripting-toolkit-win32.zip del vvvvvv-scripting-toolkit-win32.zip

echo Purging dist folder...
rd /s dist
md dist

echo Updating Python script files...
copy ..\extract.py extract
copy ..\import.py import
copy ..\utils.py extract
copy ..\utils.py import

echo Entering extract folder...
pushd extract

echo Compiling to .exe...
\Python27\python.exe setup.py py2exe

echo Copying .exe to dist...
copy dist\extract.exe ..\dist

echo Exiting extract folder...
popd

echo Entering import folder...
pushd import

echo Compiling to .exe...
\Python27\python.exe setup.py py2exe

echo Copying entire contents of import\dist to dist folder...
xcopy dist\* ..\dist

echo Exiting import folder...
popd

echo Updating README.md and license.txt...
copy ..\README.md dist
copy ..\license.txt dist

echo Making temp folder...
xcopy /I dist vvvvvv-scripting-toolkit-win32

echo packaging into zip file...
7z\7za.exe a -tzip vvvvvv-scripting-toolkit-win32.zip vvvvvv-scripting-toolkit-win32

echo Cleaning up...
rd /s vvvvvv-scripting-toolkit-win32

echo Done!