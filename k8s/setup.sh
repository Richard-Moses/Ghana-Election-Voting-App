#!/bin/bash
echo "íº€ Deploying Ghana Election Voting App stack..."

kubectl apply -f redis-deployment.yaml
kubectl apply -f postgres-deployment.yaml
kubectl apply -f vote-app-deployment.yaml
kubectl apply -f worker-deployment.yaml
kubectl apply -f result-app-deployment.yaml
kubectl apply -f services.yaml

echo "âœ… All services deployed. Use 'kubectl get svc' to find access URLs."
