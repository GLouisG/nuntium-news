class Sources:
  def __init__(self, id, name, url):
    self.id = id
    self.name = name
    self.sourceaddress = url
class Articles:
  def __init__(self, id, name, author, title, description, url, urlToImage):
    self.id = id
    self.name = name
    self.author = author
    self.title = title
    self.description = description
    self.articleurl = url
    self.imageurl = urlToImage