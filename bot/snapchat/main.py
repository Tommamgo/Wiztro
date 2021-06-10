from pprint import pprint
from pysnap import Snapchat

s = Snapchat()
s.login('wiztroesse21', 'ksdnrgoipq')
snaps = s.get_snaps()

pprint(snaps)
