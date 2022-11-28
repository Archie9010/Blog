# Beautiful Castles 

Welcome to [BlogSeed ](https://blog-archie.herokuapp.com) A place where we can share our experiences and learn from one another. Encourages freedom of speech and open discussion to spark new ideas. Helps build friendships with people from all around the world, and make new ones along the way. Blog about anything that interests you, whether it's travel, food or hobbies it's up to you!
Our blog is a place for people of all walks of life to come together and share their stories. Share your thoughts with complete freedom, without fear. It's a safe space for everyone. Building friendships and traveling the world is just one of the amazing things we do. We are all about nourishing our minds and bodies, so you can find posts about food, hobbies or even mindfulness for your mental health!

![mockup](blog/images/mockup.png)

## Index 
* [Technologies Used](#technologies-used)
* [Fearures](#features)
* [Contact](#contacts)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## Technologies Used

 * [HTML5](https://en.wikipedia.org/wiki/HTML5)
 * [CSS](https://en.wikipedia.org/wiki/CSS)
 * [Bootsrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework))
 * [Django/allauth](https://en.wikipedia.org/wiki/Django_(web_framework))
 * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
 * [Cloudinary](https://en.wikipedia.org/wiki/Cloudinary)
 * [Heroku](https://en.wikipedia.org/wiki/Heroku)
 * [Chrome](https://en.wikipedia.org/wiki/Google_Chrome)
 * [Stack Overflow](https://en.wikipedia.org/wiki/Stack_Overflow)
 * [Multi Device Website Mockup Generator](https://techsini.com/multi-mockup/index.php)
 * [Pep8](https://pypi.org/project/pep8/)
 * [W3school](https://en.wikipedia.org/wiki/W3Schools)
 * [Git](https://en.wikipedia.org/wiki/Git) 
 * [Github](https://en.wikipedia.org/wiki/GitHub)
 * [Gitpod](https://www.gitpod.io/docs/introduction) 

 ## Wireframe
The wireframe model is created as part of the project planning. Its task is to graphically present the appearance of the application on three different devices: computer - high resolution, tablet - medium resolution, mobile - low resolution. The application will be built on the basis of the created sketch.

### Landing Page
![home](blog/images/home.png)
### Landing Page Medium 
![home](blog/images/home_md.png)
### Landing Page Small
![home](blog/images/home_sm.png)

## Post Details Page

### User Post Details Large
![profile](blog/images/profile_lg.png)
### User Post Details Medium 
![profile](blog/images/profile_md.png)
### User Post Details Small
![profile](blog/images/profile_sm.png)

## Login 

### Login Large
![login](blog/images/login_lg.png)
### Login Medium
![login](blog/images/login_md.png)
### Login Small
![login](blog/images/login_sm.png)

## Features

### Navigation Bar

* Featured at the top of the page, The navigation shows the page name in the left corner: My Blog that links to the Home page. When hovered over, Categories, Add Post, Add Category and Logout menu changes color for easy navigation.
* Featured on all three pages, the full responsive navigation bar includes links to, Home page, Register or Login. When logged in includes: Categories, Add post, Add Category and User First and last name displayed on the left site of the navbar with options to edit profile, edit settings, show profile page and logout. 

### Menu Logged In
![Menu Logged In](blog/images/menu_login.png)

### Menu Logged Out
![Menu Logged Out](blog/images/menu_logout.png)

### Menu Current user
![Menu Logged Out](blog/images/menu_user.png)

### Register Page

* Register is a section created for users to easily and efficiently create an account on our page. Register form is responsive to all screen sizes.

![register](blog/images/register_user.png)

### Login Page 

* Login page form allows user to login into user account

![Login](blog/images/login_page.png)

### Change Password

* Change password form allows user to update ppassword.

![Change Password](blog/images/change_password.png)

### Change User Details

* Change User Details allows user to updated details on his profile.

![Change User Details](blog/images/change_user_details.png)

### Add Post

* Add post allows user to post articles. 

![Add Post](blog/images/add_post.png)


## Testing

### Functionality

### Manual Testing
   
| Test Label         |            Test Action           |         Expected Outcome           | Test Outcome    |
|:------------------ |:---------------------------------|:-----------------------------------|:----------------|
| Menu Test          |  Responsive Nav bar              | Navigate to the desired page.      | PASS            |
| Edit/Delete post   |  Responsive Button               | Navigate to external websites      | PASS            |
| Login button (form)|  Responsive Login button.        | Navigates to home page             | PASS            |
| Register           |  Responsive Register button      | Navigates to home page             | PASS            |
| Social media links |  Responsive Social media icons   | Navigate to social media websites  | PASS            |
| Login/Logout       |  Responsive Nav bar              | Allows to log in and out           | PASS            |
| Add post           |  Responsive User page            | Navigate to add post section       | PASS            |
| Add category       |  Responsive Nav bar              | Allows to add new category         | PASS            |
| Add comment        |  Responsive User page            | Allows to add new comment          | PASS            |
| Search by cat      |  Responsive User page            | Allows user to search by categories| PASS            |
| Edit details       |  Responsive User page            | Navigates to edit details page     | PASS            |
| Edit Settings      |  Responsive User page            | Navigates to edit settings page    | PASS            |
| Show profile       |  Responsive User page            | Navigates to user profile page     | PASS            |       
| Edit/Delete post   |  Responsive User page            | Allows to delete/edit post         | PASS            |


### Performance Test 
  ![Performance](blog/images/performance.png)

### Browser Compatibilit

* Chrome  - Pass
* firefox - Pass 
* Safari - Pass 
* Edge  - Pass 

### Bugs

* 

### Validator Testing

* HTML
  - Code pass W3C HTML without errors

* CSS
  - Code pass W3C CSS without errors

* PEP8 
  - Code pass PEP8 without critical errors

* Accessibility
  - Colors and fonts chosen are easy to read and accessible by running it through lighthouse in dev tools.


## Deployment


### Publishing 

The project was deployed using Heroku. The process is as follows:

Once you have signed up to Heroku, on the top right of the dashboard there is a button labelled 'New'. This will open a dropdown; please select 'Create new app'. On the next page you can choose your region and a name for the project. Then click 'Create app'.

On the next page there is a menu along the top. Navigate to 'Settings', where you will find the config vars. Scroll down to the section named 'Config vars' and click on the button labelled 'Reveal config vars'. Cloudinary (AWS?) and Postgres will both need config vars as per your own details. You will also need to set a secret key. Once the config vars are saved, back in Gitpod save them in an env.py file. Make sure to add env.py to your .gitignore list so that your config vars do not become publically available on Github.

If you scroll back to the top of the page you will find the 'Deploy' tab, which has multiple options for deployment. I used Github for this project. When you click on the Github button a bar will come up for you to search for the repo you wish to connect to.

Once you have connected, you have the option to deploy automatically (the app will update every time you push) or manually (update only when you choose). I chose automatic but you can do what suits you.

After the first push/update, your app will be ready to go!



### How to clone the repository

* Go to the https://github.com/Archie9010/Blog repository on GitHub
* Click the "Code" button to the right of the screen, click HTTPs and copy the link there
* Open a GitBash terminal and navigate to the directory where you want to locate the clone
* On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process

The site was deployed to Heroku. The steps to deploy are followed:
* Push the latest code to GitHub.
* Go to Heroku
* Select new in the top right corner.
* Create a new app.
* Enter the app name and select Europe as the region.
* Connect to GitHub.
* Search for repo-name.
* Select connect to the relevant repo you want to deploy.
* Select the settings tab.
* Add buildpack
* Select Python, then save changes.
* Make sure Heroku/Python is at the top of the list, followed by Heroku/Nodejs
* Navigate to the deploy tab
* Scroll down to Manual Deploy and select deploy branch.

Live link: [BlogSeed](https://blog-archie.herokuapp.com/)


## Credits

* Heroku deployment instructions from Code Institute
* Hello Django and Django blog from code institute
* Stack overflow to support debugging 
* Youtube Tutorials 
* CI Tutor Support for Help with code
* [Bootstrap documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
* [Django documentation](hhttps://docs.djangoproject.com/en/4.0/)
* The code was inspiered by PP4 DjangoBlog.
* Post Display on landing page inspiered by CodeStar Blog by Code Insitute 
* CSS Background Pattern was taken from [CSS Background Website](https://www.magicpattern.design/tools/css-backgrounds)
* Brian Macharia- Mentor support, guidance, tips, and key things to look out for throughout the project.

### Content

* Navbar and Forms styles was taken from Bootsrap and Django
* Pictures were downloaded from Pexele
* All other content was written by the developer




