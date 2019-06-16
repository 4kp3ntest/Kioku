# Basic Syntax
re.search(r'regex', string, re.[flag])
#### returns match object
re.findall(r'findall', 'for the win')


# Special character
.       # any char except \n -> see re.DOTALL
^       # start of string
$       # end of string
*       # 0 or more repetitions
+       # 1 or more repetitions
{m}     # m copies of previous regex
{m,n}   # between m and n copies
[]      # set of characters


# Defined sets
\d      # [0-9]
\D      # [^0-9]    # char in upper inverses selection
\s      # [ \t\n\r\f\v] 
\w      # [a-zA-Z0-9_] (with ASCII flag)


(AND|and|And)

# Groups !!
### non capturing group
(?:)
### Positive & negative lookahead
a(?=b) - a(?!b)

second_appearance = re.match(r'[s][o](me)str', data).group(0) # matches 'me'





Examples
========

#### Regex für directory in home folder
re.match(r'd[a-zA-z0-9: .\-]{1,}[0-9]{2}:[0-9]{2} [A-Za-z]', i)

#### Zahl mit anschließende beliebiger Anzahl an lowercase letter (20 >= Anzahl >= 1)
re.match('r[1-9][a-z]{1-20}', buff)

