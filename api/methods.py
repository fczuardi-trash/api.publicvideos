import json
import random
import redis
import tornado.web

def get_object(obj_type, obj_key):
  r = redis.Redis(host='localhost', port=6379, db=0)
  return r.get('%s:%s' % (obj_type,obj_key))

def get_random_object(list_name):
  r = redis.Redis(host='localhost', port=6379, db=0)
  list_length = r.llen(list_name)
  return r.get(r.lindex(list_name, random.randint(0,list_length-1)))

def list_items(list_name, page):
  if not page:
    page = 1
  else:
    page = int(page)
  r = redis.Redis(host='localhost', port=6379, db=0)
  begin = ((page-1)*100)
  end = begin + 99
  return r.mget(r.lrange(list_name, begin, end))
  
def list_random_items(list_name):
  r = redis.Redis(host='localhost', port=6379, db=0)
  random_indexes = range(r.llen(list_name))
  random.shuffle(random_indexes)
  result = []
  for i in range(100):
    if i > len(random_indexes)-1:
      break
    result.append(r.get(r.lindex(list_name,random_indexes[i])))
    # result.append(random_indexes[i])
  return result

def get_list_length(list_name):
  r = redis.Redis(host='localhost', port=6379, db=0)
  return r.llen(list_name)

def return_json_response(handler, content):
  handler.set_header("Content-Type", "application/json")
  if ('callback' in handler.request.arguments):
    handler.write('%s(%s)' % (handler.get_argument('callback') , content))
  else:
    handler.write(content)
  
class MainHandler(tornado.web.RequestHandler):
  def get(self):
    self.redirect("http://wiki.publicvideos.org/api/main")

class GetClip(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, clip_id, options):
    return_json_response(self, get_object('clip', clip_id))

class GetRandomClip(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version):
    return_json_response(self, get_random_object('clips'))

class GetClipSet(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, set_slug):
    return_json_response(self, json.dumps(get_object('set', set_slug)))

class GetRandomClipSet(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version):
    return_json_response(self, json.dumps(get_random_object('sets')))

class GetAuthor(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, mbox_sha1sum):
    return_json_response(self, json.dumps(get_object('author', mbox_sha1sum)))

class GetRandomAuthor(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version):
    return_json_response(self, json.dumps(get_random_object('authors')))

class GetClipVersion(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, version_key):
    return_json_response(self, json.dumps(get_object('version', version_key)))

class GetRandomClipVersion(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version):
    return_json_response(self, json.dumps(get_random_object('versions')))

class GetTranscoder(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, transcoder_id):
    return_json_response(self, json.dumps(get_object('transcoder', transcoder_id)))

class GetRandomTranscoder(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version):
    return_json_response(self, json.dumps(get_random_object('transcoders')))

class GetTranscodingStep(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, transcoding_step_id):
    return_json_response(self, json.dumps(get_object('transcoding_step', transcoding_step_id)))

class GetRandomTranscodingStep(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version):
    return_json_response(self, json.dumps(get_random_object('transcoding_steps')))

class ListRandomClips(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version):
    return_json_response(self, json.dumps(list_random_items('clips')))

class GetClipsTotal(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version):
    return_json_response(self, json.dumps(get_list_length('clips')))

class ListClips(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, p_blurb, page):
    return_json_response(self, json.dumps(list_items('clips', page)))
    
class ListRandomSets(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version):
    return_json_response(self, json.dumps(list_random_items('sets')))

class GetSetsTotal(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version):
    return_json_response(self, json.dumps(get_list_length('sets')))

class ListSets(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, p_blurb, page):
    return_json_response(self, json.dumps(list_items('sets', page)))

class ListRandomAuthors(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version):
    return_json_response(self, json.dumps(list_random_items('authors')))

class GetAuthorsTotal(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version):
    return_json_response(self, json.dumps(get_list_length('authors')))

class ListAuthors(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, p_blurb, page):
    return_json_response(self, json.dumps(list_items('authors', page)))

class ListRandomVersions(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version):
    return_json_response(self, json.dumps(list_random_items('versions')))

class GetVersionsTotal(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version):
    return_json_response(self, json.dumps(get_list_length('versions')))

class ListVersions(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, p_blurb, page):
    return_json_response(self, json.dumps(list_items('versions', page)))

class ListRandomTranscoders(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version):
    return_json_response(self, json.dumps(list_random_items('transcoders')))

class GetTranscodersTotal(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version):
    return_json_response(self, json.dumps(get_list_length('transcoders')))

class ListTranscoders(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, p_blurb, page):
    return_json_response(self, json.dumps(list_items('transcoders', page)))
    
class ListRandomTranscodingSteps(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version):
    return_json_response(self, json.dumps(list_random_items('transcoding_steps')))

class GetTranscodingStepsTotal(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version):
    return_json_response(self, json.dumps(get_list_length('transcoding_steps')))

