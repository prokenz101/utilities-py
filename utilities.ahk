F8::
    Send, ^a
    Send, ^c
    Sleep, 150
    Run, pythonw utilities.pyw %Clipboard%
    Send, {Esc}
Return

+F8::
    Send, ^c
    Sleep, 150
    Run, pythonw utilities.pyw %Clipboard%
Return
