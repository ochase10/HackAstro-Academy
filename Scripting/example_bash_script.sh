#!/bin/bash
# basic_terminal_demo.sh
# A script to demonstrate basic Bash/Unix commands.

echo "=== Basic Bash / Terminal Commands Demo ==="

# 1. Navigation
echo -e "\n-- Navigation --"
                                # Print working directory
                     # Make a new directory named demo_dir
                        # Change into it
echo "Now in: $(pwd)"
cd ..                              # Move up one directory
echo "Back to: $(pwd)"


# 2. Creating and viewing files
echo "\n-- File Creation & Viewing --"
cd demo_dir
echo "Hello, world!" > file1.txt   # Create file with text
echo "Another line" >> file1.txt   # Append text
cat file1.txt                      # What does this line do? Write answer here: 
head -n 1 file1.txt                # What does this line do? Write answer here: 
tail -n 1 file1.txt                # What about this one? Answer:

# 3. Copy, move, rename
echo "\n-- Copying & Moving --"
cp file1.txt copy_of_file1.txt     # Copy file
mv copy_of_file1.txt renamed.txt   # Rename file
ls

# 4. Removing files/directories
echo "\n-- Removing --"
mkdir temp_dir
rm renamed.txt                     # Remove a file
rmdir temp_dir                     # Remove empty directory

# 5. Clean up
cd ..
rm -r demo_dir

echo "\n=== Demo Complete ==="
