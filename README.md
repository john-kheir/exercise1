## Prequistes
 1- You need to have python 3.8 on your system. It should also work on 3.10 but I didn't test it 
 
 2- Pipenv is also required. To install pipenv, run `pip install pipenv` from the command line.
 

## Project Setup 

1- Clone the repositery. 

2- Copy the chromedriver from the resources folder to `/usr/local/bin`. `/usr/local/bin` should already be included in the system path.
   The drivers work for the last browsers, if you are looking for a certain driver that matches your browser,  Please download the intended WebDriver 
   executables for these browsers: [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for Chrome and [geckodriver](https://github.com/mozilla/geckodriver/releases) for Firefox.
```
$ cp /resources/ChromeDriver /usr/local/bin
$ cp /resource/geckodriver /usr/local/bin
```
Note: by default the tests runs against headless chrome. You can change this config in `config.json`

3- Run `pipenv install` to install the dependencies. 

4- Run `pipenv run python -m pytest` to run tests.
   
   Notes: 
   
   - Run `pipenv run python -m pytest --html=report.html`  to run tests and generate test run report.
          
   - Some test are marked for smoke testing. Run `pipenv run python -m pytest -m smoke` to run the smoke tests





