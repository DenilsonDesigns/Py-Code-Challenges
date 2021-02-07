obje = [{'status': None, 'comment': None, 'agent': 'AGL', 'request_comment': 'AGL type their reason here', 'request_id': '16c26f16-148a-a4fa-aasdfsdfdfsd9', 'command_type': 'ON'},
        {'status': None, 'comment': None, 'agent': 'AGL', 'request_comment': 'AGL type their reason here', 'request_id': '16c26f16-148a-a4fa-aasdfsdfdfsd9', 'command_type': 'ON'}]

wanted = ['request_id', 'comment', 'status']
# final = [[{k: v for k, v in x if k in wanted} for y in obje]]
# final = [k for k in obje if wanted in k.keys()]
final = [dict((k, v)
              for k, v in a.items() if k in wanted) for a in obje]

print(final)
