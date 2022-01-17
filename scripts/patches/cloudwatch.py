patches = [
    {
        "op": "move",
        "from": "/PropertyTypes/AWS::CloudWatch::Alarm.Dimension",
        "path": "/PropertyTypes/AWS::CloudWatch::Alarm.MetricDimension",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::CloudWatch::Alarm/Properties/Dimensions/ItemType",
        "value": "MetricDimension",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CloudWatch::Alarm.Metric/Properties/Dimensions/ItemType",
        "value": "MetricDimension",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::CloudWatch::AnomalyDetector.Dimension",
    },
    {
        "op": "replace",
        "path": "/ResourceTypes/AWS::CloudWatch::AnomalyDetector/Properties/Dimensions/ItemType",
        "value": "MetricDimension",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CloudWatch::AnomalyDetector.Metric/Properties/Dimensions/ItemType",
        "value": "MetricDimension",
    },
    {
        "op": "replace",
        "path": "/PropertyTypes/AWS::CloudWatch::AnomalyDetector.SingleMetricAnomalyDetector/Properties/Dimensions/ItemType",
        "value": "MetricDimension",
    },
]
