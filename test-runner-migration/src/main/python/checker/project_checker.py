import os
import filecmp


class ProjectChecker(object):
    def __init__(self):
        pass

    def compare_file_names_in_projects(self, old_project_path, new_project_path):

        old_project_files = self._project_files(old_project_path)

        new_project_files = self._project_files(new_project_path)

        result_of_compare = (sorted(new_project_files) == sorted(old_project_files))

        return result_of_compare

    def _project_files(self, project_path):

        project_files = []

        for (path, dirs, files) in os.walk(project_path):
            project_files.extend(files)

        return project_files

    def compare_packages_in_projects(self, old_project_path, new_project_path):

        new_project_path = os.path.join(new_project_path, "src", "main", "python")
        dict_new_project_files = dict()
        dict_new_project_files = self._dict_packages(new_project_path)

        old_project_path = old_project_path
        dict_old_project_files = dict()
        dict_old_project_files = self._dict_packages(old_project_path)

        compare_dict = (dict_new_project_files == dict_old_project_files)

        return compare_dict

    def _dict_packages(self, project_path):

        project_all_dirs = []
        for (path, dirs, files) in os.walk(project_path):
                project_all_dirs.extend(dirs)

        dict_project_files = dict()

        for i in range(0, len(project_all_dirs)):
            new_path = os.path.join(project_path,     project_all_dirs[i])
            dict_project_files[project_all_dirs[i]] = os.listdir(new_path)
            
        return dict_project_files

    def compare_files_contents(self, old_project_path, new_project_path):

        dict_old_project_files = dict()
        dict_old_project_files = self._dict_packages(old_project_path)
        old_project_path_files = []
        old_project_path_files = self._project_path_files(dict_old_project_files, old_project_path)

        new_project_path = os.path.join(new_project_path, "src", "main", "python")
        dict_new_project_files = dict()
        dict_new_project_files = self._dict_packages(new_project_path)
        new_project_path_files = []
        new_project_path_files = self._project_path_files(dict_new_project_files, new_project_path)

        compare_contents_file_result = []
        bad_files_path = []
        for i in range(0, len(new_project_path_files)):
            result = filecmp.cmp(old_project_path_files[i], new_project_path_files[i])
            compare_contents_file_result.append(result)
            if result == False:
                bad_files_path.append(old_project_path_files[i])
                bad_files_path.append(new_project_path_files[i])
            else:
                continue

        if False in compare_contents_file_result:
            return False
        else:
            return True


    def _project_path_files(self, project_dict, project_path):

        project_path_files = []

        for packgage, files in project_dict.iteritems():
            name_packages = packgage
            files_in_packages = files
            for j in range(0, len(files_in_packages)):
                project_path_files.append(os.path.join(project_path, name_packages, files_in_packages[j]))

        return project_path_files
