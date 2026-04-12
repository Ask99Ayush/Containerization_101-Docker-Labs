# Containerization 101 – Docker Hands-On Bootcamp Projects

## One repository. Multiple domains. Practical Docker learning.

---

## Table of Contents

* [Overview](#overview)
* [Objectives](#objectives)
* [Why This Repository Exists](#why-this-repository-exists)
* [Repository Structure](#repository-structure)
* [Domain-Based Learning Paths](#domain-based-learning-paths)

  * [Web Development](#web-development)
  * [Machine Learning](#machine-learning)
  * [Cyber Security](#cyber-security)
  * [Multi-Container Systems](#multi-container-systems)
* [Project Design Philosophy](#project-design-philosophy)
* [Getting Started](#getting-started)
* [Prerequisites](#prerequisites)
* [Docker Workflow Explained](#docker-workflow-explained)
* [Hands-On Learning Approach](#hands-on-learning-approach)
* [Bootcamp Structure](#bootcamp-structure)
* [Best Practices Followed](#best-practices-followed)
* [Common Mistakes and How to Avoid Them](#common-mistakes-and-how-to-avoid-them)
* [Expected Learning Outcomes](#expected-learning-outcomes)
* [Future Enhancements](#future-enhancements)

---

## Overview

This repository is a structured, hands-on learning resource developed as part of the **Containerization 101 Docker Hands-On Bootcamp**.

It is designed to help students understand Docker through practical implementation rather than theoretical concepts.

The repository contains multiple small, focused projects across different domains including Web Development, Machine Learning, and Cyber Security. Each project is intentionally kept simple so that the focus remains on containerization concepts rather than application complexity.

---

## Objectives

The primary objectives of this repository are:

* To introduce Docker fundamentals through real use cases
* To enable students to build and run containerized applications
* To demonstrate how Docker works across multiple domains
* To provide a structured environment for experimentation and debugging
* To prepare students for real-world development and deployment workflows

---

## Why This Repository Exists

Many learners struggle with Docker because they rely on passive learning methods such as:

* Memorizing commands without understanding
* Following tutorials without experimentation
* Avoiding debugging scenarios

This repository addresses those gaps by emphasizing active learning.

Each project is designed to:

* Encourage exploration
* Introduce controlled failure scenarios
* Reinforce understanding through iteration

The goal is not just to run containers, but to understand how and why they work.

---

## Repository Structure

The repository is organized into domain-specific directories:

```
containerization-101-docker-hands-on-bootcamp-projects/
├── web/
├── ml/
├── cyber/
└── compose-labs/
```

Each directory represents a different application domain and contains multiple independent projects.

---

## Domain-Based Learning Paths

### Web Development

Location:

```
web/
```

Focus areas:

* Backend service containerization
* Port exposure and mapping
* Running APIs inside containers
* Debugging runtime issues

Typical technologies:

* Python Flask / Node.js
* REST APIs
* Lightweight web services

---

### Machine Learning

Location:

```
ml/
```

Focus areas:

* Reproducible environments
* Dependency management
* Running ML scripts inside containers
* Model execution consistency

Typical components:

* Python scripts
* Requirements management
* Lightweight inference pipelines

---

### Cyber Security

Location:

```
cyber/
```

Focus areas:

* Safe execution of security tools
* Isolation using containers
* Packaging command-line utilities
* Controlled testing environments

---

### Multi-Container Systems

Location:

```
compose-labs/
```

Focus areas:

* Docker Compose
* Multi-service architecture
* Inter-container communication
* Real-world deployment simulation

---

## Project Design Philosophy

Each project follows a consistent structure:

```
project-name/
├── Dockerfile
├── README.md
├── application code
└── dependency files
```

Design principles:

* Minimal application complexity
* Maximum Docker exposure
* Independent execution
* Easy reproducibility

---

## Getting Started

### Step 1: Clone the repository

```
git clone https://github.com/Ask99Ayush/Containerization_101-Docker-Hands-On-Bootcamp-Projects.git
cd Containerization_101-Docker-Hands-On-Bootcamp-Projects
```

### Step 2: Navigate to a project

```
cd web/sample-project
```

### Step 3: Build the Docker image

```
docker build -t project-name .
```

### Step 4: Run the container

```
docker run -p 5000:5000 project-name
```

---

## Prerequisites

Ensure the following are installed:

* Docker Desktop
* Git
* Basic familiarity with command line
* Fundamental knowledge of your chosen domain

No prior Docker experience is required.

---

## Docker Workflow Explained

The standard workflow followed in this repository:

1. Write a Dockerfile
2. Build an image using the Dockerfile
3. Run a container from the image
4. Test the application
5. Debug and optimize

This cycle is repeated across all projects to reinforce understanding.

---

## Hands-On Learning Approach

This repository follows a practical learning model:

* Build first, understand later
* Encourage experimentation
* Introduce errors intentionally
* Learn through debugging

Users are expected to:

* Modify Dockerfiles
* Change configurations
* Observe failures
* Fix issues independently

---

## Bootcamp Structure

### Day 1

* Introduction to Docker
* Building first image
* Running containers
* Understanding Dockerfile basics

### Day 2

* Working with Docker Compose
* Multi-container applications
* Team-based problem solving
* Real-world workflow simulation

---

## Best Practices Followed

* Use of lightweight base images
* Clear separation of concerns
* Minimal and readable Dockerfiles
* Consistent folder structure
* Environment reproducibility

---

## Common Mistakes and How to Avoid Them

1. Building unnecessarily large images

   * Use minimal base images

2. Hardcoding configurations

   * Use environment variables

3. Ignoring logs

   * Always inspect container logs

4. Not understanding port mapping

   * Clearly define exposed ports

5. Copying entire directories blindly

   * Use .dockerignore effectively

---

## Expected Learning Outcomes

After completing this repository, users should be able to:

* Write Dockerfiles confidently
* Build and run Docker images
* Understand container lifecycle
* Debug container-related issues
* Work with multi-container setups
* Apply Docker concepts in real projects

---

## Future Enhancements

Planned improvements include:

* Integration with cloud platforms
* CI/CD pipeline examples
* Kubernetes introduction
* Advanced networking scenarios
* Security best practices in containers

---

## Final Note

This repository is not intended to showcase complex applications.
Its purpose is to build strong foundational understanding through practice.

If something fails, investigate it.
If you fix it, you have learned something valuable.

---
