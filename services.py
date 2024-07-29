#!/usr/bin/env python3

import random

# Define services and their categories
SERVICES = {
    "stockage": [
        "Amazon S3",
        "Amazon Elastic Block Storage (EBS)",
        "Amazon Elastic File System (EFS)",
        "Amazon Simple Storage Service Glacier"
    ],
    "calcul": [
        "Amazon EC2",
        "Amazon EC2 Auto Scaling",
        "Amazon Elastic Container Services (ECS)",
        "Amazon EC2 Container Registry (ECR)",
        "AWS Elastic Beanstalk",
        "AWS Lambda",
        "Amazon Elastic Kubernetes Services (EKS)",
        "AWS Fargate"
    ],
    "base de donnees": [
        "Amazon Relational Database Service (RDS)",
        "Amazon Aurora",
        "Amazon Redshift",
        "Amazon DynamoDB"
    ],
    "reseau": [
        "Amazon VPC",
        "Elastic Load Balancing",
        "Amazon CloudFront",
        "AWS Transit Gateway",
        "Amazon Route 53",
        "AWS Direct Connect",
        "AWS VPN"
    ],
    "securite": [
        "AWS Identity and Access Management (IAM)",
        "AWS Organizations",
        "Amazon Cognito",
        "AWS Artifact",
        "AWS Key Management Service (KMS)",
        "AWS Shield"
    ],
    "gestion des couts": [
        "Rapport de cout et d'utilisation AWS",
        "Budgets AWS",
        "AWS Cost Explorer"
    ],
    "gestion et gouvernance": [
        "AWS Management Console",
        "AWS Config",
        "Amazon CloudWatch",
        "AWS Auto Scaling",
        "AWS Command Line Interface (CLI)",
        "AWS Trusted Advisor",
        "Outil AWS Well-Architected",
        "AWS CloudTrail"
    ]
}

def get_random_service(used_services):
    available_services = [(service, category) for category, services in SERVICES.items() for service in services if service not in used_services]
    if not available_services:
        return None, None
    service, category = random.choice(available_services)
    return service, category

def main():
    used_services = set()
    total_services = sum(len(services) for services in SERVICES.values())
    score = 0
    while len(used_services) < total_services:
        service, category = get_random_service(used_services)
        if service is None:
            break
        used_services.add(service)
        guess = input(f"Quelle est la categorie du service {service}? ")
        if guess.lower() == category.lower():
            score += 1
            print("Correct!")
        else:
            print(f"FAUX! la reponse correcte etait {category}.")
        print(f"Score actuel: {score}\n")

    print(f"score final est : {score} sur {total_services}.")

if __name__ == "__main__":
    main()
