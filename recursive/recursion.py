def ghost_buster(ghosts):
    ghost_counter = 0
    for ghost in ghosts:
        if (ghost['is_ghost']):
            ghost_counter+=1

    return ghost_counter