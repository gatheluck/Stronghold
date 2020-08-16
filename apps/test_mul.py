import os
import sys
import glob
import shutil
import hydra
import omegaconf
import logging


def check_target_mode(targetpath, targetdir, mode_candidates: list = ['train', 'transfer']) -> str:
    """
    this function check weather target path is train or transfer or unknown.
    targetpath should be like, 'hoge/logs/train/fbdb_train_runtime_index_0815/2020-08-15_10-13-39_mono_fba_weight-1.0_eps-4.0_index/model_weight_final.pth'
    """

    # remove final separator and adjust targetpath
    targetdir = targetdir[:-1] if targetdir.endswith(os.sep) else targetdir
    targetdir = os.sep.join(targetdir.split(os.sep)[:-1])
    targetpath = targetpath.replace(targetdir, '')

    # check mode from targetpath
    modes = list()
    for dirname in targetpath.split(os.sep):
        modes.extend([mode for mode in mode_candidates if mode in dirname])

    # remove redanduncy
    modes = list(set(modes))
    if len(modes) == 1:
        mode = modes[0]
    else:
        mode = 'unknown'

    return mode, targetpath.lstrip(os.sep).split(os.sep)[1]


def find_needles(targetdir: str, needle='model_weight_final.pth') -> list:
    """
    find needle form targetdir.
    """
    return glob.glob(os.path.join(targetdir, '**', needle), recursive=True)

# def get 


@hydra.main(config_path="../conf/test_mul.yaml")
def main(cfg: omegaconf.DictConfig):
    if cfg.targetdir is None:
        raise FileNotFoundError('Please specify targetdir.')
    elif not cfg.targetdir.startswith('/'):
        raise FileNotFoundError('Please use abspath to specify targetdir.')

    logger = logging.getLogger(__name__)
    logger.info(" ".join(sys.argv))
    logger.info(cfg.pretty())

    # find targets
    needles = find_needles(cfg.targetdir)

    if len(needles) == 0:
        logger.error('No targets are found.')
    else:
        logger.info('{} needles are found.'.format(len(needles)))

    for needle in needles:
        logger.info('run test: {}'.format(needle))

        # create output dir and copy
        mode, dirname = check_target_mode(needle, cfg.targetdir)
        os.makedirs(os.path.join(dirname, 'test'), exist_ok=True)
        if cfg.copy_needle:
            shutil.copytree(os.path.join(cfg.targetdir, dirname), os.path.join(dirname, mode))

        # run test




if __name__ == '__main__':
    main()
