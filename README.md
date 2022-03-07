
# Blue Chip Pitch App

Blue Chip is a pitch web application.
This application enables user/(s) to create accounts so that they can post their impressions. Users must login in order to view other pitch categories.

# App screenshot
![Blue Chip]()
## Installation

Guide to install Horizon News application:

### Clone this repository
```bash
 git clone https://github.com/John-Kimani/Blue_Chip_Pitch_App.git
```
* Move into the cloned directory:
```bash
cd BLUE_CHIP_PITCH_APP
```
* Create and activate your virtual environment:
```bash
mkvirtualenv virtual
```
* Install project dependancies within your active environment: (Read: requirements.txt and use command below)
```bash
(virtual)$ pip3 Install -r requirements.txt
```
* Environment variables:
    *  Create a file called ```.env``` in the root folder
    ```bash
    (virtual)$ touch .env
    ```
    * Add the following lines to the file as seen in ```.env-template```
    ```bash 
    SECRET_KEY=
    DATABASE_URL=
    ```
* Start the flask server
```bash
(Virtual)$ flask run
```
* or

```bash
(Virtual)$ python3 bluechip.py
```
## Features and BDD

- Users are able to create user profile and login to their profiles.


## Technology Used

**Framework:** Flask
**Language** Python

### Developed with
**Structure:** Bootstrap, HTML
**Styles:** CSS

## Author

* Design and developed by: [John Kimani](https://github.com/John-Kimani)
