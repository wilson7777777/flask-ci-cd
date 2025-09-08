# Flask CI/CD Project with Automated Testing

A simple Python Flask web application that demonstrates a professional, end-to-end DevOps pipeline with automated testing.

## Overview

This project showcases a modern CI/CD workflow that automates the entire process from a code change to a live web application. The key feature of this pipeline is the inclusion of automated tests, ensuring that every deployment is validated and free of major bugs.

The automated workflow performs the following steps on every push to the `main` branch:

1.  **Runs Automated Tests**: It executes unit tests to verify the application's core functionality.
2.  **Builds the Docker Image**: If the tests pass, it builds a container image of the application.
3.  **Pushes to Docker Hub**: The newly built image is automatically pushed to Docker Hub.
4.  **Deploys to Render**: The new image is automatically pulled and deployed to the live server.

This robust pipeline ensures that your application is always in a deployable state.

## Technologies Used

* **Python & Flask**: The backend application framework.
* **pytest**: A powerful and easy-to-use testing framework for Python.
* **Docker**: Used to containerize the application, ensuring consistency across all environments.
* **GitHub Actions**: The CI/CD platform that orchestrates the entire automated workflow.
* **Docker Hub**: The container registry that stores the application's images.
* **Render**: The cloud platform used for continuous deployment.

## Getting Started

### Prerequisites

* Python 3.10+
* Docker
* Git

### Local Development

1.  Clone this repository to your local machine:
    `git clone https://github.com/wilson7777777/flask-ci-cd.git`
    `cd flask-ci-cd`

2.  Install the required Python dependencies:
    `pip install -r requirements.txt`

3.  Run the automated tests to verify your setup:
    `pytest`

4.  To run the application locally, you can use the following command:
    `gunicorn --bind 0.0.0.0:5000 app:app`

The application will be available at `http://localhost:5000`.

## CI/CD Pipeline

The CI/CD pipeline is defined in the `.github/workflows/ci-cd.yml` file. It relies on two GitHub secrets to connect to Docker Hub: `DOCKER_USERNAME` and `DOCKER_PASSWORD`.

## Deployment

The application is automatically deployed to Render. The Render service is configured to automatically pull the latest image from Docker Hub, ensuring a zero-touch deployment process after the initial setup.
