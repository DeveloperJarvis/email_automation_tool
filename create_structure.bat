@echo off

REM Root directory
@REM set ROOT=email_automation_tool
set ROOT=.

REM Create directories if they do not exist
if not exist "%ROOT%" mkdir "%ROOT%"
if not exist "%ROOT%\tests" mkdir "%ROOT%\tests"

REM Create files only if they do not exist
REM Python source files (with header)
call :create_py_file "%ROOT%\main.py"
call :create_py_file "%ROOT%\config.py"
call :create_py_file "%ROOT%\email_builder.py"
call :create_py_file "%ROOT%\mime_builder.py"
call :create_py_file "%ROOT%\sender.py"
call :create_py_file "%ROOT%\scheduler.py"
call :create_py_file "%ROOT%\queue.py"
call :create_py_file "%ROOT%\logger.py"

call :create_py_file "%ROOT%\tests\test_email_model.py"
call :create_py_file "%ROOT%\tests\test_mime_builder.py"
call :create_py_file "%ROOT%\tests\test_sender.py"
call :create_py_file "%ROOT%\tests\test_scheduler.py"

REM Non-Python files (empty)
call :create_file "%ROOT%\.gitignore"
call :create_file "%ROOT%\README.md"
call :create_file "%ROOT%\LICENSE"

echo Folder structure created (existing files and folders were preserved).
@REM do not forget to add this goto :eof    
goto :eof 

REM -------------------------------------------
REM Create empty file if it does not exist
REM -------------------------------------------
:create_file
if not exist "%~1" (
    type nul > "%~1" || echo path: %~1
)

exit /b

REM -------------------------------------------
REM Create python file with GPL header
REM -------------------------------------------
:create_py_file
if exist "%~1" exit /b

set FILEPATH=%~1
set FILENAME=%~n1

(
echo # --------------------------------------------------
echo # -*- Python -*- Compatibility Header
echo #
echo # Copyright ^(C^) 2023 Developer Jarvis ^(Pen Name^)
echo #
echo # This file is part of the email_automation_tool Library. This library is free
echo # software; you can redistribute it and/or modify it under the
echo # terms of the GNU General Public License as published by the
echo # Free Software Foundation; either version 3, or ^(at your option^)
echo # any later version.
echo #
echo # This program is distributed in the hope that it will be useful,
echo # but WITHOUT ANY WARRANTY; without even the implied warranty of
echo # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
echo # GNU General Public License for more details.
echo #
echo # You should have received a copy of the GNU General Public License
echo # along with this program. If not, see ^<https://www.gnu.org/licenses/^>.
echo #
echo # SPDX-License-Identifier: GPL-3.0-or-later
echo #
echo # email_automation_tool - Send bulk emails or scheduled emails
echo #                   Skills: smtplib, MIME types, security
echo #
echo # Author: Developer Jarvis ^(Pen Name^)
echo # Contact: https://github.com/DeveloperJarvis
echo #
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # %FILENAME%% MODULE
echo # --------------------------------------------------
echo.
echo # --------------------------------------------------
echo # imports
echo # --------------------------------------------------
echo.
) > "%FILEPATH%" || echo python_path: %FILEPATH%

exit /b
