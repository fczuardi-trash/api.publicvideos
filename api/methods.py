import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect("http://wiki.publicvideos.org/api/main")

class GetClip(tornado.web.RequestHandler):
    def get(self, v_blurb, api_version, clip_id):
        self.write("TBD: return the clip %s" % clip_id)

class GetRandomClip(tornado.web.RequestHandler):
    def get(self, v_blurb, api_version):
        self.write("TBD return a random clip")

class GetClipSet(tornado.web.RequestHandler):
    def get(self, v_blurb, api_version, set_slug):
        self.write("TBD: return the clip set %s" % set_slug)

class GetRandomClipSet(tornado.web.RequestHandler):
    def get(self, v_blurb, api_version):
        self.write("TBD return a random clip set")

class GetAuthor(tornado.web.RequestHandler):
    def get(self, v_blurb, api_version, mbox_sha1sum):
        self.write("TBD: return the author %s" % mbox_sha1sum)

class GetRandomAuthor(tornado.web.RequestHandler):
    def get(self, v_blurb, api_version):
        self.write("TBD return a random author")

class GetClipVersion(tornado.web.RequestHandler):
    def get(self, v_blurb, api_version, version_key):
        self.write("TBD: return the clip version %s" % version_key)

class GetRandomClipVersion(tornado.web.RequestHandler):
    def get(self, v_blurb, api_version):
        self.write("TBD return a random clip version.")

class GetTranscoder(tornado.web.RequestHandler):
    def get(self, v_blurb, api_version, transcoder_id):
        self.write("TBD: return the transcoder %s. API version:%s. Version prefix:%s." % (transcoder_id, api_version, v_blurb))

class GetRandomTranscoder(tornado.web.RequestHandler):
    def get(self, v_blurb, api_version):
        self.write("TBD return a random transcoder.")

