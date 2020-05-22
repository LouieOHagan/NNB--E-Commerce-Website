
<h1 align="center">NNB Responsive E-Commerce Website Project</h1>

NNB is an ecommerce store selling general electronic devices. The main part of their product assortment is prebuilt Desktop PC’s, laptops and mobile phones but also stock an 
assortment of accessories for electronic devices.

Users are welcomed on the home page with an interactive image carousel styled slider to offer the users a link to check out items in the 3 main categories of the ecommerce store, 
tablets, laptops and mobile phones. There will also be a search bar with search functionality for users to search up specific items they are interested in. 

## User Experience (UX)

- ### User stories

- ### Design
    - #### Colour Scheme

    - #### Typography

    - #### Imagery

* ### Wireframes

## Features

### Current Pages & Features

### To Do List
#### MUST DO

#### IF HAVE TIME

###### Last Updated: 11:52am GMT - 19/04/20 

### Features Left to Implement
##### These are features that have not been added at the time of development due to various reasons such as time limitations.

## Database Schema

### Product App Models

#### ProductType

```
    'id': ID,
    'name': '...',
    'friendly_name': '...',
    'description': '...',
```

#### Product

```
    'id': ID,
    'category': '...',
    'name': '...',
    'product_code': '...',
    'product_description': '...',
    'price_original': '...',
    'price_current': '...',
    'in_stock': '...',
    'stock': '...',
    'image_1': '...',
    'image_2': '...',
    'image_3': '...',
    'image_4': '...',
    'image_5': '...',
```

#### ProductReview
```
    'id': ID,
    'user': '...',
    'display_name': '...',
    'product': '...',
    'rating': '...',
    'title': '...',
    'product_review': '...',
    'date_posted': '...',
```

### Checkout App Models

### Order
```
    'id': ID,
    'order_number': '...',
    'full_name': '...',
    'email_address': '...',
    'street_address1': '...',
    'street_address2': '...',
    'town_or_city': '...',
    'county': '...',
    'postcode': '...',
    'country': '...',
    'order_date': '...',
    'total': '...',
    'delivery_cost': '...',
    'grand_total': '...',
    'original_cart': '...',
    'stripe_pid': '...',
```

### OrderProduct
```
    'id': ID,
    'order': '...',
    'product': '...',
    'quantity': '...',
    'product_cost': '...',
```



## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used
1. [Django 3.0:](https://www.djangoproject.com/)
    - Django 3.0 was the primary framework used that the website was built off of.
1. [PostgreSQL:](https://www.postgresql.org/)
    - PostgreSQL was the database used for production in Heroku
1. [Heroku:](https://www.heroku.com/home)
    - Heroku was used deploy the website.
1. [Stripe:](https://stripe.com/)
    - Stripe was used for the payment system while checking out
1. [AWS:](https://aws.amazon.com/)
    - AWS was used to store all of the static and media files inside of an S3 Bucket.
1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/) 
    - Bootstrap was used for both the gird system along with some of its custom styling classes to assist with the development of the front end. 
    - I used bootstrap classes more than I would usually do as a result of time limitations.
1. [Bootstrap Better Nav:](https://github.com/bootstrapstudio/bootstrap-better-nav)
    - Bootstrap Better Nav was used to replace the default Bootstrap navbar collapse with an off-screen menu that slides in from the right.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts was used to import the 'Open Sans' font into the style.css file which is used on all pages throughout the project (bar the Navigation bar text)
1. [Hover.css:](https://ianlunn.github.io/Hover/)
    - Hover.css was used on some of the buttons to add an animation on hover (specifically buttons within the cart/checkout templates)
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used to add icons throughout the project for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - jQuery was used by Bootstrap but was also used to write the JavaScript that toggled classes for the sites search bar.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [Gitpod:](https://www.gitpod.io/)
    - Gitpod was the primary IDE used throughout the entirety of the project. 
1. [GitHub:](https://github.com/)
    - GitHub is used to store the project code after being pushed from Git.
    - The GitHub repository is also linked to Heroku which is automatically deployed when a new commit is pushed.
1. [Photoshop:](https://www.adobe.com/ie/products/photoshop.html)
    - Photoshop was used to create the logo, images in the README and to edit most images used on the site.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](https://github.com/LouieOHagan/NNB-E-Commerce-Website#wireframes) during the design process. 
1. [Screen to GIF](https://www.screentogif.com/)
    - Screen to GIF was used to record the screen to create GIF's to demonstrate a specific task in video for the README.md file.
1. [HTML Formatter](https://htmlformatter.com/)
    - HTML Formatter was used to beautify code to keep the code neat and easy to read. It was utilised as Beautify Cmd (Shift + Alt + F) in GitPod distorted the code in GitHub.

## Testing

**Note:** All Testing Information can be located in seperate [TESTING.MD File](https://github.com/LouieOHagan/NNB-E-Commerce-Website/blob/master/TESTING.md) due to length of content.

## Deployment

I took the following steps to deploy the project successfully to Heroku.
### Deploying by connecting Github to Heroku

1. Up to the top right of the screen I clicked the "New" Dropdown button and then clicked the dropdown and selected "Create new app".
2. I called the app "nnb-store" and set the region to "Europe".
3. Once my app was created, I chose my deployment method which was "Connect to GitHub".
4. After logging and authenticating my GitHub account, I typed the repository name in to the search bar in the "Connect to GitHub" section and searched for "NNB-E-Commerce-Website".
5. When the repository appeared, I clicked the "Connect Button"
6. Once connected, I selected my master branch in the "Automatic deploys" section and clicked "Enable Automatic Deploys" button to ensure that every time I push to GitHub the app is rebuilt and is always up to date with the latest code.
7. Afterwards I went back to my Gitpod workspace and in my CLI I created a requirements.txt so Heroku knows what dependecies need to be installed for the application to run by running the following command. `pip3 freeze > requirements.txt`.
8. I then created a Procfile which Heroku also requires by running the following command. `echo web: gunicorn nnb_store.wsgi:application > Procfile`.
9. I then went through the standard process of pushing these files to Github, which Heroku recognised and rebuilt the app.

Alternatively I could have connected my application through Heroku CLI
### Deploying using Heroku CLI

1. Up to the top right of the screen I would click the "New" Dropdown button and then click the dropdown and select "Create new app".
2. I would then call the app "covid-companion" and set the region to "Europe".
3. Once my app was created, I would chose my deployment method which would be "Use Heroku CLI".
4. Next I would go to my Gitpod workspace and in my CLI I would login in to Heroku using the following command. `heroku login -i`.
5. I would then go back to my Application dashboard and in the settings section I would take the "Heroku git URL" in "App Information".
6. Back in my Gitpod workspace, I would link my repository to Heroku using the following command. `git remote add heroku https://git.heroku.com/nnb-store.git`.
7. I would then create a requirements.txt so Heroku knows what dependecies need to be installed for the application to run by running the following command. `pip3 freeze > requirements.txt`.
8. I would then create a Procfile which Heroku also requires by running the following command. `echo web: gunicorn nnb_store.wsgi:application > Procfile`.
9. Lastly, I would push my application to Heroku which I will have to do manually each time using the following command. `git push heroku -u master`.

### Setting Up Heroku Enviroment Variables

1. In the application dashboard, navigate up the top of the screen and click the "Settings" button in the navigation menu.
2. In the "Config Vars" section, click "Reveal Config Vars" which is where I added my enviroment variables.
3. I then set all the enviroment variables up by adding the variable name to the "KEY" field and the variable value to the "VALUE" field and clicking the "Add" button.
```
    AWS_ACCESS_KEY_ID = '...'
    AWS_SECRET_ACCESS_KEY = '...'
    AWS_STORAGE_BUCKET_NAME = '...'
    DATABASE_URL = '...'
    EMAIL_HOST_PASS = '...'
    EMAIL_HOST_USER = '...'
    SECRET_KEY = '...'
    STRIPE_PUBLIC_KEY = '...'
    STRIPE_SECRET_KEY = '...'
    STRIPE_WH_SECRET = '...'
    USE_AWS = '...'
```

### Setting up AWS Bucket and Linking to Project
1. In the AWS Control Panel I created an S3 Bucket
2. I installed Django Storages using the command `pip3 install django-storages`
2. AWS was linked to the project in settings.py from line 173 to line 195

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/LouieOHagan/NNB-E-Commerce-Website)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type ```git clone```, and then paste the URL you copied in Step 3.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```
7. Press Enter. Your local clone will be created.
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Spoon-Knife`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```
Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.


## Credits

### Code
- [W3Schools](https://www.w3schools.com/howto/howto_js_tab_img_gallery.asp) for tutorial on creating image gallery and javascript function for changing the images 
- [Chris Zielinksi](https://github.com/ckz8780) for inspiration/tutorials for the Stripe checkout app & sorting by categories and query/search functionality.
- Large Screen Devices home page image slider inspired by Tesla and video tutorial on make a slider like Teslas by [Online Tutorials](https://www.youtube.com/watch?v=Rn5HeWbFNOc&list=PLo8KGgXM7VLl3nZLjnDfBchtWEWkuX3Uz&index=28&t=0s) 

### Content
- Smashing Magazine for information on Thumb zone design was found [here](https://www.smashingmagazine.com/2016/09/the-thumb-zone-designing-for-mobile-users/)

### Media
- [Pixabay](https://pixabay.com/): Some stock background images were obtained from Pixabay.
- [Google Images](https://www.google.com/imghp?hl=en): The remainding images were obtained from Google Images.

### Acknowledgements
- My Mentor Adegbenga Adeye for continuous helpful feedback and ideas to improve both myself as a developer and my project.

- Kevin Loughrey and Xavier Astor for continuous assistance with technical issues and project feedback day in, day out 

- Chris Zielinksi for the support while learning Django and for continuous assistance with technical issues during the development of the project.