import re, urllib, urllib2, json

def jsonloads(string):
    if dir(json).__contains__('loads'):
        return json.loads(string)
    return json.read(string)

def jsondumps(dict):
    if dir(json).__contains__('dumps'):
        return json.dumps(dict)
    return json.write(dict)

def date_format(date):
    date = re.sub(r'[-_\.: ]+', '', date)
    yyyy = date[0:4]
    mm   = date[4:6]
    dd   = date[6:8]
    return "%s-%s-%s" % (yyyy,mm,dd)

def call(method, dict):
    params = urllib.urlencode({'params':jsondumps(dict)})
    req = urllib2.Request('http://data.rcc-acis.org/%s' % method, params, {'Accept':'application/json'})
    res = urllib2.urlopen(req)
    x = res.read();
    return jsonloads(x)

def contains(string,substring):
    return string.find(substring) >= 0

def build_elem(name):
    elem = {}
    while contains(name,'_'):
        if contains(name,'normal_'):
            name = name.replace('normal_', '')
            #elem['summary'] = 'normal'
            elem['normal'] = '1'
        elif contains(name,'ytd_'):
            name = name.replace('ytd_', '')
            elem['duration'] = 'ytd'
            elem['reduce'] = 'sum'
        else:
            name = name.replace('_','')
    elem['name'] = name
    return elem

def build_elem_list(elemstrings):
    elems = []
    for arg in elemstrings:
        if re.search(r'\{', arg):
            elems.append(eval(arg))
        else:
            elems.append( build_elem(arg) )
    return elems
