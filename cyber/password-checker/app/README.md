# 🟥 Password Strength Checker

*Containerization 101 · Cyber Security Docker Lab*

---

## 📌 Overview

The **Password Strength Checker** is a simple and ethical cyber security application that demonstrates how **security-related logic can be safely packaged and executed using Docker**.

This project focuses on:

* Running security logic in an **isolated environment**
* Understanding how user input is handled securely
* Using Docker to control and contain execution

⚠️ This is an **educational and ethical project**.
No offensive or hacking techniques are used.

---

## 🧠 Learning Objectives

After completing this lab, you will be able to:

* Understand how cyber security tools work as applications
* Explain why isolation is critical in security-related software
* Safely process sensitive user input
* Use Docker to run security logic in a controlled environment
* Build and run Docker images confidently

---

## 🏗 Application Architecture

```text
User Input (Password)
        ↓
Backend Security Logic
        ↓
Strength Evaluation
        ↓
Result Displayed on UI
```

Docker ensures the security logic runs **separately from the host system**.

---

## 📁 Project Structure

```text
password-checker/
├── app/
│   ├── app.py              # Security logic & backend
│   └── templates/
│       └── index.html      # Frontend UI
├── static/
│   └── style.css           # Styling
├── Dockerfile              # Container build instructions
└── README.md
```

Each file has a clear role:

* Backend evaluates password strength
* Frontend collects user input
* Docker isolates execution

---

## ▶️ Run the App Without Docker (Optional)

Running locally helps understand the flow before containerization.

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
docker build -t awscc-password-checker .
```

### Step 2️⃣ Run the Docker Container

```bash
docker run -p 5000:5000 awscc-password-checker
```

### Step 3️⃣ Access the Application

Open:

```
http://localhost:5000
```

---

## 🧪 Practice Tasks (Recommended)

* Try different passwords and observe strength changes
* Modify the strength rules in the backend
* Change UI text or colors
* Rebuild the Docker image after changes
* Stop and restart the container

These steps simulate **real security tool iteration**.

---

## 🎯 Key Takeaways

* Cyber security tools must be **safe and controlled**
* Docker provides isolation and predictability
* Security logic should never run directly on the host
* Containers are ideal for running security utilities

---

## 🏁 Final Note

This project shows that **cyber security is not about hacking**,
it is about **building safe, controlled, and reliable tools**.

Understanding how to containerize such tools is a **valuable industry skill**.

---

### 🐳 Build Once. Run Anywhere.

---