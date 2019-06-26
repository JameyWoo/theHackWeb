import os
from dotenv import load_dotenv

# dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# if os.path.exists(dotenv_path):
#     load_dotenv(dotenv_path)

from theHackWeb import create_app # 定义在theHackWeb的__init__.py 下

app = create_app() # 建立flask实例, 这个参数怎么没用?
