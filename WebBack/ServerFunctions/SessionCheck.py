import json


def validate_token(request_handler, raw_request):
    if raw_request.split(',')[1] in request_handler.active_tokes.keys():
        response = json.dumps({"verify":"Ok"}, indent=4, separators=(',', ': '))
    else:
        response = json.dumps({"verify": "No"}, indent=4, separators=(',', ': '))
    return response