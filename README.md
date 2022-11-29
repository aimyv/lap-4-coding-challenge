# LAP 4 Debugging Assignment - Aimy Varghese && Peter Edwards

We have been tasked with creating a URL shortener, like this: [Free URL Shortener](https://free-url-shortener.rb.gy/).

## Requirements
- Our users should be able to enter a url into an input box on your website's front page
- Our backend will then generate a shortened path at which a User can access their url
- We must implement Python in the BackEnd, and React in the FrontEnd.
- Store this shortened path and it's longer counterpart in a database
- No login should be required to create a shortened URL
- If User tries to access our website with a path we have stored in our database, they should get rerouted to the URL it relates to 
- If a User tries to access our website with a path we do not have stored in our database, they should get rerouted to our homepage where they can create a new short URL

## Installation & Usage

Clone this repo and then `cd` into the project folder. Then run `pipenv install` and then `pipenv shell`. You can then run the following commands:

- `pipenv run dev` - Runs development server, on `http://localhost:5000/`
- `pipenv run start` - Runs Gunicorn server, on `...`

## Bugs

## Wins

## Challenges

## Links
- https://github.com/aimyv/lap-4-coding-challenge -- Repo link
- https://gist.github.com/getfutureproof-admin/2c7a6c700dab1a2c41c8ad27c89f2b1f - Original project brief
