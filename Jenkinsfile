pipeline{
    agent any
    environment{
        def tag = "latest"
    }
    stages{
        stage('scm check out the code'){
            steps{
                echo "checking out the code from git source branch"
            }
        }
        stage('Docker build'){
            steps{
                echo "build the docker image with the current build"
                sh 'ls -al'
                sshagent(['ec2login']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ubuntu@15.206.73.0
                    ssh ubuntu@15.206.73.0 ls -al
                    ssh ubuntu@15.206.73.0 sudo docker images
                    ssh sudo docker rm -f web1
                    """
                }
            }
        }
        stage('Docker push to hub'){
            steps{
                echo "push the builded docker to hub"
                sshagent(['ec2login']) {
                sh """
                ssh ubuntu@15.206.73.0 sudo docker build -t py .
                ssh ubuntu@15.206.73.0 sudo docker images
                ssh ubuntu@15.206.73.0 sudo docker run -d --name web1 py
                """
                }
            }
        }
        stage('ssh into ec2 and deploy the code'){
            steps{
                echo "deploy the container"
                sshagent(['ec2login']) {
                sh """
                ssh ubuntu@15.206.73.0 sudo docker ps -a
                ssh ubuntu@15.206.73.0 sudo docker logs web1
                """
                }
            }
        }
    }
}
