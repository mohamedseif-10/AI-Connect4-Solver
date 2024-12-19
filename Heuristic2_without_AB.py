from Global import  *


def is_valid_window(window, piece):
    # A window is valid if it has no opponent pieces and at least one empty space
    opponent_piece = 1
    return opponent_piece not in window and window.count(piece) > 0


def count_winning_opportunities(board, piece):
    WINDOW_LENGTH = 4
    opportunities = 0

    ## Horizontal
    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(COLUMN_COUNT - WINDOW_LENGTH + 1):
            window = row_array[c:c + WINDOW_LENGTH]
            if is_valid_window(window, piece):
                opportunities += 1

    ## Vertical
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(ROW_COUNT - WINDOW_LENGTH + 1):
            window = col_array[r:r + WINDOW_LENGTH]
            if is_valid_window(window, piece):
                opportunities += 1

    ## Positive Diagonal
    for r in range(ROW_COUNT - WINDOW_LENGTH + 1):
        for c in range(COLUMN_COUNT - WINDOW_LENGTH + 1):
            window = [board[r + i][c + i] for i in range(WINDOW_LENGTH)]
            if is_valid_window(window, piece):
                opportunities += 1

    ## Negative Diagonal
    for r in range(ROW_COUNT - WINDOW_LENGTH + 1):
        for c in range(COLUMN_COUNT - WINDOW_LENGTH + 1):
            window = [board[r + 3 - i][c + i] for i in range(WINDOW_LENGTH)]
            if is_valid_window(window, piece):
                opportunities += 1

    return opportunities



def minimax(board, depth, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI_PIECE):
                return (None, 100000000000000)
            elif winning_move(board, PLAYER_PIECE):
                return (None, -10000000000000)
            else: # Game is over, no more valid moves
                return (None, 0)
        else: # Depth is zero
            return (None, count_winning_opportunities(board, AI_PIECE))
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, AI_PIECE)
            new_score = minimax(b_copy, depth-1, False)[1]
            if new_score > value:
                value = new_score
                column = col
        return column, value

    else: # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, PLAYER_PIECE)
            new_score = minimax(b_copy, depth-1, True)[1]
            if new_score < value:
                value = new_score
                column = col
        return column, value



while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, Black, (0,0, width, SQUARESIZE))
			posx = event.pos[0]
			if turn == PLAYER:
				pygame.draw.circle(screen, Mint_green, (posx, int(SQUARESIZE/2)), RADIUS)

		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, Black, (0,0, width, SQUARESIZE))
			#print(event.pos)
			# Ask for Player 1 Input
			if turn == PLAYER:
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, PLAYER_PIECE)

					if winning_move(board, PLAYER_PIECE):
						label = myfont.render("Player 1 wins!!", 1, Mint_green)
						screen.blit(label, (40,10))
						game_over = True

					turn += 1
					turn = turn % 2

					print_board(board)
					draw_board(board)


	# # Ask for Player 2 Input
	if turn == AI and not game_over:				

		if (board == 0).sum() == board.size:
			col = random.choice(get_valid_locations(board))
		else:
			col, minimax_score = minimax(board, level_of_difficulty, True)  # will cause a delay because no Alpha and Beta

		if is_valid_location(board, col):
			# pygame.time.wait(500)
			row = get_next_open_row(board, col)
			drop_piece(board, row, col, AI_PIECE)

			if winning_move(board, AI_PIECE):
				label = myfont.render("Player 2 wins!!", 1, Purple)
				screen.blit(label, (40,10))
				game_over = True

			print_board(board)
			draw_board(board)

			turn += 1
			turn = turn % 2

	if game_over:
            pygame.time.wait(2000)
            print("Heuristic2 without Alpha & Beta")
            print(f"Level of difficulty = {level_of_difficulty}")