# 🧑‍💼 Employee Management System

*Containerization 101 · Docker Compose Lab*

---

## 📌 Overview

The **Employee Management System (EMS)** is a simple, real-world inspired application designed to teach **how multi-container systems are built and run using Docker Compose**.

This project goes beyond running a single container and introduces students to **industry-style workflows**, where applications are composed of **multiple services working together**.

> 🎯 **Goal:** Help students understand how backend services and databases communicate inside a Dockerized system.

---

## 🧠 Learning Objectives

After completing this lab, you will be able to:

* Understand why real applications need **multiple containers**
* Use **Docker Compose** to run a complete system
* Connect a backend service to a database container
* Use **environment variables (`.env`)** for configuration
* Debug common multi-container issues
* Think in terms of **systems**, not just apps

---

## 🏗 System Architecture

```text
Browser (UI)
   ↓
Flask Backend (API + UI)
   ↓
MongoDB Database
```

* The **backend** handles UI rendering and business logic
* The **database** stores employee data
* Docker Compose manages networking and startup order

---

## 📁 Project Structure

```text
employee-management/
├── backend/
│   ├── app.py              # Flask backend application
│   ├── Dockerfile          # Backend container definition
│   ├── requirements.txt    # Python dependencies
│   ├── templates/          # HTML UI templates
│   └── static/             # CSS styles
│
├── docker-compose.yml      # Multi-container system definition
├── .env                    # Environment variables (local)
├── .env.example            # Sample environment file
└── README.md
```

### 🔑 Design Rule

> **One service = one folder = one Dockerfile**

---

## ⚙️ Environment Configuration

The application uses environment variables for configuration.

### `.env` (example)

```env
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=change-this-secret

MONGO_URI=mongodb://mongo:27017
DATABASE_NAME=employee_management
```

> ⚠️ `mongo` is the **service name**, not `localhost`.

Docker Compose automatically injects these values into the backend container.

---

## 🐳 Running the System with Docker Compose

### Step 1️⃣ Build & Start Services

From the `employee-management/` directory:

```bash
docker compose up --build
```

### Step 2️⃣ Access the Application

Open your browser:

```
http://localhost:5000
```

You can now:

* Add employees
* View employee list
* Restart containers without losing data

---

## 🧪 What to Observe (Important)

While the system is running, notice:

* Two containers running (`backend` and `mongo`)
* Backend connects to database using **service name**
* Data persists due to Docker volumes
* No database runs on your host machine

This is **exactly how real systems behave**.

---

## 🛠 Debugging Tips (Day 2 Focus)

Useful commands:

```bash
docker compose ps
docker compose logs
docker exec -it ems_backend env
```

Try intentionally breaking:

* `MONGO_URI`
* Service name in Compose
* Database container

Then fix it.
👉 **Breaking and fixing is learning.**

---

## 🎯 Key Takeaways

* Docker Compose runs **systems**, not just containers
* Services communicate via **service names**
* Environment variables control configuration
* Databases should be isolated in their own containers
* This pattern is used in **real companies**

---

## 🧭 Career Relevance

Skills practiced in this lab are directly applicable to:

* Backend Engineering
* DevOps & Cloud roles
* System Design interviews
* Internships involving Docker & microservices

Example resume point:

> *Built and ran a multi-container Employee Management System using Docker Compose with backend–database communication.*

---

## 🏁 Final Note

This project is intentionally **simple in features but strong in architecture**.

If you understand this lab, you understand:

* How real applications are structured
* How Docker fits into production workflows

---

### 🐳 Containerization 101

**Build Once. Run Anywhere.**

---

