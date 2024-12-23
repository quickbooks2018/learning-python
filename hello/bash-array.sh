# Defining an array
my_array=(10 20 30 40 50)

######################
# Accessing an element
######################
#echo ${my_array[1]}  # Outputs: 20 because array index starts from 0

######################
# Adding a new element
######################
#my_array[5]=60
#echo ${my_array[5]}  # Outputs: 60
#echo ${my_array[@]}  # Outputs: 10 20 30 40 50 60

########################
# Loop through the array
########################
for element in "${my_array[@]}"; do
  echo $element
done
