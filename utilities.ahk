F8::
Send, ^a
Send, ^c
Sleep, 150
Run, pythonw utilities.pyw %Clipboard%
Return

+F8::
Send, ^c
Sleep, 150
Run, pythonw utilities.pyw %Clipboard%
Return

#IfWinNotActive, ahk_exe Code.exe

$"::
SendRaw, ""
Send, {Left}
Return

$'::
If (A_PriorKey = "Space") {
    SendRaw, ''
    Send, {Left}
} Else {
    SendRaw, '
}
Return

$(::
If (A_PriorKey = ";") {
    SendRaw, (
}
Else {
    SendRaw, ()
    Send, {Left}
}
Return

${::
SendRaw, {}
Send, {Left}
Return

$[::
SendRaw, []
Send, {Left}
Return

^+K::
Send, {Home}
Sleep, 150
Send, {Shift down}
Send, {End down}
Send, {Shift up}
Send, {End up}
Send, {BackSpace 2}

F9::
Reload
Return