# Trivy Demo

Install [instructions](https://aquasecurity.github.io/trivy/v0.18.3/installation/)

## Running locally

```sh
trivy fs .
```

This will scan for python dependency files (Pipfile.lock or requirements.txt) and check for vulnerabilities.