pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Activate virtual environment and install dependencies
                    bat """
                        python -m venv venv
                        call venv\\Scripts\\activate
                        pip install -r requirements.txt
                    """
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Activate virtual environment and run tests
                    bat """
                        call venv\\Scripts\\activate
                        pytest
                    """
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
