# Sensor_integration

A web application project with microservices architecture for sensor integration and data processing.

## Table of Contents

- [Microservices Architecture](#microservices-architecture)
- [Components](#components)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Dockerization](#dockerization)
- [Deployment](#deployment)
- [Scalability and Fault Tolerance](#scalability-and-fault-tolerance)
- [Contributing](#contributing)
- [License](#license)

## Microservices Architecture

The project follows a microservices architecture consisting of the following components:

- **Sensor Integration Service**
- **Data Processing Service**
- **Web Application Backend**
- **Angular Frontend (Dashboard)**

For detailed information about each microservice and their interactions, refer to the [Microservices Architecture documentation](docs/microservices_architecture.md).

## Components

1. **Sensor Integration Service:**
   - Integrates data from different sensors.
   - API Endpoint: `/sensor-data`

2. **Data Processing Service:**
   - Processes data based on sensor types.
   - API Endpoint: `/process-data`

3. **Web Application Backend:**
   - Serves as the backend for the Angular frontend.
   - API Endpoint: `/get-sensor-data`

4. **Angular Frontend (Dashboard):**
   - Displays dummy values of temperature, motion, and humidity.
   - Integrates with microservices through REST API services.

For detailed information about each component, refer to the documentation in the 'docs/' directory.

## Technology Stack

- **Backend:** Django
- **Frontend:** Angular
- **Containerization:** Docker
- **Orchestration:** Docker Compose

## Getting Started

### Prerequisites

- Docker installed on your machine.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/RAMANATHAN-19/sensor_integration_project
## Deployment

To deploy this project run

1. Change your working directory:

```bash
  cd sensor_integration
```

2.Build Docker containers:
```bash
  docker-compose build
```
3.Start the application:
```bash
  docker-compose up
```


## Usage

Access the Angular frontend at http://localhost:
Dockerization
The project uses Docker for containerization. Each microservice has its own Dockerfile for easy deployment. For more information, refer to the Dockerization documentation.

Deployment:

Instructions for deploying and scaling the Dockerized services can be found in the Deployment and Scaling documentation.

Scalability and Fault Tolerance:

The microservices architecture is designed for scalability and fault tolerance. For detailed information, refer to the Scalability and Fault Tolerance documentation.

Contributing:

If you would like to contribute to the project, please follow the guidelines outlined in the CONTRIBUTING.md file.


## Project Structure

sensor_project/
|-- sensor_integration/             
|   |-- sensor_integration/
        
|   |   |-- __init__.py

|   |   |-- asgi.py
|   |   |-- settings.py
|   |   |-- urls.py
|   |   |-- wsgi.py
|--|-- sensor_integration_app/      
|   |   |-- __init__.py
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- migrations/
|   |   |   |-- __init__.py
|   |   |-- models.py               
|   |   |-- tests.py
|   |   |-- views.py               
|   |-- manage.py                   
|   |-- requirements.txt            
|-- data_processing/               
|   |-- data_processing/           
|   |   |-- __init__.py
|   |   |-- asgi.py
|   |   |-- settings.py
|   |   |-- urls.py
|   |   |-- wsgi.py
|--|-- data_processing_app/       
|   |   |-- __init__.py
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- migrations/
|   |   |   |-- __init__.py
|   |   |-- models.py               
|   |   |-- tests.py
|   |   |-- views.py                
|   |-- manage.py                   
|   |-- requirements.txt           
|-- sensor-dashboard/              
|   |-- e2e/
|   |   |-- src/
|   |   |   |-- app.e2e-spec.ts
|   |   |   |-- app.po.ts
|   |   |-- protractor.conf.js
|   |-- src/
|   |   |-- app/
|   |   |   |-- app.component.html
|   |   |   |-- app.component.css
|   |   |   |-- app.component.spec.ts
|   |   |   |-- app.component.ts
|   |   |   |-- app.module.ts
|   |   |   |-- app-routing.module.ts
|   |   |-- assets/
|   |   |-- environments/
|   |   |-- favicon.ico
|   |   |-- index.html
|   |   |-- main.ts
|   |   |-- polyfills.ts
|   |   |-- styles.css
|   |-- .editorconfig
|   |-- .gitignore
|   |-- angular.json
|   |-- package.json
|   |-- README.md
|   |-- tsconfig.json
|   |-- tslint.json
|-- web_app_backend/               
|   |-- web_app_backend/          
|   |   |-- __init__.py
|   |   |-- asgi.py
|   |   |-- settings.py
|   |   |-- urls.py
|   |   |-- wsgi.py
|--|-- web_app_backend_app/       
|   |   |-- __init__.py
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- migrations/
|   |   |   |-- __init__.py
|   |   |-- models.py               
|   |   |-- tests.py
|   |   |-- views.py               
|   |-- manage.py                   
|   |-- requirements.txt            
|-- .gitignore
|-- README.md
|-- requirements.txt               



## Project_Diagram


                +-------------------+
                |  Sensor Integration|
                |  (Django App)      |
                +-------------------+
                        |
                        v
                +-------------------+
                |    Data Processing|
                |    (Django App)    |
                +-------------------+
                        |
                        v
                +-------------------+
                |Web App Backend    |
                |(Django App)        |
                +-------------------+
                        |
                        v
                +-------------------+
                |Angular Web App     |
                |(`sensor-dashboard`)|
                +-------------------+



## Frontend_Diagram

+--------------------------------------------------+
|               Angular Web App                     |
|           (`sensor-dashboard`)                     |
+--------------------------------------------------+
        |                     |                    |
        v                     v                    v
+----------------+ +-------------------+ +----------------+
| DashboardComp  | | TemperatureComp   | | MotionComp     |
|                | |                   | |                |
|                | |                   | |                |
+----------------+ +-------------------+ +----------------+
        |                     |                    |
        v                     v                    v
+----------------+ +-------------------+ +----------------+
| HumidityComp   | | ApiService        | | Other Services |
|                | |                   | |                |
|                | +-------------------+ +----------------+
+----------------+
        |
        v
+-------------------+
| Angular Material  |
| Components        |
+-------------------+






