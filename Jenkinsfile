pipeline {
     agent any

     stages {
        stage('Build') {
            steps {
                sh '''
                    pip install virtualenv
                    virtualenv env
                    source env/bin/activate
                    pip3 install docker-compose==1.10.1
                    ls
                    docker-compose up --build'''
            }
        }
        stage('Test') {
            steps{
                sh '''
                    source bin/activate
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