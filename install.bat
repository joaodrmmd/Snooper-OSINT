@echo off
REM SNOOPER - Installation Script for Windows
REM Makes 'snooper' available as a global command

setlocal enabledelayedexpansion

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║           SNOOPER v3.0 - Installation Script                   ║
echo ║              Windows Installation Wizard                       ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Get script directory
set "SCRIPT_DIR=%~dp0"

REM Create batch wrapper in Windows directory
set "INSTALL_DIR=%USERPROFILE%\AppData\Local\Programs\Snooper"
set "WRAPPER=%INSTALL_DIR%\snooper.bat"

echo [+] Creating installation directory...
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

REM Copy main script
echo [+] Copying snooper.py...
copy /Y "%SCRIPT_DIR%snooper.py" "%INSTALL_DIR%\snooper.py" >nul

REM Create batch wrapper
echo [+] Creating command wrapper...
(
echo @echo off
echo python "%INSTALL_DIR%\snooper.py" %%*
) > "%WRAPPER%"

REM Add to PATH if not already there
echo [+] Checking PATH...
echo %PATH% | findstr /C:"%INSTALL_DIR%" >nul
if errorlevel 1 (
    echo.
    echo [!] WARNING: %INSTALL_DIR% is not in your PATH
    echo [!] You have two options:
    echo.
    echo     Option 1 - Add to PATH manually:
    echo     1. Open System Properties ^> Advanced ^> Environment Variables
    echo     2. Edit 'Path' under User variables
    echo     3. Add: %INSTALL_DIR%
    echo     4. Click OK and restart your terminal
    echo.
    echo     Option 2 - Run directly:
    echo     %WRAPPER%
    echo.
) else (
    echo [+] Installation directory already in PATH
)

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║                   Installation Complete!                       ║
echo ║                                                                ║
echo ║  Run 'snooper' from any terminal to start the tool            ║
echo ║  (You may need to restart your terminal first)                ║
echo ║                                                                ║
echo ║  See you next time!                                           ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

pause
