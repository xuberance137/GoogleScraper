# GoogleScraper - Automated scraping search engines


### Table of Contents

1. [Installation](#install)
2. [Description](#quick)
3. [Contact](#contact)


<a name="install" \>
## Installation

GoogleScraper is written in Python 3. You should install at least Python 3.4. The last major development was all done with Python3.5. So when using 
Ubuntu 15.10 and Python3.5 for instance, please install:

```
sudo apt-get install python3.5-dev
virtualenv --python python3 env
source env/bin/activate
pip install GoogleScraper
pip install lxml selenium cssselect requests PyMySql sqlalchemy chardet aiohttp
brew install chromedriver 
```

<a name="quick" />
## Quick Start

Read original descriptions at https://github.com/NikolaiT/GoogleScraper

Modified to get GoogleScraper to write to JSON.

<a name="contact" \>
## Contact

If you feel like contacting me, do so and send me a mail or message me here. 

[1]: http://www.webvivant.com/google-hacking.html "Google Dorks"
[2]: https://code.google.com/p/socksipy-branch/ "Socksipy Branch"
[3]: http://incolumitas.com/about/contact/ "Contact with author"
[4]: http://incolumitas.com/2013/01/06/googlesearch-a-rapid-python-class-to-get-search-results/
[5]: http://incolumitas.com/2014/11/12/scraping-and-extracting-links-from-any-major-search-engine-like-google-yandex-baidu-bing-and-duckduckgo/
