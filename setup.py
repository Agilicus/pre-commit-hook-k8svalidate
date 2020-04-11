"""Fake setup for pre-commit hook."""

from setuptools import setup

setup(
    name="k8svalidate",
    description="A pre-commit hook to validate Kubernetes YAML files",
    url="https://github.com/Agilicus/pre-commit-hook-k8svalidate",
    version="0.0.0",
    install_requires=["ruamel.yaml>=0.16.10", "kubernetes-validate>=1.16.0"],
    scripts=["pre_commit_hooks/k8svalidate"],
)
