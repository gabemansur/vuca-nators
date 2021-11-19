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

## Project Part 2: First Sprint

### Forecast
We did not have any data from previous sprints to base our velocity on so we made an estimation and forecasted 10 user story points to deliver in the first sprint. This forecast was based on the skill level and size of our development team. We plan to adjust our next sprints based on the experience we have in our first sprint. In the upcoming sprints, we will use Yesterday's Weather to make a more calculated decision based on the data that is already known.

![image](https://user-images.githubusercontent.com/41925616/141844945-55df0aeb-c66b-4753-91c9-824f62c89799.png)


### Sprint Backlog
For this first sprint we pulled user stories from the top of our product backlog. Only developers participated in this activity. We also made sure that the aggregate size of our stories did not exceed our forecast of 10 user story points. In order to remain under the forecast, we pulled in user stores FT-2 (3 points), FT-4 (2 points), and FT-3 (3 points). Each user story was decomposed into developer tasks.
Our Kanban Board with user stories and developer tasks: [Kanban-Fortune-Teller](https://trello.com/b/u1anMbHM/fortune-teller)

### Burndown Chart (Friday, Nov 12th)
![image](https://user-images.githubusercontent.com/65990764/141510282-302d9243-01ce-436b-86c3-dfaa9d3182f7.png)
### Burndown Chart (Monday, Nov 15th)
![image](https://user-images.githubusercontent.com/65990764/141839413-05b870e2-85ef-4632-9351-78f41385e484.png)
Direct Link: https://miro.com/app/board/o9J_lmkBur8=/?invite_link_id=207030815636

### Daily Scrums (Sample of 1 Day)
Screenshot: ![Daily Scrum](https://user-images.githubusercontent.com/65990764/141836995-6b70d682-7b05-48a9-af49-f8eba0390ecf.JPG)

Raul:
<li>What did you do in the last 24 hours?</li>
<ul>
<li>I installed the Jira TeamHealth Extension for the Scrum Forecast.</li>
<li>I changed the workflow stages(split in progress into three new stages (in Dev, Dev-Test, and UAT). Also, added a previous stage "Ready to Deploy" before to Done. The idea is to have a more transparent process and have a better idea of how the sprint is moving.</li>
<li>I installed Django and cloned the Fortune-Teller project.</li>
<li>I inspected the website CoinMarketCap and I registered as a developer to get the API key</li>
</ul>
<li>What will you do in the next 24 hours?</li>
<ul>
<li>I will create the Unified Test to Fail and Success/Pass for the API connection to CoinMarketCap website.</li>
</ul>
<li>Are there any impediments?</li>
<ul>
<li>None</li>
</ul>

<br/>
Rachel:
<li>What did you do in the last 24 hours?</li>
<ul>
<li>FT-28: added login and admin functionality - includes views, models, urls, etc.</li>
<li>Created a superuser (admin) and verified admin site - login credentials (endpoint /admin)</li>
<li>Cryptoinvestor can register using Username, Email Address, Password(endpoint /register). Added functionality to allow user to register if they do not have login info</li>
<li>Added functionality to allow user to login with Username/Password(enpoint /login)</li>
<li>Added functionality to show content only available to users that are authenticated</li>
</ul>
<li>What will you do in the next 24 hours?</li>
<ul>
<li>Deploy the site to a droplet on digital ocean and create the kanban board with user stories and developer tasks.</li>
</ul>
<li>Are there any impediments?</li>
<ul>
<li>None</li>
</ul>

<br/>
James:
<li>What did you do in the last 24 hours?</li>
<ul>
<li> I created tests for our API implementation and developed a function following TDD procedures. </li>
</ul>  
<li>What will you do in the next 24 hours?</li>
<ul>
<li> I will continue to build out API price functionality and integrate with our front end. </li>
</ul>  
<li>Are there any impediments?</li>
<ul>
<li>As the product owner, I need to adjust our backlog items to include front end HTML/CSS for a homepage, at minimum</li>
</ul>

<br/>
Gabe:
<li>What did you do in the last 24 hours?</li>
<ul>
<li> I wrote unit tests for user registration and login; I tested and merged our API app for requesting data from glassnode.com </li>
</ul>  
<li>What will you do in the next 24 hours?</li>
<ul>
<li> I will participate in sprint planning and get started on my next assigned task (probably building out the API more) </li>
</ul>  
<li>Are there any impediments?</li>
<ul>
<li>No impediments at the moment</li>
</ul>

<br/>
Folake:
<li>What did you do in the last 24 hours?</li>
<ul>
<li> I have not worked on sprint tasks in the last 24 hours. </li>
</ul>  
<li>What will you do in the next 24 hours?</li>
<ul>
<li> I do not plan on working on sprint tasks in the next 24 hours. </li>
</ul>  
<li>Are there any impediments?</li>
<ul>
<li>None</li>
</ul>


### Pair Programming Proof
Gabe and James had a productive session on Wednesday!
![teamProgramming](https://user-images.githubusercontent.com/65990764/141510468-8f29d1cc-a047-4557-b4aa-b717a7e9288b.JPG)

### Sprint Review - Stakeholder Present
Jack owns cryptocurrency, we showed him our product increment from the first sprint. Due to his feedback, we chose to add a homepage HTML/CSS item to our backlog, because it was clear we didn't have that built yet.
We completed zero of ten story points. In our next sprint, we plan on communicating more, and working on more specific product backlog items, that better align to our goals.
![Capture](https://user-images.githubusercontent.com/65990764/141836922-f7178234-2d76-430f-ac58-045ca7e550b5.JPG)

### Sprint Retrospective - Resulting Action Item
![image](https://user-images.githubusercontent.com/65990764/141837677-38f4ed75-1bbc-40f1-b0fe-e915d6a54fe6.png)

### Working Software for Product Increment
We made our site publicly accessible. Please visit: [Fortune Teller](http://143.198.157.232:8080/)

### Building Test First (Examples of 10 miro-scale unit tests that pass)
Credit to Raul for these passing tests.
![image](https://user-images.githubusercontent.com/65990764/141837913-c085e46a-6da3-4d8d-83f3-ead908379329.png)

Credit to Gabe for these passing tests.
![image](https://user-images.githubusercontent.com/14114255/141843850-83cb26db-ea5d-4cfc-b5a1-0f41140207a4.png)
![image](https://user-images.githubusercontent.com/65990764/141842960-2ae47461-b494-43da-84af-9d517995c3c7.png)

Credit to James for these passing tests.
![image](https://user-images.githubusercontent.com/65990764/141842920-60fc0610-d3c2-48e2-9f52-92b91cce08b5.png)

--------

