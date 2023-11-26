class BadWordsList:
    def __init__(self):
        pass

    def banned_by_google(self, file_txt: str=None, storage=False):
        if storage:
            try:
                with open(file_txt, "r") as file:
                    BLACKLIST_WORDS = [line.strip() for line in file]
                return BLACKLIST_WORDS
            except FileNotFoundError:
                print(f"Error: File '{file_txt}' not found.")
                return []
            except Exception as e:
                print(f"Error reading file: {e}")
                return []
        else:
            return "Error required storage=True"
