pipeline {
  agent {
    docker {
      image "python:latest"
    }
    label "python-docker"
  }
  stages {
    stage("runApp") {
      sh "python3 main.py"
    }
  }
}
