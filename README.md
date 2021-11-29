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

**Sprint Goal:** Have a website with a working homepage (both front-end and back-end) that displays current cryptocurrency data.

Value this sprint will bring: This sprint will be valuable becuase we have a much better understanding of the amount of work we can deliver compared to the last sprint. We also forecasted a lot better this sprint compared to the last and our sprint goal is more attainable.  

Jira Product Backlog: [JIRA-URL](https://vuca-nators.atlassian.net/jira/software/projects/FT/boards/1/backlog)

### Forecast
In this sprint we forcasted 13 story points. The rationale for this forecast was that we had a lot of user stories carried over from the previous sprint but these user stories had started to be worked on already. We added only 3 more story points with the assumption that the majority or all of the work from the previous sprint would get completed.

We pulled stories into our sprint 2 backlog and only developers participated in this activity. (Based on our scrum team roles becuase our team has everyone in the role of a developer this included the whole team). 

Our sprint backlog where the aggregate size of the stories does not exceed our forecast(the size of each backlog item is less than half the forecast velocity for this sprint): https://vuca-nators.atlassian.net/jira/software/projects/FT/boards/1/backlog  

We decomposed user stories into developer tasks:

![image](https://user-images.githubusercontent.com/64049629/143790423-7058affa-fd9f-45b6-a441-3fb166b60318.png)
  
### Sprint Burdown Chart

An initial view of our sprint burdown chart
![image](https://user-images.githubusercontent.com/64049629/143729109-ded25b36-d463-45bd-81c9-4538e06725f8.png)

    
The initial view of our Sprint Board/Kanban Board before it was updated: 
![image](https://user-images.githubusercontent.com/64049629/143729267-eaae767e-1705-4e18-82e6-543689025a5b.png)


URL of the current board(end of this sprint):https://vuca-nators.atlassian.net/jira/software/projects/FT/boards/1
  


### Daily Scrums(Sample)
Outcome from Daily Scrum meeting
![image](https://user-images.githubusercontent.com/64049629/143728837-75d74aaf-d103-48a9-8c83-021afcdc3915.png)

### What did you do since our last meeting?

<ul>
<li> 
Raul: Working on the code from ticket FT-27 to remove the static data in the front end. Fixing the JSON to get it working properly.
</li>
<li>
Rachel: Worked on setting up the CI/CD pipeline with test, build and deploy in the workflow .yaml files.
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

An update of our sprint 2 burndown chart
![image](https://user-images.githubusercontent.com/64049629/143729028-203697fc-1e6e-4cbf-9628-802b84ca40a1.png)

An update of our Sprint board/Kanban board
![image](https://user-images.githubusercontent.com/64049629/143729456-aef1ee47-2834-48b4-8ca7-c40438c4370e.png)

### Pair and Mob Programming

Our productive mob programming session on Tuesday, Nov. 23rd with James, Rachel, Gabe, and Raul.
![image](https://user-images.githubusercontent.com/64049629/143620114-dc742fab-3f06-44f6-bdf5-27256f9f1693.png)
![GroupProgramming](https://user-images.githubusercontent.com/65990764/143922094-d99ffa85-7cc5-4a01-85e9-ceeb58d5f9d4.JPG)

Folake and Rachel met for Pair programming on Thursday, Nov. 25th to work on the front end. 
![image](https://user-images.githubusercontent.com/64049629/143627694-7a5028c9-9e60-474b-93f3-56d959d3b9bb.png)

Mob Programming on Nov. 27th at 6pm
![image](https://user-images.githubusercontent.com/64049629/143728956-53b39cd0-b87d-45db-97eb-f598738dbc69.png)

### Test-Driven Development

Our work currently has 20 unit tests and they all pass: (Evidence showing that they pass) 
![image](https://user-images.githubusercontent.com/64049629/143921214-4185bad4-4a11-43ef-b450-df60c25f38a7.png)


URLs to all of the tests in the vuca-nators repository:

<li>
  https://github.com/gabemansur/vuca-nators/blob/main/fortuneteller/app/tests.py
<li/>
<li>
 https://github.com/gabemansur/vuca-nators/blob/main/fortuneteller/app/test/tests_api.py
<li/>
<li>
 https://github.com/gabemansur/vuca-nators/blob/main/fortuneteller/app/test/test_views.py
<li/>
<li>
 https://github.com/gabemansur/vuca-nators/blob/main/fortuneteller/app/test/test_urls.py
<li/>
<li>
 https://github.com/gabemansur/vuca-nators/blob/main/fortuneteller/app/test/test_models.py
<li/>
<li>
  https://github.com/gabemansur/vuca-nators/blob/main/fortuneteller/app/test/test_forms.py
<li/>
  
### Continuous Integration and Continuous Deployment 
<ul>
  <li>
    A Continuous Integration system running: The full CI file is here: https://github.com/gabemansur/vuca-nators/actions/runs/1513591623/workflow
  </li>
  <li>
    The CI workflow is triggered everytime code is pushed to either the main/trunk/master branch or for all branches that are not main.
  </li>
  <li>
    The CI system automatically executes tests:https://github.com/gabemansur/vuca-nators/actions/runs/1513591623
  </li>
</ul>

![image](https://user-images.githubusercontent.com/64049629/143787298-82bc336c-05dd-4494-a9a8-5571d53d974d.png)

<ul>
  <li>
    You have a Continuous Delivery system running: The full CD file is here: https://github.com/gabemansur/vuca-nators/actions/runs/1513591625/workflow
  </li>
   <li>
    When the build is green the CD system deploys code to production: https://github.com/gabemansur/vuca-nators/actions/runs/1513607021
  </li>
  <li>
    The production is not altered: The build will stop and not deploy to production if the tests do not pass: https://github.com/gabemansur/vuca-nators/actions/runs/1513527306. If the build passes the the deploy will continue running. 
  </li>
  <li>
    Evidence that the CI and CD system exists and behaves properly:
  </li>  
</ul>

![image](https://user-images.githubusercontent.com/64049629/143787261-b83fc30c-2b1e-437c-9d95-baa94b0bcd7b.png)

![image](https://user-images.githubusercontent.com/64049629/143787298-82bc336c-05dd-4494-a9a8-5571d53d974d.png)

![image](https://user-images.githubusercontent.com/64049629/143787322-62cd802e-8150-400a-90d2-ee6bb9b0532e.png)

![image](https://user-images.githubusercontent.com/64049629/143787351-649169e4-6896-46f1-97a4-5a1dba71542d.png)

![image](https://user-images.githubusercontent.com/64049629/143787378-11bbf29f-d225-43bd-b30b-32733693e821.png)


### Product Increment
The URL of the working software: http://143.198.157.232:8080
  
### Sprint Review
We conducted a sprint review on Nov. 28th at 7pm.

Evidence of our sprint review with our stakeholder present:
(I, James did not save the screenshot with our stakeholder. Here is textual evidence.)
Slack:
![image](https://user-images.githubusercontent.com/65990764/143920685-47df35b4-28b4-47bd-b40a-0afbf99b596d.png)
Our Stakeholder, Jack, confirming attendance:
![Screenshot_20211129-131131_Message+ 4116](https://user-images.githubusercontent.com/65990764/143921223-c3335826-c5e7-40d2-af82-e701cda6afcf.jpg)


### Sprint Retrospective with Improvement Plan for next sprint
  
We conducted a sprint retrospective on Nov. 28th at 7pm, right after the sprint review. (Please note we left the sprint open on Jira and did not select "Complete Sprint" for grading purposes.) Evidence of our sprint retrospective team meeting:

![image](https://user-images.githubusercontent.com/64049629/143826542-e895cad2-2ac4-492a-98fc-2b2431597230.png)


As a team we identified at least one helpful change to improve our effectiveness together. We created a concrete plan/activty to make this change for the next sprint. To accomplish this plan each team member listed answers for the following to pinpoint impediments needed to be corrected for the next sprint:
  
#### What went well this sprint?
  
<ul>
  <li> 
    Raul:  
  </li>
  <li>
    Rachel: We accomplished more user stories this sprint. Our communication as a team has improved a lot as well.   
  </li>
  <li>
    James: Our communication and problem solving was much stronger than last sprint! Really good!
  </li>
  <li>
    Gabe: Communication and overall organization was much better this sprint. This was a big weakness last sprint and I think we did a good job recognizing that and making corrections. We also completed more story points than the previous sprint.
  </li>
  <li>
    Folake: This sprint I was able to complete what I had proposed to do. I was able to finish the front end portion of the index page with the requirements/requests made by my group members. I think we also met more times this week, and did both pair and mob programming which helped to facilitate in overall more efficient project growth.
  </li>
</ul>
  
#### What did not go well this sprint?
  
  
  <ul>
  <li> 
    Raul:  
  </li>
  <li>
    Rachel: We did not focus as much on code integrations and functionality of different parts.  
  </li>
  <li>
    James: We struggled to integrate elements, and started integrating them a bit late. 
  </li>
  <li>
    Gabe: While I think we did a good job communicating and problem-solving, actually integrating the separate pieces we were working on was a bit of a challenge. 
  </li>
  <li>
    Folake: I was not able to integrate the API/back end portion of the index page onto the site. 
  </li>
</ul>
  
#### Ideas/Improvements: How could we do things differently?
  
  <ul>
  <li> 
    Raul:  
  </li>
  <li>
    Rachel: More mob programming or communication on code as its being built that way the whole team is aware of all the moving parts. 
  </li>
  <li>
    James: I would like to schedule mob programming for integrating our work early on, then build the functionality out in a working frame. (We tended to build out functions first then try to integrate them in). 
  </li>
  <li>
    Gabe: I think having some higher-level discussions about how the various elements of our product will work together, and having a clearer shared vision of the end product are important. As others mentioned, mob programming was really helpful this sprint and we should definitely aim for more of that. 
  </li>
  <li>
    Folake: Collectively, I think sticking to our backlog helped us this week better flesh out what tasks needed to be done. Additionally, it helped to administer accountability. 
  </li>
</ul>
  
Our sprint retrospective action item added to the top of the product backlog for sprint 3: We aim to share a crystal clear product vision and integrate our work proactively.

