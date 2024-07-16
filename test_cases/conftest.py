import pytest
import os
import logging
from selenium import webdriver
from pytest_metadata.plugin import metadata_key

path = ""


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='chrome',
                     help='Specify the browser: chrome or firefox or edge')


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def report_path(request):
    # Fetch the path specified by the user or provide a default path
    return request.config.getoption("--html", default="./reports/report.html")


@pytest.fixture()
def creation(report_path):
    global path
    path = report_path
    # Additional logic to ensure report is generated at the specified path
    if path == "./reports/report.html":
        # Generate report at default path
        print(f"Generating report at default path: {path}")
        # Your code to generate report at default path
    else:
        # Generate report at user-specified path
        print(f"Generating report at user-specified path: {path}")
        # Your code to generate report at user-specified path


@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported error")
    return driver


# For pytest html reports
# hook for adding environment info in html report
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'Ecommerce Project'
    config.stash[metadata_key]['Test Website Name'] = 'nopcommerce'
    config.stash[metadata_key]['Test Website Link'] = 'https://admin-demo.nopcommerce.com/login'
    config.stash[metadata_key]['Test Module Name'] = 'Admin Login Tests'
    config.stash[metadata_key]['Tester Name'] = 'KHAJAVALI'


# hook for delete/modify environment info in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA HOME', None)
    metadata.pop('Plugins', None)


# # Hook to set up logging before tests start
# @pytest.fixture(scope="session", autouse=True)
# def setup_logging(request):
#     # Configure logging
#     logging.basicConfig(
#         level=logging.INFO,  # Set desired logging level
#         format='%(asctime)s - %(levelname)s - %(message)s',
#         filename='pytest.log',  # Log file name
#         filemode='w'  # Overwrite log file for each run
#     )
#
#     # Define a handler to also print logs to console
#     console = logging.StreamHandler()
#     console.setLevel(logging.INFO)
#     formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#     console.setFormatter(formatter)
#     logging.getLogger('').addHandler(console)
#
#     # Teardown function to finalize logging after tests complete
#     def teardown_logging():
#         logging.shutdown()
#
#     request.addfinalizer(teardown_logging)
#
#
# # Optional: This fixture can be used to pass the logging object to tests if needed
# @pytest.fixture(scope="function")
# def logger(request):
#     def log_function_call(func):
#         def wrapper(*args, **kwargs):
#             # Log function name and parameters
#             logger = logging.getLogger(__name__)
#             logger.info(f"Calling function '{func.__name__}' with args: {args}, kwargs: {kwargs}")
#             return func(*args, **kwargs)
#
#         return wrapper
#
#     return log_function_call


# Hook to set up logging before tests start
@pytest.fixture(scope="session", autouse=True)
def setup_logging(request):
    # Determine the path where you want to save the log file
    log_directory = os.path.join(os.path.dirname(__file__),
                                 'logs')  # Assuming this script is in the root of your project

    # Ensure the logs directory exists, create if not
    os.makedirs(log_directory, exist_ok=True)

    # Configure logging
    log_file_path = os.path.join(log_directory, 'pytest.log')
    logging.basicConfig(
        level=logging.INFO,  # Set desired logging level
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=log_file_path,  # Log file path
        filemode='w'  # Overwrite log file for each run
    )

    # Define a handler to also print logs to console
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    # Teardown function to finalize logging after tests complete
    def teardown_logging():
        logging.shutdown()

    request.addfinalizer(teardown_logging)


# Optional: This fixture can be used to pass the logging object to tests if needed
@pytest.fixture(scope="function")
def logger(request):
    def log_function_call(func):
        def wrapper(*args, **kwargs):
            # Log function name and parameters
            logger = logging.getLogger(__name__)
            logger.info(f"Calling function '{func.__name__}' with args: {args}, kwargs: {kwargs}")
            return func(*args, **kwargs)

        return wrapper

    return log_function_call
