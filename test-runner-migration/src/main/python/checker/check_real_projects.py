from project_checker import  ProjectChecker

check = ProjectChecker()

old_project_path = "/home/gliwny/Desktop/test_runner_old"
new_project_path = "/home/gliwny/Desktop/test-runner"

result_compare_file_names = check.compare_file_names_in_projects(old_project_path, new_project_path)

result_compare_names_package = check.compare_package_names_in_project(old_project_path, new_project_path)


