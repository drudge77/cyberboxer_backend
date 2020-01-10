# Format response data
def response_format(success, message, data):
    obj = {
        'message': message
    }
    if success:
        obj['data'] = data
        obj['type'] = "success"
    else:
        obj['type'] = "failed"
    return obj
