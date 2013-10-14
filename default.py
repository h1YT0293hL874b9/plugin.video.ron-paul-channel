import xbmcplugin
import xbmcgui
import sys

from BeautifulSoup import BeautifulSoup

from resources.lib import ronpaulchannel


thisPlugin = int(sys.argv[1])

def createListing():
  """
  Get list of most recent episodes
  """
  #req = urllib2.Request('http://www.ronpaulchannel.com/video/')
  #res = urllib2.urlopen(req)
  #html = res.read()
  #res.close()
  #soup = BeautifulSoup(html)
  #vids = soup.findAll('div', 'video-entry')
  vids = ronpaulchannel.getvideos()
  listing = []
  for vid in vids:
    # [label, label2, iconImage, thumbnailImage, path]
    item = [vid.__unicode__(), '', vid.thumbnail, vid.thumbnail, vid.url]
    listing.append(item)
  return listing


def sendToXbmc(listing):
  """
  Sends a listing to XBMC for display as a directory listing
  Plugins always result in a listing
  """
  global thisPlugin

  for item in listing:
    listItem = xbmcgui.ListItem(item)
    # handle, url, listitem [,isFolder=False, totalItems])
    xbmcplugin.addDirectoryItem(thisPlugin, '', listItem)
  
  xbmcplugin.endOfDirectory(thisPlugin)

sendToXbmc(createListing())
