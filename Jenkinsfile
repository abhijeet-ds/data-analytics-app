pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat '''
                    C:\\Users\\nishw\\AppData\\Local\\Programs\\Python\\Python311\\python.exe -m pip install --upgrade pip
                    C:\\Users\\nishw\\AppData\\Local\\Programs\\Python\\Python311\\python.exe -m pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                bat 'pytest'
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
                bat 'kubectl apply -f k8s\\deployment.yaml'
            }
        }
    }
}
