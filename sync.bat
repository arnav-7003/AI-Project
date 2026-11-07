
@echo off
setlocal EnableDelayedExpansion
title GitHub Auto Sync

cd /d "%~dp0"

echo.
echo ==========================================
echo          GITHUB AUTO SYNC
echo ==========================================
echo.

:: Check Git repository
git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
    echo [X] Error: Not a Git repository!
    goto :END
)

:: Get repository name
for /f "delims=" %%i in ('git remote get-url origin 2^>nul') do set "REPO=%%i"

if not defined REPO (
    echo [X] Error: Git remote origin not found!
    goto :END
)

:: Extract repository name
for %%A in ("!REPO!") do set "REPO_NAME=%%~nxA"
set "REPO_NAME=!REPO_NAME:.git=!"

echo [i] Repository: !REPO_NAME!
echo.

:: Stage changes
echo [1/3] Adding changes...
git add -A
if errorlevel 1 (
    echo [X] Failed to add files!
    goto :END
)
echo [OK] Files added successfully!
echo.

:: Check changes
git diff --cached --quiet
if not errorlevel 1 (
    echo [OK] No new changes to upload.
    echo.
    echo ==========================================
    echo [OK] !REPO_NAME! - No changes pending
    echo ==========================================
    goto :END
)

:: Commit
set /p "MSG=Enter commit message: "
if not defined MSG set "MSG=Updated project files"

echo.
echo [2/3] Committing changes...
git commit -m "!MSG!"
if errorlevel 1 (
    echo [X] Commit failed!
    goto :END
)
echo [OK] Commit successful!
echo.

:: Push
echo [3/3] Pushing to GitHub...
git push origin HEAD
if errorlevel 1 (
    echo [X] Push failed! Check connection/authentication.
    goto :END
)

echo.
echo ==========================================
echo       [OK] SUCCESSFULLY COMPLETED
echo ==========================================
echo.
echo [OK] Repository: !REPO_NAME!
echo [OK] Changes uploaded to GitHub!
echo [OK] !REPO_NAME! changes done.
echo.

:END
echo.
echo ==========================================
echo Press any key to close this window...
echo ==========================================
pause >nul
