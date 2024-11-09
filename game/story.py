class Story:
    def __init__(self, file_path):
        self.file_path = file_path
        self.chapters = {}
        self.load_story()

    def load_story(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            chapter_number = ""
            current_text = []

            for i, line in enumerate(lines):
                line = line.strip()

                if line.startswith('Chapter'):
                    chapter_number = line
                    if chapter_number:
                        self.chapters[chapter_number] = '\n'.join(current_text)
                        current_text = []

                else:
                    current_text.append(line)

                #adding the last chapter
                if i == len(lines) - 1:
                    self.chapters[chapter_number] = '\n'.join(current_text)

    def get_chapter(self, chapter):
        chapter_key = f'Chapter {chapter}'
        print(self.chapters.get(chapter_key, 'Chapter not found'))

