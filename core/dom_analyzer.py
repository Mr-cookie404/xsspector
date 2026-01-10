DOM_SINKS = [
    "innerHTML",
    "outerHTML",
    "document.write",
    "eval",
    "setTimeout",
    "setInterval",
    "location.href"
]

DOM_SOURCES = [
    "location.search",
    "location.hash",
    "document.URL",
    "document.referrer",
    "window.name"
]

def analyze_dom(js_content):
    sinks = [s for s in DOM_SINKS if s in js_content]
    sources = [s for s in DOM_SOURCES if s in js_content]

    return {
        "sources": sources,
        "sinks": sinks
    }
