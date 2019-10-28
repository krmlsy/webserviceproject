# Specification Heading

This is an executable specification file. This file follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.

To execute this specification, run
	gauge run specs


* Vowels in English language are "aeiou".

## Vowel counts in single word

tags: single word

* The word "gauge" has "3" vowels.


## Vowel counts in multiple word

This is the second scenario in this specification

Here's a step that takes a table

* Almost all words have vowels
     |Word  |Vowel Count|
     |------|-----------|
     |Gauge |3          |
     |Mingle|2          |
     |Snap  |1          |
     |GoCD  |1          |
     |Rhythm|0          |

## JsonPlaceHolder testi hpt-1
tags: servis test hpt-1
* JsonPlaceHolder servisi "1" ile çağırılır

## JsonPlaceHolder testi hpt-2
tags: servis test hpt-2
* JsonPlaceHolder servisi "2" ile çağırılır

## JsonPlaceHolder testi hpt-3
tags: servis test hpt-3
* JsonPlaceHolder servisi "3" ile çağırılır

## JsonPlaceHolder testi hpt-4
tags: servis test hpt-4
* JsonPlaceHolder servisi "4" ile çağırılır