class ListTranscodingSteps(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, p_blurb, page):
    return_json_response(self, json.dumps(list_items('transcoding_steps', page)))

class ListRandomClipsFromAuthor(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, mbox_sha1sum):
    return_json_response(self, json.dumps(list_random_items('clips:author:%s' % mbox_sha1sum)))

class TotalClipsFromAuthor(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, mbox_sha1sum):
    return_json_response(self, json.dumps(get_list_length('clips:author:%s' % mbox_sha1sum)))

class ListClipsFromAuthor(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, mbox_sha1sum, p_blurb, page):
    return_json_response(self, json.dumps(list_items('clips:author:%s' % mbox_sha1sum, page)))

class ListRandomClipsFromSet(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, set_slug):
    return_json_response(self, json.dumps(list_random_items('clips:set:%s' % set_slug)))

class TotalClipsFromSet(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, set_slug):
    return_json_response(self, json.dumps(get_list_length('clips:set:%s' % set_slug)))

class ListClipsFromSet(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, set_slug, p_blurb, page):
    return_json_response(self, json.dumps(list_items('clips:set:%s' % set_slug, page)))

class ListRandomSetsFromAuthor(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, mbox_sha1sum):
    return_json_response(self, json.dumps(list_random_items('sets:author:%s' % mbox_sha1sum)))

class TotalSetsFromAuthor(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, mbox_sha1sum):
    return_json_response(self, json.dumps(get_list_length('sets:author:%s' % mbox_sha1sum)))

class ListSetsFromAuthor(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, mbox_sha1sum, p_blurb, page):
    return_json_response(self, json.dumps(list_items('sets:author:%s' % mbox_sha1sum, page)))

class ListRandomVersionsOfClip(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, clip_id):
    return_json_response(self, json.dumps(list_random_items('versions:clip:%s' % clip_id)))

class TotalVersionsOfClip(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, clip_id):
    return_json_response(self, json.dumps(get_list_length('versions:clip:%s' % clip_id)))

class ListVersionsOfClip(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, clip_id, p_blurb, page):
    return_json_response(self, json.dumps(list_items('versions:clip:%s' % clip_id, page)))

class ListRandomVersionsGeneratedWithTranscoder(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, transcoder_id):
    return_json_response(self, json.dumps(list_random_items('versions:transcoder:%s' % transcoder_id)))

class TotalVersionsGeneratedWithTranscoder(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, transcoder_id):
    return_json_response(self, json.dumps(get_list_length('versions:transcoder:%s' % transcoder_id)))

class ListVersionsGeneratedWithTranscoder(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, transcoder_id, p_blurb, page):
    return_json_response(self, json.dumps(list_items('versions:transcoder:%s' % transcoder_id, page)))

class ListRandomVersionsGeneratedWithTranscoderByAuthor(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, transcoder_id, mbox_sha1sum):
    return_json_response(self, json.dumps(list_random_items('versions:transcoder:%s:author:%s' % (transcoder_id, mbox_sha1sum))))

class TotalVersionsGeneratedWithTranscoderByAuthor(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, transcoder_id, mbox_sha1sum):
    return_json_response(self, json.dumps(get_list_length('versions:transcoder:%s:author:%s' % (transcoder_id, mbox_sha1sum))))

class ListVersionsGeneratedWithTranscoderByAuthor(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, transcoder_id, mbox_sha1sum, p_blurb, page):
    return_json_response(self, json.dumps(list_items('versions:transcoder:%s:author:%s' % (transcoder_id, mbox_sha1sum), page)))

class ListRandomVersionsGeneratedWithTranscoderForClipsOnSet(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, transcoder_id, set_slug):
    return_json_response(self, json.dumps(list_random_items('versions:transcoder:%s:set:%s' % (transcoder_id, set_slug))))

class TotalVersionsGeneratedWithTranscoderForClipsOnSet(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, transcoder_id, set_slug):
    return_json_response(self, json.dumps(get_list_length('versions:transcoder:%s:set:%s' % (transcoder_id, set_slug))))

class ListVersionsGeneratedWithTranscoderForClipsOnSet(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, transcoder_id, set_slug, p_blurb, page):
    return_json_response(self, json.dumps(list_items('versions:transcoder:%s:set:%s' % (transcoder_id, set_slug), page)))

class ListRandomTranscodingStepsUsedByTranscoder(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, transcoder_id):
    return_json_response(self, json.dumps(list_random_items('transcoding_steps:transcoder:%s' % (transcoder_id))))

class TotalTranscodingStepsUsedByTranscoder(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, transcoder_id):
    return_json_response(self, json.dumps(get_list_length('transcoding_steps:transcoder:%s' % (transcoder_id))))

class ListTranscodingStepsUsedByTranscoder(tornado.web.RequestHandler):
  def get(self, v_blurb, api_version, transcoder_id, p_blurb, page):
    return_json_response(self, json.dumps(list_items('transcoding_steps:transcoder:%s' % (transcoder_id), page)))
