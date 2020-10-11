from troposphere import Template


t = Template()

t.set_description("Example to show adding a Metadata section to the template")
t.add_metadata({
    "Comments": "Initial Draft",
    "LastUpdated": "Jan 1st 2015",
    "UpdatedBy": "First Last",
    "Version": "V1.0",
})

print(t.to_json())
