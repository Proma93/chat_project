<h1 align="center">Real-Time Chat Application with Django & React</h1>

<div align="justify">
Currently building a powerful real-time chat app from scratch using Django Channels and React.
The project features a Django backend with WebSocket support, Daphne as the ASGI server, Redis for message handling,
and a responsive React frontend powered by Vite to deliver seamless live messaging.
</div>

---

## Table of Contents

- [Key Features](#key-features)
- [Tech Stack](#tech-stack)

---

## Key Features

### Backend:

- **WebSocket Integration**: Utilizes Django Channels to support WebSocket connections for real-time messaging.
- **Redis**: Acts as the message broker to enable WebSocket functionality and handle asynchronous events.
- **Daphne**: A production-ready ASGI server used to serve WebSocket and HTTP traffic.
- **Message Persistence**: Messages are stored in a PostgreSQL or SQLite database using Django ORM.
- **Authentication**: Supports token-based authentication for secure communication.
- **Online and Typing Indicators**: Real-time updates for online users and typing notifications.
- **Role-based Access**: Ensures users can only access conversations they are part of.
- **Swagger UI for API Documentation**: Added Swagger UI (via drf-yasg) to automatically generate interactive API documentation

---

## Tech Stack
This project leverages the following technologies:

| **Layer**              | **Technology**                                                                | **Description**                                       |
| ---------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------- |
| 🐍 Backend Framework   | [Django](https://www.djangoproject.com/)                                      | High-level Python web framework                       |
| 🔗 API Toolkit         | [Django REST Framework](https://www.django-rest-framework.org/)               | Flexible toolkit to build Web APIs                    |
| 🔄 Real-time Framework | [Django Channels](https://channels.readthedocs.io/)                           | Adds WebSocket and async support to Django            |
| ⚙️ ASGI Server         | [Daphne](https://github.com/django/daphne)                                    | ASGI server to run Django Channels                    |
| ⚛️ Frontend Framework  | [React](https://reactjs.org/)                                                 | JavaScript library for building UIs                   |
| ⚡ Frontend Tooling    | [Vite](https://vitejs.dev/)                                                   | Fast frontend build tool and dev server               |
| 🌐 Real-time Protocol  | [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) | Bi-directional real-time communication                |
| 🧰 Message Broker      | [Redis](https://redis.io/)                                                    | In-memory data structure store, used as channel layer |

---
