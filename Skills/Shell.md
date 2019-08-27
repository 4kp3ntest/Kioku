# Programms and Utilities
sed
tr
sort
paste
## images
fls


# Examples
## sed
#### Get print line range of textfile
sed -n 12,22p file

## tr
#### switch parentheses
cat file | tr '()' '[]'
#### squeeze repeated characters
cat Batteries.txt | tr -s '\t' > tmp.txt

## sort
#### sort input based on third column (column seperated by blanks or tab)
sort -k 3,3 file
#### same but with ',' as delimiter
sort -t ',' -k 3,3 file

## paste
#### not super useful - just changes tabs to ';'
cat file | paste -s ';'
#### now it gets useful - merge three lines like this: a,b,c\n
paste -s ',,\n'
