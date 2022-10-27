# Lazy way of searching a text in a file using another input file.

# Limitations:
# Not thoroughly tested

# Input:
# small_file: The file we use for search. Contains multiple lines bu can contain also just one line.
# big_file: The file we search into.

# Output:
# Text in big_file if they are in small_files
# and "not found" when they are not

import sys
from re import search

small_file = open(sys.argv[1],'r')
big_file = open(sys.argv[2],'r')#.readlines()

found = False

for line_sm in small_file:
	line_sm=line_sm.strip()
	## print("\n\n---\nCURRENT SUBSTRING: " + line_sm + "\n---\n")
	
	found = False
	big_file.seek(0)  # Reset to the beginning of the big_file

	for line_bg in big_file:
		line_bg=line_bg.strip()
		## print("CURRENT BGSTRING: " + line_bg + "\n")
		    
    #if line_sm in line_bg:  # --> does not work, as it matches if line_sm is a subset of line_bg
		
    # Uses esact match instead
    if search(r'\b' + line_sm + r'\b', line_bg):
			## print("SAME!!!   " + line_bg.strip() + "\n")
			print(line_bg)
			found = True
			break #if found, no need to continue searching the rest of big_file
	
	if not found:
		print(line_sm + "  (not found)")
