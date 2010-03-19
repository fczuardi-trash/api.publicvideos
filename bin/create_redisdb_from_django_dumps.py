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

import os
import redis
import json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
PV_DUMP_DIR = os.path.join(PROJECT_ROOT, 'data', 'pv-dump')

r = redis.Redis(host='localhost', port=6379, db=0)
r.flushall()

#transcoders
transcodingjob_dump_file = open(os.path.join(PV_DUMP_DIR, 'transcodingjob.json'), 'r')
transcodingjob_json = json.load(transcodingjob_dump_file)
transcodingjob_dump_file.close()
for transcoder in transcodingjob_json:
  fields = transcoder['fields']
  fields['id'] = transcoder['pk']
  key = 'transcoder:%s' % transcoder['pk']
  #create the objects
  r.set(key, json.dumps(fields, sort_keys=True))
  #update the transcoders list
  r.rpush('transcoders', key)

print '%s transcoders added.' % r.llen('transcoders')

#transcoding_steps
transcodingpass_dump_file = open(os.path.join(PV_DUMP_DIR, 'transcodingpass.json'), 'r')
transcodingpass_json = json.load(transcodingpass_dump_file)
transcodingpass_dump_file.close()
for transcoding_step in transcodingpass_json:
  fields = transcoding_step['fields']
  fields['id'] = transcoding_step['pk']
  del fields['from_extension']
  del fields['slug']
  key = 'transcoding_step:%s' % transcoding_step['pk']
  #create the objects
  r.set(key, json.dumps(fields, sort_keys=True))
  #update the transcoders list
  r.rpush('transcoding_steps', key)

print '%s transcoding_steps added.' % r.llen('transcoding_steps')

#transcoding_steps/transcoder  
transcodingjobpass_dump_file = open(os.path.join(PV_DUMP_DIR, 'transcodingjobpass.json'), 'r')
transcodingjobpass_json = json.load(transcodingjobpass_dump_file)
transcodingjobpass_dump_file.close()
transcoders = {}
for transcodingjobpass in transcodingjobpass_json:
  fields = transcodingjobpass['fields']
  if fields['transcoding_job'] not in transcoders.keys():
    transcoders[fields['transcoding_job']] = {}
  transcoders[fields['transcoding_job']][fields['step_number']] = 'transcoding_step:%s' % fields['transcoding_pass']
for i in transcoders.keys():
  steps = []
  for j in range(1,len(transcoders[i])+1):
    list_name = 'transcoding_steps:transcoder:%s' % i
    r.rpush(list_name, transcoders[i][j])

#authors
author_mboxes = {
  'id3':'04dded97254eab027077f6ebbacba4ec2a84baf1',
  'id4':'c8d4eed17b40ace37ef4beed7ca7146952723f3d'
}
author_obj = {
  'id' : '3',
  'first_name' : 'Ace',
  'last_name' : 'of Spades',
  'mbox_sha1sum' : author_mboxes['id3']
}
r.set('author:3', json.dumps(author_obj, sort_keys=True))
r.rpush('authors', 'author:3')

author_obj = {
  'id' : '4',
  'first_name' : 'Marcio',
  'last_name' : 'Galli',
  'mbox_sha1sum' : author_mboxes['id4']
}
r.set('author:4', json.dumps(author_obj, sort_keys=True))
r.rpush('authors', 'author:4')
print '2 authors added.'


#clips and sets
video_dump_file = open(os.path.join(PV_DUMP_DIR, 'video.json'), 'r')
video_json = json.load(video_dump_file)
video_dump_file.close()
sets = {}
for clip in video_json:
  fields = clip['fields']
  if fields['status'] != 'transcoded': continue
  fields['id'] = clip['pk']
  fields['author'] = author_mboxes['id%s' % fields['author']]
  fields['fps'] = fields['fps_choice']
  del fields['mimetype']
  del fields['status']
  del fields['mute_export']
  del fields['description']
  del fields['extension']
  del fields['title']
  del fields['updated_at']
  del fields['height']
  del fields['width']
  del fields['duration']
  del fields['fps_choice']
  set_slug = fields['set_slug']
  #clips
  key = 'clip:%s' % clip['pk']
  r.set(key, json.dumps(fields, sort_keys=True))
  r.rpush('clips', key)
  r.rpush('clips:author:%s' % fields['author'], key)
  r.rpush('clips:set:%s' % set_slug, key)
  #sets
  key = 'set:%s' % fields['set_slug']
  if set_slug not in sets.keys():
    set_obj = {
      'author' : fields['author'],
      'set_slug' : set_slug
    }
    sets[set_slug] = True
    r.set(key, json.dumps(set_obj, sort_keys=True))
    r.rpush('sets', key)
    r.rpush('sets:author:%s' % set_slug, key)

print '%s clips and %s sets added.' % (r.llen('clips'), r.llen('sets'))

#versions
videoversion_dump_file = open(os.path.join(PV_DUMP_DIR, 'videoversion.json'), 'r')
videoversion_json = json.load(videoversion_dump_file)
videoversion_dump_file.close()
for version in videoversion_json:
  fields = version['fields']
  clip = r.get('clip:%s' % fields['source'])
  if clip == None: continue
  clip_json = json.loads(clip)
  fields['id'] = version['pk']
  del fields['mimetype']
  del fields['updated_at']
  del fields['duration']  
  key = 'version:%s_%s' % (fields['source'], fields['transcoded_with'])
  #create the objects
  r.set(key, json.dumps(fields, sort_keys=True))
  #update the transcoders list
  r.rpush('versions', key)
  r.rpush('versions:clip:%s' % fields['source'], key)
  r.rpush('versions:transcoder:%s' % fields['transcoded_with'], key)  
  r.rpush('versions:transcoder:%s:author:%s' % (fields['transcoded_with'],clip_json['author']), key)
  r.rpush('versions:transcoder:%s:set:%s' % (fields['transcoded_with'],clip_json['set_slug']), key)

print '%s versions added.' % (r.llen('versions'))
print 'Done'