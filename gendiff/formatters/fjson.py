import json


def get_json_diff(diff: dict) -> str:
    '''Convert diff dict to the json difference report
    '''
    return json.dumps(diff, indent=2)
