// pipeline {
//     agent any

//     stages {
//         stage('Build') {
//             steps {
//                 echo "build complted successful"
//             }
//         }

//         stage('Test') {
//             steps {
//                 echo "test complted successful"
//             }
//         }

//         stage('Package') {
//             steps {
//                 echo "Package complted successful"
//             }
//         }

//         stage('Deploy') {
//             steps {
//                 echo "deploy complted successful"
//             }
//         }
//     }
 
// }





pipeline {
    agent any

    environment {
        LABS = credentials('labcreds') 
        }
        
    stages{
        stage('Build')
            steps {
                sh 'pip install --user pipenv'
                sh '/bitnami/jenkins/home/.local/bin/pipenv --rm || exit 0'
                sh '/bitnami/jenkins/home/.local/bin/pipenv install'
            }
        }

        stage('Test') {
            steps {
                sh '/bitnami/jenkins/home/.local/bin/pipenv run pytest'
            }
        }

        stage('Package') {
            steps {
                sh 'zip -r retailproject.zip .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'sshpass -p $LABS_PSW scp -o StrictHostKeyChecking=no -r .
                $LABS_USR@g02.itversity.com:/home/itv005857/retailproject'
            }
        }
    }
}