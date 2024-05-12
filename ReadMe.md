# Service Overview

The service primarily revolves around a Django-based application designed to handle asynchronous workloads with real-time user interaction capabilities. Below is a detailed breakdown:

## User Authentication
- **Base Functions:**
  - Includes essential pages like Home, About, and user-specific features such as login, signup, and logout functionalities.
- **Navigation Enhancements:**
  - Once authenticated, the user's username is displayed in the navigation bar, enhancing the personalized user experience.

## Websocket Connection
- **User-Specific Connection:**
  - Establishes a websocket connection on page load if the user is authenticated, allowing real-time communication.
- **Redis Integration:**
  - Utilizes Redis channels for distributed messaging, ensuring scalability and responsiveness across different services.

## Asynchronous Task Management
- **REST API:**
  - Facilitates the asynchronous queuing of workloads via RESTful calls, seamlessly integrating front-end activities with server-side processing.
- **Celery Worker:**
  - Processes the enqueued tasks asynchronously, ensuring efficient management of compute resources.
- **Real-Time Notifications:**
  - Upon completion of tasks, notifications are promptly sent to the user, ensuring they are kept in the loop about the status of their operations.

## UI Components

### Home Page
- Features interactive elements such as a button to initiate tasks and a display for recent tasks, coupled with live notifications for completed tasks.

### About Page
- Provides comprehensive information about the service, outlining its functionalities and the technology stack utilized.

## Background Worker
- Dedicated to processing tasks queued by the REST API. This component also handles sending notifications back to the user, confirming the completion of tasks.

# UI screenshot
![UI screenshot with notifications](assets/images/UI_Screenshot.png)

# Tech Stack

1. **Framework**: Django + Django Channels + Celery
2. **RabbitMQ**: Celery broker for the async tasks execution in the background.
3. **Redis**: Django Channels backend for distributed messaging between the background task and channel service.
4. **PostgreSQL**: Database for maintaining users and Celery backend for maintaining tasks.

# Tasks Checklist

- [x]  User authentication
    - [x]  Base page, Home page, and About page
    - [x]  User login
    - [x]  New user signup
    - [x]  Logout API endpoint
    - [x]  Display user's username in the navigation bar if they're logged in
- [x]  Websocket connection with user authentication
    - [x]  Establish websocket connection on page load if authenticated
    - [x]  Test the websocket for sending and receiving messages
    - [x]  Setup redis channel for distributed service
- [x]  REST API call to queue workload asynchronously
- [x]  Celery worker for processing workload from queue
- [x]  Notification upon completion of the async workload
