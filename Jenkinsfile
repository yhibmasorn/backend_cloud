pipeline{
    agent any
    environment {
        PROJECT_ID = 'yhibmasorn'
        DOCKER_IMAGE = 'gcr.io/${PROJECT_ID}/backend_cloud:${BUILD_NUMBER}'
        REGION = 'asia-southeast1'
        SERVICE_NAME = 'backend-cloud-api-service'
    }

    stages{
        stage('Checkout'){
            steps{
                checkout scm

            }

        }

        stage('Build and Push Image'){
            steps{
                script{
                    withCredentials([file(credentialsId: 'jenkins-service-account', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                        sh '''
                        gcloud auth activate-service-account --key-file=$GOOGLE_APPLICATION_CREDENTIALS
                        gcloud auth configure-docker
                        '''

                        sh "docker build -t ${DOCKER_IMAGE} ."
                        sh "docker push ${DOCKER_IMAGE}"

                    }
                }

            }

        }

        stage('Deploy'){
            steps{
                script{
                    withCredentials([file(credentialsId: 'jenkins-service-account', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                        sh """
                        gcloud run deploy ${SERVICE_NAME} \
                          --image ${DOCKER_IMAGE} \
                          --platform managed \
                          --region ${REGION} \
                          --allow-unauthenticated \
                          --project ${PROJECT_ID}
                        """
                    }
                }

            }
        }

    }

    post{
        always{
            echo 'Pipeline execution complete.'
        }

    }

}