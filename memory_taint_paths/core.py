from collections import deque
from .common import unique_ids,identifier

def run(data):
    nodes=data['nodes'];revoked=set(data['revoked'])
    if len(nodes)>1000:raise ValueError('size')
    ids=set(unique_ids(nodes));by={n['id']:n for n in nodes};children={k:set() for k in ids}
    if not revoked<=ids:raise ValueError('revoked_unknown')
    for n in nodes:
        if n['kind'] not in ('source','derived'):raise ValueError('kind')
        if n['kind']=='source' and n.get('rules'):raise ValueError('source_rules')
        for rule in n.get('rules',[]):
            if not rule or len(rule)!=len(set(rule)) or not set(rule)<=ids:raise ValueError('rule')
            for parent in rule:children[parent].add(n['id'])
    supported={n['id'] for n in nodes if n['kind']=='source' and n['id'] not in revoked};proof={s:[] for s in supported}
    while True:
        changed=False
        for n in nodes:
            if n['id'] in supported or n['id'] in revoked:continue
            rule=next((r for r in n.get('rules',[]) if set(r)<=supported),None)
            if rule is not None:supported.add(n['id']);proof[n['id']]=list(rule);changed=True
        if not changed:break
    paths={s:[s] for s in revoked};queue=deque(sorted(revoked))
    while queue:
        parent=queue.popleft()
        for child in sorted(children[parent]):
            if child not in paths:paths[child]=paths[parent]+[child];queue.append(child)
    return {'nodes':[{'id':n['id'],'supported_by_unrevoked_sources':n['id'] in supported,'clean_support_rule':proof.get(n['id']),'revoked_ancestor_path':paths.get(n['id']),'requires_regeneration_review':n['id'] in paths and n['id'] not in revoked} for n in nodes],'scope':'declared AND rules with OR alternatives; support is not proof the stored text was regenerated or deleted'}
