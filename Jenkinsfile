pipeline {
  agent {
    docker {
      image "python:latest"
      label "first-vm"
    }
  }
  stages {
    stage("runApp") {
      steps {
        sh "python3 main.py"
      }
    }
  }
}
