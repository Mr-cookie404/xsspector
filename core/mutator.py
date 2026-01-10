def mutate_param(name, payload):
    return [
        f"{name}={payload}",
        f"{name}[]={payload}",
        f"{name}=%22{payload}%22",
        f"{name}=javascript:{payload}",
        f"{name}={{\"x\":\"{payload}\"}}"
    ]
