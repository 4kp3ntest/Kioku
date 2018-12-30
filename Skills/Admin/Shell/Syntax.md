# IF
if [[ expr ]]; then
    do stuff
elif [[ expr ]]; then
    do more stuff
else
    ...
fi

# LOOP
for y in {1..99..2}; do
    echo $y
done

# FUNCTION
bash_function() {
    echo Argumente werden nummeriert addressiert: $1 ist arg 1
    cat $2 # ist arg 2
}
bash_function "hallo" file.txt

# Array
arr[0]="2 million"
arr[1]="1 million"
arr[2]="3 million"
array=( getsu ka sui moku kin do duno )
### Loop through elements
for X in "${array[@]}"; do
    echo $X
done


# EOF multiline output -------------------
cat << EOF
usage: up [--level <n>| -n <levels>][--help][--version]

Report bugs to: 
up home page:
EOF
#t -------------------t -------------------

# TODO
while IFS='' read -r line; do
    tasks+=("$line")
done < "$file"

# random Random--------------------------
rand=$[$RANDOM%3]
echo ${arr[$rand]}
#----------------------------------------

# Length of string 
string = 'hallo welt'
echo ${#string} # no '$' !

