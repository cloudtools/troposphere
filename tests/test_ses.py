from troposphere import Template, Ref, ses
from troposphere.ses import (
  Template as Temp,
  EmailTemplate,
)
t = Template()
t.add_transform('AWS::Serverless-2016-10-31')


t.add_resource(Temp(
  'TemplateName',
  Template=EmailTemplate(
    'EmailTemplateTest',
    HtmlPart="<h1>Hej</h1>",
    SubjectPart='test',
    TemplateName='test',
    TextPart='hej',
  )
))

print(t.to_json())
