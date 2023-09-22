
main_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
backup_list = [[3, 3, 3, 3, 3], [6, 4, 4, 4, 10], [5, 5, 5, 5, 5]]

for primary_index in range(len(main_list)):
    print()
    print('# START main', primary_index)
    print()
    for secondary_index in range(len(main_list[primary_index])):
        print('main value  ', main_list[primary_index][secondary_index])
        print('backup value', backup_list[primary_index][secondary_index])

    print()
    print('# FIN main', primary_index)
    print()
