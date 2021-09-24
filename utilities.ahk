F8::
    Send, ^a
    Send, ^c
    Sleep, 150
    Run, pythonw utilities.pyw %Clipboard%
Return

+F7::
    Run, powershell Get-Process AutoHotkey | Stop-Process
Return

+F8::
    Send, ^c
    Sleep, 150
    Run, pythonw utilities.pyw %Clipboard%
Return
