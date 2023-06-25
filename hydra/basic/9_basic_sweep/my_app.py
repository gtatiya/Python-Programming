# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from omegaconf import DictConfig

import hydra


@hydra.main(version_base=None, config_path="conf", config_name="config")
def my_app(cfg: DictConfig) -> None:
    print(f"driver={cfg.db.driver}, timeout={cfg.db.timeout}")


if __name__ == "__main__":
    my_app()


'''
https://hydra.cc/docs/tutorials/basic/running_your_app/multi-run/

python 9_basic_sweep/my_app.py -m db=mysql
'''
