# CI/CD Pipeline for a Data-Driven Flask Application

A professional, end-to-end CI/CD pipeline for a Python Flask application. This project demonstrates how to automate the build, test, and deployment of a full-stack application that includes a PostgreSQL database.

## Key Features

* **Continuous Integration (CI):** A GitHub Actions workflow that automatically runs unit tests on every code push.
* **Continuous Deployment (CD):** A zero-touch deployment process that automatically builds a new Docker image, pushes it to Docker Hub, and deploys it to Render.com.
* **Containerization:** The entire application is containerized with Docker, ensuring a consistent environment from development to production.
* **Automated Testing:** The pipeline validates code quality by automatically running a suite of `pytest` unit tests.
* **Database Integration:** The application connects to a PostgreSQL database on Render to handle and persist data.

## Technologies Used

* **Python & Flask:** The backend web framework.
* **Gunicorn:** The production-grade web server.
* **PostgreSQL:** The relational database used to store data.
* **Flask-SQLAlchemy & psycopg2-binary:** Python libraries for database integration.
* **Docker:** Used to containerize the application.
* **pytest:** The testing framework for the application's business logic.
* **GitHub Actions:** The CI/CD platform that automates the entire workflow.
* **Render:** The cloud platform used for continuous deployment.

## CI/CD Pipeline Overview

The pipeline is defined in the `.github/workflows/ci-cd.yml` file. On every push to the `main` branch, the workflow performs the following steps:

1.  **Tests:** Runs `pytest` to ensure all tests pass.
2.  **Build:** Builds a new Docker image of the application.
3.  **Push:** Pushes the image to Docker Hub.
4.  **Deploy:** Notifies Render to pull the new image and deploy it, making the changes live.

## Getting Started

### Prerequisites

* Git
* Docker
* Python 3.10+
* A Render.com account
* A Docker Hub account

### Local Development

1.  Clone this repository to your local machine:
    `git clone https://github.com/wilson7777777/flask-ci-cd.git`
    `cd flask-ci-cd`

2.  Install the required dependencies:
    `pip install -r requirements.txt`

3.  Run the tests to ensure everything is working locally:
    `pytest`

## Deployment

The application is deployed to Render. The service is configured with the `DATABASE_URL` environment variable, which allows it to connect to the PostgreSQL database.

## Author

* **wilson7777777** - [https://github.com/wilson7777777](https://github.com/wilson7777777)
