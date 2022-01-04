pipeline {
    agent none

    options {
        disableConcurrentBuilds()
    }

    stages {
        stage('Init') {
            steps {
                sh 'sh script/init.sh'
            }
        }

        stage('Test') {
            agent {
                docker {
                    image("test")
                    args("--user root")
                }
            }
        }
        
        stage('permission') {
            steps {
                dir ('test') {
                    sh("chmod +x script/*")
                }
            }
            stage('plan') {
                dir('test') {
                    sh("pip install redis")
                    sh("source .env")
                    sh("python apim_redis.py")
                }
            }
        }


        stage('Deploy') {
            steps {
            sh 'echo deploying...'
            //  sh 'sh script/deploy.sh'
            }
        }
    }

    post {
        always {
        echo 'success'
        // dingTalk accessToken:'290c19dc81fce490ac73d1db02e36d7c177b6aa834b27cf8fd2c0a39a3238266', imageUrl:'', jenkinsUrl:'', message:'�~^~D建�~H~P�~J~_', notifyPeople:'Jenkins-PipeLine'
        }
        failure {
        echo 'failure'
        }
        unstable {
        echo 'unstable'
        }
        aborted {
        echo 'aborted'
        }
        changed {
        echo 'changed'
        }
    }
}
