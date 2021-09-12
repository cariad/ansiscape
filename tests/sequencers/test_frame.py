# from typing import Optional

# from pytest import mark

# from ansiscape.encoders import FrameSequencer
# from ansiscape.enums import Frame, InterpretationKey, SelectGraphicRendition
# from ansiscape.types.sequencer_result import SequencerResult


# def test_key() -> None:
#     assert FrameSequencer().key == InterpretationKey.FRAME


# @mark.parametrize(
#     "frame, expect",
#     [
#         (None, SequencerResult(sgr=SelectGraphicRendition.FRAME_OFF)),
#         (Frame.CIRCLE, SequencerResult(sgr=SelectGraphicRendition.FRAME_CIRCLE)),
#         (Frame.BOX, SequencerResult(sgr=SelectGraphicRendition.FRAME_BOX)),
#         (Frame.NONE, SequencerResult(sgr=SelectGraphicRendition.FRAME_OFF)),
#     ],
# )
# def test_resolve(frame: Optional[Frame], expect: SequencerResult) -> None:
#     assert FrameSequencer().resolve(frame) == expect
