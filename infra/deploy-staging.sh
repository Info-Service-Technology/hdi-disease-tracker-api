#!/bin/bash
# infra/deploy-hom.sh

set -e

TAG=hom-${GITHUB_SHA::7}

# Gera artefato ZIP do Dockerrun.aws.json, Dockerfile etc
# (pode customizar conforme seu ambiente)

# Exemplo genérico Elastic Beanstalk Dockerrun.aws.json:
cat > Dockerrun.aws.json <<EOF
{
  "AWSEBDockerrunVersion": 1,
  "Image": {
    "Name": "hdi-disease-tracker-api:latest",
    "Update": "true"
  },
  "Ports": [
    {
      "ContainerPort": "8080"
    }
  ]
}
EOF

zip -r deploy.zip Dockerrun.aws.json Dockerfile .ebextensions/ app/ requirements.txt

# Deploy via EB CLI (faça login e configure antes!)
# eb init, eb labs etc podem ser rodados em step separado, ou use eb deploy diretamente!
eb deploy hom-env --label $TAG
