# coding:utf-8
import os, sys
from source.AuxiliaryTools.ConfigTool import update_config

cur_dir = os.path.abspath(os.path.dirname(__file__))
if cur_dir not in sys.path:
    sys.path.append(cur_dir)

def refresh_config_file(config_path='./config.json'):
    print('Config Position:', config_path)
    # For my linux server setting
    update_config(os.path.join(cur_dir, "data"), config_path=config_path)


if __name__ == "__main__":
    refresh_config_file()
