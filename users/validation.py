import re


class Validation:
    @staticmethod
    def is_empty(value):
        return value is None or value.strip() == ""

    @staticmethod
    def is_any_empty(*args):
        for arg in args:
            if Validation.is_empty(arg):
                return True
        return False

    @staticmethod
    def match(p1, p2):
        return p1.strip() == p2.strip()

    @staticmethod
    def is_valid_email(email):
        if email is None or email.strip() == "":
            return False
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email):
            return False
        return True

    @staticmethod
    def file_exists(file):
        return file is not None

    @staticmethod
    def valid_file_size(file, size):
        return file.size <= size * 1024 * 1024

    @staticmethod
    def valid_file_extension(file, extensions):
        return file.name.split(".")[-1] in extensions
