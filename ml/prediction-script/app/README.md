# 🟩 ML Prediction Web App

*Containerization 101 · Machine Learning Docker Lab*

---

## 📌 Overview

The **ML Prediction Web App** demonstrates how **machine learning logic can be packaged and deployed as a web application using Docker**.

Instead of focusing on complex ML algorithms, this project focuses on the **deployment mindset**:

* How ML logic is separated from UI
* How a backend connects ML logic to users
* How Docker makes ML applications **reproducible and portable**

> 🎯 Goal: Help students understand how **ML code becomes a usable application** with Docker.

---

## 🧠 Learning Objectives

After completing this lab, you will be able to:

* Understand the difference between **ML logic and ML deployment**
* Connect ML code to a web interface
* Explain why ML projects often fail on different machines
* Use Docker to solve dependency and environment issues
* Build and run a Dockerized ML application

---

## 🏗 Application Architecture

```text
User Input (Web UI)
        ↓
Flask Backend
        ↓
ML Logic (Prediction)
        ↓
Result shown on UI
```

All components run **inside a single Docker container**, ensuring consistency across systems.

---

## 📁 Project Structure

```text
prediction-script/
├── app/
│   ├── app.py              # Backend server
│   ├── model.py            # ML prediction logic
│   └── templates/
│       └── index.html      # Frontend UI
├── static/
│   └── style.css           # UI styling
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker build instructions
└── README.md
```

### Why this structure matters

* ML logic is **isolated and reusable**
* Backend controls input/output
* Frontend remains simple and clean
* Docker packages everything together

---

## ▶️ Run the App Without Docker (Optional)

Running locally helps you understand the flow **before containerization**.

```bash
python app/app.py
```

Open in browser:

```
http://localhost:5000
```

Enter a number and observe the prediction result.

---

## 🐳 Run the App With Docker

### Step 1️⃣ Build the Docker Image

```bash
docker build -t awscc-ml-predict .
```

### Step 2️⃣ Run the Docker Container

```bash
docker run -p 5000:5000 awscc-ml-predict
```

### Step 3️⃣ Access the Application

Open:

```
http://localhost:5000
```

You are now using an **ML-powered web app running inside Docker**.

---

## 🧪 Practice Tasks (Recommended)

To deepen your understanding, try the following:

* Modify the prediction logic in `model.py`
* Add new prediction categories
* Change UI colors and text
* Rebuild the Docker image after changes
* Observe how Docker ensures consistent behavior

---

## 🎯 Key Takeaways

* ML code alone is **not enough**
* Deployment is as important as modeling
* Docker makes ML applications **portable**
* Containers solve dependency conflicts
* One image can run the same ML app everywhere

---

## 🏁 Final Note

This project represents a **real-world ML deployment pattern**:

* Simple model
* Backend API
* Frontend UI
* Dockerized environment

If you understand this flow, you are **thinking like an industry ML engineer**, not just a student.

---

### 🐳 Build Once. Run Anywhere.

---
