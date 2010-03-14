#
# api.publicvideos - REST API for the Public Videos repository.
#
# Copyright (c) 2010, Fabricio Zuardi
# All rights reserved.
#  
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
#   * Neither the name of the author nor the names of its contributors
#     may be used to endorse or promote products derived from this
#     software without specific prior written permission.
#  
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
__author__ = ('Fabricio Zuardi', 'fabricio@fabricio.org', 'http://fabricio.org')
__license__ = "BSD"

import tornado.httpserver
import tornado.ioloop
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


application = tornado.web.Application([
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


if __name__ == "__main__":
  server_port = 8888
  http_server = tornado.httpserver.HTTPServer(application)
  http_server.listen(server_port)
  print "Server running on port %s..." % server_port
  tornado.ioloop.IOLoop.instance().start()