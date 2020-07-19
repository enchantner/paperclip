@Library('powerpony@dev') _

pipeline {
    agent any
    environment {
        PYPI_USERNAME   = credentials('pypi_username')
        PYPI_PASS       = credentials('pypi_pass')
        PYPI_URL        = credentials('pypi_url')
    }
    stages {
        stage("Push package to PyPI repository") {
            when {
                branch 'master'
            }
            agent {
                docker { image 'python:3.8' }
            }
            steps {
                buildPythonPackage(PYPI_USERNAME, PYPI_PASS, PYPI_URL)
            }
        }
    }
}