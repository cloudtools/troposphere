patches = [
    # Omit Connect::EvaluationForm for now due to recursion issues
    {
        "op": "remove",
        "path": "/ResourceTypes/AWS::Connect::EvaluationForm",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Connect::EvaluationForm.EvaluationFormBaseItem",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Connect::EvaluationForm.EvaluationFormSection",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Connect::EvaluationForm.EvaluationFormItem",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Connect::EvaluationForm.NumericQuestionPropertyValueAutomation",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Connect::EvaluationForm.EvaluationFormNumericQuestionAutomation",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Connect::EvaluationForm.EvaluationFormNumericQuestionProperties",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Connect::EvaluationForm.EvaluationFormQuestionTypeProperties",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Connect::EvaluationForm.EvaluationFormQuestion",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Connect::EvaluationForm.EvaluationFormSingleSelectQuestionAutomationOption",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Connect::EvaluationForm.EvaluationFormSingleSelectQuestionAutomation",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Connect::EvaluationForm.EvaluationFormSingleSelectQuestionProperties",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Connect::EvaluationForm.EvaluationFormNumericQuestionOption",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Connect::EvaluationForm.EvaluationFormSingleSelectQuestionOption",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Connect::EvaluationForm.ScoringStrategy",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::Connect::EvaluationForm.SingleSelectQuestionRuleCategoryAutomation",
    },
]
