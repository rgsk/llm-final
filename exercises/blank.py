# the blank in an exercise; comparing against it fails without printing the
# real value, which pytest's assert message would otherwise show
class Blank:
    def __eq__(self, other: object) -> bool:
        # pytest leaves this frame, and so the real value in other, out of tracebacks
        __tracebackhide__ = True
        raise AssertionError("fill in this blank")

    __hash__ = None  # type: ignore[assignment]


___ = Blank()
