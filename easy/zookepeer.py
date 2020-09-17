print("Hello! Which habitat do you need?")
animal = int(input("\nInput num of your habitat\n0 - Exit\n1 - Camel\n2 - Monkey\n3 - Wolf\nInput: "))

while(animal != 0):
    if(animal == 1):
        print(r"""
             _''''_.
         ___.  @   |         _.'''''''
        /___       |        /         '-
        ',,,,.     \    _.-'            \
             '      '.-'                 \
             |                            ,_.
             |                               ',
             |                                 '',
             |                                  , ':;
              ',,-,                            ,   ;;
                   ',,| ;,,                 ,'     ;;
                      ! ; !'',,,',',,,,'!  ;       :;
                     : ;  ! !       ! ! ;  ;       ;,
                     ; ;   ! !      ! !  ; ;
                    ; ;    ! !     ! !   ; ;
                    ; ;    ! !    ! !     ; ;
                   ;,,      !,!   !,!     ;,;
                   /_I      L_I   L_I     /_I
        """)
        print("Camel - nice habitat. He's live in Afrika")

    if(animal == 2):
        print(r"""
             __
             w  c(..)o   (
              \__(-)    __)
                  /\   (
                 /(_)___)
                 w /|
                  | \
                 m  m
        """)
        print("Monkey like banana! Monkey lives in jungle")

    if(animal == 3):
        print(r"""
                           ,     ,
                        |\---/|
                       /  , , |
                  __.-'|  / \ /
         __ ___.-'        ._O|
      .-'  '        :      _/
     / ,    .        .     |
    :  ;    :        :   _/
    |  |   .'     __:   /
    |  :   /'----'| \  |
    \  |\  |      | /| |
     '.'| /       || \ |
     | /|.'       '.l \\_
     || ||             '-'
     '-''-'

        """)
        print("Wolf say AUFF!! Wolf lives in forest")

    if(animal == 0):
        break

    animal = int(input("\nInput num of your habitat\n0 - Exit\n1 - Camel\n2 - Monkey\nInput: "))

