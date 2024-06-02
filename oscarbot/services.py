from django.apps import apps
from django.conf import settings


def get_bot_model():
    try:
        *app_name_lst, app_model = settings.OSCARBOT_BOT_MODEL.split('.')
        app_name = '.'.join(app_name_lst)
        bot_model = apps.get_model(app_name, app_model)
        return bot_model
    except Exception:
        raise RuntimeError('Failed to get Bot model. Add to settings.py OSCARBOT_BOT_MODEL = app.BotModel')
