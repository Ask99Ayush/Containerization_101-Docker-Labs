# 🟦 HealthCheck Web App

*Containerization 101 · Docker Practice Lab*

---

## 📌 Overview

The **HealthCheck Web App** is a beginner-friendly full-stack web application built to demonstrate **how real web applications are packaged and run using Docker**.

This project intentionally keeps the application logic simple so that students can focus on **understanding Docker**, not complex web development.

The application includes:

* A **frontend UI** built with HTML and CSS
* A **backend server** built using Flask
* A **Dockerfile** that packages everything into a single container

> 🎯 Goal: Help students clearly see how **frontend + backend = one Dockerized application**.

---

## 🧠 Learning Objectives

After completing this lab, you will be able to:

* Understand what a **backend** does in a web application
* See how a **frontend communicates with a backend API**
* Explain how Docker packages applications
* Build and run a Docker image locally
* Debug basic container issues

---

## 🏗 Application Architecture

```
Browser (Frontend UI)
        ↓
Flask Backend (Routes & Logic)
        ↓
Docker Container
```

* The **frontend** runs in the browser
* The **backend** runs inside the Docker container
* Docker ensures the app runs the same everywhere

---

## 📁 Project Structure

```
healthcheck-api/
├── app/
│   ├── app.py              # Backend application
│   └── templates/
│       └── index.html      # Frontend UI
├── static/
│   └── style.css           # Styling for UI
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker build instructions
└── README.md
```

Each folder has a clear responsibility:

* `app/` → backend logic
* `templates/` → frontend HTML
* `static/` → CSS styles

---

## ▶️ Run the App Without Docker (Optional)

This helps you understand the app **before containerization**.

```bash
python app/app.py
```

Open in browser:

```
http://localhost:5000
```

---

## 🐳 Run the App With Docker

### Step 1️⃣ Build the Docker Image

```bash
docker build -t awscc-healthcheck .
```

### Step 2️⃣ Run the Docker Container

```bash
docker run -p 5000:5000 awscc-healthcheck
```

### Step 3️⃣ Access the App

Open:

```
http://localhost:5000
```

You should see the **AWS Cloud Club – KIET** branded web page.

---

## 🧪 Practice Tasks (Highly Recommended)

Try the following to strengthen your Docker understanding:

* Change the UI text and rebuild the image
* Change the exposed port and update port mapping
* Stop and restart the container
* Break the Dockerfile intentionally and fix it

> 💡 Learning Docker comes from experimenting and fixing mistakes.

---

## 🎯 Key Takeaways

* Even simple web apps have a **backend**
* Docker packages **frontend + backend + dependencies**
* Containers make applications **portable and consistent**
* Docker is a **deployment tool**, not just a dev tool

---

## 🏁 Final Note

This project is not about building a feature-rich web app.
It is about building the **right mental model for Docker**.

If you understand this app, you understand **Docker fundamentals**.

---

### 🐳 Build Once. Run Anywhere.

---
