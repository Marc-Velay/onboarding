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
                    docker-compose -f docker-compose.test.yml -p onb up --build
                    echo `docker logs -f onb_sut_1`'''
            }
        }
        stage('Deploy') {
            steps{
                sh '''
                    rm -rf env
                    virtualenv env
                    source env/bin/activate
                    python -V
                    pip3 install docker-compose
                    ls
                    docker-compose -f docker-compose.yml up --build'''
            }
        }
    }
    post {
        always {
            sh ''' echo "done" '''
        }
    }
}