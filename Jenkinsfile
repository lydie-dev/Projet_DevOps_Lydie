pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/lydie-dev/Projet_DevOps_Lydie.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t flask-app .'
            }
        }

        stage('Run') {
            steps {
                sh 'docker rm -f flask-app || true'
                sh 'docker run -d --name flask-app -p 5001:5000 flask-app'
            }
        }
    }
}
