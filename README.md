##OTOMOTO.PL price tracker

A python program with an user interface created based on kivy language, that looks for an user specified car on Polish
otomoto.pl website considering parameters like **make**, **model**, **year** and **engine type**, perform various 
calculations on those cars data and plot 2 kinds of graphs (average of daily prices on a weekly perspective, and average
of weekly prices on a monthly perspective)

## Instructions
Simply run main.py and subsequently provide car you are interested in by filling 4 fields (i.e. **make**, **model**, 
**year** and **engine type**(diesel/benyzna/benzyna+lpg which stands for diesel/benzine/benzine+lpg))

## Quick note:
Note, algorithm loads results of given car make and model from the first search page only.
Loading from remaining search pages may be added in the next versions of the program.

Algorithm works with a version of otomoto.pl website on a day 19/10/2020. This may change, if the website's layout be
modified

## Requirements:
have installed the following packages:
* beautifulsoup4==4.9.1
* certifi==2020.6.20
* chardet==3.0.4
* Kivy==1.11.1
* Kivy-Garden==0.1.4
* kiwisolver==1.2.0
* matplotlib==3.3.0
* Pillow==7.2.0
* Pygments==2.6.1
* pymongo==3.11.0
* pyparsing==2.4.7
* python-dateutil==2.8.1
* requests==2.24.0
* six==1.15.0
* soupsieve==2.0.1
* urllib3==1.25.10


built on python 3.7