pipeline {
  agent any

  stages {
    
    stage('Init') {
      steps {
        sh 'sh script/init.sh'
      }
    }
//     post {
//       changed {
//          echo 'pipeline post changed by init'
//       }
//       always {
//          echo 'pipeline post always by init'
//       }
//       success {
//          echo 'pipeline post success by init'
//       }
//       // 省略其他条件块
//     }
  
    stage('Build') {
      steps {
        sh 'sh script/build.sh'
      }
    }

    stage('Test') {
      steps {
        sh 'echo testing...'
          
        sh "docker run --privileged --rm --name test test /bin/sh -c 'cd / && pip install redis'"
        sh "echo ${myImg.id} ||:"
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
      //当此Pipeline成功时打印消息
      echo 'success'
      // dingTalk accessToken:'290c19dc81fce490ac73d1db02e36d7c177b6aa834b27cf8fd2c0a39a3238266', imageUrl:'', jenkinsUrl:'', message:'构建成功', notifyPeople:'Jenkins-PipeLine'
    }
    failure {
      //当此Pipeline失败时打印消息
      echo 'failure'
    }
    unstable {
      //当此Pipeline 为不稳定时打印消息
      echo 'unstable'
    }
    aborted {
      //当此Pipeline 终止时打印消息
      echo 'aborted'
    }
    changed {
      //当pipeline的状态与上一次build状态不同时打印消息
      echo 'changed'
    }        
  }
}
