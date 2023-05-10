"""Dataset creation pipeline config"""
import os

from dataclasses import dataclass


# pylint: disable=invalid-name
@dataclass
class GeneralConfig:
    """
    General configs
    Params:
        GCP_PROJECT_ID (str): the id of the gcp project
        ENV (str): the project run environment (sbx, dev, prd)
    """

    GCP_PROJECT_ID = "soy-audio-379412"
    ENV = os.environ.get("ENV", "dev")


@dataclass
class KubeflowConfig(GeneralConfig):
    """
    Configs for the Kubeflow cluster
    Params:
        BASE_PATH (str): the base path used to store the artifacts
        CLUSTER_NAME (str): the name of the k8 cluster hosting KFP
        CLUSTER_ZONE (str): the zone of the k8 cluster hosting KFP
        HOST (str): the kfp host url
    """

    BASE_PATH = "gcs://soy-audio-379412_kfp-artifacts/custom_artifact"
    CLUSTER_NAME = "kfp-fondant"
    CLUSTER_ZONE = "europe-west4-a"
    HOST = "https://52074149b1563463-dot-europe-west1.pipelines.googleusercontent.com/"