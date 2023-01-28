patches = [
    # Remove attribute property OutputColumn and Sheets
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::QuickSight::DataSet.OutputColumn",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::QuickSight::Analysis.Sheet",
    },
    {
        "op": "remove",
        "path": "/PropertyTypes/AWS::QuickSight::Dashboard.DashboardVersion",
    },
]
