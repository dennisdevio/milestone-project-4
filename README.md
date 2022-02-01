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

## Testing

#### Bugs Fixed
- Stripe API not working was fixed by setting the Stripe API Keys in config vars in Heroku.
- Heroku App crash was fixed by setting 'parse' in the database url if statement in settings.py.
- Rolled to a new STRIPE_SECRET_KEY as the old one was accidentally compromised during Stripe API bug troubleshooting 

### Acknowledgements
- Thank you to [Code Institute](https://codeinstitute.net/)'s tutor Chris and his video lessons from 'Boutige Ado' on creating a Django project.
- Thank you to [Code Institute](https://codeinstitute.net/)'s Tutor Support who help me tremendously along the way.
- Thank you to My mentor [Akshat Garg](https://github.com/akshatnitd) for his very much appreciated and needed support.
- Thank you to [Code Institute](https://codeinstitute.net/)'s Student Care
- Thank you to [Code Institute](https://codeinstitute.net/)'s Slack community.

#### This project was made as part of Code Institute's Full Stack Software Development Programme. 
#### This is for educational purposes only.
#### Created by Dennis Chmielewski.
