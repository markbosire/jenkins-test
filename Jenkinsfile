pipeline { 
    agent any
    environment {
        IMAGE_NAME = "python-flask-app"
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')  // Use your credentials ID here
        DOCKERHUB_USERNAME = "${env.DOCKERHUB_CREDENTIALS_USR}"
        DOCKERHUB_REPO = "${DOCKERHUB_USERNAME}/${IMAGE_NAME}"
    }

    stages {
        stage('Checkout') {
               
                steps {
                    checkout scm
                }
            }
        stage('Build Docker Image') {
           
            steps {
                sh '''
                    docker build -t ${DOCKERHUB_REPO}:latest .
                '''
            }
        }
        
        stage('Push to DockerHub') {
            agent {
                label 'jenkins-slave-dind'
            }
            steps {
                sh '''
                    echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin
                    docker push ${DOCKERHUB_REPO}:latest
                    docker logout
                '''
            }
        }
        
        stage('Run Container') {
            // This stage doesn't use the Docker slave as requested
            agent { label '!built-in' }
            steps {
                bat '''
                    docker ps -q --filter "name=%IMAGE_NAME%" | findstr . >nul && docker stop %IMAGE_NAME%
                    docker ps -a -q --filter "name=%IMAGE_NAME%" | findstr . >nul && docker rm %IMAGE_NAME%
                    docker pull %DOCKERHUB_USERNAME%/%IMAGE_NAME%:latest
                    docker run -d -p 5000:5000 --name %IMAGE_NAME% %DOCKERHUB_USERNAME%/%IMAGE_NAME%:latest
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