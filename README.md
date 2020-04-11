## k8svalidate

This is a [pre-commit](https://pre-commit.com/) hook to validate input YAML
against the Kubernetes API specification.

It will ignore input YAML which are not Kubernetes
types (including unknown CRD and unknown other files).
If they do match a known API, they are checked.

It uses [kubernetes-validate](https://github.com/willthames/kubernetes-validate)
as an upstream.

## Usage:

```
k8s-validate [--kubernetes-version X.X.X] [--exclude glob-pattern] files
```

Add a section similar to this to your .pre-commit-hooks.yaml:
  - repo: https://github.com/Agilicus/pre-commit-hook-k8svalidate.git
    rev: v0.0.4
    hooks:
      - id: k8svalidate
        args: [--exclude, "*.patch.yaml"]
        files: .yaml$
