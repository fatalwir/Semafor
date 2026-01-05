import pcbnew

# Get the current board
board = pcbnew.GetBoard()

# Loop through all footprints on the board
for fp in board.GetFootprints():
    # Reference text
    ref = fp.Reference()
    if ref:
        ref.SetVisible(True)
        ref.SetLayer(pcbnew.F_Fab)

    # Value text
    val = fp.Value()
    if val:
        val.SetVisible(True)
        val.SetLayer(pcbnew.F_SilkS)

    # If reference starts with "R", move text to footprint center
    if ref.GetText().startswith("R"):
        # Get pad positions (board coordinates)
        pad1 = None
        pad2 = None

        # Find pads 1 and 2
        for pad in fp.Pads():
            if pad.GetPadName() == "1":
                pad1 = pad
            elif pad.GetPadName() == "2":
                pad2 = pad
        p1 = pad1.GetPosition()
        p2 = pad2.GetPosition()

        # Midpoint between pads
        center = pcbnew.VECTOR2I(
            (p1.x + p2.x) // 2,
            (p1.y + p2.y) // 2
        )

        ref.SetPosition(center)
        val.SetPosition(center)

        # Horizontal centering
        ref.SetHorizJustify(pcbnew.GR_TEXT_H_ALIGN_CENTER)
        val.SetHorizJustify(pcbnew.GR_TEXT_H_ALIGN_CENTER)

        # Vertical centering
        ref.SetVertJustify(pcbnew.GR_TEXT_V_ALIGN_CENTER)
        val.SetVertJustify(pcbnew.GR_TEXT_V_ALIGN_CENTER)


# Refresh the PCB view
pcbnew.Refresh()
