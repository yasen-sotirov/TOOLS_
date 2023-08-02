class Comment:
    CONTENT_LEN_MIN = 3
    CONTENT_LEN_MAX = 200
    CONTENT_LEN_ERR = f'Content must be between {CONTENT_LEN_MIN} and {CONTENT_LEN_MAX} characters long!'

    # Todo: Finish the implementation
    # Names of methods/attributes should be exactly match those in the README file

    def __init__(self, content: str, author) -> None:
        self.content = content
        self.author = author

    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, value):
        if len(value) < self.CONTENT_LEN_MIN or len(value) > self.CONTENT_LEN_MAX:
            raise ValueError(self.CONTENT_LEN_ERR)
        self._content = value

    def to_string(self):

        comment_body = self.content
        author = f'User: {self.author}'
                
        return '\n'.join(['----------', comment_body, author,'----------'])
    

    