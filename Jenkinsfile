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
                }
            }
        }
        stage('Deploy to Minikube') {
            steps {
                    bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\kubectl.exe" config use-context minikube'
                    bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\kubectl.exe" apply -f k8s\\deployment.yaml --validate=false'
                    bat '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\kubectl.exe" apply -f k8s\\service.yaml --validate=false'
            }
        }
    }
}
