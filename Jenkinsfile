pipeline {
     agent any

     stages {
        stage('Build') {
            steps {
                sh '''
                    rm -rf env
                    virtualenv env
                    source env/bin/activate
                    python -V
                    pip3 install docker-compose
                    ls
                    docker-compose up --build
                    docker-compose down'''
            }
        }
        stage('Test') {
            steps{
                sh '''
                    deactivate
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