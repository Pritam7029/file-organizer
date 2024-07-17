# Python program to automatically organize
# Downloads folder in Python

# Import the libraries
from os import listdir
from os.path import isfile, join
import os
import shutil

# Obtain the path to be organized
file_path = 'D:\\test'

# Obtain all the files from the path in list
files = [f for f in listdir(file_path) if isfile(join(file_path, f))]

# Create the blank list and dictionary
file_list = []
filetype_dict = {}

# Create a loop
for file in files:

	# Split the name of file from dot
	filetype = file.split('.')[-1]

	# Check if the file type exists in the list
	if filetype not in file_list:

		# Add the file type in list if not already there
		file_list.append(filetype)

		# Give naming to the newly created folders
		new_folder_name = file_path+'/' + filetype + '_folder'

		# Add the new folder name in dictionary with the key value pairs
		filetype_dict[str(filetype)] = str(new_folder_name)

		# Check if the folder exists or not
		if os.path.isdir(new_folder_name) == True:

			# Come out of the loop if folder exists
			continue
		else:

			# Create the new folder if does not exist
			os.mkdir(new_folder_name)

# Declare a variable with value 1
i = 1

# Create the loop for all the files
for file in files:

	# Get the source path of each file
	src_path = file_path+'/'+file

	# Split the name of file by dot
	filetype = file.split('.')[-1]

	# Check if the file type exists in the dictionary
	if filetype in filetype_dict.keys():

		# Add the file type in dictionary if not already there
		dest_path = filetype_dict[str(filetype)]

		# Move the file from source path to destination path
		#shutil.move(src_path, dest_path)
		# if not os.path.exists(dest_path):
		# 	shutil.move(src_path, dest_path)
		# else:
		# 	print("Destination already exists. Skipping move operation.")

		# Extracting the filename from the source path
		file_name = os.path.basename(src_path)

# Constructing the destination path
		dest_path = os.path.join(dest_path, file_name)

		if not os.path.exists(dest_path):
			shutil.move(src_path, dest_path)
			print("File moved successfully to destination folder.")
		else:
			print("File already exists in destination folder. Skipping move operation.")
	#src_path = "source_file_path"
	#dest_path = "destination_file_path"

	
	# Print from where to where a file is being moved
	print(i, '. ', src_path + '>>>' + dest_path)

	# Increment the value of variable by 1
	i = i+1
