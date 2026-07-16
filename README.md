# 🚀 AWS Three-Tier Web Application

A secure three-tier web application deployed on **Amazon Web Services (AWS)** using **React**, **Python (Flask)**, and **PostgreSQL**. The application is designed following cloud architecture best practices with isolated networking, HTTPS, and a custom domain.

---

## 🌐 Live Demo

🔗 https://sarafaysal.site

---

# 📖 Project Overview

This project demonstrates the deployment of a secure three-tier web application on AWS.

The application consists of:

- **Frontend:** React (User Interface)
- **Backend:** Python Flask REST API
- **Database:** PostgreSQL

The frontend sends user input to the backend, which appends the current date and time before storing the data in PostgreSQL.

Only the frontend is publicly accessible, while the backend and database remain securely isolated inside private subnets.

---

# 🏗 Architecture

```
                    Internet
                        │
                        ▼
             Route 53 (Custom Domain)
                        │
                        ▼
         Application Load Balancer (HTTPS)
                        │
                        ▼
              Frontend EC2 (React)
                Public Subnet
                        │
              Private IP Communication
                        ▼
            Backend EC2 (Python Flask)
                Private Subnet
                        │
                        ▼
             PostgreSQL Database EC2
                Private Subnet
```

---

# ☁ AWS Services Used

- Amazon EC2
- Amazon VPC
- Public & Private Subnets
- Security Groups
- Internet Gateway
- Route Tables
- Application Load Balancer (ALB)
- AWS Certificate Manager (ACM)
- Amazon Route 53

---

# 💻 Technology Stack

### Frontend
- React
- Vite
- JavaScript
- HTML
- CSS

### Backend
- Python
- Flask
- REST API

### Database
- PostgreSQL

---

# ✨ Features

- Three-tier cloud architecture
- Secure VPC networking
- Public and private subnet isolation
- HTTPS using ACM SSL Certificate
- Custom domain with Route 53
- Application Load Balancer
- REST API communication
- PostgreSQL data storage
- Secure backend using private IP communication

---

# 📂 Project Structure

```
aws-3tier-app/
│
├── backend/
│
├── frontend/
│
├── screenshots/
│
├── README.md
│
└── .gitignore
```

---

# 🔄 Application Workflow

1. User enters text in the React frontend.
2. Frontend sends the request to the Python backend.
3. Backend appends the current date and time.
4. Backend stores the processed data in PostgreSQL.
5. Data is successfully saved in the database.

---

# 🔒 Network Architecture

- Frontend deployed in a **Public Subnet**
- Backend deployed in a **Private Subnet**
- PostgreSQL deployed in a **Private Subnet**
- Backend communicates with the database over a private network.
- Only the frontend is exposed to the internet through an Application Load Balancer.

---

# 🌍 HTTPS & Domain

The application is accessible through a custom domain secured using SSL/TLS.

- **Domain:** https://sarafaysal.site
- **SSL Certificate:** AWS Certificate Manager (ACM)
- **DNS Management:** Amazon Route 53

---

# 📸 Screenshots

> Add screenshots inside the `screenshots` folder and update the filenames below.

### AWS Architecture

![Architecture](screenshots/architecture.png)

### EC2 Instances

![EC2](screenshots/ec2-instances.png)

### Application Load Balancer

![ALB](screenshots/load-balancer.png)

### Route 53

![Route53](screenshots/route53.png)

### ACM Certificate

![ACM](screenshots/acm-certificate.png)

### Application

![Application](screenshots/application-ui.png)

### PostgreSQL Database

![Database](screenshots/database.png)

---

# 🚀 Future Improvements

- Dockerize the application
- CI/CD pipeline using GitHub Actions
- Infrastructure as Code using Terraform
- Auto Scaling Group
- Amazon CloudWatch Monitoring
- AWS WAF integration
- Secrets management using AWS Secrets Manager

---

# 👩‍💻 Author

**Sara Faysal**

Bachelor's in Data Science — GIKI

GitHub: https://github.com/sarafaysal

LinkedIn: https://www.linkedin.com/in/sara-faysal-700904326

---

## ⭐ If you found this project helpful, consider giving it a star!
