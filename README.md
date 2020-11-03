# Milestone Three - Data Centric Development, Simon George #
## Where to next? ##

![Mockupimages](https://github.com/SimonGeorgeNZ/Milestone_three/blob/master/static/images/macimages.png?raw=true)

Where to now is a website that is inctended for people who love to travel, and love to travel on a budget. It's a place for backpackers to share
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
take the user past the accommodation page. 

After leaving their review the user is given a chance to view or edit what they have written, as well as delete a section or the entire review. If they want 
to delete any or all, they will need to verify their review title to do so. ON the final screen of the review process the user is reminded of their title. 

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


# Fratures left to implement #

- Ability to search for cities or any piece of a review - restaurant names, accommodation names or attractions etc. 

- Log in feature that would allow users to control their reviews without the need to validate with their review title. 

- Search with multiple criteria for an advanced search option. 

- OPtion to select what questions the user wants to answer in the review to customize the experiene.

# Resources and technologies used #

I developed this on Gitpod using Heroku as a deployment site and MongoDB as a database. The code is HTML, CSS and Python with a small amount of Javascript. I used Materialise for a number of 
components including the navbar, search feature and cards. Below are resources I have used to help develope my site

- [Stack Overflow](https://stackoverflow.com/)
- [Slask])(https://slack.com/intl/en-gb/)
- [Materialize](https://materializecss.com/)
- [Python trips](https://book.pythontips.com/en/latest/)
- Student tutor help - From Code Institute website
- [W3 Schools](https://www.w3schools.com/)
- [MongoDB](https://www.mongodb.com/)
- [Heroku](https://www.heroku.com/)
- [Gitpod](https://www.gitpod.io/)

# Testing #

I used HTML and CSS validators to get rid of errors, then manually tested the site myself, and had my flatmates test for me as well. I tried to use lighthouse on Chrome Dev tools.

An interesting bug I found was on the date pickers on the first info for the review. I set a function that if the start date was after the end date, the page was reloaded with an error 
message. However after this any dates picked after this would give the same error, regardless of if they were in order or not. I tried to set the value as none however this didn't solve
the issue. I was unsure how to proceed. 



# Deployment #

To deploy the project on Heroku there are a number of steps, please follow them carefully. 

- Create a Procfile using the command in the terminal echo web: python app.py > Procfile

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

Firstly I would like to acknowledge the tutor support. Without the expertise and direction I recieved throughout this assessment I would have struggled
a lot. 

# Anti Plagiarism #

To the best of my knowledge I have credited all sources of media and code that is not my own. Anything missed is absolutely an error on my part, and is unintentional, and is in no way me trying to be villainous.
