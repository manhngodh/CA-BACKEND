import os
STATS_ENDPOINT = os.environ.get('STATS_ENDPOINT', '')
SECRET_KEY_FERNET = os.environ.get('SECRET_KEY_FERNET','QaBguu2w72LwQxHTg5KWa77gVeez5d_MGm2v5KN9ucI=').encode()