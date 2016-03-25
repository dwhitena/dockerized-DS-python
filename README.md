# Containerized Data Science w/ Python & Docker
This is a simple example of containerized data science illustrating how one can (and should) dockerize a data science application.  The simple app that we are dockerizing here is a k-NN classification model trained on the famous [iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set).  The app could definitely be improved in terms of logging, error handling, etc., but many of those things have been left out here for illustration purposes.

# Technologies

- [Python](https://www.python.org/)
- [Scikit-Learn](http://scikit-learn.org/stable/)
- [Flask-Restful](http://flask-restful-cn.readthedocs.org/en/0.3.4/)
- [Docker](https://www.docker.com/)

# Motivation

As you may or may not know, data scienctists often form habits of producing less-than-production-ready code, and, regardless how cool your deeplearning model is, it is not going to be useful if you can't put it into production.  [Docker](https://www.docker.com/) can help us out of this situation.  

By dockerizing your data science applications, you can ease the burden of putting your application into production, integrate your data science work into your company's CI/CD pipelines, make your application portable, scale your application easily across data center, and more.

This example is very simple, but the hope is that it provides a starting point for data scientists (familiar with python and scikit-learn) for experimentation with Docker and possibly JSON APIs.

# Installation

- Install these dependencies:
  - [Docker](https://www.docker.com/)
  - [Scikit-Learn](http://scikit-learn.org/stable/)
  - [Flask-Restful](http://flask-restful-cn.readthedocs.org/en/0.3.4/)
- Clone this repo.
- From the root of this repo build the Docker image:

  ```
  docker build --force-rm=true -t pythoniris .
  ```

- Now run the Docker image with:

  ```
  docker run --net host -d --name iris pythoniris
  ```

- The app's JSON API is now listening on port `5000` of this host.  Congrats! You just deployed your first dockerized data science application.  Now go forth and develop, train, test, validate, dockerize, and deploy more.

# JSON API Usage

This application listens on port `5000` of the host on which it is running.  You can query a prediction for a species of Iris using a `GET` request to the `/prediction` endpoint with parameters for the Sepal Length, Sepal Width, Petal Length, Pteal Width.  For example, the following query:

```
http://localhost:5000/prediction?slength=1.5&swidth=0.7&plength=1.3&pwidth=0.3
```

should return:

```
{
  "pwidth": 0.3, 
  "plength": 1.3, 
  "slength": 1.5, 
  "species": "setosa", 
  "swidth": 0.7
}
```

