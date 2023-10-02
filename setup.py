"""Fake setup for pre-commit hook."""

from setuptools import setup

setup(
    name="k8svalidate",
    description="A pre-commit hook to validate Kubernetes YAML files",
    url="https://github.com/Agilicus/pre-commit-hook-k8svalidate",
    version="0.1.1",
    install_requires=["ruamel.yaml>=0.16.10", "kubernetes-validate>=1.21.0"],
    scripts=["pre-commit-hooks/k8svalidate"],
)
