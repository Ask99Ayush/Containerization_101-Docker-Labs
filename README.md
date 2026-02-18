# 🐳 Containerization 101 – Docker Labs

**One repository. Multiple domains. Real Docker practice.**

> **Containerization_101-Docker-Labs** is a hands-on Docker learning repository designed for students from **Web Development, Machine Learning, and Cyber/Security** domains.
>
> This repo focuses on **learning Docker by practice**, not by heavy theory or large applications.

---

## 🎯 Why This Repository Exists

Most students struggle with Docker because they:

* Memorize commands ❌
* Copy-paste tutorials ❌
* Never understand *why* Docker is used ❌

This repository fixes that.

> **Here, you learn Docker by building images, running containers, breaking things, and fixing them.**

Each folder contains a **small, domain-related project** whose main goal is to help you:

* Write Dockerfiles
* Build Docker images
* Run containers
* Understand Docker’s role in real projects

---

## 🧠 Repository Structure (High-Level)

This is **ONE repository** with **MULTIPLE small Docker labs**, grouped by domain.

```
Containerization_101-Docker-Labs/
├── web/            # Web / Backend Docker labs
├── ml/             # Machine Learning Docker labs
├── cyber/          # Cyber / Security Docker labs
└── compose-labs/   # Multi-container systems (Advanced / Day 2)
```

👉 You **do not** need to work on everything.
👉 Choose the folder related to **your domain**.

---

## 🧑‍💻 Choose Your Domain

### 🟦 Web Development

Go to:

```
web/
```

You will practice:

* Backend containerization
* Port mapping
* Running web services inside Docker

---

### 🟩 Machine Learning

Go to:

```
ml/
```

You will practice:

* Reproducible ML environments
* Dependency management
* Running ML scripts and APIs in containers

---

### 🟥 Cyber / Security

Go to:

```
cyber/
```

You will practice:

* Running security-related tools safely
* Isolated execution using containers
* Packaging utilities with Docker


---

### 🧩 Multi-Container Systems (Advanced)

Go to:

```
compose-labs/
```

You will practice:

* Running multiple containers together
* Docker Compose
* Real-world system architecture
* Team-based workflows

---

## 📁 How Each Project Folder Is Designed

Every project folder follows the **same simple pattern**:

```
project-name/
├── Dockerfile
├── README.md
├── code files (app.py / model.py / index.html etc.)
└── requirements.txt (if needed)
```

This ensures:

* Each lab is independent
* Easy debugging & retry
* Focus stays on Docker, not app complexity

---

## 🧪 How to Use This Repository (Student Guide)

### Step 1️⃣ Clone the repository

```bash
git clone https://github.com/Ask99Ayush/Containerization_101-Docker-Labs.git
cd Containerization_101-Docker-Labs
```

### Step 2️⃣ Navigate to your domain folder

Example:

```bash
cd web/healthcheck-api
```

### Step 3️⃣ Follow the project README

Each project has its **own README.md** with:

* What the project does
* Why it exists
* Docker commands to try
* Suggested experiments

👉 **Always follow the README inside the project folder.**

---

## 🛠 Prerequisites

You need:

* A laptop 💻
* Docker Desktop installed 🐳
* Basic understanding of your domain

> ❗ No prior Docker knowledge is required.

---

## 📚 Learning Philosophy

This repository follows the:

> **Learn → Break → Fix → Understand** approach

You are encouraged to:

* Modify Dockerfiles
* Change ports
* Remove or add dependencies
* Read Docker error messages carefully

> **If you break something and fix it, you are learning correctly.**

---

## 🚀 How This Repo Is Used in Containerization 101 Bootcamp

### Day 1

* Students choose **one domain**
* Build **one Docker image**
* Run **one container**
* Understand Docker basics

### Day 2

* Students move to `compose-labs/`
* Run **multi-container systems**
* Learn real-world Docker workflows
* Work collaboratively in teams

---

## 🏁 Final Note

This is **not a showcase repository**.
This is a **practice lab**.

If something breaks — good.
If you understand *why* it broke — even better.

---

### 🐳 Containerization 101

**Build Once. Run Anywhere.**

---
