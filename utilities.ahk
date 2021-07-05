F8::
Send, ^a
Send, ^c
Sleep, 150
Run pythonw powertoys-utilities.pyw %Clipboard%
Return

$"::
SendRaw, ""
Send, {Left}
Return

$'::
SendRaw, ''
Send, {Left}
Return

$(::
SendRaw, ()
Send, {Left}
Return

${::
SendRaw, {}
Send, {Left}
Return

$[::
SendRaw, []
Send, {Left}
Return

F9::
Reload
Return