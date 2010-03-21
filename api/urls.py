import tornado.web
from api.methods import *

patterns = tornado.web.Application([
    (r"/", MainHandler),
    (r"(/v/([0-9]+)/|/)clip/?", GetRandomClip),
    (r"(/v/([0-9]+)/|/)clip/([0-9]+)/?", GetClip),
    (r"(/v/([0-9]+)/|/)set/?", GetRandomClipSet),
    (r"(/v/([0-9]+)/|/)set/([^/]+)/?", GetClipSet),
    (r"(/v/([0-9]+)/|/)author/?", GetRandomAuthor),
    (r"(/v/([0-9]+)/|/)author/([^/]{40})/?", GetAuthor),
    (r"(/v/([0-9]+)/|/)version/?", GetRandomClipVersion),
    (r"(/v/([0-9]+)/|/)version/([0-9]+_[0-9]+)/?", GetClipVersion),
    (r"(/v/([0-9]+)/|/)transcoder/?", GetRandomTranscoder),
    (r'(/v/([0-9]+)/|/)transcoder/([0-9]+)/?$', GetTranscoder),
    (r"(/v/([0-9]+)/|/)transcoding_step/?", GetRandomTranscodingStep),
    (r'(/v/([0-9]+)/|/)transcoding_step/([0-9]+)/?$', GetTranscodingStep),

    (r"(/v/([0-9]+)/|/)clips/?", ListRandomClips),
    (r"(/v/([0-9]+)/|/)clips/length/?", GetClipsTotal),
    (r"(/v/([0-9]+)/|/)clips/latest(/([0-9]+))?/?", ListClips),
    
    (r"(/v/([0-9]+)/|/)sets/?", ListRandomSets),
    (r"(/v/([0-9]+)/|/)sets/length/?", GetSetsTotal),
    (r"(/v/([0-9]+)/|/)sets/latest(/([0-9]+))?/?", ListSets),
    
    (r"(/v/([0-9]+)/|/)authors/?", ListRandomAuthors),
    (r"(/v/([0-9]+)/|/)authors/length/?", GetAuthorsTotal),
    (r"(/v/([0-9]+)/|/)authors/latest(/([0-9]+))?/?", ListAuthors),
    
    (r"(/v/([0-9]+)/|/)versions/?", ListRandomVersions),
    (r"(/v/([0-9]+)/|/)versions/length/?", GetVersionsTotal),
    (r"(/v/([0-9]+)/|/)versions/latest(/([0-9]+))?/?", ListVersions),
    
    (r"(/v/([0-9]+)/|/)transcoders/?", ListRandomTranscoders),
    (r"(/v/([0-9]+)/|/)transcoders/length/?", GetTranscodersTotal),
    (r"(/v/([0-9]+)/|/)transcoders/latest(/([0-9]+))?/?", ListTranscoders),
    
    (r"(/v/([0-9]+)/|/)transcoding_steps/?", ListRandomTranscodingSteps),
    (r"(/v/([0-9]+)/|/)transcoding_steps/length/?", GetTranscodingStepsTotal),
    (r"(/v/([0-9]+)/|/)transcoding_steps/latest(/([0-9]+))?/?", ListTranscodingSteps),
    
    (r"(/v/([0-9]+)/|/)clips/author/([^/]{40})/?", ListRandomClipsFromAuthor),
    (r"(/v/([0-9]+)/|/)clips/author/([^/]{40})/length/?", TotalClipsFromAuthor),
    (r"(/v/([0-9]+)/|/)clips/author/([^/]{40})/latest(/([0-9]+))?/?", ListClipsFromAuthor),
    
    (r"(/v/([0-9]+)/|/)clips/set/([^/]+)/?", ListRandomClipsFromSet),
    (r"(/v/([0-9]+)/|/)clips/set/([^/]+)/length/?", TotalClipsFromSet),
    (r"(/v/([0-9]+)/|/)clips/set/([^/]+)/latest(/([0-9]+))?/?", ListClipsFromSet),
    
    (r"(/v/([0-9]+)/|/)sets/author/([^/]{40})/?", ListRandomSetsFromAuthor),
    (r"(/v/([0-9]+)/|/)sets/author/([^/]{40})/length/?", TotalSetsFromAuthor),
    (r"(/v/([0-9]+)/|/)sets/author/([^/]{40})/latest(/([0-9]+))?/?", ListSetsFromAuthor),
    
    (r"(/v/([0-9]+)/|/)versions/clip/([0-9]+)/?", ListRandomVersionsOfClip),
    (r"(/v/([0-9]+)/|/)versions/clip/([0-9]+)/length/?", TotalVersionsOfClip),
    (r"(/v/([0-9]+)/|/)versions/clip/([0-9]+)/latest(/([0-9]+))?/?", ListVersionsOfClip),
    
    (r"(/v/([0-9]+)/|/)versions/transcoder/([0-9]+)/?$", ListRandomVersionsGeneratedWithTranscoder),
    (r"(/v/([0-9]+)/|/)versions/transcoder/([0-9]+)/length/?$", TotalVersionsGeneratedWithTranscoder),
    (r"(/v/([0-9]+)/|/)versions/transcoder/([0-9]+)/latest(/([0-9]+))?/?$", ListVersionsGeneratedWithTranscoder),
    
    (r"(/v/([0-9]+)/|/)versions/transcoder/([0-9]+)/author/([^/]{40})/?$", ListRandomVersionsOfClipsGeneratedWithTranscoderByAuthor),
    (r"(/v/([0-9]+)/|/)versions/transcoder/([0-9]+)/author/([^/]{40})/length/?$", TotalVersionsOfClipsGeneratedWithTranscoderByAuthor),
    (r"(/v/([0-9]+)/|/)versions/transcoder/([0-9]+)/author/([^/]{40})/latest(/([0-9]+))?/?$", ListVersionsOfClipsGeneratedWithTranscoderByAuthor),
    
    (r"(/v/([0-9]+)/|/)versions/transcoder/([0-9]+)/set/([^/]+)/?$", ListRandomVersionsGeneratedWithTranscoderForClipsOnSet),
    (r"(/v/([0-9]+)/|/)versions/transcoder/([0-9]+)/set/([^/]+)/length/?$", TotalVersionsGeneratedWithTranscoderForClipsOnSet),
    (r"(/v/([0-9]+)/|/)versions/transcoder/([0-9]+)/set/([^/]+)/latest(/([0-9]+))?/?$", ListVersionsGeneratedWithTranscoderForClipsOnSet),
    
    (r"(/v/([0-9]+)/|/)transcoding_steps/transcoder/([0-9]+)/?", ListRandomTranscodingStepsUsedByTranscoder),
    (r"(/v/([0-9]+)/|/)transcoding_steps/transcoder/([0-9]+)/length/?", TotalTranscodingStepsUsedByTranscoder),
    (r"(/v/([0-9]+)/|/)transcoding_steps/transcoder/([0-9]+)/latest(/([0-9]+))?/?", ListTranscodingStepsUsedByTranscoder),

])
