# AGILE TEAM: VUCA-nators
Public repo for CSCI-E71 group project

## Project Description
### Product Name: Fortune Teller

#### Near Vision: Cryptocurrency investors can access a webpage with relevant price information.
#### Far Vision: Investors can use a cryptocurrency price prediction model in the application to facilitate investment decisions.   

## Project Part 1
###  Scrum Team Name  "VUCANATORS"
###  Slack channel : [vucanators-agile-team](https://agilesoftwarecourse.slack.com/archives/C02L5H02672)
###  Git Repository : [vuca-nators](https://github.com/gabemansur/vuca-nators)
###  Scrum Team Roles:
**Folake Adeshina, Scrum Master & Developer** <br/>
**James Burns, Product Owner & Developer** <br/>
**Rachel Wallace, Developer** <br/>
**Gabe Mansur, Developer** <br/>
**Raul Pulido, Developer**

## Stakeholders
### 1. Cryptocurrency Investors, specifically, with at least 1k in the market (Example: Corey Gibson)
### 2. Blockchain Enthusiasts, people who love and enjoy the technical powers of blockchain
### 3. Casual Investors, specifically, people with little knowledge and less than 1k in the market


## Persona- Corey Gibson (His real name)
![image](https://user-images.githubusercontent.com/65990764/139624331-da912d5b-2341-4a1e-8ce2-805027d8e77d.png)
![image](https://user-images.githubusercontent.com/65990764/139624081-3b11c9fd-277d-48a9-bead-34b4fd5c5bd7.png)

Image Source: https://www.topaccountingdegrees.org/faq/what-is-a-chartered-accountant/

## Backlog Ordering

We have ordered the backlog items so that the first ones are infrastructure tasks that will need to be in place before development can begin (setting up boilerplate code, a server, etc.).

Next, we've scheduled the items that will give us a very minimal first iteration of the app. Then, we've ordered the various features we'd like to add, in rough order of importance/value.

## Team Definition of Ready

*Before work can be started on a ticket, it must:*
### 1. Have a title
### 2. Have a user story opening sentence
### 3. Have all business requirements clearly defined
### 4. Have clearly defined acceptance criteria
### 5. Have a story point estimate

## Product Backlog
### Jira Product Backlog <br/>
We stored our product backlog in Jira. The Professor and TA have been given access. [JIRA-URL](https://vuca-nators.atlassian.net/jira/software/projects/FT/boards/1/backlog)

### Estimating the Backlog <br/>
The developers all contributed to a one at a time estimating activity points using Polly. A multi-question app in Slack that uses comments and questions to engage in discussions over each user story. We used the Fibonacci Scale for estimating our user story points. The Fibonacci sequence is exponential instead of linear so it helped us to identify the different complexities of each story.

## Project Part 2: SPRINT 1

All of the information for FortuneTeller Sprint 1 can be found here: (https://github.com/gabemansur/vuca-nators/blob/main/Sprint1README.md) 

## Project Part 3: SPRINT 2

### Sprint Planning
Planning was held Monday, November 15th at 6PM.
<br/>
Sprint Goal: Have a website with a working homepage (both front-end and back-end) that displays current cryptocurrency data.
<br/>
Value this sprint will bring:
<br/>
Jira Product Backlog: [JIRA-URL](https://vuca-nators.atlassian.net/jira/software/projects/FT/boards/1/backlog)

### Forecast

### Sprint Burdown Chart

### Daily Scrum
Daily Scrum meeting, we met on Friday, November 19th at 7PM.

### What did you do since our last meeting?
<ul>
<li> 
Raul: Working on the code from ticket FT-27 to remove the static data in the front end. Fixing the JSON to get it working properly.
</li>
<li>
Rachel: Worked on setting up the CI/CD pipeline with test, build and deploy. In the ci.yaml file test was included and in the cd.yaml file is build and deploy.
</li>
<li>
James: Created two different things in Figma, layout of homepage design and two different logos. Moved tests to the right directory.
</li>
<li>
Gabe: Worked on understanding the definition of stand alone unit tests. 
</li>
<li>
Folake: Setting up static files with Templates and CSS
</li>
</ul>
### What will you do until our next meeting?
<ul>
<li> 
Raul: Complete tests and add to the repo as well as make changes in the code to make sure the data from the API is displayed in the templates.
</li>
<li>
Rachel: Test the pipeline to make sure that it will continue to run without breaking. Update the readme with current sprint documentation.
</li>
<li>
James: Make sure that the API directory and app directory fit together correctly.
</li>
<li>
Gabe: Working to structure market cap of cryptocurrency
</li>
<li>
Folake: Will be continuing to work on ticket FT-30 to develop the design in the frontend
</li>
</ul>
### Are there any impediments?
<ul>
<li> 
Raul: Had an issue with working with the levels for the API. 
</li>
<li>
Rachel: Had an issue initially with the pipeline consistently breaking but was able to resolve after seeing that secrets were needed to be added into the .yaml files and also in github actions under settings 
</li>
<li>
James: Not finding modules to test the code. 
</li>
<li>
Gabe: Blocked by how exactly we will structure the backend of the site. 
</li>
<li>
Folake: Was blocked by the CSS not loading but together as a team we were able to unblock the issue allowing CSS to display correctly.
</li>
</ul>
### Update of Sprint Board and Burndown Chart

### Pair and/or Mob Programming

### Test-Driven Development

### Sprint Review

### Sprint Retrospective with Improvement Plan for next sprint

### Continuous Integration

### Continuous Deployment


