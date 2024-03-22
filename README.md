# <p style="text-align: center; font-size: 40px;">**Scrum Sisters**</p>

![](testing/readme-images/ss-am-i-responsive.png)

[View the Scrum Sisters live website here](https://scrum-sisters-f6136ef90930.herokuapp.com/)

# **Introduction**
Scrum Sisters is an app for users to find women and girls rugby teams in South Wales. The app serves as a solution to a problem that I had when finding women's teams in my area. There are a wealth of rugby clubs in South Wales, but not all of them have female teams. When I was looking for a local team to play for, I found that information I did find was often wrong. Rugby clubs can are encouraged to register an account and upload all their female teams. Visitors to the Scrum Sisters website will be able to find teams and view the teams profile information. 


# **UX/UI**
## **Strategy**

### **Project Goals**
- Allow visitors to the site to find their local female rugby teams.
- Allow visitors to register an account.
- Allow account holders to add, edit and delete teams.

### **User Stories**

**Non-account holders**
- As a user with no account, I want to find teams easily.
- As a user with no account, looking for girls teams I want to find the age range of the girls teams.
- As a user with no account, I want to find the training location details.
- As a user with no account, I want to find training day and time for the team.
- As a user with no account, I want to easily register an account and sign in.

**Account holders**
- As a user with an account, I want to be able to sign into my account easily.
- As a user with an account, I want to be able to edit my account details easily.
- As a user with an account, I want to be able to delete my account easily.
- As a user with an account, I want to be able to upload a team.
- As a user with an account, I want to be able to edit my team information.
- As a user with an account, I want to be able to delete my team.
- As a user with an account, I want to be able to sign out of my account.
- As a user with an account, I want to add links to my team's social media.


## Scope
### Features

Responsive design for use on mobile, tablet and desktops.

**Navigation Bar** - No account or not signed in
- Scrum Sisters logo
- Home nav link
- Teams nav link
- Register nav link
- Sign in nav link

**Navigation Bar** - When User Registered and Signed in
- Scrum Sisters logo
- Teams nav link
- Profile nav link
- Sign Out nav link

**Footer**
- Copyright
- Project for educational purposes disclaimer

**Home Page**
- Nav Bar
- Footer
- Hero image of Pink Rhinos scrum.
- Button to view teams under hero image
- Teams carousel - teams carousel was removed along with the decision to include profile pictures
- Prompt to register

**Teams Page**
- Teams Title
- Grid tiles of teams
- View Profile button for each tile - Amended to using card reveal
- Pagination - Moved to future features

**Registration Page**
- Form
- First Name
- Last Name
- Email
- Check if email exists
- Error message for invalid email
- Error message for existing Username - No longer necessary as using first and last name.
- Password (min 8 characters)
- Password Hashed using Werkszeug
- Confirm Password
- Select Rugby club
- Submit button
- POST method

**Profile Page** accessible only to the registered/logged in users
- Displays user's details
- Full Name
- Email address
- Option to change details.
- Option to delete account.
    - Modal pop up to confirm deletion
- My Club section with hyperlink to club page

**Club Page** accessible only to the logged in users
- Displays teams that come under the club
- Add team button for user's to add new teams

**Team Profile** - accessible only to the logged in users
- Team Name
- Club Name
- Age Group
- Training Days & Times
- Training location
- Social media links
- Edit button 
- Delete button
    - Modal pop up to confirm deletion

**Sign In Page**
- Form
- Email
- Password
- Sign In Button
- Checks Username and hashed Password match
- On successful sign in direct to Profile page
- Link to Registration page

**Team Profile** accessible only to the registered/logged in users
- Team Title
- Display team info
- Team Name
- Age Group
- Training Day
- Training Time
- Training Location
- Edit button
- Delete button
    - Modal pop up to confirm deletion

**Add Team Page** accessible only to the registered/logged in users
- Form
- Team Name
- Club Name - already populated from user data
- Age group - dropown selection
- Training days - drowpdown selection
- Training time
- Training location
- Social media URLs
- User id - already populated from user data 

**Edit Team Page** accessible only to the registered/logged in users
All data will be pre-populated from previously filled out data.
- Form
- Team Name
- Club Name - already populated from user data
- Age group - dropown selection
- Training days - drowpdown selection
- Training time
- Training location
- Social media URLs
- User id - already populated from user data 

### Future Features
- Profile pictures for clubs & teams
- Public profile page with team news, fixture updates and announcements.
- Coach and player registration with coach/player profiles.


## Structure

**Site Structure**
![Structure mind map](testing/readme-images/ss-structure.png "Site Structure Map")

**Relational Database Structure**
![Structure mind map](testing/readme-images/ss-db-relational.png "Site Structure Map")

**Non Account Holders**
No account is needed to simply view teams and their profile. Scrum Sisters is designed for people to find teams suitable to them. It's important that this is as easy to achieve as possible for visitors.

**Users**
An account is needed if a user wishes to upload a team to Scrum Sisters. Upon completion of the registration form, the user will need to select a rugby club from the list provided. This user acts as an admin for the club and its teams. Each club can have one user and a user can only have one club.
Other details include first name, last name, email and password.

**Clubs**
All South Wales rugby clubs will be entered into the clubs table at the development stage to avoid any duplicate entries due to user error.
This will display to the user as a dropdown box on the registration page.

**Teams**
Clubs can have many teams. The teams database will hold the team name, club id, age group, training days, training time, training location and URL to social media pages.

**Age Group**
The age groups, like the clubs will be pre populated within the database to ensure uniformity in catergories. For example if one user was to enter "under 15s" and another "U15s", finding the right age group as a visitor will become much more complicated.

**Training Days**
Training days will also be pre populated in the database.


## Skeleton


<details>
<summary>Homepage</summary>
<details>
<summary>Mobile</summary>

![Mobile](testing/readme-images/wf-homepage-mobile.png)
</details>
<details>
<summary>Desktop</summary>

![Desktop](testing/readme-images/wf-homepage-desktop.webp)

</details>
</details>

<details>
<summary>Register</summary>
<details>
<summary>Mobile</summary>

![Mobile](testing/readme-images/wf-register-mobile.png)
</details>
<details>
<summary>Desktop</summary>

![Desktop](testing/readme-images/wf-register-desktop.webp)

</details>
</details>

<details>
<summary>Sign In</summary>
<details>
<summary>Mobile</summary>

![Mobile](testing/readme-images/wf-signin-mobile.png)
</details>
<details>
<summary>Desktop</summary>

![Desktop](testing/readme-images/wf-signin-desktop.webp)

</details>
</details>

<details>
<summary>My Teams</summary>
<details>
<summary>Mobile</summary>

![Mobile](testing/readme-images/wf-my-teams-mobile.png)
</details>
<details>
<summary>Desktop</summary>

![Desktop](testing/readme-images/wf-my-teams-desktop.webp)

</details>
</details>

<details>
<summary>Teams</summary>
<details>
<summary>Mobile</summary>

![Mobile](testing/readme-images/wf-teams-mobile.png)
</details>
<details>
<summary>Desktop</summary>

![Desktop](testing/readme-images/wf-teams-page-desktop.webp)

</details>
</details>

<details>
<summary>Team Profile</summary>
<details>
<summary>Mobile</summary>

![Mobile](testing/readme-images/wf-team-profile-mobile.png)
</details>
<details>
<summary>Desktop</summary>

![Desktop](testing/readme-images/wf-team-profile-desktop.webp)

</details>
</details>

<details>
<summary>Add Team</summary>
<details>
<summary>Mobile</summary>

![Mobile](testing/readme-images/wf-add-team-mobile.png)
</details>
<details>
<summary>Desktop</summary>

![Desktop](testing/readme-images/wf-add-team-dektop.webp)

</details>
</details>

<details>
<summary>My Account</summary>
<details>
<summary>Mobile</summary>

![Mobile](testing/readme-images/wf-my-account-mobile.png)
</details>
<details>
<summary>Desktop</summary>

![Desktop](testing/readme-images/wf-my-account-desktop.webp)

</details>
</details>

## Surface
### **Colour Scheme**

<img src="testing/readme-images/ss-colour-scheme.webp" height="400"/> 

### **Typography**
All typography for the project has been sourced from [Google Fonts](https://fonts.google.com/).

#### **Scrum Sisters Logo**
Ostrich Sans Inline Regular & Ostrich Sans Light

#### **All other content**
Karla - used on all headings
Merriweather Sans - used for all other text

# **Features**

# **Technologies Used**

## **Languages**
[HTML5](https://en.wikipedia.org/wiki/HTML5)

[CSS3](https://en.wikipedia.org/wiki/CSS)

[Python](https://www.python.org/)


## **Frameworks, libraries & programs**
[Flask](https://flask.palletsprojects.com/en/3.0.x/) Python framework.

[Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/) used for database interaction with PostgreSQL.

[Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/) used for database migrations throughout the project.

[Flask Login](https://flask-login.readthedocs.io/en/latest/) used for user log in.

[Random Keygen](https://randomkeygen.com/) used to randomise a fort knox password used for the secret key.

[PostgreSQL](https://www.postgresql.org/) used for the relational database.

[Materialize CSS](https://materializecss.com/) CSS framework.

[Materialize Design](https://fonts.google.com/icons) used with Materialize CSS.

[jQuery](https://jquery.com/) used with Materialize CSS.

[Git](https://git-scm.com/) used for version control. I used the terminal and git commit/push commands and the source control panel.

[GitHub](https://github.com/) used as storage for the Scrum Sisters repository.

[Google Fonts](https://fonts.google.com/) used to import all fonts used on the website.

[Font Awesome](https://fontawesome.com/) used for social media icons used in team profiles.

[Coolors](https://coolors.co/) used to build the colour palette.



# **Deployment**
ScrumSisters live website was deployed using Heroku.

## **Local Deployment**

**How to Fork**
- Go to GitHub repository.
- In the top right of the screen, click the fork button.
- A form will appear, you can edit the name and description or keep it the same.
- Click the green "Create Fork" button.

**How to Clone**
- In the GitHub respository click the green Code button, that sits above the repository files.
- When the dropdown appears choose from HTTP, SSH or GitHub CLI.
- Click the copy button to the right of the URL to copy to your clipboard.
- Open Git Bash / terminal, make sure your current working directory is what you want to use for the cloned directory.
- Type ```git clone``` followed by ```https://github.com/abz2489/scrum-sisters.git``` into the terminal and press enter.
- If you're not using the Code Institute template then set up a virtual environment.
- Install packages from requirements.txt file by running ```pip3 install -r requirements.txt``` in the terminal.

## **Set up the PostgreSQL Database**
**Set up ElephantSQL account**
- Navigate to ElephantSQL.com and click "Log In".
- Log in as normal or sign up wit Github.
- You will be prompted to authorise ElephantSQL with your selected GitHub account. Click "Authorize ElephantSQL".
- A Create New Team form will appear. You will need to:
    - Add a Team Name
    - Read the Terms of Service and select "Yes" to agree.
    - Select "Yes" for GDPR and provide and email address.
    - Click "Create Team".

**Set up ElephantSQL database**
- Click the green "Create New Instance" button.
- Choose a name for your database.
- Select the Tiny Turtle (Free) plan.
- You can add tags or leave the tag field blank.
- Click "Select Region" and select your nearest data centre.
- Click "Review".
- Check the details of your instance before clicking "Create Instance" in the bottom right.
- Return to your ElephantSQL dashboard.
- Click you database instance name.
- In the URL section, copy your database URL to your clipboard by clicking the copy icon.

Click “Create New Instance”.
Set up your plan. (You can leave the 'tags' field blank.)
Select region.
Select a data center near you
Then click “Review”.
Check your details are correct and then click “Create instance”.
Return to the ElephantSQL dashboard and click on the database instance name for this project
In the URL section, clicking the copy icon will copy the database URL to your clipboard
Leave this tab open, we will come back here later

## **Heroku Deployment**
1. Create a requirements.txt file containing project dependencies. To do this run ```pip3 freeze > requirements.txt```
in the terminal.
2. Create a procfile with 'web: python run.py'. To do this run ```echo web: python run.py > Procfile``` in the terminal.
Double check the Procfile has no blank lines under content.
3. Commit changes to github repository.
4. Sign up or log in to Heroku. 
5. Click the 'New' button on the right and select 'Create New App'.
6. Enter app name (the chosen name needs to be unique) and select your nearest region. Click 'Create App'.
7. Click the 'Deploy' tab on your app dashboard.
8. In the 'Deployment Method' section click Github to connect. Search for your repository name and click 'Connect'.
9. Click 'Settings', navigate to the config vars section and click 'Reveal Config Vars'.
10. Enter the config vars from your env.py file:

    | Key         | Value                 |
    | ----------- | --------------------- |
    | IP          | 0.0.0.0               |
    | PORT        | 5000                  |
    | DB_URL      | ENTER_YOUR_DB_URL     |
    | SECRET_KEY  | ENTER_YOUR_SECRET_KEY |
    | DEBUG       | TRUE\*                |

    *The DEBUG variable can be deleted after debugging is finished. This is to avoid the situation of Debug mode accidentally being read as active or True by Heroku.
11. Click 'Deploy' tab.
12. You can now choose whether you prefer to allow 'Automatic Deploys' or to manually deploy each time you push changes to your repository. 

    **Automatic Deploys**
    - Navigate to 'Automatic Deploys' section and click 'enable automatic deploys'.

    **Manual Deploys**
    - Navigate to 'Manual Deploy' section and click 'Deploy Branch'
13. When the build is done, click the 'view' button to launch the app. Alternatively click 'open app' located at the top right.


# **Testing**
All tests can be found at [TESTING.md](TESTING.md).

# **Credits**

## **Content**
All content on the Scrum Sisters website was written by myself.

[WRU Official Website](https://community.wru.wales/?utm_source=website&utm_medium=header%20link&utm_campaign=Community%20Site) for information on local teams and hubs.

## **Media**
[Nia Anwen Photography](https://www.facebook.com/niaanweneventphotography/) official photographer at Llantwit Fardre RFC for allowing me to use the fantastic image of the girls mid scrum for my hero image.

## **Code**
[Codemy Youtube Channel](https://www.youtube.com/playlist?list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz) This channel helped me understand and grasp Flask much better. I particularly found the Flask Login and Flask Migrate videos.

[W3Schools](https://www.w3schools.com/howto/howto_css_overlay.asp) used to refresh on css overlays.

## **Acknowledgments**
Cohort facilitator Iris Smok for all her help and support with our cohort.