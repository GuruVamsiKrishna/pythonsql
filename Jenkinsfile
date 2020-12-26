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
                    ssh -o StrictHostKeyChecking=no ubuntu@52.66.82.14
                    ssh ubuntu@52.66.82.14 ls -al
                    ssh ubuntu@52.66.82.14 sudo docker images
                    """
                }
            }
        }
        stage('Docker push to hub'){
            steps{
                echo "push the builded docker to hub"
                sshagent(['ec2login']) {
                sh """
                ssh ubuntu@52.66.82.14 docker build -t py .
                ssh ubuntu@52.66.82.14 docker images
                ssh ubuntu@52.66.82.14 docker run -d --name web1 py
                """
                }
            }
        }
        stage('ssh into ec2 and deploy the code'){
            steps{
                echo "deploy the container"
                sshagent(['ec2login']) {
                sh """
                ssh ubuntu@52.66.82.14 docker ps -a
                ssh ubuntu@52.66.82.14 docker logs web1
                """
            }
        }
    }
}
