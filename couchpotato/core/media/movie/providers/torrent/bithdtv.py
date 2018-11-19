from couchpotato.core.helpers.encoding import tryUrlencode
from couchpotato.core.logger import CPLog
from couchpotato.core.event import fireEvent
from couchpotato.core.media._base.providers.torrent.bithdtv import Base
from couchpotato.core.media.movie.providers.base import MovieProvider
import re

log = CPLog(__name__)

autoload = 'BiTHDTV'


class BiTHDTV(MovieProvider, Base):
    cat_ids = [
        ([7], ['720p', '1080p', 'bd50','2160p','brrip']),
    ]
    cat_backup_id = 7 # Movies

    def buildUrl(self, media, quality):
        value = fireEvent('library.query', media, single = True)
        pattern = re.compile('([^\s+\w]|_)+')

        query = tryUrlencode({
            'search': ' '.join(pattern.sub('', value).split()),
            'cat': self.getCatId(quality)[0]
        })
        return query
