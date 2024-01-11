class ForumPost():
    def __init__(self, author: str, text: str, upvotes: int):
        self.author = author
        self.text = text
        self.upvotes = upvotes
        self.replies = []

    def add_reply(self, reply: str):
        self.replies.append(reply)

    def view(self):
        post_view = f'{self.text} / by {self.author}, {self.upvotes} votes.'
        replies_view = '\n'.join((f'- {reply}' for reply in self.replies))
        
        return post_view + '\n' + replies_view