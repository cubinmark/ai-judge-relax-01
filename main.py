import os

TEXT = """The rain has finished with the banana leaves.
One drop still travels the long green rib, gathers itself, and lets go.
Somewhere a frog tries one low note, then thinks better of it.
The kettle is warm, not hot. The tea can wait.
Nothing is being asked of this hour.
The road outside has emptied; even the dogs have gone in.
Light the colour of weak tea rests on the wet stones,
and the stones, which held the whole day's heat, are giving it back slowly.
Whatever was unfinished can stay unfinished until morning.
It will keep. Things mostly do.
For now the world is only this: a cool floor underfoot,
air that smells of rain and woodsmoke,
and time moving at the speed of a drop on a leaf."""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
