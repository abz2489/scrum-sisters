# Scrum Sisters

# **Introduction**
Scrum Sisters is an app for users to find women and girls rugby teams in South Wales. The app serves as a solution to a problem that I had when finding women's teams in my area. There are a wealth of rugby clubs in South Wales, but not all of them have female teams. When I was looking for a local team to play for, I found that information I did find was often wrong. Scrum Sisters allows users to register an account, with which they can add a team to the database, edit their team's information and delete the team altogether. Visitors to the Scrum Sisters website will be able to find teams and view the teams profile only.


# **UX/UI**
## **Strategy**

### **Project Goals**
- Allow visitors to the site to find their local female rugby teams.
- Allow visitors to register an account.
- Allow account holders to add, edit and delete teams.

### **User Stories**
Non-account holders
- As a user with no account, I want to find teams easily.
- As a user with no account, I want to find contact information for the team.
- As a user with no account, looking for girls teams I want to find the age range of the girls teams.
- As a user with no account, I want to find the training location details.
- As a user with no account, I want to find training days and times for the team.
- As a user with no account, I want to easily register an account.

Account holders
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
- Teams nav link
- Register nav link
- Sign in nav link

**Navigation Bar** - When User Registered and Singed In
- Scrum Sisters logo
- Teams nav link
- My Teams nav link
- My account nav link
- Sign Out nav link

**Footer**
- Link to GitHub
- Link to LinkedIn
- Project for educational purposes disclaimer

**Home Page**
- Nav Bar
- Footer
- Hero image (to be chosen)
- Button to view teams under hero image
- Teams carousel
- Prompt to register

**Teams Page**
- Teams Title
- Grid tiles of teams
- View Profile button for each tile
- Pagination
    - 5 teams per page for mobile
    - 9 teams per page for tablet
    - 12 teams per page for desktop

**Team Profile**
- Team Name
- Club Name
- Age Group
- Training Days & Times
- Training location
- Social media links
- Edit button (available for team admin)
- Delete button (available for team admin)
    - Modal pop up to confirm deletion

**Registration Page**
- Form
- First Name
- Last Name
- Email
- Check if email exists
- Error message for invalid email
- Error message for existing Username
- Password (min 8 characters)
- Hashed using Werkszeug
- Error message for invalid password
- Confirm Password
- Submit button
- POST method

**Sign In Page**
- Form
- Email
- Password
- Sign In Button
- Checks Username and hashed Password match
- On successful sign in direct to My Teams page
- Link to Registration page

**My Account Page**
- Displays user's details
- Full Name
- Email address
- Option to change details.
- Option to delete account.
    - Modal pop up to confirm deletion

**My Teams Page** (available to account holders only)
- My Teams tile
- Grid tiles of user teams
- Team Name
- Edit button
- Delete button
    - Modal pop up to confirm deletion
- Empty tile at the end of the grid with Add Team button

**Add Team Page** (available to account holders only)
- Form
- Team Name
- Club Name
- Age group - dropown selection
- Training days - multiple selection
- Training time - dropdown selection
- Training location
- Social media URL 

### Future Features
- Introduce Clubs
    - Club and Users have one to one relationship
    - Club and Teams have one to many relationship


## Structure

**Site Structure**
![Structure mind map](readme-images/ss-structure.png "Site Structure Map")

**Relational Database Structure**
![Structure mind map](readme-images/ss-db-relational.png "Site Structure Map")

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
Training days will also be pre populated in the database. Users will be able to select more than one option as many teams train more than once a week.


## Skeleton


<details>
<summary>Homepage</summary>
<details>
<summary>Mobile</summary>

![Mobile](readme-images/wf-homepage-mobile.png)
</details>
<details>
<summary>Desktop</summary>
*Enter Link Here*

</details>
</details>

<details>
<summary>Register</summary>
<details>
<summary>Mobile</summary>

![Mobile](readme-images/wf-register-mobile.png)
</details>
<details>
<summary>Desktop</summary>
*Enter Link Here*

</details>
</details>

<details>
<summary>Sign In</summary>
<details>
<summary>Mobile</summary>

![Mobile](readme-images/wf-signin-mobile.png)
</details>
<details>
<summary>Desktop</summary>
*Enter Link Here*

</details>
</details>

<details>
<summary>My Teams</summary>
<details>
<summary>Mobile</summary>

![Mobile](readme-images/wf-my-teams-mobile.png)
</details>
<details>
<summary>Desktop</summary>
*Enter Link Here*

</details>
</details>

<details>
<summary>Teams</summary>
<details>
<summary>Mobile</summary>

![Mobile](readme-images/wf-teams-mobile.png)
</details>
<details>
<summary>Desktop</summary>
*Enter Link Here*

</details>
</details>

<details>
<summary>Team Profile</summary>
<details>
<summary>Mobile</summary>

![Mobile](readme-images/wf-team-profile-mobile.png)
</details>
<details>
<summary>Desktop</summary>
*Enter Link Here*

</details>
</details>

<details>
<summary>Add Team</summary>
<details>
<summary>Mobile</summary>

![Mobile](readme-images/wf-add-team-mobile.png)
</details>
<details>
<summary>Desktop</summary>
*Enter Link Here*

</details>
</details>

<details>
<summary>My Account</summary>
<details>
<summary>Mobile</summary>

![Mobile](readme-images/wf-my-account-mobile.png)
</details>
<details>
<summary>Desktop</summary>
*Enter Link Here*

</details>
</details>