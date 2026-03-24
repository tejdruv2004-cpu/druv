# Flask + Docker + GitHub Actions CI/CD

Prepared for **Druvtej kumar**.

This project demonstrates a production-style CI/CD pipeline for a simple Flask application using Docker and GitHub Actions.

## Run locally

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000` and you should see:

`Hello, World!`

## Run tests

```bash
pytest -v
```

## Docker commands

```bash
docker build -t flaskapp .
docker run -p 5000:5000 flaskapp
```

## CI/CD security notes

- **Why GitHub Secrets are used**
  - Secrets keep credentials (Docker Hub and SMTP) out of source code and commit history.
- **Key risks**
  - Secret leaks, unauthorized registry/account access, and supply chain attacks through compromised dependencies/actions.
- **Best practices**
  - Never hardcode credentials; always use secrets.
  - Rotate credentials regularly.
  - Apply least-privilege permissions.
  - Use environment protection rules and required reviewers for sensitive deployments.
