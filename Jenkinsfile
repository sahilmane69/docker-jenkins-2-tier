pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest tests/ -v'
            }
        }

        stage('Build & Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh 'docker login -u $USERNAME -p $PASSWORD'
                    sh 'docker build -t sahilmane74/docker-jenkins-2-tier:latest .'
                    sh 'docker push sahilmane74/docker-jenkins-2-tier:latest'
                }
            }
        }
    }
}
