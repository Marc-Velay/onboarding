pipeline {
     agent any

     stages {
        stage('Build') {
            steps {
                sh '''
                    ls
                    docker-compose up --build'''
            }
        }
        stage('Test') {
            steps{
                sh '''
                    docker-compose run web python3 manage.py test'''
            }
        }
    }
    post {
        always {
            sh ''' echo "done" '''
        }
    }
}