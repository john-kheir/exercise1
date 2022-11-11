"""
This module contains shared fixtures.
"""

import json
import pytest
import selenium.webdriver


@pytest.fixture
def config(scope='session'):

  # Read the config file
  with open('config.json') as config_file:
    config = json.load(config_file)
  
  # Assert config values are acceptable
  assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
  assert isinstance(config['implicit_wait'], int)
  assert config['implicit_wait'] > 0
  return config


@pytest.fixture
def browser(config):

  # Initialize the WebDriver instance
  if config['browser'] == 'Firefox':
    b = selenium.webdriver.Firefox()
  elif config['browser'] == 'Chrome':
    b = selenium.webdriver.Chrome()
  elif config['browser'] == 'Headless Chrome':
    opts = selenium.webdriver.ChromeOptions()
    opts.add_argument('headless')
    b = selenium.webdriver.Chrome(options=opts)
  else:
    raise Exception(f'Browser "{config["browser"]}" is not supported')

  # Let the calls wait for elements to appear ..
  # just for simplicity but it is not the best practise because it can cause performance issues
  b.implicitly_wait(config['implicit_wait'])
  b.get('http://zero.webappsecurity.com/')
  b.maximize_window()

  # Return the WebDriver for the test to run
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit()

