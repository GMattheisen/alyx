from textwrap import dedent

# ALYX-SPECIFIC
ALLOWED_HOSTS = ['*','barn.mrsic-flogel.swc.ucl.ac.uk']
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'GB'
GLOBUS_CLIENT_ID = '525cc517-8ccb-4d11-8036-af332da5eafd'
SUBJECT_REQUEST_EMAIL_FROM = 'g.mattheisen@ucl.ac.uk'
DEFAULT_SOURCE = 'Cruciform BSU'
DEFAULT_PROTOCOL = '1'
SUPERUSERS = ('root',)
STOCK_MANAGERS = ('charu',)
WEIGHT_THRESHOLD = 0.75
DEFAULT_LAB_NAME = 'mrsicflogellab'
DEFAULT_LAB_PK = '4027da48-7be3-43ec-a222-f75dffe36872'
SESSION_REPO_URL = \
    "home/glynism/Desktop/mrsicflogellab/public/projects/{project}/{batch}/DAQ/{subject}/{date}/{number:03d}/"
NARRATIVE_TEMPLATES = {
    'Headplate implant': dedent('''ss
    == General ==

    Start time (hh:mm):   ___:___
    End time (hh:mm):    ___:___

    Bregma-Lambda :   _______  (mm)

    == Drugs == (copy paste as many times as needed; select IV, SC or IP)
    __________________( IV / SC / IP ) Admin. time (hh:mm)  ___:___

    == Coordinates ==  (copy paste as many times as needed; select B or L)
    (B / L) - Region: AP:  _______  ML:  ______  (mm)
    Region: _____________________________

    == Notes ==
    <write your notes here>
        '''),
}
