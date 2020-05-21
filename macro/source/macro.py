import sys, os, io, traceback
from troposphere.template_generator import TemplateGenerator

def handle_template(template):
    troposphere_code = template["Troposhere"]
    del template["Troposhere"]

    macro_template = TemplateGenerator(template)
    exec(troposphere_code)

    return macro_template.to_json()

def handler(event, context):
    request_id = event['requestId']
    parameters = event['templateParameterValues']

    macro_response = {
        'status': 'success',
        'requestId': request_id
    }

    try:
        macro_response['fragment'] = handle_template(event['fragment'])
    except Exception as e:
        traceback.print_exc()
        macro_response['status'] = 'failure'
        macro_response['errorMessage'] = str(e)

    return macro_response
