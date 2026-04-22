User → Ingress → FastAPI App → Groq API
                ↓
           Kubernetes (HPA auto-scale)
                ↓
        CI/CD (GitHub Actions)
                ↓
     Docker + Registry (Docker Hub)
                ↓
   Monitoring (Prometheus + Grafana)