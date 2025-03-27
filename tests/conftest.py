import pytest
import os
from datetime import datetime


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Define the custom report directory (outside the 'tests' folder)
    report_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Test_Reports"))

    # Create the directory if it doesn't exist
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # Add timestamp to report filename
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = os.path.join(report_dir, f"report_{now}.html")


# Configuration file for allure reporting......

# import pytest
# import os
#
#
# @pytest.hookimpl(tryfirst=True)
# def pytest_configure(config):
#     # Define the custom Allure report directory
#     allure_report_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Allure_Reports"))
#
#     # Create the directory if it doesn't exist
#     if not os.path.exists(allure_report_dir):
#         os.makedirs(allure_report_dir)
#
#     # Set the Allure report directory
#     config.option.allure_report_dir = allure_report_dir


