pipeline {
     agent any

     stages {
        stage('Test') {
            steps {
                sh '''
                    rm -rf env
                    virtualenv env
                    source env/bin/activate
                    python -V
                    pip3 install docker-compose
                    ls
                    docker-compose -f docker-compose.test.yml build
                    docker-compose -f docker-compose.test.yml up
                    echo `docker logs -f api_1`'''
            }
        }
        stage('Deploy') {
            steps{
                sh '''
                    echo "DEPLOYING"
                    rm -rf env
                    virtualenv env
                    source env/bin/activate
                    ls
                    docker-compose -f docker-compose.yml up'''
            }
        }
    }
    post {
        always {
            sh ''' echo "done" '''
        }
    }
}