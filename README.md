# Roman Numerals

I always ignored making a decimal-to-Roman numeral converter because I thought it would be really complicated and lead to ugly code (since I assumed you needed some form of back tracing to handle the subtraction part), but it turns out it's actually really simple: just treat it as place values and concatenate them.

|     | Thousands | Hundreds | Tens | Units |
| :-: | :-------: | :------: | :--: | :---: |
|  1  |     M     |    C     |  X   |   I   |
|  2  |    MM     |    CC    |  XX  |  II   |
|  3  |    MMM    |   CCC    | XXX  |  III  |
|  4  |           |    CD    |  XL  |  IV   |
|  5  |           |    D     |  L   |   V   |
|  6  |           |    DC    |  LX  |  VI   |
|  7  |           |   DCC    | LXX  |  VII  |
|  8  |           |   DCCC   | LXXX | VIII  |
|  9  |           |    CM    |  XC  |  IX   |

_Table from [Wikipedia][wikipedia-roman-numerals]_

So if someone wanted to get the number 1386 (random number) for some reason, then we can extract those cells from the table like so,

|       | Thousands | Hundreds | Tens | Units |
| :---: | :-------: | :------: | :--: | :---: |
| digit |     1     |    8     |  8   |   6   |
| roman |     M     |   CCC    | LXXX |  VI   |

then concatenate them together to make MCCCLXXXVI.

For converting Roman numerals to decimal, we can use the following table info:

|         |     |     |     |     |     |     |      |
| :-----: | :-: | :-: | :-: | :-: | :-: | :-: | :--: |
|  roman  |  I  |  V  |  X  |  L  |  C  |  D  |  M   |
| decimal |  1  |  5  | 10  | 50  | 100 | 500 | 1000 |

For each character, if the next character's value is greater, we subtract the current character's value from the sum, otherwise, we add it.

This code does not check for the validity of a Roman numeral or if the input to `decimal_to_roman` is out of bounds (or invalid).

[wikipedia-roman-numerals]: https://en.wikipedia.org/wiki/Roman_numerals
