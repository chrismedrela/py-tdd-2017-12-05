from behave import *

@step(u'a user navigates to home page')
def step_impl(context):
    context.resp = context.client.get('/')

@then(u'{text} should be displayed')
def step_impl(context, text):
    assert text in context.resp

@given(u'I have entered {value} as {field} number')
def step_impl(context, value, field):
    context.resp.form[field] = value

@when(u'I press add')
def step_impl(context):
    context.resp = context.resp.form.submit()
