class Story:
    def __init__(self, file_path):
        self.file_path = file_path
        self.chapters = {}
        self.load_story()


