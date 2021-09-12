class Sources:
  def __init__(self, id, name, url):
    self.source_id = id
    self.name = name
    self.source_address = url[10:]
class Articles:
  def __init__(self, id, name, author, title, description, url, urlToImage, publishedAt):
    self.id = id
    self.name = name
    self.author = author
    self.title = title
    self.description = description
    self.articleurl = url
    self.imageurl = urlToImage
    self.publishtime = publishedAt[:-10]