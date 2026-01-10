def extract_path_params(parsed_url):
    params = []
    parts = parsed_url.path.strip("/").split("/")

    for part in parts:
        if part.isdigit() or len(part) <= 2:
            params.append({
                "name": "path_segment",
                "value": part,
                "type": "path"
            })

    return params
