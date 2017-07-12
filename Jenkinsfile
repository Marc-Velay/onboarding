pipeline {
     agent any

     stages {
        stage('Build') {
            steps {
                sh '''
                    rm -rf env
                    virtualenv --python=python3.4 env
                    source env/bin/activate
                    pip install docker-compose
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