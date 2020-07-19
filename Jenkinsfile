@Library('powerpony@dev') _
pipeline {
        agent any
        stages {
            stage("Push package to PyPI repository") {
                when {
                    branch 'master'
                }
                agent {
                    docker { image 'python:3.8' }
                }
                steps {
                    buildPythonPackage()
                }
            }
        }
    }