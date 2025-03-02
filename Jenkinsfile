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
            agent {
                label 'jenkins-slave-dind'
            }
            steps {
                sh """
                    docker build -t ${DOCKERHUB_REPO}:latest .
                """
            }
        }
        
        stage('Push to DockerHub') {
            agent {
                label 'jenkins-slave-dind'
            }
            steps {
                sh """
                    echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin
                    docker push ${DOCKERHUB_REPO}:latest
                    docker logout
                """
            }
        }
        
        stage('Run Container') {
            steps {
                sh """
                   for container in \$(docker ps -q --filter "name=${IMAGE_NAME}"); do
                        docker stop "\$container"
                    done

                    for container in \$(docker ps -a -q --filter "name=${IMAGE_NAME}"); do
                        docker rm "\$container"
                    done
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