import unittest
import os

from checker.project_checker import ProjectChecker


class CheckFileTestSuite(unittest.TestCase):

    def test_should_check_if_files_in_projects_directories_are_the_same(self):
        # GIVEN
        current_file_path = os.getcwd()
        test_resource_path = os.path.join(current_file_path, "resources")
        old_project_path = os.path.join(test_resource_path, "old_project")
        new_project_path = os.path.join(test_resource_path, "new_project")
        checker = ProjectChecker()
        # WHEN
        result = checker.compare_file_names_in_projects(old_project_path, new_project_path,)
        # THEN
        self.assertTrue(result, msg="Files in directories are different.")


    def test_should_check_if_packages_are_the_same(self):
        # GIVEN
        current_file_path = os.getcwd()
        test_resource_path = os.path.join(current_file_path, "resources")
        old_project_path = os.path.join(test_resource_path, "old_project")
        new_project_path = os.path.join(test_resource_path, "new_project")
        checker = ProjectChecker()
        # WHEN
        result = checker.compare_packages_in_projects(old_project_path, new_project_path )
        # THEN
        self.assertTrue(result, msg="Packages are different")


    def test_should_check_if_contents_files_are_the_same(self):
        # GIVEN
        current_file_path = os.getcwd()
        test_resource_path = os.path.join(current_file_path, "resources")
        old_project_path = os.path.join(test_resource_path, "old_project")
        new_project_path = os.path.join(test_resource_path, "new_project")
        checker = ProjectChecker()
        # WHEN
        result = checker.compare_files_contents(old_project_path, new_project_path)
        # THEN
        self.assertTrue(result, msg="Contents of files are different.")



if __name__ == '__main__':
    unittest.main()
