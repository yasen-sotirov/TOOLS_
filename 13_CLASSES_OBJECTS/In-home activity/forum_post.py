class ForumPost():
    def __init__(self, author: str, text: str, upvotes: int):
        self.author = author
        self.text = text
        self.upvotes = upvotes
        self.replies_collection = []

    def add_reply(self, new_reply: str):
        self.replies_collection.append(new_reply)

    def view(self):
        if self.replies_collection:
            post_view = f"{self.text} / by {self.author}, {self.upvotes} votes."
            replies = '\n'.join(f"- {rpl}" for rpl in self.replies_collection)
            return post_view + '\n' + replies
        return f"{self.text} / by {self.author}, {self.upvotes} votes."


