class StringSet:
    def __init__(self, a_string: str = "") -> None:
        self.__words = []
        for word in a_string.split():
            self.add(word)

    def __str__(self) -> str:
        return " ".join(self.__words)

    def add(self, word: str) -> None:
        if word not in self.__words:
            self.__words.append(word)

    def __add__(self, other: "StringSet") -> "StringSet":
        result = StringSet()
        for word in self.__words:
            result.add(word)
        for word in other.__words:
            result.add(word)

        return result

    def size(self) -> int:
        return len(self.__words)

    def at(self, index: int) -> str:
        return self.__words[index]

    def find(self, word: str) -> bool:
        return word in self.__words
