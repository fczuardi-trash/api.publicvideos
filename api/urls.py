import tornado.web
from api.methods import *

urlpatterns = tornado.web.Application([
    (r"/", MainHandler),
    (r"(/v/([0-9]+)/|/)clip/?", GetRandomClip),
    (r"(/v/([0-9]+)/|/)clip/([0-9]+)/?", GetClip),
    (r"(/v/([0-9]+)/|/)set/?", GetRandomClipSet),
    (r"(/v/([0-9]+)/|/)set/([^/]+)/?", GetClipSet),
    (r"(/v/([0-9]+)/|/)author/?", GetRandomAuthor),
    (r"(/v/([0-9]+)/|/)author/([^/]{40})/?", GetAuthor),
    (r"(/v/([0-9]+)/|/)version/?", GetRandomClipVersion),
    (r"(/v/([0-9]+)/|/)version/([0-9]+:[0-9]+)/?", GetClipVersion),
    (r"(/v/([0-9]+)/|/)transcoder/?", GetRandomTranscoder),
    (r'(/v/([0-9]+)/|/)transcoder/([0-9]+)/?$', GetTranscoder),
])
