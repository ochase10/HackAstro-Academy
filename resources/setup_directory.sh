#!/bin/bash

# Create the base directory
mkdir -p bash_practice/research

# Instructions for students
cat << EOF > bash_practice/instructions.txt
Welcome to Bash Practice!

Here are your tasks:

1. Use 'mkdir' to create the following subdirectories:
   - project1
   - project2
   - project3

2. Once you have created these directories, run the next populate_directories.sh script.
EOF

cp populate_directories.sh bash_practice

echo "Base setup complete! Students can follow the instructions in bash_practice/instructions.txt."
