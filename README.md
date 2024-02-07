# Running the Flask App Locally
Prerequisites:

Ensure you have Python 3.9 (or the appropriate Python version for your project) installed on your local machine.
Create and activate a virtual environment (optional but recommended for isolating dependencies).
Install the required dependencies. You can do this by running the following command in your project directory:

`pip install -r requirements.txt`

Running the App:

Open a terminal in the project directory.
Activate your virtual environment (if you're using one).
Run the server with the following command:

`python3 main.py`

You should see output indicating that the Flask development server is running. It will be accessible at http://localhost:8080/.


# Running Unit Tests
Prerequisites:

Ensure you have followed the steps above to set up your project locally, including installing dependencies.

Open a terminal in your project directory.
Activate your virtual environment (if you're using one).
Run the tests with the following command:

`python3 -m unittest discover -s tests -p 'test_app.py'`
