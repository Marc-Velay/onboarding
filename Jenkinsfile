pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''rm -rf env
                    virtualenv env
                    source env/bin/activate
                    pip3 install docker-compose
                    docker-compose up --build'''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    source env/bin/activate
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