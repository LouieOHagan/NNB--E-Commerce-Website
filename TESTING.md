<h1 align="center">NNB Responsive E-Commerce Website Project</h1>

##### Note: TESTING.MD is a connected to [README.md](https://github.com/LouieOHagan/NNB-E-Commerce-Website/blob/master/README.md) but a seperate file has been created to keep README a reasonable length and to maintain cleanliness

## Testing

### Testing Accounts

#### Normal User Account
    - Login Details:
        - Email Address: test-user@nnb.ie
        - Password: dodger2020

#### Super User Account Details
    - Login Details:
        - Email Address: test-superuser@nnb.ie
        - Password: dodger2020

### Automated Testing
I conducted automated testing using Djangos built in TestCase on all 4 of my custom apps.
Coverage was used to generate a report of the tests which achieved the following:

- Products App 
    - 96% test coverage, 293 statements overall, tested 280 statements, 13 statements missed
- Home App
    - 100% test coverage, 22 statements overall, tested 22 statements, 0 statements missed
- Cart App
    - 97% test coverage, 90 statements overall, tested 87 statements, 3 statements missed
- Checkout App
    - 70% test coverage, 286 statements overall, tested 199 statements, 87 statements missed

- 4 Custom Apps Overall Report 
    - 82% test coverage, 716 statements overall, tested 590 statements, 126 statements missed
	- Last Updated 2:41pm on 22/5/2020

- Overall Coverage GIF can be found [Here](https://github.com/LouieOHagan/NNB-E-Commerce-Website/blob/master/README-ASSETS/test-coverage-gif.gif)


### Further Testing
- The search bar was becoming visible properly however when trying to close the search bar it would start to transition but then would just snap/hide straight away
    - This issue was fixed by noticing that the page was being reloaded so the transition was happening but the page was being reloaded hence the search bar was starting to fade 
    and then when the page reloaded it would just be hidden as thats its default state. I looked in to why it was being reloaded and the href for the anchor tag was like `href=""`
    and was reloading the page. Issue fixed by adding a # (`href="#"`) to stop the page reloading
- All navigation items were moving to right when the search icon button was clicked just before they faded
	- After looking in to the issue, the items were being hidden in jquery using the `.hide()` method. I originally fixed the issue by adding new margin properties to push it out when 
	the button was selected but the issue happened again when I tried adding a fade. 
    - The issue was fixed by removing the `.hide()` method and adding a custom class using visibility:hidden & opacity:1 css properties so icons are still there but just hidden 
    meaning the items maintain their space and no other items are being moved and the use of opacity and transition allowed for a fade in/out
- Orders were going through but when there was a delivery cost the order was then failing and spitting out this error message - Unsupported operand type(s) for *: 'float' and 'Decimal'
    - Debug mode was on and I saw that there was an error on line 51 of my checkout.models.py which is where the grand_total was being updated by adding the total with the 
    delivery cost. I looked in to it and found out that the order.total was a DecimalField in the models but the delivery cost which was coming from the settings.py was a float so 
    I import Decimal from decimal from django and converted the float to a decimal so they could both be added together without errors.
- Whole website kept giving 404 pages no matter what page I was on
    - After having no idea what was causing the issue I decided to test the site on my laptop which did not return any errors. After further research in to the issue I realised I had
    just removed a product from the database prior to the issue occuring and it turned out that I had the product in my cart at the time. 
    - The issue was fixed by going in to chrome developer tools and deleting my session which cleared my cart and the website went back to functioning normal again.
- Stripe was returning a 500 error in the stripe dashboard > webhooks when a field was left blank in the checkout form
    - The error in the developer dashboard was - Error was saying that "ERROR: null value in column "street_address2" violates not-null constraint"
    - The issue was fixed by adding null=True in to any of the fields that had blank=True in the models.py and migratingas the changes. After looking in to the issue I discovered that
    blank=True was doing form validation and saying it didnt need to be filled out but stripe wasexpecting some sort of value and null=True did that.
 


### Known Bugs
- The Sign in with google button is non-functional
    - During setup and testing of logging in through social accounts with allauth, I discovered that gitpod wasnt allowing google to redirect back to the site after a user logged in
    with their google account, the only way it would work was if it returned localhost:8000 however which didnt return anything.
    - Once deployed I planned to set it up with Heroku and get the redirect links working however due to time limitations I was unable to complete this or safely remove it from the
    site without breaking all of the allauth functionality.
-  Allauth pages (Sign In, Sign Up etc) do not have finished styling
    - Buttons are not centered on the allauth templates, due to time limitations this issue along with additional styling of the allauth pages could not be completed. 