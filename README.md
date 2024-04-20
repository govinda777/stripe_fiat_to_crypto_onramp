# Integrate with Stripe onramp

https://docs.stripe.com/crypto/integration-recipes
https://docs.stripe.com/crypto/quotes-api

Build a simple page to use Stripe onramp. Included are some basic
build and run scripts you can use to start up the application.

## Running the sample

1. Build the server

~~~
pip3 install -r requirements.txt
pipenv install -r requirements.txt

pipenv install pre-commit
~~~

2. Run the server

~~~
export FLASK_APP=server.py
python3 -m flask run --port=4242

export FLASK_APP=server.py
pipenv run python -m flask run --port=4242
~~~

3. Build the client app

~~~
npm install
~~~

4. Run the client app

~~~
npm start
~~~

5. Go to [http://localhost:3000](http://localhost:3000)