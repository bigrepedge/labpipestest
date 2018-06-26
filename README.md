# BigRep HMI

## Application Stack
* This is a Minimal Flask App with Vuejs frontend.
* [Flask-RestPlus](http://flask-restplus.readthedocs.io) API with class-based secure resource routing
* [PyTest](http://pytest.org) test suite
* [vue-cli 3](https://github.com/vuejs/vue-cli/blob/dev/docs/README.md) with Babel and ESlint.
* [Vuex](https://vuex.vuejs.org/) for state management
* [Vue Router](https://router.vuejs.org/)
* [Axios](https://vuex.vuejs.org/) for backend communication
* [Vue Filters](https://vuejs.org/v2/guide/filters.html)

## Template Structure

The template uses Flask & Flask-RestPlus to create a REST style API,
and let's VueJs + vue-cli handle the front end and asset pipline.

### Blueprints

The Flask application is setup with with two blueprints:


#### Api Blueprint

Uses Flask-RestPlus to serve resources at the `/api` endpoint.
Flask-RestPlus can be discarded if you prefer standard view functions routing.

#### Client Blueprint

A simple Flask view is used to serve the entry point into the Vue application at the root endpoint `/`
The template uses vue-cli 3 and assumes Vue.js & Webpack will manage front-end resources and assets,
so it does overwrite template delimiter.

The Vue instance is preconfigured with Filters, Vue-Router, Vuex; each of these can easilly removed if they are not desired.

## Installation

##### Before you start

* Make sure node + npm are installed (tested with npm v5.6)
* Python 3 is installed (tested with 3.6)

##### Clone this repository

##### Create virtual env
	```
	$ cd pro_control_HMI
	$ virtualenv venv
	```

##### Template and Dependencies

* Install Python dependencies using pip or pipenv from the project directory:

	`pip install -r requirements.txt`

* Install npm dependencies

	```
	$ cd app/client/vue_app
	$ npm install
	```


## Development Server

While it's possible to use Flask to serve the vue app and the rest api, it is less than ideal as each change in client code would required a full rebuild and reload. Instead, we will use flask the serve the api endpoints, but we will serve the client app using the vue-cli dev server.
This combination allows you have both your backend python files and the Vue appplication files auto-reload on save.

This template also includes a few functions to help us manage the 2 servers.

This enables us to take advantage of Hot Module Replacement (HMR) and ESlint.
I think it is a small price to pay for the amount of time saved by HMR alone.

##### Api Server

From the root directory run:

```
$ python3 -m app serve_api
```

This will start the flask development server on `localhost:5000` and will respond to all requests on `/api.`.
This command is the same as running `python3 run.py`

##### Client Server

Start another terminal window, and from the same directory run:

```
$ python3 -m app serve_client
```

This will launch your browser and server the Vue application on `localhost:8080`. T
he vue app will hit `localhost:5000` to fetch resources.

This combination allows you have both your backend python files, as well as the Vue app files autoreload on each file save.


##  Build your Vue Application:

```
$ python3 -m app build
```
This commands is a shorcut for cd-ing into `/app/client/vue_app` and running `$ npm run build`.

## Frontend Unit Tests

For unit testing jest is used it has been set up there is a script in the package json if you need to run it on its own.
```
$ npm run test:unit
```
Jest is loaded as a vue-cli plugin.

* [@vue/cli-plugin-unit-jest](https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-unit-jest)
* [jest](https://facebook.github.io/jest/)

## Server python tests

pytest has been added with coverage.

```
$ pytest
```
* [pytest](https://pytest-cov.readthedocs.io/en/latest/)

## Frontend e2e Tests

These e2e tests only go as far as the browser. The tests are performed using cypress. There is a script in the package json if you need to run it on its own.

```
$ npm run test:e2e
```
If you have this error when running tests in Ubuntu OS __"error while loading shared libraries: libgconf-2.so.4: cannot open shared object file: No such file or directory"__

```
$ sudo apt-get install -y libgconf-2-4
```

Cypress is loaded as a vue-cli plugin.

* [@vue/cli-plugin-e2e-cypress](https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-e2e-cypress)
* [cypress](https://docs.cypress.io/guides/overview/why-cypress.html#)


## Other Useful links

* [vue-cli documentation](https://github.com/vuejs/vue-cli/tree/dev/docs)
* [Vue.js](https://vuejs.org/)

##### Installed CLI Plugins

* [babel](https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel)
* [eslint](https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint)

##### Installed Vue.js Plugins

* [vue-router](https://router.vuejs.org/en/essentials/getting-started.html)
* [vuex](https://vuex.vuejs.org/en/intro.html)
* [vue-devtools](https://github.com/vuejs/vue-devtools#vue-devtools)
* [vue-loader](https://vue-loader.vuejs.org/en)
* [awesome-vue](https://github.com/vuejs/awesome-vue)