# Shoppinglist

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5f0fcd8fd4094250b52dcaf7b08f1cb4)](https://www.codacy.com/app/EinsteinCarrey/Shoppinglist?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=EinsteinCarrey/Shoppinglist&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/EinsteinCarrey/Shoppinglist.svg?branch=master)](https://travis-ci.org/EinsteinCarrey/Shoppinglist)
[![Code Health](https://landscape.io/github/EinsteinCarrey/Shoppinglist/master/landscape.svg?style=flat)](https://landscape.io/github/EinsteinCarrey/Shoppinglist/master)
[![Coverage Status](https://coveralls.io/repos/github/EinsteinCarrey/Shoppinglist/badge.svg?branch=master)](https://coveralls.io/github/EinsteinCarrey/Shoppinglist?branch=master)



The Shopping-list app is an application that allows users to record and keep track of things they want to shop or buy. It allows them to keeping track of their shopping carts.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### How to run this application

##### Install Python

​	You can find the documentation for python **[here](https://www.python.org/)**

​	https://www.python.org/

##### Clone this repository

> https://github.com/EinsteinCarrey/Shoppinglist.git

1. ##### Create a virtual environment

   ​	Use this [**guide**](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/).

   ​	Activate the  virtual environment.

   1. ##### Install project dependencies

     run the command `pip -r install requirements.txt` on the command line


##### Run the server

> `python app.py`

##### Access the server on a browser

Open a browser and access **[this location](http://127.0.0.1:5000/)**.

> [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

​

### Usage

The shopping-list app provides an interactive Graphical User Interface which is easy to interact with

##### User create a user account

![Sign Up](https://raw.githubusercontent.com/EinsteinCarrey/Shoppinglist/flask/Designs/screenshots/signup-screen.png)

##### User can now login to the account

![Login](https://raw.githubusercontent.com/EinsteinCarrey/Shoppinglist/flask/Designs/screenshots/login-screen.png)

##### User can signout

![Sign-out](https://raw.githubusercontent.com/EinsteinCarrey/Shoppinglist/flask/Designs/screenshots/signout.png)

##### User can create and view shopping-lists

![Shopping-lists](https://raw.githubusercontent.com/EinsteinCarrey/Shoppinglist/flask/Designs/screenshots/shopping-list.png)



## Running the tests

This code has been tested using three common python test libraries `py.test`, `unittest` and `nosetest`.

```python
# Testing in nosetest
# Navigate to the project root directory
# run the following command
nosetests _tests

# Sample output
.........................................................
----------------------------------------------------------------------
Ran 57 tests in 0.459s

OK
```

### Coding style tests

This application complies with the [**PEP8**](https://www.python.org/dev/peps/pep-0008/) convention for Python. To check compliance run the following command in your command line `pep8 .` Remember to exclude your virtual environment from the scope if it is in the project directory.



## Deployment

This product is still at the development stage. I strongly discourage deploying it on a production server.

## Built With

* [**Flask**](http://flask.pocoo.org/) - An open-source  web microframework for python
* [**pip**](https://pypi.python.org/pypi/pip) - Python Dependency Manager
* [**Bootstrap CSS**](http://getbootstrap.com/css/) - User Interface styling
* [**JQuery**](https://jquery.com/) - HTML document traversal, manipulation and event handling

## Versioning

I use [Semantic Versioning](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* [Einstein Njoroge](https://github.com/EinsteinCarrey) - You can view my profile and other works on [GitHub](https://github.com/EinsteinCarrey)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [**Felix Wambiri**](https://github.com/FelixWambiri)- Code review
* [**Hound-ci**](https://github.com/houndci-bot) - css-linting and code review
* **[Coveralls](https://coveralls.io/)** - Test Coverage checker

