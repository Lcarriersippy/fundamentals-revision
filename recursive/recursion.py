def ghost_buster(ghosts):
    ghost_counter = 0
    for ghost in ghosts:
        if type(ghost) == list:
            ghost_counter += ghost_buster(ghost)

        elif (ghost['is_ghost']):
            ghost_counter+=1

    return ghost_counter