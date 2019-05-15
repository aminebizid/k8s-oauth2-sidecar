import os
oauth_config = {
    'well_known_url': os.getenv('well_known_url'),
    'client_id': os.getenv('client_id'),
    'redirect_uri': os.getenv('redirect_uri'),
    'audience': os.getenv('audience'),
    'scopes': os.getenv('scopes'),
    'whitelist': os.getenv('whitelist').split(',')
}
