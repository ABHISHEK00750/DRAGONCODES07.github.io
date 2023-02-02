Dim Message, Speak
Message=InputBox("Put the text","Talkative")
Set Speak=CreateObject("sapi.spvoice")

Speak.Speak Message
