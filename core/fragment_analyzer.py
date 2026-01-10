def extract_fragment_params(parsed_url):
    params = []
    if parsed_url.fragment:
        if "=" in parsed_url.fragment:
            parts = parsed_url.fragment.split("&")
            for p in parts:
                if "=" in p:
                    k, v = p.split("=", 1)
                    params.append({
                        "name": k,
                        "value": v,
                        "type": "fragment"
                    })
    return params
