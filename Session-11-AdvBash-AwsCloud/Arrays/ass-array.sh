# Associative Array : stores values in Key and Value pair
#!/bin/bash
declare -A capitals # declaring empty array
capitals[India]="New Delhi" # assining values
capitals[France]="Paris"
capitals[Japan]="Tokyo"

##Access
echo "Capital of Japan: ${capitals[Japan]}"
# Iteration accessing values
for capital in "${capitals[@]}";do  
    echo $capital
done

# access key and value both
# ! expands keys
for country in "${!capitals[@]}";do  
    echo "Capital of $country is ${capitals[$country]}"
done

## Declare and assign array together
declare -A myArray=([name]="sonam" [role]="Trainer" [city]="Mumbai")
echo "${myArray[name]}"