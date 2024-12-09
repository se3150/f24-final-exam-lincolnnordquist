import behave_webdriver

def before_all(context):
    context.behave_driver = behave_webdriver.Chrome(headless=True)

def after_all(context):
    if hasattr(context, 'behave_driver'):
        context.behave_driver.quit()