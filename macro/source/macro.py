from troposphere.template_generator import TemplateGenerator
import traceback

def handle_template(event):
    template = event['fragment']
    macro_parameters = event['templateParameterValues']

    troposphere_code = template["Troposhere"]
    del template["Troposhere"]

    macro_template = TemplateGenerator(template)
    exec(troposphere_code)

    return macro_template.to_dict()

def handler(event, context):
    request_id = event['requestId']

    macro_response = {
        'status': 'success',
        'requestId': request_id
    }

    try:
        macro_response['fragment'] = handle_template(event)
    except Exception as e:
        traceback.print_exc()
        macro_response['status'] = 'failure'
        macro_response['errorMessage'] = str(e)

    return macro_response


