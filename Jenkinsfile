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
                    docker stop %IMAGE_NAME% || exit 0
                    docker rm %IMAGE_NAME% || exit 0
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
