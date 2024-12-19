ai_or_player = input(
"""
Welcome to our < Connect Four Game > :)
Choose between 1 : 2
1 => Vs AI,
2 => Two players
""")

# level_of_difficulty = 2

if ai_or_player == '1':
    choice = input(
                    '''
Choose between 1 : 4
1 => Heuristic1 with Alpha & Beta,
2 => Heuristic1 without Alpha & Beta,
3 => Heuristic2 with Alpha & Beta,
4 => Heuristic without Alpha & Beta,
''')
    
        
    if choice == '1':
        import Heuristic1_with_AB

    elif choice == '2':
        import Heuristic1_without_AB

    elif choice == '3':
        import Heuristic2_with_AB

    elif choice == '4':
        import Heuristic2_without_AB

    else:
        print("Invalid option")

elif ai_or_player == '2':
    import Two_players
else:
    print("Invalid option")







