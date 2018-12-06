# Change default shell
#### find path
which bash | zsh
#### change
chsh -s /usr/bin/zsh

# Oh-my-ZSH
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
cp /usr/share/oh-my-zsh/zshrc ~/.zshrc


=========================================================================================
                                    Syntax Section
=========================================================================================

arr[0]="2 million"
arr[1]="1 million"
arr[2]="3 million"

# random Random--------------------------
rand=$[$RANDOM%3]
echo ${arr[$rand]}
#----------------------------------------

# Length of string 
string = 'hallo welt'
echo ${#string} # no '$' !

# Function
bash_function() {
    echo Argumente werden nummeriert addressiert: $1 ist arg 1
    cat $2 # ist arg 2
}
bash_function "hallo" file.txt

# IF
if [[ expr ]]; then
    do stuff
elif [[ expr ]]; then
    do more stuff
else
    ...
fi

# EOF multiline output -------------------
cat << EOF
usage: up [--level <n>| -n <levels>][--help][--version]

Report bugs to: 
up home page:
EOF
#t -------------------t -------------------

# Equivalent to range() in python
for y in {1..99..2}
do
    echo $y
done

# Loop through element of array
array=( getsu ka sui moku kin do duno )
for X in "${array[@]}"
do
    echo $X
done

# TODO
while IFS='' read -r line; do
    tasks+=("$line")
done < "$file"

