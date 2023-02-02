Set wshshell = wscript.CreateObject("wscript.shell")
do
wshshell.run "Notepad"
wscript.sleep 500
wshshell.AppActivate "Notepad"
WshShell.SendKeys "H"
WScript.Sleep 100
WshShell.SendKeys "E"
WScript.Sleep 100
WshShell.SendKeys "L"
WScript.Sleep 100
WshShell.SendKeys "L"
WScript.Sleep 100
WshShell.SendKeys "O"
loop
