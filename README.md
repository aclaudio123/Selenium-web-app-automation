# Set up

Need to install a few things:

- https://sites.google.com/a/chromium.org/chromedriver/downloads
- behave (http://pythonhosted.org/behave/)
- selenium (http://selenium-python.readthedocs.io/installation.html)

Or you can run the requirements.txt 

`pip install -r requirements.txt`

For the chrome driver, you can add it to environment variable or 
copy and paste it into a package and then use the relative path.


## Running the tests

To run the tests, you'll need to do this in a terminal (but remember to have the Flask app running!):

```bash
source venv/bin/activate        # if using a virtualenv
cd Selenium-web-app-automation/
python -m behave tests/acceptance
```

If you want to run the tests in PyCharm, you'll need to create appropriate configurations. 
Checkout the wiki on how to setup a multirun configuration!
