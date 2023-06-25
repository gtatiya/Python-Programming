# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from omegaconf import DictConfig, OmegaConf

import hydra


@hydra.main(version_base=None, config_path="conf", config_name="config")
def my_app(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()

'''
python 5_defaults/my_app.py
python 5_defaults/my_app.py db=postgresql db.timeout=20
python 5_defaults/my_app.py db=postgresql ~db
'''
