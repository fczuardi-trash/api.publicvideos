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

from fabric.api import *
import redis
import tornado.httpserver
import tornado.ioloop
from api import urls

PROJECT_ROOT = os.path.dirname(__file__)

def start(port=8888):
  """Start the web server.
  
  Parameters:
  port: which port to run the server."""
  
  http_server = tornado.httpserver.HTTPServer(urls.patterns)
  http_server.listen(int(port))
  print "Server running on port %s..." % port
  tornado.ioloop.IOLoop.instance().start()
  
def get_db_dump():
  """Get the latest database dump files from Public Videos."""
  with cd('data/pv-dump/'):
    local('curl -K urls.txt', capture=False);
    
def start_redis():
  """Start the database."""

  if not os.path.exists(os.path.join(PROJECT_ROOT, 'run')):
    os.makedirs(os.path.join(PROJECT_ROOT, 'run'))
  if not os.path.exists(os.path.join(PROJECT_ROOT, 'conf')):
    os.makedirs(os.path.join(PROJECT_ROOT, 'conf'))
  # define redis configuration parameters
  redis_pid_file = os.path.join(PROJECT_ROOT, 'run', 'redis.pid')
  redis_db_file = os.path.join(PROJECT_ROOT, 'data', 'api-redis', 'publicvideos.rdb')
  redis_config_path = os.path.join(PROJECT_ROOT, 'conf', 'redis.conf')
  redis_options = {
    'pidfile /var/run/redis.pid': 'pidfile %s' % redis_pid_file,
    'daemonize no': 'daemonize yes',
    'dir ./': 'dir ./data/api-redis/',
    'save 900 1': 'save 3 1',
    'dbfilename dump.rdb': 'dbfilename %s' % redis_db_file    
  }
  # read redis default configuration parameters
  redis_default_config = open(os.path.join(PROJECT_ROOT, 'deps', 'redis', 'redis.conf'), 'r')
  redis_config_raw = redis_default_config.read()
  redis_default_config.close()
  # write redis app-specific configuration parameters
  redis_config = open(redis_config_path, 'w')
  for defaultv, newv in redis_options.items():
    redis_config_raw = redis_config_raw.replace(defaultv, newv)
  redis_config.write(redis_config_raw)
  redis_config.close()
  # start redis server
  local("%s %s" % (os.path.join(PROJECT_ROOT, 'deps', 'redis', 'redis-server'), redis_config_path))

def populate_redis():
  """Recreates the database based on the dump files from publicvideos."""
  local('python bin/create_redisdb_from_django_dumps.py', capture=False);
  
def kill_redis():
  """Shutdown the database."""
  # kill redis server
  local("kill `cat %s`" % os.path.join(PROJECT_ROOT, 'run', 'redis.pid'))

def flush_redis(db=0):
  """Clear all data in the database."""
  r = redis.Redis(host='localhost', port=6379)
  if type(db) is int: # flushes data from one specific DB
    r.select(r.host, r.port, db)
    r.flush()
  elif db is None: # flushes data from all DBs
    r.flushall()
