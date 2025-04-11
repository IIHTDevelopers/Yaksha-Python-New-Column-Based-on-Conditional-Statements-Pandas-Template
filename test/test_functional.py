import unittest
import pandas as pd
from mainclass import EmployeeAnalysis
from test.TestUtils import TestUtils
import os


class FunctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.analysis = EmployeeAnalysis("employee_data.csv")
        cls.test_obj = TestUtils()

    def test_csv_loading(self):
        """Test if the CSV file is loaded correctly."""
        try:
            if not self.analysis:
                self.test_obj.yakshaAssert("TestCSVLoading", False, "functional")
                print("TestCSVLoading = Failed")
                return
            obj = not self.analysis.df.empty
            self.test_obj.yakshaAssert("TestCSVLoading", obj, "functional")
            print("TestCSVLoading = Passed" if obj else "TestCSVLoading = Failed")
        except:
            self.test_obj.yakshaAssert("TestCSVLoading", False, "functional")
            print("TestCSVLoading = Failed")
                
    def test_create_salary_level(self):
        """Test if the Salary_Level column is created correctly."""
        try:
            self.analysis.calculate_salary_level()
            obj = 'Salary_Level' in self.analysis.df.columns
            self.test_obj.yakshaAssert("TestCreateSalaryLevel", obj, "functional")
            print("TestCreateSalaryLevel = Passed" if obj else "TestCreateSalaryLevel = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCreateSalaryLevel", False, "functional")
            print("TestCreateSalaryLevel = Failed")

    def test_export_updated_csv(self):
        """Check if the updated CSV file is saved."""
        self.analysis.export_updated_csv()
        try:
            pd.read_csv("updated_employee_data.csv")
            obj = True
        except FileNotFoundError:
            obj = False
        self.test_obj.yakshaAssert("TestExportUpdatedCSV", obj, "functional")
        print("TestExportUpdatedCSV = Passed" if obj else "TestExportUpdatedCSV = Failed")
