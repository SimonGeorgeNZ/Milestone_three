# Milestone Three - Data Centric Development, Simon George #
## Where to next? ##

![Mockupimages](https://github.com/SimonGeorgeNZ/Milestone_three/blob/master/static/images/macimages.png?raw=true)

Where to Next is a website that is inctended for people who love to travel, and love to travel on a budget. It's a place for backpackers to share
experiences, ideas and secrets that otherwise might not be found. Users can review a city that they have traveled to by listing the reasons for their
trip, where they stayed, where they ate and drank, what they did on their trip as well as some overall lasting memories. 

I have designed it to look like a well loved scrapbook full of planning ideas, hand written notes and scrap paper. The use of clean lines and minimal color
was purposful to represent the idea of getting ideas on paper quickly, then jetting off to have an adventure. 

# Design #

This website is incredibly reliant on user input however I have created some mock reviews to give an idea of how things would work. The user is 
first asked to specify the country, the user spelling is checked against an imported python list called pycountry to make sure the spelling is correct. If
the spelling is incorrect then a list of countries starting with the same letter as the user input is displayed for the user to pick the correct country. After
this the user adds the city they are reviewing, with cities already reviewed from that country displayed to the user so that the same city isn't added 
to MongoDB twice, and that spelling (hopefully correct) is preserved. The user is then asked to give their review a title - This title acts as a password for
the review should the user want to delete or edit their review in the future. From here the user goes on to add the info for the review, when the user adds the dates
they traveled on, if the user selects the same date for start and end of their trip, their trip is deemed to be a day trip and therefor not need accommodation and will 
take the user past the accommodation page. The user should also not be able to add a start date after their end date, with the page reloading if they try to, with an
error message displayed. 

After leaving their review the user is given a chance to view or edit what they have written, as well as delete a section or the entire review. If they want 
to delete any or all, they will need to verify their review title to do so. On the final screen of the review process the user is reminded of their title. 

Here the user can add new sections to accommodation, attractions and hospitality, or if the user deletes the first or last sections, they can add a new one. 

Once finished the user can return to the main landing page where their newly created review will be displayed along with the other 8 newest reviews. 

# Planning #

## Wireframes and ideas ##

![Mockupimages](https://github.com/SimonGeorgeNZ/Milestone_three/blob/master/static/images/planning1.jpg?raw=true)

![Mockupimages](https://github.com/SimonGeorgeNZ/Milestone_three/blob/master/static/images/planning2.jpg?raw=true)

![Mockupimages](https://github.com/SimonGeorgeNZ/Milestone_three/blob/master/static/images/planning3.jpg?raw=true)

Image one shows the flow of information that I mapped out. The country is added to a collection on it's own, the ciry then features the country name as well, 
the title then features the city name also, the title is then added to each doccument as the review is created, which ties the whole review together. I wanted to have 
individual collections for each segment, as this would allow for multiple documents to be added for the same collection against the same review, allowing the user to 
add multiple restaurants, attractions and accommodation against one city. 

I planned some simple wireframes for the design but most of the design was done on the fly and based on looks. As mentioned earlier I wanted the looks of the site to 
be like a hand created scrapbook, made to look like it made quickly with excitement for the upcoming trip. 

## Strategy Plane ##

Where to Next is designed for the thrifty traveller in mind. People who like to plan their experiences based on like minded reviews and also share their experiences with others

## Scope Plane ##

The users will have the ability to add all relevant information from their trip to a certain place, using the country and city as a link. Sections of the review will include
accommodation, hospitality and attractions as well as dates traveled, reasons for the trip and travel around the city. See "Features left to implement" for further release. 

## Structure Plane ##

Users will first be asked to add a country for their review, if the country exists in the database it will no be added again to keep the database free from unneccessary double additions. 

The user will then add a city which will have the country linked with it, then add a password to their review which will have the city linked against it. From here all following review sections
will include the password as a way to link all sections together into one review. 

## Skeleton Plane ##

Where to Next will be structured in a straight line process. The user will be guided through the review process with no inteded way to deviate from the inteded process. Outside of the review process
the user can search for reviews and be taken to them based on their search criteria, or click the link from the landing page to see the review. See wireframe documents above for further evidence of 
planning process. 

## Surface Plane ##

I intend for Where to Next to look like a well loved, hand written scrap book. The only colour differences I envision will look like different ink colours or drawn borders. Clean straight lines will 
give the impression of hand drawn borders and underlined titles to look like a permanent marker.

# User Stories #

- Mike is from Australia living in London for 2 years. He want's to do as much traveling as possible while he's here and wants to know how to travel cheaply. He spends his time 
looking through Where to Next for ideas on cheap accommodation options in cities he wants to go to. In future updates it would be possible for people to search for accommodation only
and even within a price range. 

- Lucy is travel blogger, she travels a lot and likes to doccuments her trips. Lucy uses Where to Next as a way of doccumenting her trips before spending her time writing the full blog. 

- John is planning a trip to the annual beer drinking festival, Oktoberfest. He uses Where to Next to search for other trips to Munich to find good ideas on where to stay and activities 
to do while on his trip. 

### As a user I would like to...

- Easily find review of cities I want to visit
- Add my reviews to the website
- Edit or delete my reviews
- Have the faith that no one else can edit my reviews or delete them 

# Current Features #

- Add new countries to the database
- Retrieve existing countries from the database using matching user input
- Add cities to the database linked to a country
- Link a title to the city which will link the entire review
- Add all review data 
- Edit and delete part or all of the review
- Search for all reviews linked to a country

# Features left to implement #

- Ability to search for cities or any piece of a review - restaurant names, accommodation names or attractions etc. 

- Log in feature that would allow users to control their reviews without the need to validate with their review title. 

- Search with multiple criteria for an advanced search option. 

- Option to select what questions the user wants to answer in the review to customize the experiene.

- Interactive map with location pins of reviewed cities

- Featured aspects on the landing page for cities/restaurants/attractions that have been reviewed the most

- Add photos to reviews

# Resources and technologies used #

I developed this on Gitpod using Heroku as a deployment site and MongoDB as a database. The code is HTML, CSS and Python with a small amount of Javascript. I used Materialise for a number of 
components including the navbar, search feature and cards. Below are resources I have used to help develop my site

- [Stack Overflow](https://stackoverflow.com/)
- [Slask](https://slack.com/intl/en-gb/)
- [Materialize](https://materializecss.com/)
- [Python tips](https://book.pythontips.com/en/latest/)
- Student tutor help - From Code Institute website
- [W3 Schools](https://www.w3schools.com/)
- [MongoDB](https://www.mongodb.com/)
- [Heroku](https://www.heroku.com/)
- [Gitpod](https://www.gitpod.io/)
- [Python Code Checker](https://extendsclass.com/python-tester.html)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/)
- [Pycountry](https://pypi.org/project/pycountry/)
- [Border and button CSS](https://codemyui.com/hand-drawn-border-buttons-css/)
- [Background image](https://www.freeimages.com/photo/wrinkled-note-book-paper-1151925)
- [Card background](http://clipart-library.com/clipart/LcdoqpLni.htm)
- [Map image for nav](https://www.freepik.com/free-vector/hand-drawn-world-map_1133919.htm)
- [Side nav image](https://www.nicepng.com/s/ripped-paper/)

### Please see Deployment section for necessary imports ###

# Testing #

I used HTML and CSS validators to get rid of errors, then manually tested the site myself, and had my flatmates test for me as well. I tried to use lighthouse on Chrome Dev tools.

Because of using templates there were errors returned that were impossible to clear - Manual testing found they didn't impact site use.


## Landing page ##

The user will be greeted with the latest 9 reviews in the database, by clicking the link at the bottom of the postit image "View this review", the user will be taken to the full review. 

## Nav Bar ##

The nav bar is simple in design. The main title of the app - Where to Next? on the left side of the nav will bring the user back to the landing page by clicking on it. On the right side
the new review button will bring the user to the first page of adding a new review, where the search field will bring bring the user to any reviews added under that country. If there are no 
reviews for that country, the user is brought to the "add country" page, where an error message shows them there are no reviews, but they can add one if they like. 

The nav bar is fully responsive and will drop to a hamburger menu on tablet and mobile, where both new review button and search bar act the same way on a popout. 

## New review ##

The review procedure is explained in the design section above, and there should be no way to deviate from the intended procedure. There are buttons on appropriate pages to skip the section
or add another under the same heading - accommodation, hospitality, attractions. By clicking the back button the user will be taken back to the previous page however it will not delete the
previous input from the database. If the user clicks back to take them back to the title page, then any new title added will then become their title, but against the same city. 

## View review ## 

The user will be presented with their review to view, each section is in a collapsible menu to save space on the page. In sections where multiple input is possible, all entries will be available to 
view. The user will also have the option here to edit or delete part or all of their review. 

## Edit ##

By clicking the edit button they will be taken directly to a screen to edit that section of their review. All previous inputs will be available to them to see and anything unchanged will not be updated. 

## Delete ## 

To delete part or all of their review, the user needs to validate their title to do so. I added this feature on all delete screens by way of a two step process to ensure it wasn't as simple as clicking
one button to do so. 

## Viewing review from landing page or search ##

This page acts in a similar way to the page the page the user is greeted by after completing their review. The main difference is the addition of a button at the top of the screen asking if the review is theirs. 
By clicking this button they are asked again to validate their title to be allowed to edit or delete. 

## Add new section from view review page ##

I decided to add a button for the user to add more data when reviewing their review. These buttons are available at the final stage of adding a review, or if the user validates a review is theirs off the landing
page or search. The add button will only appear on the first and last segments if there isn't existing information attached to their review. This was decided for a number of reasons, for example it will stop a 
review having multiple dates against it, or in the case of the final section, there is no need for multiple entries. The add button will stay active on Accommidation, Activities and Hospitality however, as a user
is already able to add multiple entries for these collections. Clicking the add button will take the user to a page displaying very much the same as the page they saw when adding the review from scratch. There are some
subtle differences however. There is no skip button for accommodation, hospitality, attractions or final, and there is no option on accommodation, attractions and hospitality to add another. All pages have one 
submit button at the very bottom, that will take the user back to the view review page, that will now display their new data. 

# Compatibility #

I used Dev tools on Google Chrome and [Am I responsive](http://ami.responsivedesign.is/#) to test compatibility. I designed for mobile, desktop/laptop and tablet. At the bottom of the CSS file there is responsive stylings
for both tablet and mobile. 


# Deployment #

To deploy the project on Heroku there are a number of steps, please follow them carefully. 

- Download the github file 

- Create a Procfile using the command in the terminal echo web: python app.py > Procfile

- Make sure you have the following installed on the project
    - import os
    - import pycountry
    - from flask import Flask, render_template, redirect, request, url_for
    - from flask_pymongo import PyMongo
    - from bson.objectid import ObjectId
    - from os import path

- Make sure you have a requirements.txt file by using the command pip3 freeze --local > requirements.txt

- In your Heroku profile, create a new app 

- Connect your Github to Heroku in Heroku - Go to Deploy - App connected to Github

- In Heroku set the following Config vars

    - IP - 0.0.0.0
    - Mongo_URI - mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority;
    - PORT - 5000

- Commit and push your entire file to Github, making sure your requirements file and Procfile are complete

- Once pushed you can go back to Heroku and in the top right corner, click "Open App"

My app is deployed on Heroku and can be found at [Where to Next](https://milestonethree.herokuapp.com/)

I used Github for version control and can be found at [Milestone Three](https://github.com/SimonGeorgeNZ/Milestone_three)


# Credits #

Firstly I would like to acknowledge the tutor support. Without the expertise and direction I recieved throughout this assessment I would have struggled a lot. Also to my friends and family who gave me the encouragement I
needed to complete this assessment and test it for me. 

# Anti Plagiarism #

To the best of my knowledge I have credited all sources of media and code that is not my own. Anything missed is absolutely an error on my part, and is unintentional, and is in no way me trying to be villainous.
