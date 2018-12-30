# SED
#### Get print line range of textfile
sed -n 12,22p file

# TR
#### switch parentheses
cat file | tr '()' '[]'


# SORT
#### sort input based on third column (column seperated by blanks or tab)
sort -k 3,3 file
#### same but with ',' as delimiter
sort -t ',' -k 3,3 file

# PASTE
#### not super useful - just changes tabs to ';'
cat file | paste -s ';'
#### now it gets useful - merge three lines like this: a,b,c\n
paste -s ',,\n'
