pipeline { 
    agent any

    environment {
        IMAGE_NAME = "python-flask-app"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                bat '''
                    docker --debug build -t %IMAGE_NAME% .
                '''
            }
        }
        stage('Run Container') {
            steps {
                bat '''
                    docker ps -q --filter "name=%IMAGE_NAME%" | findstr . >nul && docker stop %IMAGE_NAME%
                    docker ps -a -q --filter "name=%IMAGE_NAME%" | findstr . >nul && docker rm %IMAGE_NAME%
                    docker run -d -p 5000:5000 --name %IMAGE_NAME% %IMAGE_NAME%
                '''
            }
        }
    
    }

    post {
        success {
            echo 'Deployment successful! Flask app running at http://localhost:5000'
        }
        failure {
            echo 'Check Docker daemon configuration and agent permissions'
        }
    }
}
