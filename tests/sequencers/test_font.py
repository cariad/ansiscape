# from typing import Optional

# from pytest import mark

# from ansiscape.encoders import FontSequencer
# from ansiscape.enums import Font, InterpretationKey, SelectGraphicRendition
# from ansiscape.types.sequencer_result import SequencerResult


# def test_key() -> None:
#     assert FontSequencer().key == InterpretationKey.FONT


# @mark.parametrize(
#     "font, expect",
#     [
#         (None, SequencerResult(sgr=SelectGraphicRendition.FONT_DEFAULT)),
#         (Font.ALT_0, SequencerResult(sgr=SelectGraphicRendition.FONT_ALT_0)),
#         (Font.ALT_1, SequencerResult(sgr=SelectGraphicRendition.FONT_ALT_1)),
#         (Font.ALT_2, SequencerResult(sgr=SelectGraphicRendition.FONT_ALT_2)),
#         (Font.ALT_3, SequencerResult(sgr=SelectGraphicRendition.FONT_ALT_3)),
#         (Font.ALT_4, SequencerResult(sgr=SelectGraphicRendition.FONT_ALT_4)),
#         (Font.ALT_5, SequencerResult(sgr=SelectGraphicRendition.FONT_ALT_5)),
#         (Font.ALT_6, SequencerResult(sgr=SelectGraphicRendition.FONT_ALT_6)),
#         (Font.ALT_7, SequencerResult(sgr=SelectGraphicRendition.FONT_ALT_7)),
#         (Font.ALT_8, SequencerResult(sgr=SelectGraphicRendition.FONT_ALT_8)),
#         (Font.DEFAULT, SequencerResult(sgr=SelectGraphicRendition.FONT_DEFAULT)),
#     ],
# )
# def test_resolve(font: Optional[Font], expect: SequencerResult) -> None:
#     assert FontSequencer().resolve(font) == expect
