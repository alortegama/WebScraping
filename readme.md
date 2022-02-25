# Web Scraping Example

## Dependencies:

````shell
    pip install - r requirements.txt
````
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
  * ```pip install beautifulsoup4 ```
* [dominate](https://pypi.org/project/dominate/)
  * ```pip install dominate ```
## main.py

It contains all the information to retrieve the desired web page and analyze its content properly.

This file contains the main function to be started

## article.py

Contains the Article data class

## html_builder

It is the main constructor of the desired web page, it uses [bootstrap](https://getbootstrap.com) to give a correct
format in a simple and fast way The link for the css used can be found at:

````html

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
      integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
````