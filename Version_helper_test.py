from wiki_440_version_helper import Version_Helper as help

filepath = raw_input("Enter a file path: ")


print "Choose one of the following options: "
print "1. get file name from path"
print "2. get path without file name"
print "3. get highest version of file path"

answer = input()
if (answer== 1):
    print help.get_filename_from_path(filepath)
elif (answer == 2):
    print help.get_path_without_filename(filepath)
elif (answer == 3):
    print help.get_highest_version_of_file_path(filepath)
else:
    print "Thats not one of the options"

