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
                bat '''
                    set PYTHONPATH=C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\data-analytics-app\\src
                    C:\\Users\\nishw\\AppData\\Local\\Programs\\Python\\Python311\\Scripts\\pytest.exe
                '''
            }
        }
        stage('Docker Build') {
            steps {
            script {
                    // Build the Docker image
                    bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" build -t "data-analytics-app:latest" .'
                    
                    // Optional: if you need to push the image to a Docker registry
                    // Authenticate with Docker registry if necessary
                    // bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'

                    // Push the Docker image
                    bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" push data-analytics-app:latest'
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
