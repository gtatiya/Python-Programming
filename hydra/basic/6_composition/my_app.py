# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from omegaconf import DictConfig, OmegaConf

import hydra


@hydra.main(version_base=None, config_path="conf", config_name="config")
def my_app(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))


if __name__ == "__main__":
    my_app()

'''
python 6_composition/my_app.py

python 6_composition/my_app.py hydra.mode=MULTIRUN db=mysql,postgresql schema=warehouse,support,school
python 6_composition/my_app.py --multirun db=mysql,postgresql schema=warehouse,support,school
python 6_composition/my_app.py -m db=mysql,postgresql schema=warehouse,support,school
python 6_composition/my_app.py -m db=mysql

# just show the config without running your function:
python 6_composition/my_app.py --cfg job
python 6_composition/my_app.py --cfg hydra
python 6_composition/my_app.py --cfg all

# use --package or -p to display a subset of the configuration:
python 6_composition/my_app.py --cfg hydra --package hydra.job

# The --info flag can provide information about various aspects of Hydra and your application:
python 6_composition/my_app.py --info all
python 6_composition/my_app.py --info config
python 6_composition/my_app.py --info defaults
python 6_composition/my_app.py --info defaults-tree
python 6_composition/my_app.py --info plugins

'''
