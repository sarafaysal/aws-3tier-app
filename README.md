# AWS 3-Tier Web Application

A full-stack application demonstrating a secure, production-style 3-tier architecture on AWS, built as part of my DevOps internship (DecodeLabs, Batch 2026).

## Architecture

- **Frontend (React + Vite)** — deployed on an EC2 instance in a **public subnet**, the only publicly accessible layer.
- **Backend (Python + Flask)** — deployed on an EC2 instance in a **private subnet**, reachable only from the frontend.
- **Database (PostgreSQL)** — deployed on an EC2 instance in a **private subnet**, reachable only from the backend.

Internet
│
▼
[ ALB / HTTPS ]
│
▼
[ Frontend EC2 - Public Subnet ]
│  (private IP)
▼
[ Backend EC2 - Private Subnet ]
│  (private IP)
▼
[ Database EC2 - Private Subnet ]

### Networking
- Custom **VPC** with 1 public and 1 private subnet
- **NAT Gateway** allows private instances to reach the internet (e.g. for package installs) without being exposed to it
- **Security Groups** enforce least-privilege access:
  - Frontend: accepts HTTP/HTTPS from the internet, SSH from admin IP
  - Backend: accepts traffic only from Frontend's security group
  - Database: accepts traffic only from Backend's security group

## How it works

1. User visits the frontend in their browser and enters text into the input box.
2. On clicking **Insert**, the frontend sends a POST request to the backend's `/insert` endpoint, using the backend's private IP.
3. The backend receives the text, appends the current server-side date & time, and inserts the record into PostgreSQL.
4. The frontend calls the backend's `/entries` endpoint (GET) to fetch and display all stored entries.

## Tech Stack

| Layer     | Technology         |
|-----------|---------------------|
| Frontend  | React (Vite)         |
| Backend   | Python, Flask, Flask-CORS |
| Database  | PostgreSQL            |
| Infra     | AWS EC2, VPC, NAT Gateway, Security Groups, (ALB + Route 53/Namecheap — in progress) |

## Project Structure
aws-3tier-app/
├── frontend/     # React application
├── backend/      # Flask API
│   ├── app.py
│   └── requirements.txt
└── README.md

## Running Locally / On EC2

**Backend**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

**Frontend**
```bash
cd frontend
npm install
npm run dev -- --host
```

## Status
- [x] VPC, subnets, NAT Gateway, security groups configured
- [x] PostgreSQL database deployed and configured
- [x] Flask backend deployed, connected to database
- [x] React frontend built and connected to backend
- [x] Custom domain (Namecheap) + HTTPS via ALB


