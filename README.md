# Welcome to Resumate!

## [For Installation Instructions, click here!](#installation)

## About the project

Recently, the Canadian government has announced a new plan to welcome over 500,000 immigrants each year by 2025. We see a demand for Resumate since it can help fight some of the many challenges that new immigrants face when settling in a new country. Resumate can provide help with resume editing, as well as suggest courses and education to increase their skills and experience level. Through this, Resumate can improve a new immigrant’s chance of securing a job.

## Inspiration
When we worked with international students during our time at the UBC career center, we noticed that many international students and immigrants faced challenges in finding employment in Canada due to their lack of knowledge about the Canadian job market and poor resume writing skills. 
We also know that the quality and content of one’s resume is one of the most important factors when it comes to securing a job. In addition, the federal government is planning on bringing in 500,000 immigrants to Canada each year by 2025.
Therefore, we took inspiration from this potential issue to create an app to help international students and immigrants secure a job in Canada by suggesting improvements to their current resume and ways to upgrade their skills.

## What it does
A user can input their resume, and get back a rewritten resume as well as tips on how to better improve their resume
Based on the user’s resume and a job description for a job they’re interested in, they can get a list of courses they can take to improve their skills and make them better suited  for the job.

## How we built it
Front end was built using React, HTML, CSS, and JavaScript, and Axios was used to handle data between our front end and back end, which was created using Python and Flask. Our back end then makes requests to the OpenAI API.

## Challenges we ran into
POSTing to our back end from our front end and reading the data correctly
Deploying both our front-end and back-end servers due to time constraints and account issues
Translating our app menus and instructions
Generating correct  and usable responses from the OpenAI API

## Accomplishments that we're proud of
Our app is usable in multiple languages
Creating both a front end and a back end



## What we learned
Learning more about React
How to create a back end using Flask
Gaining more experience with HTTP requests and API calls

## What's next for Resumate
Implementation of a Community page where new immigrants can network and connect with other new immigrants
Directory of helpful resources for new immigrants
Implementation of responsive design that supports all media size
A mobile app version 


What languages, frameworks, platforms, cloud services, databases, APIs, or other technologies did you use?
Front end:
React, HTML, CSS, Axios, JavaScript
Back end:
Python, Flask
OpenAI API


## Installation

### Commands
- To run the app locally, enter 'flask run' in terminal in the project directory (open in port # 5000)

### Resource
- Used to initialize: https://tms-dev-blog.com/python-backend-with-javascript-frontend-how-to/