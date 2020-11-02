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