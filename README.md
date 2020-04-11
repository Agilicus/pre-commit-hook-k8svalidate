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
