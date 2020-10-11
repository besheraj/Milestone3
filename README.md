![WebSite](doc/images/Website.png)
live version on: [link to live version!](http://aj-photogallery.herokuapp.com/)
# Aj Photo Gallery "Milestone 3" Project:
Aj photo gallery a web application store user photos in the cloud using AWS and represent the photos in your own gallery, its private as every user have their own account and can upload unlimited numbers of photos and store it online.
its very easy to use sign up to creat your new account upload your photos and thats it.

# User Story:

**As a User:** :
* Ability to creat a private account.
* Ability to upload photos.
* Ability to display the photos in gallery.
* Ability to delete the photos.
* Ability to edit the account name or password.
* Ability to delete the account.
* Ability to contact thru contact form to report a proble.

## Wrieframes:
The wireframes designed by Balsamiq tool, [link to wireframes!](wireframes/wireframes.pdf)

# Features:
## Existing Features:
* The menu bar will switch to a button that collapse in the mobile and tablet version.
* A signup button in the main page.
* Sign Up form to creat a new account.
* Upload photo button with a name field.
* Fancybox gallery enables user to go thru photos by clicking right and left.
* Hover over the photos to view it in bigger mode.
* Every 6 photos will be viewed in single page and a nav bar will be shown below gallery to navigate thru pages.
* Button below each photo to delete it.
* From to edit the profile name and password.
* Button to delete the whole profile with all the photos.

## Future Features:
* Ability to add new albums.
* Ability to change or delete albums.
* Ability to login using instagram or pinterest.

# Technology:
* **Languages**:HTML5, CSS3, Javascript, Python
* **Frameworks**: Bootstrap, Flask, Jingja, Jquery
* **Databases**: MongoDB.
* **Balsamiq**:Designed the wireframes.
* **VSCode**: This whole project code written using VScode.
* **Github**: The whole project commited and pushed to github repository and published on Github pages.
* **JS Email**: Used with the contact form. 
* **Heroku**: Depolyed on Heroku.

# Testing:

## testing cycle:
**Navbar**:
* Click on "login" Direct to login page.
* Click on "profile": 
if not Logged in direct to login page.
if logged in direct to profile page.
* Click on "contact" Direct to contact form.
* Click on "logout" Direct to main page.

**Home**:
* Click on the "Signup" button direct to Signup form.
**Signup**:
* All fields are required.
* If password and confirm password fields dosent match will return "passwrd dosent match"
* If user name existed will return"this email already exist please try to login"
* If password not 8 charcters will return "please match the password format"
![password-not-match](doc/images/password-not-match.png)
![existing-user](doc/images/existing-user.png)
![password-format-not-match](doc/images/password-format-not-match.png)

**login**
* E-mail and Password field are required.
* If Email dosent exist will return " this email dosent exist in our system please signup"
* if passwword and email dosent match will return " incorrect username/password "
![incorrect-password](doc/images/incorrect-password.png)
![incorrect-name](doc/images/incorrect-name.png)

**Profile** 
* Click on choose file to select a photo.
* If the file not a photo will return"we only accept photos with the following extentions png, jpg, jpeg, gif"
* Click on "edit my profile" will direct to edit my profile page.
* Click on "My Gallery" will direct to Gallery page.
![accepted-photos](doc/images/accepted-photos.png)

**Gallery**
* Hover over photo will make it bigger.
* Click on photo to display Galeery mode and press right or left to surf the photos and Press esc to exit.
* Click on Delete Photo the photo will disappear.
* if Uploaded more than 6 photos a tap will appear in the bottom with numbers to go thru the pages and each page display 6 photos and information bar will display how many photos uploaded.
![Gallery1](doc/images/gallery1.png)
![Gallery2](doc/images/gallery2.png)

**Edit My Profile**
* Email field cant be edited and will display the user email.
* All fields are required.
* If password and confirm password fields dosent match will return "passwrd dosent match"
* If user name existed will return"this email already exist please try to login"
* If password not 8 charcters will return "please match the password format"
* Click on Delete my profile will have checkbox to confirm delete if click on cancle will be back to page and if click ok will return "your account deleted succesfully" on the main page.
![password-not-match](doc/images/password-not-match.png)
![existing-user](doc/images/existing-user.png)
![password-format-not-match](doc/images/password-format-not-match.png)
![confirmation-delete-account](doc/images/confirmation-delete-account.png)
![deleted](doc/images/deleted.png)

**Contact page and form**
* If you scroll down more you will see the contact form section.
* If you enter your name and click on "send now" you will be asked to fill in your email address field.
* If you enter your email and click on "send now" you will be asked to fill in your name field.
* If you enter your message and click on "send now" you will be asked to fill in your name field.
* If you enter your name and email and click on "send now" you will be asked to fill in your message field.
* If you enter your name and message and click on "send now" you will be asked to fill in your email address field.
* If you enter your email and message and click on "send now" you will be asked to fill in your name field.
* If you enter your name, email and message and click on "send now" you will get an alert "Your message has been sent.".
* If you enter your name, email and message and click on "send now", and some how there is an error with the server you will get an alert "FAILED... please try again later!".
* Onec the form completetd and the alert "Your message has been sent." pop up the developer will receive an email with the the form details as follows:
![email test](doc/images/sample-email.png)
![email test](doc/images/sample-email-form.png)

### Responsiveness tesing:
The design was tested using chrome devtools for the following devices:
* Responsive (googlechrome dev tools).
* Moto G4.
* Galaxy S5.
* Pixel 2.
* Pixel 2 XL.
* Iphone 5/SE.
* Iphone 6/7/8.
* Iphone 6/7/8 Plus.
* Iphone X .
* Ipad.
* Galaxy Fold.
* Surface Duo.
### W3 Schools validation:
* HTML code passed by w3schools html validator without errors.
* CSS code passed by W3schools CSS jigsaw without errors.

# Delpyment:

## Local Deployment:

### Prerequisites to work with this Site
* Dedicated MongoDB (Sign up at www.mongodb.com)
* Dedicated S3 Bucket with AWS (Sign up at www.aws.amazon.com)
* Optional: Heroku Account (Sign up at www.heroku.com)

Official Github Documentation on cloning a repositiory: https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository

1- Navigate to Mainpage of the repository.
2- Click on "Code" button.
3- Choose "Clone with HTTPs" & copy URL.
4- Open Terminal
5- Change the current working directory to prefered location.
6- Type git clone and past copied URL git clone https://github.com/besheraj/milestone3.git
7- Press Enter to create local Clone - Make sure your environment supports "python3 -".
8- Type "pip3 install -r requirements.txt" into Terminal.
9- Create env.py, .env and .gitignore and add the first 2 to git ignore.
10- Fill env.py with the following data:
import os

os.environ["MONGO_URI"] = "mongodb+srv://root:Password@testcluster.pscp8.mongodb.net/DBNAME?retryWrites=true&w=majority"
os.environ["SECRET_KEY"] = "YOUR SECRET KEY"

S3_BUCKET = "S3 BUCKET NAME"
os.environ["S3_BUCKET"] = "S3 BUCKET NAME"
os.environ["S3_KEY"] = "S3KEY"
os.environ["S3_SECRET"] = "S3 SECRET"
os.environ["S3_LOCATION"] = 'https://{0}.s3-ap-southeast-1.amazonaws.com/'.format(S3_BUCKET)

### Deployment to Heroku
1- Log in to your Heroku account and create a new App.
2- Set the environment variables in Settings > Reveal Config Variables
3- The following Variables must be set:
os.environ["MONGO_URI"] = "mongodb+srv://root:Password@testcluster.pscp8.mongodb.net/DBNAME?retryWrites=true&w=majority"
os.environ["SECRET_KEY"] = "YOUR SECRET KEY"
S3_BUCKET = "S3 BUCKET NAME"
os.environ["S3_BUCKET"] = "S3 BUCKET NAME"
os.environ["S3_KEY"] = "S3KEY"
os.environ["S3_SECRET"] = "S3 SECRET"
os.environ["S3_LOCATION"] = 'https://{0}.s3-ap-southeast-1.amazonaws.com/'.format(S3_BUCKET)
IP = 0.0.0.0 
PORT = 5000
4- Create requirements.txt from your project with the help of pip3 freeze --local > requirements.txt
5- Create a Procfile echo web: python app.py > Procfile
6- Commit changes to Git git add . followed by git commit -m ""
7- Log in to heroku from your terminal heroku login.
8- Add exisitng repository to Heroku heroku git:remote -a <your repository>
9- Push changes to Heroku git push heroku master.

# Credits:
The backgroundImages and main page was imported from https://startbootstrap.com/ 





