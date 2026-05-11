pipeline {
    agent any
    stages {
        stage('Code Linting') {
            steps {
                sh 'pip3 install flake8 --break-system-packages'
                sh 'flake8 app.py --max-line-length=120'
            }
        }
        stage('Code Build') {
            steps {
                sh "docker build -t myapp:${BUILD_NUMBER} ."
            }
        }
        stage('Containerized Deployment') {
            steps {
                sh 'docker stop myapp-container || true'
                sh 'docker rm myapp-container || true'
                sh "docker run -d --name myapp-container -p 5000:5000 myapp:${BUILD_NUMBER}"
                sh 'sleep 5'
            }
        }
        stage('Containerized Selenium Testing') {
            steps {
                sh "docker build -f Dockerfile.test -t myapp-tests:${BUILD_NUMBER} ."
                sh 'docker run --rm --network host myapp-tests:latest'
            }
        }
    }
    post {
        always {
            sh 'docker stop myapp-container || true'
            sh 'docker rm myapp-container || true'
        }
    }
}
