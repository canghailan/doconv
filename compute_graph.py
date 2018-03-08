import json


def floyd(g):
    sources = set(g.keys())
    targets = set([k for v in g.values() for k in v.keys()])

    for i in sources:
        gi = g[i]

        for s in sources:
            gs = g[s]
            if s == i:
                continue
            if not i in gs:
                continue

            for t in targets:
                if s == t or t == i:
                    continue
                if not t in gi:
                    continue

                if not t in gs:
                    gs[t] = {'quality': 0}

                gst = gs[t]
                gsi = gs[i]
                git = gi[t]
                if gst['quality'] < gsi['quality'] * git['quality']:
                    si = gsi['path'] if 'path' in gsi else [i]
                    it = git['path'] if 'path' in git else [t]
                    gs[t] = {
                        'quality': gsi['quality'] * git['quality'],
                        'path': si + it
                    }

    return g


with open("graph-source.json", encoding='utf-8') as file_in, open("graph.json", mode='w', encoding='utf-8') as file_out:
    json.dump(floyd(json.load(file_in)), file_out, indent=4)
