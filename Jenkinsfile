pipeline { 
    environment { 
        registry = 'abhijeet6001/abhi123' 
        registryCredential = 'dockerhub_id' 
        dockerImage = '' 
    }
    agent any 
    stages { 
        stage('Cloning our Git') { 
            steps { 
                git branch: 'new-branch', changelog: false, poll: false, url: "https://github.com/abhiduish/Task1.git"
            }
        } 
        stage('Building our image') { 
            steps { 
                script { 
                    dockerImage = docker.build registry + ":$BUILD_NUMBER" 
                }
            } 
        }
        stage('Deploy our image') { 
            steps { 
                script { 
                    docker.withRegistry( '', registryCredential ) { 
                        dockerImage.push() 
                    }
                } 
            }
        } 
    }
}


// pipeline{
//     agent{ docker { image '<img-id>' } }
//     stages('build'){
//         steps {
//             sudo chmod +x <filename>
//         }
//     }

//     stages('post-build'){
//         steps {
            
//         }
//     }
// }




