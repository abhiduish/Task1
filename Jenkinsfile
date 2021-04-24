pipeline { 
    environment { 
        registry = "060504961461.dkr.ecr.ap-south-1.amazonaws.com/abhivouch" 
        registryCredential = 'aws-credentials'
        dockerImage = ''
    }
    agent any 
    stages { 
        stage('Cloning our Git') { 
            steps { 
                git branch: 'branch3', changelog: false, poll: false, url: "https://github.com/abhiduish/Task1.git"
            }
        } 
        stage('Building our image') { 
            steps { 
                script { 
                    dockerImage = docker.build registry 
                    docker.build('abhivouch')
                }
            } 
        }
        stage ('docker-push'){
            steps { 
                script {
                    docker.withRegistry("http://060504961461.dkr.ecr.ap-south-1.amazonaws.com/abhivouch", "ecr:ap-south-1:aws-credentials") {
                        docker.image("abhivouch").push()
                    }
                }
            }
        }
        stage('docker-run') {
            steps {
                script {
                    dockerImage.run("-p 8000:8000 --rm --name abhivouch1")
                }
            }
        }
    }
}
