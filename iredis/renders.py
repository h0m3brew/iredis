"""
Render redis-server responses.
"""

def render_dict(pairs):
    for k, v in pairs.items():
        print(k)
        print(v)
