import os

Path = os.getcwd()


all_dirs = []
for (path, dirs, files) in os.walk(Path):
	all_dirs.extend(dirs)
	print files
	print dirs
	print "----"

files_dict = dict()

for i in range(0,len(all_dirs)):
	files_dict[all_dirs[i]] = 'a'

#new_path = os.path.join(Path, all_dirs[2])

#print new_path
#print os.listdir(new_path)
print files_dict	
