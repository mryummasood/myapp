
pipeline {
    agent any
    environment {
        APP_IMAGE = "myapp:${BUILD_NUMBER}"
        TEST_IMAGE = "myapp-tests:${BUILD_NUMBER}"
    }
    stages {
        stage('Code Linting') {
            steps {
                sh 'pip3 install flake8'
                sh 'flake8 app.py --max-line-length=120'
            }
        }
        stage('Code Build') {
            steps {                sh 'docker build -t ${APP_IMAGE} .'
            }
        }
        stage('Containerized Deployment') {
            steps {
                sh 'docker stop myapp-container || true'
                sh 'docker rm myapp-container || true'
                sh 'docker run -d --name myapp-container -p 5000:5000 ${APP_IM>
                sh 'sleep 5'
            }
        }
        stage('Containerized Selenium T
