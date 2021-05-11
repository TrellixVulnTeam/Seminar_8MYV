import logging
from scrapy.utils.project import get_project_settings

from TweetScraper.items import Tweet_item
from unternehmen.models import Tweets
import datetime

logger = logging.getLogger(__name__)
SETTINGS = get_project_settings()

class SaveToFilePipeline(object):

    def process_item(self, item, spider):

        if isinstance(item, Tweet_item):        # Item des Models Tweet erstellen, infos aus Tweet_item des Crawlers
            unternehmensname = item['unternehmensname']
            userId = item['userId']
            datum = item['datum']
            woerter = item['woerter']
            schluessel = item['schluesselId']

            if (userId == schluessel ):
                Tweets.objects.create(
                    unternehmensname=unternehmensname,
                    userId=userId,
                    datum=datum,
                    woerter=woerter,
                    schluesselId=schluessel,
                )

        else:
            print("Der Tweet gehört nicht zu dem Benutzer(d.h. Werbung oder Retweet)")
