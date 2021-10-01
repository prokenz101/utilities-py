SetBatchLines -1
IncrementValue = 5
MouseDelay = 0

Left::
Right::
Up::
Down::

Loop, {
If (A_ThisHotkey = "Down")
	xVal := 0, yVal := IncrementValue
If (A_ThisHotkey = "Up")
	xVal := 0, yVal = -IncrementValue
If (A_ThisHotkey = "Left")
	xVal := -IncrementValue, yVal = 0
If (A_ThisHotkey = "Right")
	xVal := IncrementValue, yVal = 0
If GetKeyState(A_ThisHotKey, "P")
	MouseMove, %xVal%, %yVal%,%MouseDelay%,R
Else
	Break
}
Return

F5::
Click, Left
Return

F6::
Click, Right
Return

F13::ExitApp
