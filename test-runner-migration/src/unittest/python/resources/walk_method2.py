import os

current_path = os.getcwd()

new_project_path = os.path.join(current_path, "new_project", "src", "main", "python")


new_project_all_dirs = []
for (path, dirs, files) in os.walk(new_project_path):
	new_project_all_dirs.extend(dirs)


dict_new_project_files = dict()

for i in range(0, len(new_project_all_dirs)):
	new_path = os.path.join(new_project_path, new_project_all_dirs[i])
	dict_new_project_files[new_project_all_dirs[i]] = os.listdir(new_path)





old_project_path = os.path.join(current_path, "old_project")


old_project_all_dirs = []
for (path, dirs, files) in os.walk(old_project_path):
	old_project_all_dirs.extend(dirs)

dict_old_project_files = dict()
for i in range(0, len(new_project_all_dirs)):
	new_path = os.path.join(old_project_path, new_project_all_dirs[i])
	dict_old_project_files[old_project_all_dirs[i]] = os.listdir(new_path)


compare_dict = (dict_new_project_files == dict_old_project_files)

pass



	
