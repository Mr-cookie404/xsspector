def link_params_to_sinks(params, dom_analysis):
    dangerous = []

    if dom_analysis["sources"] and dom_analysis["sinks"]:
        for p in params:
            dangerous.append({
                "parameter": p,
                "sources": dom_analysis["sources"],
                "sinks": dom_analysis["sinks"],
                "risk": "high"
            })

    return dangerous
