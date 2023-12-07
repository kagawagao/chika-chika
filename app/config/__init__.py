import os
import sys
from pathlib import Path

from dynaconf import Dynaconf

_BASE_DIR = os.getcwd()

settings_files = [
    Path(__file__).parent / 'settings.yml',
]  # 指定绝对路径加载默认配置

settings = Dynaconf(
    envvar_prefix="APP",  # 环境变量前缀
    settings_files=settings_files,
    environments=False,  # 启用多层次日志，支持 dev, pro
    load_dotenv=True,  # 加载 .env
    env_switcher="APP_ENV",  # 用于切换模式的环境变量名称
    lowercase_read=False,  # 禁用小写访问
    # 自定义配置覆盖默认配置
    includes=[os.path.join(sys.prefix, 'etc', 'app', 'settings.yml')],
    base_dir=_BASE_DIR,  # 编码传入配置
)
