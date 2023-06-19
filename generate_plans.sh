
FOLDER=$1
DOMAIN="$FOLDER/domain.pddl"

# Function to extract the number from a filename
extract_number() {
  filename="$1"  # Get the filename from command-line argument
  number=$(echo "$filename" | sed -n 's/p\([0-9]\+\)\.pddl/\1/p')  # Extract the number using sed
  echo "$number"  # Print the extracted number
}

for PROBLEM_FILE in $FOLDER/p*.pddl; do
    number=$(extract_number $(basename $PROBLEM_FILE))
    echo "Problem number $number"
    planutils run lama-first $DOMAIN $PROBLEM_FILE > /dev/null
    if [ -e "sas_plan" ]; then
        python3 convert.py sas_plan > ${FOLDER}/p${number}.steps
        mv sas_plan ${FOLDER}/p${number}.sas
    else
        echo "No file generated."
    fi
done
