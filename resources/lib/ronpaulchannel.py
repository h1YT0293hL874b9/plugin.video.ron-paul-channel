import urllib2

from BeautifulSoup import BeautifulSoup

BASE_URL = 'http://www.ronpaulchannel.com/'

def getvideos(category=None, page=None):
  """
  Get a list of videos
  """
  url = BASE_URL
  if category is not None:
    url += "video_category/%s" % category
  else:
    url += 'video/'

  if page is not None:
    url += "page/%s" % page
   
  req = urllib2.Request(url)
  res = urllib2.urlopen(req)
  html = res.read()
  res.close()
  soup = BeautifulSoup(html, 
     convertEntities=BeautifulSoup.HTML_ENTITIES)
  vids = soup.findAll('div', 'video-entry')
  videoItems = []

  for vid in vids:
    thumbnail = vid.find('img')['src']
    title = vid.find('h3').text
    date = vid.find('div', 'updated').text.replace('Updated ', '')
    url = vid.find('a')['href']
    videoItem = VideoItem(title, url, date, thumbnail)
    videoItems.append(videoItem)
  
  return videoItems


class VideoItem:

  def __init__(self, title, url, date, thumbnail):
    self.thumbnail = thumbnail
    self.title = title
    self.date = date
    self.url = url

  def __unicode__(self):
    return u"%s - %s" % (self.date, self.title)


if __name__ == '__main__':
  vids = getvideos()
  for vid in vids:
    print vid.__unicode__()

