import re

# Regular Expression

# \s white-space

# findall - If no matches are found, an empty list is returned.
print(re.findall("ai", "The rain in Spain")) # ['ai', 'ai']

# search - If no matches are found, the value None is returned.
print(re.search("\s", "The rain in Spain").start())
# The first white-space character (\s) is located in position - 3

# Match Object
print(re.search("\s", "The rain in Spain")) # <re.Match object; span=(3, 4), match=' '>
"""
.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""

# any words that starts with an upper case "S":
print(re.search(r"\bS\w+", "The rain in Spain").span()) # (12, 17)
print(re.search(r"\bS\w+", "The rain in Spain").string) # The rain in Spain
print(re.search(r"\bS\w+", "The rain in Spain").group()) # Spain

# split
print(re.split("\s", "The rain in Spain")) # ['The', 'rain', 'in', 'Spain']
# maxsplit parameter - number of occurrences
print(re.split("\s", "The rain in Spain", 2)) # ['The', 'rain', 'in Spain']

# sub
print(re.sub("\s", "9", "The rain in Spain")) # The9rain9in9Spain
# count parameter
print(re.sub("\s", "9", "The rain in Spain", 1)) # The9rain in Spain

"""
[] A set of characters "[a-m]"
\ Signals a special sequence "\d"
. Any character (except newline) "he..o" "hello planet"
^ Starts with "^hello"
$ Ends with "planet$"
* Zero or more occurrences "he.*o" starts with "he", followed by 0 or more (any) characters, and an "o" "hello"
+ One or more occurrences "he.+o" starts with "he", followed by 1 or more (any) characters, and an "o" "hello"
? Zero or one occurrences "he.?o" that starts with "he", followed by 0 or 1 (any) character, and an "o" []
{} Exactly the specified number of occurrences	"he.{2}o" followed excactly 2 (any) characters "hello"
| Either or	"falls|stays"
() Capture and group

\A	at the beginning of the string	"\AThe"
\b	at the beginning or at the end of a word r"\bain" r"ain\b"
\B	present, but NOT at the beginning (or at the end) of a word r"\Bain" r"ain\B"

\d	contains digits (numbers from 0-9) "\d"
\D	DOES NOT contain digits	"\D"

\s	contains a white space character "\s"
\S	DOES NOT contain a white space character "\S"

\w	contains any word characters (characters from a to Z digits from 0-9, and the underscore _ character) "\w"
\W	DOES NOT contain any word characters "\W"

\Z at the end of the string	"Spain\Z"

[arn] where one of the specified characters (a, r, or n) is present
[^arn] for any character EXCEPT a, r, and n

[a-n] for any lower case character, alphabetically between a and n

[0123] where any of the specified digits (0, 1, 2, or 3) are present
[0-9] for any digit between 0 and 9
[0-5][0-9] for any two-digit numbers from 00 and 59

[a-zA-Z] for any character alphabetically between a and z, lower case OR upper case

[+]	In sets, +, *, ., |, (), $, {} has no special meaning, so [+] means: for any + character in the string
"""