"""TMDB catalog updater. Run ONLY when appropriate API/data rights are secured."""
import datetime as dt, json, os, pathlib, time, urllib.parse, urllib.request
KEY=os.environ['TMDB_API_KEY']
TODAY=dt.date.today()
START=TODAY-dt.timedelta(days=45)
END=TODAY+dt.timedelta(days=120)
ROOT=pathlib.Path(__file__).resolve().parent
DEST=ROOT/'data'/'movies.json'
existing=json.loads(DEST.read_text(encoding='utf-8')) if DEST.exists() else {'movies':[]}
by_id={str(x['id']):x for x in existing.get('movies',[]) if 'id' in x}

def get(path,params):
    params={**params,'api_key':KEY}
    url='https://api.themoviedb.org/3/'+path+'?'+urllib.parse.urlencode(params)
    for attempt in range(4):
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'GlobalSubHub/0.1'})
            with urllib.request.urlopen(req,timeout=30) as r:return json.load(r)
        except Exception:
            if attempt==3:raise
            time.sleep(2**attempt)

# Discover uses original release-date range and pages; TMDB coverage is not exhaustive.
for page in range(1,11):
    data=get('discover/movie',{'sort_by':'primary_release_date.desc','primary_release_date.gte':START.isoformat(),'primary_release_date.lte':END.isoformat(),'include_adult':'false','page':page})
    for m in data.get('results',[]):
        if not m.get('id'):continue
        release=m.get('release_date') or ''
        by_id[str(m['id'])]={'id':m['id'],'title':m.get('title') or m.get('original_title') or 'Untitled','original_title':m.get('original_title'),'release_date':release,'original_language':m.get('original_language'),'overview':m.get('overview') or '', 'status':'released' if release and release<=TODAY.isoformat() else 'upcoming'}
    if page>=data.get('total_pages',1):break
    time.sleep(.3)
# Deduplicate by TMDB movie ID; trim old entries so the catalog remains manageable.
movies=[m for m in by_id.values() if not m.get('release_date') or m['release_date']>=(TODAY-dt.timedelta(days=180)).isoformat()]
movies.sort(key=lambda m:m.get('release_date') or '',reverse=True)
DEST.write_text(json.dumps({'source':'tmdb','updated':TODAY.isoformat(),'movies':movies},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Saved',len(movies),'unique movie listings')
