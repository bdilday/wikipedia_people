
from __future__ import print_function
import requests
import os
import re

def query(request):
    request['action'] = 'query'
    request['format'] = 'json'
    request['gcmlimit'] = 500
    request['lhlimit'] = 500
    request['cllimit'] = 500

    lastContinue = {'continue': ''}
    while True:
        # Clone original request
        req = request.copy()
        # Modify it with the values returned in the 'continue' section of the last result.
        req.update(lastContinue)

        # Call API
        result = requests.get('http://en.wikipedia.org/w/api.php', params=req).json()
        if 'error' in result: raise Exception(result['error'])
        if 'warnings' in result: print(result['warnings'])
        if 'query' in result: yield result['query']
        if 'continue' not in result: break
        lastContinue = result['continue']

def gather_results(year=1755, prop='info|linkshere|categories', vbose=False):
    data = []
    aa = {}
    prog = re.compile('Category:([0-9]{4})\s+deaths')

    for result in query({'generator':'categorymembers',
                          'prop': prop,
                          'gcmtitle': 'Category:{} births'.format(year)
    }):
        for page_id, v in result.items():
            for tk in v:
                k = unicode(tk)
                t = v[k]['title']

                if not t in aa:
                    aa[t] = {'linkshere': 0, 'length': 0, 'demise': -9999, 'linkspage': 0}

                    if vbose:
                        print('new t', t, year)

                if 'length' in v[k]:
                    length = v[k]['length']
                else:
                    length = 0

                if 'linkshere' in v[k]:
                    linkshere = len(v[k]['linkshere'])
                    ss = [1 for x in v[k]['linkshere'] if x['ns']==0]
                    linkspage = sum(ss)
                else:
                    linkshere = 0
                    linkspage = 0

                if 'categories' in v[k]:
                    for c in v[k]['categories']:
                        re_match = prog.search(c['title'])
                        if re_match:
                            aa[t]['demise'] = int(re_match.group(1))
                aa[t]['length'] += length
                aa[t]['linkshere'] += linkshere
                aa[t]['linkspage'] += linkspage

    return data, aa

if __name__=='__main__':

    minyr = 1642 # Newton
    maxyr = 1642

    for yr in range(minyr, maxyr+1):
        print('starting year', yr)
        ofile = 'data/wiki_%d.csv' % yr
        if os.path.exists(ofile):
            print('file {} exists. continue'.format(ofile))
            continue
        data, aa = gather_results(year=yr)

        ofp = open(ofile, 'w')
        for k in aa:
            print(k, aa[k])
            s = '%d,%d,%d,%d,%d,%s\n' % (aa[k]['length'],
                                         aa[k]['linkshere'],
                                         aa[k]['linkspage'],yr,
                                         aa[k]['demise'],
                                         unicode(k)
            )
            ofp.write(s.encode('utf-8'))
        ofp.close()

