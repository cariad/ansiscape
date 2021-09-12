# from typing import Optional

# from pytest import mark

# from ansiscape.encoders import OverlineSequencer
# from ansiscape.enums import InterpretationKey, SelectGraphicRendition
# from ansiscape.types.sequencer_result import SequencerResult


# def test_key() -> None:
#     assert OverlineSequencer().key == InterpretationKey.OVERLINE


# @mark.parametrize(
#     "overline, expect",
#     [
#         (None, SequencerResult(sgr=SelectGraphicRendition.OVERLINE_OFF)),
#         (True, SequencerResult(sgr=SelectGraphicRendition.OVERLINE_ON)),
#         (False, SequencerResult(sgr=SelectGraphicRendition.OVERLINE_OFF)),
#     ],
# )
# def test_resolve(overline: Optional[bool], expect: SequencerResult) -> None:
#     assert OverlineSequencer().resolve(overline) == expect
