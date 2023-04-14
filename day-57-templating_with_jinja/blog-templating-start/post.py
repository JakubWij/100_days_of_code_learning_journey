class Post():
    def __init__(self, posts_dictionary, post_number):
        self.dictionary = posts_dictionary
        self.body = self.dictionary[post_number]["body"]
        self.title = self.dictionary[post_number]["title"]
        self.subtitle = self.dictionary[post_number]["subtitle"]
        self.id = self.dictionary[post_number]["id"]



