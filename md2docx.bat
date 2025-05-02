@echo off

:: Get full path and filename without extension
set "filepath=%~1"
set "filename=%~n1"
set "output=%~dp1%filename%.docx"

:: Call pandoc to convert .md to .docx
pandoc -s "%filepath%" -o "%output%"

:: Notify user
echo Conversion complete: %output%
pause
