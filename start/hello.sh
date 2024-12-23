#!/opt/homebrew/bin/bash

# string
#x='Hello World Islam'
#for i in $x; do echo $i; done


# Array or List in Bash
x=("Hello" "World" "Islam Pakistan")

for i in "${x[@]}"; do
    echo $i
done


