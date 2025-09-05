#!/bin/bash
# basic_terminal_demo.sh
# A script to demonstrate basic Bash/Unix commands.

echo "=== Basic Bash / Terminal Commands Demo ==="

# 1. Navigation
echo -e "\n-- Navigation --"
pwd                                # Print working directory
mkdir demo_dir                     # Make a new directory
cd demo_dir                        # Change into it
echo "Now in: $(pwd)"
cd ..                              # Move up one directory
echo "Back to: $(pwd)"

# 2. Listing files
echo -e "\n-- Listing Files --"
ls -l                              # Long listing
ls -a                              # Show hidden files

# 3. Creating and viewing files
echo -e "\n-- File Creation & Viewing --"
cd demo_dir
echo "Hello, world!" > file1.txt   # Create file with text
echo "Another line" >> file1.txt   # Append text
cat file1.txt                      # Display contents
head -n 1 file1.txt                # First line
tail -n 1 file1.txt                # Last line

# 4. Copy, move, rename
echo -e "\n-- Copying & Moving --"
cp file1.txt copy_of_file1.txt     # Copy file
mv copy_of_file1.txt renamed.txt   # Rename file
ls

# 5. Removing files/directories
echo -e "\n-- Removing --"
mkdir temp_dir
rm renamed.txt                     # Remove a file
rmdir temp_dir                     # Remove empty directory

# 6. Permissions
echo -e "\n-- Permissions --"
touch script.sh
chmod +x script.sh                 # Add execute permission
ls -l script.sh

# 7. Searching
echo -e "\n-- Searching --"
grep "Hello" file1.txt             # Search inside file
echo -e "one\ntwo\nthree" > numbers.txt
grep "t" numbers.txt               # Lines containing 't'

# 8. Counting
echo -e "\n-- Counting --"
wc -l numbers.txt                  # Count lines
wc -w numbers.txt                  # Count words

# 9. Environment & processes
echo -e "\n-- Environment & Processes --"
echo "User: $USER"
echo "Home directory: $HOME"
echo "Current shell: $SHELL"
ps                                  # Show running processes

# 10. Clean up
cd ..
rm -r demo_dir

echo -e "\n=== Demo Complete ==="
