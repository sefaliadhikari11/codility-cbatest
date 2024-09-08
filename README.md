# PetStore-RegressionTest

## Overview

This project includes test cases for the Swagger Petstore API, focusing on various endpoints. The tests are written using `pytest` and utilize the `requests` library for making HTTP requests to the API.

## Prerequisites
Before running the tests, ensure you have the following installed:

>- Python (version 3.6 or later)  <br>
>- pip (usually comes with python)  <br>
>- IDE - PyCharm (optional) <br>

## Setup

1. **Clone the Repository** <br>
First, clone the repository to your local machine: <br> 
    ```
    git clone https://github.com/sefaliadhikari11/codility-cbatest.git
    git checkout feature/SefaliAdhikari-CBATest  
    cd codility-cbatest
    ```

2. **Create a Virtual Environment** <br>
Create a virtual environment to isolate your project's dependencies: <br>
    ```
    python -m venv venv
    ```

3. **Activate the Virtual Environment** <br>
Activate the virtual environment: <br><br>
    **On Windows**: <br> 
    ```
    venv\Scripts\activate
    ```
    **On macOS and Linux**: <br>
    ```
    source venv/bin/activate
    ```

4. **Install Dependencies** <br>
Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```
   The requirements.txt file should include the necessary packages, e.g.: <br>
    ``` 
    requests==2.28.1
    pytest==7.1.2
    ```


## Running the Tests

1. **Navigate to the tests Directory** <br>
Ensure you are in the root directory of the project where the `pytest` configuration is located. <br> <br> 

2. **Run Tests with `pytest`** <br>
Execute the tests using `pytest`:
    ```
    pytest
    ```
   By default, `pytest` will discover and run all the test files that match the pattern `test_*.py` or `*_test.py` in the `tests` directory. <br> <br> 
3. **Viewing Test Results** <br>
After running the tests, `pytest` will display the results in the terminal. It will show which tests passed, failed, or were skipped.


## Test File Structure
- `tests/test_pet.py`: Contains test cases for the Pet API endpoints.
- `tests/helpers/ai_helpers.py`: Contains helper functions for making API requests.