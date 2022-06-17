#  Jirani App

### An application that allows engagement within a neighbourhood to avail crucial information.

#### By **Joy Machuka**

+ [Description](#Description)
+ [How to run the code](#Setup)
+ [Live Site](#Live-Site)
+ [Technologies](#Technologies-and-Languages-Used)
+ [Authors Info](#Author)
+ [Licence](#Licence)

# Description
Jirani is swahili for neighbour. This is a a web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.
## Live-Site
[View Site](https://jirani.herokuapp.com/)


## BDD
* As a user, I would like to sign in with the application to start using.
* As a user, I would like to Set up a profile about me and a general location and my neighborhood name.
* As a user, I would like to Find a list of different businesses in my neighborhood.
* As a user, I would like to Find Contact Information for the health department and Police authorities near my neighborhood.
* As a user, I would like to Create Posts that will be visible to everyone in my neighborhood.
* As a user, I would like to Change My neighborhood when I decide to move out.
* As a user, I would like to Only view details of a single neighborhood.

## Setup

To get the project .......  
  
##### Fork then Clone the repository:  
 ```bash 
git clone https://github.com/MachukaJoy/jirani.git 
```
##### Navigate into the folder
 ```bash 
cd jirani
```
##### Create and activate virtual environment  
 ```bash 
pipenv –-three
```
##### Activate Virtual Environment
 ```bash 
pipenv shell 
```  
##### Install Dependencies  
 ```bash 
 pipenv  install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations jirani
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test jirani
```
Open the application on your browser `127.0.0.1:8000`.


## Known Bugs
There are not any known bugs as at now. But feel free to let us know should you find any.

## Technologies-and-Languages-Used
* Python
* Visualstudio
* Django
* postgress sql

## Support and contact details
Should you have any issues or questions, ideas or concerns feel free to reach out to me. Also feel free to make contribution to the code and can contact me at machukajoy@gmail.com
## Author

- [Joy Machuka](https://github.com/MachukaJoy)
### Licence
[MIT LICENSE](https://github.com/MachukaJoy/jirani/blob/main/LICENSE)<br>


** <br>
Copyright (c) {2022} [Joy Machuka ](https://github.com/MachukaJoy)