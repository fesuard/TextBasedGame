import os
import sys


class Story:
    def __init__(self):
        # Adjust the base path for development environment and for executable environment
        if hasattr(sys, '_MEIPASS'):
            base_path = os.path.join(sys._MEIPASS) # Temp directory for bundled files
        else:
            base_path = os.path.dirname(os.path.dirname(__file__))  # Development environment

        story_file = os.path.join(base_path, 'assets', 'text', 'story.txt')

        # Ensure the file exists
        if not os.path.exists(story_file):
            raise FileNotFoundError(f"Story file not found: {story_file}")

        # Load the story
        with open(story_file, 'r') as file:
            self.chapters = self.load_story(file)

    def load_story(self, file):
        chapters = {}
        chapter_number = ""
        current_text = []

        for line in file:
            line = line.strip()

            if line.startswith('Chapter'):
                chapter_number = line
                if chapter_number:
                    chapters[chapter_number] = '\n'.join(current_text)
                    current_text = []

            else:
                current_text.append(line)

        #adding the last chapter
        if chapter_number:
            chapters[chapter_number] = '\n'.join(current_text)

        return chapters

    def get_chapter(self, chapter):
        chapter_key = f'Chapter {chapter}'
        print(self.chapters.get(chapter_key, 'Chapter not found'))

