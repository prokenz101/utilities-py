# Utilities Help Center

Aha, so you have stumbled upon the utilities help center. If you don't know how to use a certain utility, maybe one of these links should help you out.

And if you were unaware, utilities is also dependent on 4 modules.

They are: [pyperclip](https://pypi.org/project/pyperclip/), [pyautogui](https://pypi.org/project/PyAutoGUI/), [win10toast](https://pypi.org/project/win10toast/) and [numpy](https://pypi.org/project/numpy/)

## Use:
Type your command and press F8.

**Alternatively**, you can use Shift + F8 if you don't want utilities to press Ctrl + A.

The video might be able to explain a bit better:

<img src="media\shiftF8showcase.gif"/>

In the first one, we see that pressing F8 selects the entire thing, making it basically useless. But in the second one, we select the command for utilities to run and then press shift + F8.

<br />

## Current Utilities:
| Utility                              | Summary |
----------------------------------|-----|
| [Google Search](#google-search) | Searches google. |
| [Youtube Search](#youtube-search) | Searches youtube. |
| [Google Images Search](#google-images-search) | Searches google images. |
| [Translate](#translate) | Translates text via google translate. |
| [Sarcasm](#sarcasm) | Randomly switches case, lIkE ThIs |
| [Spoilerspam](#spoilerspam) | Turns each induvidual letter into a spoiler. (For Discord) |
| [Copypaste](#copypaste) | Copies annoying-to-get characters to the clipboard. |
| [Emojify](#emojify) | Turns each letter into an emoji (For Discord) |
| [Spam](#spam) | Types text repeatedly. |
| [Autoclick](#autoclick) | An autoclicker. |
| [TapeMouse](#tapemouse) | Holds down a specific mouse button. |
| [Reverse](#reverse) | Reverses text, like this -> siht ekil |
| [Bubbletext](#bubbletext) | Turns text into bubbletext -> ⓛⓘⓚⓔ ⓣⓗⓘⓢ |
| [DoubleStruck](#doublestruck) | Converts letters into doublestruck -> 𝕙𝕖𝕝𝕝𝕠 |
| [Cursive](#cursive) | Converts letters into cursive -> 𝓱𝓮𝓵𝓵𝓸 |
| [Flip](#flip) | Flips text. hello -> ollǝɥ |
| [Exponent](#exponent) | Turns numbers and letters into exponents. |
| [Remind](#remind) | A basic reminder. |
| [Title](#title) | Turns Each First Letter Into Capital Letter |
| [ArrowMouse](#arrowmouse) | Lets you move mouse pointer using arrow keys. |
| [Format](#format) | Formats a sentence with other utilities. |
| [Cube Root](#cube-root) | Finds cube root of a number. |
| [HCF](#hcf) | Finds HCF of numbers. |
| [LCM](#lcm) | Finds LCM of numbers. |
| [Fraction](#fraction) | Generates a fraction. 1/2 -> ¹⁄₂ |
| [Randnum](#randnum) | Generates a random number from two start and end points. |

<br />

# How to use all of the utilities:

## Google Search
A simple utility which searches google. Prefix is `-`.

Example: `-hello world` opens ["hello world"](https://www.google.com/search?q=hello+world) in google.

There are no aliases for this utility.

<br />

## Youtube Search
A utility which searches youtube, similar to google search. Prefix is `youtube`.

Example: `youtube drinking amoung us potion at 3 am` searches [that](https://www.youtube.com/watch?v=dQw4w9WgXcQ) in youtube.


Aliases: `yt`

<br />

## Google Images Search
A utility which searches google images. Prefix is `images`.

Example: `images landscape` opens google images with landscape in the search bar.

There are no aliases for this utility.

<br />

## Translate
A utility which searches google translate. Prefix is `translate`.

Syntax: `translate <language> <query>`

Example: `translate french Hello.` which opens [that](https://translate.google.com/?sl=en&tl=fr&text=Hello.&op=translate) in google translate.

List of languages:
```
"tofrench" = french (english -> french)
"f" = french 
"french" = french
"toenglish" = english (uses detect language)
"e" = english
"english" = english
"toarabic" = arabic (english -> arabic)
"a" = arabic
"arabic" = arabic
```

There are no aliases for this utility.

<br />

## Sarcasm
Utility which alternates your text from uppercase to lowercase.

Example: `sarcasm hello world!` returns "hElLo wOrLd!"

There are no aliases for this utility.

<br />

## Spoilerspam
Utility which adds || before and after a letter to turn it into a spoiler turning each induvidual letter into its own spoiler.

This is mostly used in discord to "troll" or annoy your friends.

Example: `spoilerspam hello world` returns ||h||||e||||l||||l||||o|||| ||||w||||o||||r||||l||||d||

Or this image:

<img src="media\spoilerspamexample.png"/>

In this image, we can see that each induvidual letter is its own spoiler.

There are no aliases for this utility.

<br />

## Copypaste
A utility used to set your clipboard to characters that are more annoying to get.

Example: `cp divide` (the divison symbol) copies ÷ to your clipboard.

Copypaste is most useful for getting french letters without a french keyboard.

List of all strings in copypaste: (I'm too lazy to type it all out so you can just have the dictionary.)
```

"aigu e": "é", "aigu E": "É", "grave a": "à",
"grave e": "è", "grave u": "ù", "grave A": "À",
"grave E": "È", "grave U": "Ù", "chapeau a": "â",
"chapeau e": "ê", "chapeau i": "î", "chapeau o": "ô",
"chapeau u": "û", "chapeau A": "Â", "chapeau E": "Ê",
"chapeau I": "Î", "chapeau O": "Ô", "chapeau U": "Û",
"trema e": "ë", "trema i": "ï", "trema u": "ü", "bullet": "•",
"trema E": "Ë", "trema I": "Ï", "trema U": "Ü",
"cedille c": "ç", "cedille C": "Ç", "3164": "ㅤ",
"hangul filler": "ㅤ", "divison": "÷", "divide": "÷", "multi": "×",
"!=": "≠", "congruence": "≅", "greater than or equal to": "≥",
">=": "≥", "lesser than or equal to": "≤", "<=": "≤",
"shrug": R"¯\_(ツ)_/¯", "trademark": "™️", "copyright": "©️",
"csprint": """using System;

namespace Code
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("");
        }
    }
}"""
```
Aliases: `cp`

<br />

## Emojify
A utility which converts all your text into emojis on discord.

Example: `emojify hello world!` returns 
```
:regional_indicator_h: :regional_indicator_e: :regional_indicator_l: :regional_indicator_l: :regional_indicator_o: :black_large_square: :regional_indicator_w: :regional_indicator_o: :regional_indicator_r: :regional_indicator_l: :regional_indicator_d: :exclamation:
```

Or this image:

<img src="media\emojifyexample.png"/>

Copypasting that into discord will show all the letters as their own emoji.

There are no aliases for this utility.

<br />

## Spam
A more interesting utility.

This utility types whatever you ask it to and presses enter a set amount of times at a set interval. The syntax is a bit complex but easy if you understand it.

If you want to stop the spammer, then put your mouse in any corner of the screen while it starts to type, it should give a notification showing that it has stopped spamming.

Syntax: `spam {number} {text} {--interval=int in seconds}

Example: `spam 10 hello world! --interval=3` will type "hello world!" 10 times every 3 seconds.

Note: If you want the spammer to spam infinitely, then use `infinite` as a number, example: `spam infinite hello world --interval=3` which spams "hello world" every 3 seconds forever.

Another Note: If you do not want an interval, then you can leave that blank. Example: `spam infinite hello world` which spams "hello world" at max speed forever. However, this can crash certain apps due to how fast it types, so tread carefully.

There are no aliases for this utility.

<br />

## Autoclick
Another interesting utility.

This utility uses the mouse and clicks at a set interval, for a set amount of times. The syntax is a bit different to spam's syntax.

If you want to stop the autoclicker, press F7.

Syntax: `autoclick {interval in milliseconds} {mouse button: left or right} {count}`

Example: `autoclick 2500 left 50` left clicks every 2.5 seconds 50 times.

Note: If you do not want an interval, then leave that blank, and if you do not have a set count and want to click forever, then leave that blank as well. For example, if you want the fastest possible autoclicker clicking forever, you can type `autoclick left`.

There are no aliases for this utility.

<br />

## TapeMouse
A simple utility which holds down the mouse button that you specify.

To stop the mouse from being taped down, just click on the mouse button you specified. If you taped the right mouse button, then just right click to stop it.

Syntax: `tapemouse {mousebutton: left or right}`

Example: `tapemouse left` holds down the left mouse button.

There are no aliases for this utility.

<br />

## Reverse
Another simple utility which reverses text.

Example: `reverse hello world` returns "dlrow olleh".

There are no aliases for this utility.

<br />

## Bubbletext
Another simple utility which turns all letters and numbers into bubbles.

Example: `bubbletext hello world 12345` returns ⓗⓔⓛⓛⓞ ⓦⓞⓡⓛⓓ ①②③④⑤.

Aliases: `bubble`

<br />

## Doublestruck
A utility similar to bubbletext. This utility turns all letters into their doublestruck form.

Example: `doublestruck hello world!` returns 𝕙𝕖𝕝𝕝𝕠 𝕨𝕠𝕣𝕝𝕕!

Aliases: `dbs`

<br />

## Cursive
Another utility similar to bubbletext and doublestruck. This one turns all letters into cursive letters.

Example: `cursive hello world!` returns 𝓱𝓮𝓵𝓵𝓸 𝔀𝓸𝓻𝓵𝓭!

There are no aliases for this utility.

<br />

## Flip
~~Does a flip~~

This utility flips letters. There's not much more to it than that.

Example: `flip do a flip!` returns !dᴉlɟ ɐ op. (It also reverses the text.)

There are no aliases for this utility.

<br />

## Exponent
A utility that converts text into its superscript form.

Mostly used for exponents in math, like x². It is the same thing as x^2, but looks fancier.

Syntax: `exponent {text or numbers}`

Example: `exponent hello world 12345` returns ʰᵉˡˡᵒ ʷᵒʳˡᵈ ¹²³⁴⁵.

Aliases: `ep`

<br />

## Remind
A utility that sends a reminder in the form of a notification.

Units:
```
"s" = second
"m" = minute
"h" = hour
```

Syntax: `remind {time} {text}`

Example: `remind 15s hello world` gives me a notification in 15 seconds.

Note: If you do not specify text, the utility will still work; instead telling you that the time is up.

There are no aliases for this utility.

<br />

## Title
A very simple utility that turns the first letter of text to uppercase.

Example: `titlecase hello how are you doing` returns "Hello How Are You Doing"

There are no aliases for this utility.

<br />

## Arrowmouse
A utility that starts an autohotkey, allowing you to move your mouse using the arrow keys on your keyboard.

Syntax: `arrowmouse {enable or disable}`

There are no aliases for this utility.

<br />

## Format
A utility that formats text inside curly braces to utilities.

This one is a bit difficult to explain so I'll just use an example.

Example: `format {cursive hello} {doublestruck world}`

We can see in the example that two seperate commands are given in the same sentence, so utilities formats the sentence and turns it into "𝓱𝓮𝓵𝓵𝓸 𝕨𝕠𝕣𝕝𝕕".

Format only reads commands that are inside curly braces, if you put something inside curly braces that IS NOT a utilities command, then the program will error.

This is especially useful when typing out mathematical expressions with several exponents. Like `format x{ep 2} + y{ep 3} {cp divide} z{ep 4}` which returns x² + y³ ÷ z⁴.

This utility takes a bit longer to run that the others, due to it having to run several other functions and overall just do a lot of things.

There are no aliases for this utility.

<br />

## Cube Root
A utility which finds the cube root of a number, sends the answer as a notification and copies it to your clipboard.

This utility does make use of the `cbrt()` function in numpy.

Example: `cuberoot 729` returns 9.0

Aliases: `cbrt`

<br />

## HCF
A utility that finds the HCF of any amount of numbers.

**Note:** Numbers must be seperated with spaces, and no commas.

Example: `hcf 12 48 96` returns the HCF of those numbers, which is 12.

Aliases: `gcd`

<br />

## LCM
A utility that finds the LCM of any amount of numbers.

Similar to HCF, numbers must be seperated with spaces, and no commas.

Example: `lcm 12 128 256` returns the LCM of those numbers, which is 768.

There are no aliases for this utility.

<br />

## Fraction
A more complex utility which generates a fraction from a regular divison problem.

Example: `fraction pog1/2` returns ᵖᵒᵍ¹⁄₂

This command does work with letters; however, some letters are not there in subscript form, so you will be greeted by an error if you use them. For example: doing `fraction 1/b` will give you an error, because the letter b is not available in subscript form.

List of letters that are not available in subscript:
```
b, c, d, f, g, w, y and z
```

Aliases: `fc`

<br />

## Randnum
A utility that generates a random number, similar to the [random number generator](https://www.google.com/search?q=random+number+generator) that you find on google.

Syntax: `randnum <first number>, <second number>`

Example: `randnum 1, 5` generates a random number from 1 to 5.

**Note:** A comma is necessary for seperating the two numbers.

This utility makes use of the `randint()` function in `random`.

Aliases: `randint`

<br />

## Got any Doubts?
Feel free to contact me on discord.

```
prokenz101#9729
```
And also if there were any typos, please DM me on discord.