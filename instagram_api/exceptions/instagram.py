

class InstagramException(Exception):

    def __init__(self, *args, response: dict, **kwargs):
        self.message = args[0]
        self.response = response

        super(InstagramException, self).__init__(*args, **kwargs)
