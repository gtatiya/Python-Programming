# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
import logging

from omegaconf import DictConfig

import hydra

# A logger for this file
log = logging.getLogger(__name__)


@hydra.main(version_base=None)
def my_app(_cfg: DictConfig) -> None:
    log.info("Info level message")
    log.debug("Debug level message")


if __name__ == "__main__":
    my_app()

'''
python 8_logging/my_app.py

# enable DEBUG level logging
python 8_logging/my_app.py hydra.verbose=true

# disable the logging output
python 8_logging/my_app.py hydra/job_logging=disabled
'''
