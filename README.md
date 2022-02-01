# Men's Style Store
Men's Style Store is a fully functional E-commerce website that cater to men's clothing and style needs.
It's allows the customer to select the clothing item for their choice, pick the desired size & quantity and order it directly online via credit card payments. Furthermore the customer can create their personal account which allows them to see their current and past orders.
The purpose of this website is to provide an easy and appealing way for the site owner to run an online business and gain a location independent, pontentially global customer base, as well as for the customer to purchase their desired items regardless of their location.

## Showcase
You can view the Men's Style Store E-commmerce website [here](https://mens-style-store.herokuapp.com/).

### Wireframes
I made wireframes for a total of six pages - the landing page, the category view, the single item view, the register page, the login page, and the personal account page.The landing page shows the top sold items in the store. The category page shows all products in a given category, including an 'All Products' page. When the user clicks on a product they are redirected to the single items view. The register and login pages layout are basically identical but with differing functionality. Lastly, if the user wishes to track their orders they can register and login to their perosnal account to view their current orders displayed at the top of the page and their previous orders displayed further down the page.
I decided to go with three sizes of wireframes to account for the responsive design that allows the page to be view on any screen, from mobile phones to large desktop monitors. For large screens, medium size screens and small screens each page.
- The wireframes were created using - [InVision](https://www.invisionapp.com/). 
- The wireframes for this project can be found [at this link](https://dennischmielewski323696.invisionapp.com/freehand/Mens-Style-Store-WkUKYDrWh)

## Features
- Responsive Design across all device sizes, including a hamburger menu button on smaller screens.
- A clothing item sarch and sorting function.
- A profile page with saved personal order information.
- A wishlist function for logged in user.
- An order and payment function.
- A contact form for customer support.

#### Features Left to Implement
Due to time constraints the following features are left unimplemented at this point but will be implemented on a future release:

- A review function for each clothing product.
- Stripe webhooks for increased security.

## Technologies
The technologies used to build this website are the following

#### Development
- [Gitpod Online IDE](https://www.gitpod.io/) for all code editing.
- [Firefox Devtools](https://developer.mozilla.org/en-US/docs/Tools) for all functional testing throughout the development process.

#### Testing

#### Images
- [Unsplash](https://unsplash.com/) the landing page images were downloaded from Unsplash. 
- [Boutiqe Ado](https://github.com/Code-Institute-Solutions/boutique_ado_images/tree/master/pics) the men's wear product images provided in the 'Boutiqe Ado' walkthrough project were filtered out and used for this project.

#### Fonts & Icons
- [Google Fonts](https://fonts.google.com/share?selection.family=Noto%20Sans%20KR%7COpen%20Sans) the fonstyle 'Roboto' was used on the website. 
- [Font Awesome](https://fontawesome.com/start) for all website icons.

#### API's
- [Stripe API](https://stripe.com/docs/api) for making test payments during this project.

### Languages 
- [HTML5](https://en.wikipedia.org/wiki/HTML5) was used for laying the foundation and structuring the basis of the website. 
- [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3) was used for the placement and styling of all HTML5 content on the website. 
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for creating interactivity with Stripe, Toast messages, searching products and setting the shopping cart quantities.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) was used for handling the data base models and app logic with Django.

### Frameworks
- [Bootstrap v4.4.1](https://getbootstrap.com/docs/4.4/getting-started/download/) Bootstrap 4.4.1 was used to implement a responsive mobile-first design on the website.
- [Django 3.2](https://docs.djangoproject.com/en/4.0/releases/3.2/) Django 3.2 was used to implement a Full Stack website with python.

## Testing

#### Bugs Fixed
- Stripe API not working was fixed by setting the Stripe API Keys in config vars in Heroku.
- Heroku App crash was fixed by setting 'parse' in the database url if statement in settings.py.
- Rolled to a new STRIPE_SECRET_KEY as the old one was accidentally compromised during Stripe API bug troubleshooting 

#### Bugs Left
- The Country field styling in the checkout form should be gray but I left it due to time constraints.

### Acknowledgements
- Thank you to [Code Institute](https://codeinstitute.net/)'s tutor Chris and his video lessons from 'Boutige Ado' on creating a Django project.
- Thank you to [Code Institute](https://codeinstitute.net/)'s Tutor Support who help me tremendously along the way.
- Thank you to My mentor [Akshat Garg](https://github.com/akshatnitd) for his very much appreciated and needed support.
- Thank you to [Code Institute](https://codeinstitute.net/)'s Student Care
- Thank you to [Code Institute](https://codeinstitute.net/)'s Slack community.

#### This project was made as part of Code Institute's Full Stack Software Development Programme. 
#### This is for educational purposes only.
#### Created by Dennis Chmielewski.
