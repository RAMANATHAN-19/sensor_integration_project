# Microservices Architecture

## Overview

The microservices architecture for the web application involves several components, each serving a specific purpose. This document provides an overview of the key microservices, their roles, and how they interact to achieve the goals of scalability, high performance, and easy deployment.

## Components

### 1. **Sensor Integration Service**

- Responsible for integrating data from various sensors.
- Implements a scalable architecture to handle data from different types of sensors (e.g., temperature, motion).
- Ensures graceful handling of sensor failures without affecting the entire system.

### 2. **Data Processing Service**

- Processes the data received from the Sensor Integration Service.
- Implements data processing logic based on the type of sensor data.
- Designed to scale horizontally to handle increased data processing requirements.

### 3. **Web Application Backend**

- Serves as the backend for the web application.
- Integrates with the Data Processing Service to provide processed data to the frontend.
- Implements an API for the frontend to request sensor data and processed information.

### 4. **Angular Frontend (Dashboard)**

- Develops the frontend using the Angular framework.
- Displays dummy values of temperature, motion, and humidity on a responsive dashboard.
- Integrates with microservices through REST API services.
- Includes graphs (bar chart, pie chart) for displaying data with date filters.

## Interaction

The microservices interact in the following sequence:

1. **Sensor Integration Service receives data from sensors:**
   - Data is sent to the `/sensor-data` endpoint.

2. **Data Processing Service processes the received data:**
   - Sensor Integration Service forwards data to the `/process-data` endpoint.

3. **Web Application Backend fetches processed data:**
   - The frontend requests sensor data from the `/get-sensor-data` endpoint.

4. **Angular Frontend displays the information:**
   - The Angular components receive data and update the dashboard.

## Technology Stack

The microservices are implemented using Django for the backend, and the frontend is developed with the Angular framework. Docker is employed for containerization, allowing easy deployment and scaling of the system.

## Conclusion

The microservices architecture ensures a modular and scalable design for the web application. Each microservice plays a specific role in the data flow, contributing to the overall efficiency and performance of the system.

For detailed documentation on each microservice, refer to the individual markdown files in the 'docs' directory.
