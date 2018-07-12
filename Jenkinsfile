#!/usr/bin/env groovy

node('master') {
    def SLACK_CHANNEL = "#jenkins-slack-testing"

    try {
        //library
        def LIBRARY_BRANCH = 'master'

        //repos
        def CONFIG_BRANCH = 'master'
        def CONFIG_DIR = 'config'
        def GIT_CREDS = 'github-private'

        def TOOLS_DIR = 'tools'
        def TOOLS_BRANCH = 'master'

        // choice param used as params.env and cron trigger
        properties([
            parameters([
                choice(choices: 'sandbox',
                description: '',
                name: 'env')])
        ])

        ansiColor('xterm') {
            //grab libraries
            library identifier: "broker@${LIBRARY_BRANCH}", retriever: modernSCM([
                $class: 'GitSCMSource',
                credentialsId: "${GIT_CREDS}",
                remote: "git@github.com:fedspendingtransparency/data-act-broker-config.git",
                ])

            stage ("pull repos") {
                deleteDir()
                dir("${CONFIG_DIR}") {
                    git url: 'git@github.com:fedspendingtransparency/usaspending-config.git',
                    credentialsId: "${GIT_CREDS}",
                    branch: "${CONFIG_BRANCH}"
                    sh """pwd"""
                }

                dir("${TOOLS_DIR}") {
                  git url: 'https://github.com/fedspendingtransparency/data-act-build-tools.git',
                  // temporary branch: "${TOOLS_BRANCH}"
                  branch: "jenkins-pipeline-setup"
                }
            } // pull repos stage

            stage('Copy Configs') {
                sh """
                ### configs for API
                cp ${CONFIG_DIR}/deploy/ansible-vars-${params.env}.yml ${TOOLS_DIR}/usaspending-deploy/
                cp ${CONFIG_DIR}/deploy/terraform-api/usaspending-packer.json ${TOOLS_DIR}/usaspending-deploy/
                cp ${CONFIG_DIR}/deploy/terraform-api/usaspending-start-${params.env}.sh ${TOOLS_DIR}/usaspending-deploy/
                cp ${CONFIG_DIR}/deploy/terraform-api/vars-${params.env}.tf.json ${TOOLS_DIR}/usaspending-deploy/usaspending-vars.tf.json 

                ### configs for Bulk-Download
                cp ${CONFIG_DIR}/deploy/ansible-vars-${params.env}.yml ${TOOLS_DIR}/usaspending-deploy/bulk-download/${params.env}-bulk-download-vars-ansible.yml
                cp ${CONFIG_DIR}/deploy/terraform-bulk-download/${params.env}-bulk-download-vars.tf.json ${TOOLS_DIR}/usaspending-deploy/bulk-download/usaspending-bulk-download-vars.tf.json
                """
            } // copy configs

            stage('Run Terraform init') {
                sh """
                cd ${TOOLS_DIR}/usaspending-deploy/
                /opt/terraform/terraform init .
                cd bulk-download
                /opt/terraform/terraform init .
                """
            } // terraform stage

            stage('Deploy API') {
                sh """
                cd ${TOOLS_DIR}/usaspending-deploy/
                python3.5 -u usaspending-deploy.py --${params.env}
                """
            } // deploy API stage

            stage('Deploy BulkDownload') {
                sh """
                cd ${TOOLS_DIR}/usaspending-deploy/bulk-download/
                python3.5 -u usaspending-bulk-download-deploy.py --${params.env}
                """
            } // deploy BD stage
        } // ansi color
    } catch (e) {
        currentBuild.result = "FAILED"
        throw e
    } finally {
        slack(currentBuild.result, "${SLACK_CHANNEL}")
    }
} //node
