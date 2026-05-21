import urllib.request
import urllib.parse
import json

class TrmxResponse:
    def __init__(self, raw_response, status_code):
        self.content = raw_response
        self.status_code = status_code
        self.text = raw_response.decode('utf-8')

    def json(self):
        return json.loads(self.text)

def get(url, headers=None):
    actual_headers = {"User-Agent": "TrmxRequests/1.0"}
    if headers:
        actual_headers.update(headers)
    req = urllib.request.Request(url, headers=actual_headers, method='GET')
    try:
        with urllib.request.urlopen(req) as response:
            return TrmxResponse(response.read(), response.getcode())
    except urllib.error.HTTPError as e:
        return TrmxResponse(e.read(), e.code)

def post(url, headers=None, json_data=None, data=None):
    actual_headers = {"User-Agent": "TrmxRequests/1.0"}
    if headers:
        actual_headers.update(headers)

    send_data = b""
    
    if json_data is not None:
        actual_headers['Content-Type'] = 'application/json'
        # تحويل نقي لـ Bytes بلا أي تغيير ف الـ Structure د الحروف العربية
        json_str = json.dumps(json_data, ensure_ascii=False)
        send_data = json_str.encode('utf-8')
    elif data is not None:
        actual_headers['Content-Type'] = 'application/x-www-form-urlencoded'
        send_data = urllib.parse.urlencode(data).encode('utf-8')

    actual_headers['Content-Length'] = str(len(send_data))

    req = urllib.request.Request(url, data=send_data, headers=actual_headers, method='POST')
    
    try:
        with urllib.request.urlopen(req) as response:
            return TrmxResponse(response.read(), response.getcode())
    except urllib.error.HTTPError as e:
        return TrmxResponse(e.read(), e.code)
    except Exception as e:
        return TrmxResponse(str(e).encode('utf-8'), 500)
