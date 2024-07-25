pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Install dependencies directly using global Python installation
                     sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run tests using global Python installation
                    bat 'pytest'
                }
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    docker.build('data-analytics-app:latest')
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                script {
                    // Deploy application using kubectl
                    bat 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}
