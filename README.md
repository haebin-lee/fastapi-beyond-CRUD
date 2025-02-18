# FastAPI Beyond CRUD

This is the source code for the [FastAPI Beyond CRUD](https://youtube.com/playlist?list=PLEt8Tae2spYnHy378vMlPH--87cfeh33P&si=rl-08ktaRjcm2aIQ) course. The course focuses on FastAPI development concepts that go beyond the basic CRUD operations.

For more details, visit the project's [website](https://jod35.github.io/fastapi-beyond-crud-docs/site/).

## Table of Contents

- [FastAPI Beyond CRUD](#fastapi-beyond-crud)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Project Setup](#project-setup)
  - [Running the Application](#running-the-application)
  - [Running Tests](#running-tests)
  - [Contributing](#contributing)
  - [Github Actions](#github-actions)

## Getting Started

Follow the instructions below to set up and run your FastAPI project.

### Prerequisites

Ensure you have the following installed:

- Python >= 3.10
- PostgreSQL
- Redis

### Project Setup

1. Clone the project repository:
   ```bash
   git clone https://github.com/jod35/fastapi-beyond-CRUD.git
   ```
2. Navigate to the project directory:

   ```bash
   cd fastapi-beyond-CRUD/
   ```

3. Create and activate a virtual environment:

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables by copying the example configuration:

   ```bash
   cp .env.example .env
   ```

6. Run database migrations to initialize the database schema:

   ```bash
   alembic upgrade head
   ```

7. Open a new terminal and ensure your virtual environment is active. Start the Celery worker (Linux/Unix shell):
   ```bash
   sh runworker.sh
   ```

## Running the Application

Start the application:

```bash
fastapi dev src/
```

Alternatively, you can run the application using Docker:

```bash
docker compose up -d
```

## Running Tests

Run the tests using this command

```bash
pytest
```

## Contributing

I welcome contributions to improve the documentation! You can contribute [here](https://github.com/jod35/fastapi-beyond-crud-docs).

## Github Actions

pr-check.yml:

- GitHub Actions that verify the PR title and commit message follow the Conventional Commits format during PR creation.
- If there's a failure, it sends an email notification.

nightly-build.yml:

- GitHub Actions that test and build this project at midnight every day and push this image to GitHub container registry.
- If there's a failure, it sends an email notification.

- Wrong commit
