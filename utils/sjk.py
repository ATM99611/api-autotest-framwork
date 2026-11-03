from config.url import base_url2


def mo2(mo):
    method = mo["method"]
    url = base_url2 + mo["path"]
    headers = eval(mo["headers"]) if isinstance(mo["headers"], str) else None
    params = eval(mo["params"]) if isinstance(mo["params"], str) else None
    data = eval(mo["data"]) if isinstance(mo["data"], str) else None
    json = eval(mo["json"]) if isinstance(mo["json"], str) else None
    files = eval(mo["files"]) if isinstance(mo["files"], str) else None

    request_data = {"method": method,
                    "url": url,
                    "headers": headers,
                    "params": params,
                    "data": data,
                    "json": json,
                    "files": files
                    }
    return request_data