import os

from flask import Flask, render_template, request

from theHackWeb.blueprints.auth import auth_bp
from theHackWeb.setting import config

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('theHackWeb')
    # app.run(host='127.0.0.1', port=8080)
    app.config.from_object(config[config_name])

    # 使用flask routes 命令查看当前程序注册的路由
    app.register_blueprint(auth_bp, url_prefix="/auth") # 添加蓝本, url前缀
    return app