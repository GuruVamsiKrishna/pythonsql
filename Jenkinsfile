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
            }
        }
        stage('Docker push to hub'){
            steps{
                echo "push the builded docker to hub"
            }
        }
        stage('ssh into ec2 and deploy the code'){
            steps{
                echo "deploy the container"
            }
        }
    }
}