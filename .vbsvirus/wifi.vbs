Function GetOutput(command)
  Set Shell = Wscript.CreateObject("WScript.Shell")
  Set cmd = Shell.Exec("cmd /c  " & command)
  strOut = ""

  Do While Not cmd.StdOut.AtEndOfStream
    strOut = strOut & cmd.StdOut.ReadLine() & "\n"
  Loop
  GetOutput=strOut
End Function

Function saveIt(wifi, passwd)
  wifi = Replace(Replace(wifi, ">", "-"), "<", "-")
  Set objFSO=CreateObject("Scripting.FileSystemObject")
  Set objFile=objFSO.CreateTextFile(wifi & ".txt")
  objFile.Write(passwd)
  objFile.Close
End Function

strText=Split(GetOutput("netsh wlan show profile"), "\n")

i = 0

For Each x in strText
	If i > 8 And i < Ubound(strText)-1 Then
		Name = Split(x, ": ")(1)
		str=Split(GetOutput("netsh wlan show profile """ & Name & """ key=clear"), "\n")
    For Each options in str
      options=Replace(options, " ", "")
      If UBound(Split(options, ":")) >= 1 Then
        If Split(options, ":")(0) = "KeyContent" Then
          passwd = Split(options, ":")(1)
          saveIt Name, passwd
        End If
      End If
    Next
	End If
	i = i + 1
Next
