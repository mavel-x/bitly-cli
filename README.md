# Bitly URL Shortener

A simple command line interface for Bitly written in Python. 
Shorten URLs or get click statistics for existing bitlinks (shortened links).

## How to Install

### Get a Bitly Token
You will need an API token to use Bitly via this script.

To obtain it, create an account on [Bitly](https://bitly.com/). 
I recommend signing up with email &mdash; for some reason, getting an API token
gets trickier if you create an account using social media.

Confirm your email and then go to [Developer settings](https://app.bitly.com/settings/api/) 
and generate an access token. It will be a string looking something like this:
`17c09e20ad155405123ac1977542fecf00231da7`.

Create a file named ".env" in the same directory as the script. This is where your API token
will be (more or less safely) stored. Add the following line to the file:
"BITLY_TOKEN=_your_token_" (remove the quotation marks). The file will look like this:
```
BITLY_TOKEN=17c09e20ad155405123ac1977542fecf00231da7
```

### Install the Required Packages
Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```console
$ pip install -r requirements.txt
```
Optionally, you can use [virtualenv](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv) 
to install the packages inside a virtual environment and not on your entire system. 
In this case you will need to configure running the script from the virtual environment 
as well.

### Run the Script
Open the terminal and run:
```console
$ python3 path/to/the/script/main.py https://long-link.that/you-want?to=shorten 
```
or to get statistics (total clicks) for an existing bitlink:
```console
$ python3 path/to/the/script/main.py bit.ly/link-code 
```
Keep in mind that the script will not shorten links without the URL scheme supplied 
(`http://`, `https://`, etc).

## Project Purpose

The code is written for educational purposes as part of 
an online course for web developers at [dvmn.org](https://dvmn.org/).

## References
- [Bitly Docs](https://dev.bitly.com/get_started.html)
- [Pipenv & Virtual Environments](https://docs.python-guide.org/dev/virtualenvs/)
- [dvmn.org](https://dvmn.org/)