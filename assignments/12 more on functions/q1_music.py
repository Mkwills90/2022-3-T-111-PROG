def main():
    music, group, singer = input("Input music, group, singer: ").split(",")
    state_music_opinion(music, group, singer)
    state_music_opinion()


def state_music_opinion(
    genre: str = "Classic Rock",
    music_group: str = "The Beatles",
    vocalist: str = "Freddie Mercury",
) -> None:
    print(f"The best type of music is {genre}")
    print(f"The best music group is {music_group}")
    print(f"The best lead vocalist is {vocalist}")


if __name__ == "__main__":
    main()
