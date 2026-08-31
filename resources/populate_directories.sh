#!/bin/bash

# Verify required directories exist
if [[ ! -d "research/project1" || ! -d "research/project2" || ! -d "research/project3" ]]; then
    echo "Error: Ensure project1, project2, and project3 directories exist under bash_practice/research before running this script."
    return 1
fi

# Populate project1
mkdir -p research/project1/{script,data}
echo "The README file for project1!" > research/project1/readme.txt
echo "You need to move me to project1/data." > research/project1/script/data.txt
echo "A file to concatenate!" > research/project1/data/file2.txt

cat << EOF > research/project1/script/script1.py
import numpy as np

def add(a, b):
    return a + b

print(add(5, 10))
EOF

# Populate project2
mkdir -p research/project2/{softwares,script,data}
cat << 'EOF' > research/project2/softwares/runme.sh
#!/bin/bash
# Script for students to fix paths and execute
echo "Fix the paths below to make this script work!"
cat ../../folder1/readme.txt
cat ../../project2/scripts/file2.txt
EOF
chmod +x research/project2/softwares/runme.sh
touch research/project2/script/editme.py

# Populate project3
mkdir -p research/project3/{data/raw,data/processed,script}
echo "Concatenate this text with research/project1/data/file2.txt" > research/project3/data/raw/file1.txt
echo -e "Line 1: Star\nLine 2: Galaxy\nLine 3: Black Hole" > research/project3/data/raw/astronomy.txt

# Add a script to verify student tasks
cat << 'EOF' > verify_tasks.sh
#!/bin/bash
echo "Verifying tasks..."
[ -f research/project1/data/data.txt ] && echo "Task 3 complete!"
[ -f research/project2/script/editme.py ] && echo "Task 4 complete!"
[ -x research/project2/softwares/runme.sh ] && echo "Task 5 complete!"
[ ! -f research/project1/data/file2.txt ] && echo "Task 6 complete!"
echo "All tasks verified if no errors above!"
EOF

# Make the verification script executable
chmod +x verify_tasks.sh

# Final instructions
cat << EOF > next_steps.txt

Here are your tasks:

1. Use 'ls' to explore the directory structure. Note the hierarchy of folders.
2. Use 'mv' to move project1/script/data.txt to project1/data.
3. Use 'cp' to copy the content of project1/data/file2.txt into project3/data/raw/.
4. Use 'vi' or 'nano' to edit project2/script/editme.py and copy the content of project1/script/script1.py into it.
5. Fix the file paths in project2/softwares/runme.sh and execute it after making it executable using 'chmod'.
6. Use 'rm' to delete research/project1/data/file2.txt after concatenating it with research/project3/data/raw/file1.txt.
7. Use 'grep' to search for the word "Galaxy" in project3/data/raw/astronomy.txt.
8. Use 'find' to locate all `.py` scripts in the directory structure.
9. Execute verify_tasks.sh to check your work.

EOF

echo "Projects populated! Follow the next steps in next_steps.txt."
