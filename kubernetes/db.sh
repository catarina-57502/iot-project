export PROJECT_ID=$(gcloud info --format='value(config.project)')
gcloud services enable cloudapis.googleapis.com  container.googleapis.com containerregistry.googleapis.com
gcloud container clusters create cluster-steam --zone northamerica-northeast1-a --num-nodes 1 --enable-autoscaling --min-nodes 1 --max-nodes 1 --enable-autorepair

# Kubernetes Apply YAML files
kubectl apply -f mongo-secrets.yaml
kubectl apply -f pv.yaml
kubectl apply -f deployment.yaml
