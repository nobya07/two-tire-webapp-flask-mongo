# 🚀 Two-Tier Web App — Flask + MongoDB + Docker + Jenkins CI/CD

A fully automated two-tier web application with CI/CD pipeline. Every code push to GitHub automatically triggers Jenkins to build and deploy the application using Docker.

---

## 📸 Architecture

```
Developer → GitHub → Jenkins → Docker → Live App
  (push)   (trigger)  (CI/CD)  (containers)

┌─────────────────────────────────────────┐
│              Docker Network             │
│                                         │
│  ┌──────────────┐    ┌───────────────┐  │
│  │   Flask App  │───▶│   MongoDB     │  │
│  │  (port 5000) │    │  (port 27017) │  │
│  └──────────────┘    └───────────────┘  │
└─────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Flask | Web Framework (Frontend + Backend) |
| MongoDB | NoSQL Database |
| Docker | Containerization |
| Docker Compose | Multi-container Orchestration |
| Jenkins | CI/CD Pipeline Automation |
| GitHub | Source Code Management |

---

## 📁 Project Structure

```
two-tire-webapp/
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Flask container config
├── docker-compose.yml      # Multi-container setup
├── Jenkinsfile             # CI/CD pipeline definition
└── templates/
    └── index.html          # Frontend UI
```

---

## ⚙️ CI/CD Pipeline Flow

```
1. Developer pushes code to GitHub
2. Jenkins polls GitHub every minute (pollSCM)
3. Jenkins detects new commit
4. Pulls latest code
5. Builds new Docker image
6. Stops old containers
7. Starts new containers
8. App is live — zero manual work!
```

### Jenkins Pipeline Stages
```
Clone → Build Image → Deploy
  ✅         ✅          ✅
```

---

## 🚀 How to Run Locally

### Prerequisites
- Docker installed
- Docker Compose installed

### Steps

**1. Clone the repo**
```bash
git clone https://github.com/nobya07/two-tire-webapp-flask-mongo.git
cd two-tire-webapp-flask-mongo
```

**2. Start the containers**
```bash
docker-compose up --build
```

**3. Open in browser**
```
http://localhost:5000
```

**4. Stop containers**
```bash
docker-compose down
```

---

## 🔧 Jenkins Setup

### Prerequisites
- Jenkins installed
- Docker installed on Jenkins server
- Jenkins user added to docker group

```bash
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
```

### Create Jenkins Pipeline Job

```
1. Jenkins → New Item → Pipeline
2. Pipeline → Definition → Pipeline script from SCM
3. SCM → Git
4. Repository URL → https://github.com/nobya07/two-tire-webapp-flask-mongo.git
5. Branch → */main
6. Script Path → Jenkinsfile
7. Save → Build Now
```

### Jenkinsfile
```groovy
pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Clone') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/nobya07/two-tire-webapp-flask-mongo.git'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker-compose down && docker-compose up -d'
            }
        }
    }

    post {
        failure {
            echo 'Build Failed!'
        }
        success {
            echo 'Deployed Successfully!'
        }
    }
}
```

---

## 🌐 App Features

- Add records (Name, Email, Message) via UI
- Data stored in MongoDB
- View all records in real time
- Delete individual records
- REST API → `GET /api/records`

---

## 📝 What I Learned

- Two-tier application architecture
- Writing Dockerfiles and docker-compose
- Container networking in Docker
- Building Jenkins pipeline with Jenkinsfile
- Automating deployments with pollSCM trigger
- End-to-end CI/CD workflow

---

## 🔗 Connect

- GitHub: [nobya07](https://github.com/nobya07)

---

⭐ If you found this helpful, give it a star!
