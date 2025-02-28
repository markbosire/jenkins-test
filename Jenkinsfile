pipeline {
    agent any

    environment {
        IMAGE_NAME = "python-flask-app"
    }
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    
                        sh '''
                            export DOCKER_TLS_VERIFY=0,
                            export DOCKER_HOST=tcp://localhost:2375,
                            unset DOCKER_CERT_PATH'
                            printenv | grep TLS
                            docker info
                            docker --debug build -t ${IMAGE_NAME} .
                        '''
                    
                }
            }
        }
        stage('Run Container') {
            steps {
                sh '''
                    docker stop ${IMAGE_NAME} || true
                    docker rm ${IMAGE_NAME} || true
                    docker run -d -p 5000:5000 --name ${IMAGE_NAME} ${IMAGE_NAME}
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