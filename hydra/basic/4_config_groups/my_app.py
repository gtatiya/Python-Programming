# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from omegaconf import DictConfig, OmegaConf

import hydra


@hydra.main(version_base=None, config_path="conf")
def my_app(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()

'''
python 4_config_groups/my_app.py
python 4_config_groups/my_app.py +db=postgresql
python 4_config_groups/my_app.py +db=postgresql db.timeout=20
'''
