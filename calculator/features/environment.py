from webtest import TestApp

from frontend import app


def before_scenario(context, scenario):
    context.client = TestApp(app)


def after_scenario(context, scenario):
    del context.client
