pipeline { 
    agent any
    environment {
        IMAGE_NAME = "python-flask-app"
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')  // Use your credentials ID here
        DOCKERHUB_USERNAME = "${DOCKERHUB_CREDENTIALS_USR}"
        DOCKERHUB_REPO = "${DOCKERHUB_USERNAME}/${IMAGE_NAME}"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                bat """
                    docker build -t ${DOCKERHUB_REPO}:latest .
                """
            }
        }
        
        stage('Push to DockerHub') {
            steps {
                bat """
                    echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin
                    docker push ${DOCKERHUB_REPO}:latest
                    docker logout
                """
            }
        }
        
        stage('Run Container') {
            steps {
                bat """
                    for /f "tokens=*" %%i in ('docker ps -q --filter "name=${IMAGE_NAME}"') do docker stop %%i
                    for /f "tokens=*" %%i in ('docker ps -a -q --filter "name=${IMAGE_NAME}"') do docker rm %%i
                    docker pull ${DOCKERHUB_REPO}:latest
                    docker run -d -p 5000:5000 --name ${IMAGE_NAME} ${DOCKERHUB_REPO}:latest
                """
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
