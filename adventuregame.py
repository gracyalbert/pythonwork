import time
from tkinter import *
from random import *
import os,sys
os.system("title READY...FOR FUN!!!")
def dice_rolling():
    os.system("cls")
    os.system("color B")
    number=randint(1,6)
    if number==1:
        print("The dice is showing:")
        print("[------------]")
        print("[            ]")
        print("[     O      ]")
        print("[            ]")
        print("[------------]")
        print('\n')
        time.sleep(1)
        print("▒█▀▀█ ░█▀▀█ ▒█▀▀▀█ ▒█▀▀▀█ ")
        print("▒█▄▄█ ▒█▄▄█ ░▀▀▀▄▄ ░▀▀▀▄▄ ")
        print("▒█░░░ ▒█░▒█ ▒█▄▄▄█ ▒█▄▄▄█ ")
        print("")
        print(" You pass the your chance, now  next player turn")
        input("Press enter to continue....")
        
    if number==2:
        os.system("cls")
        os.system("color E")
        print("The dice is showing:")
        print("[------------]")
        print("[            ]")
        print("[   O   O    ]")
        print("[            ]")
        print("[------------]")
        print('\n')
        time.sleep(1)
        print('@@           @@  @@@@@  @        @@@@@    @@@@@@        @@   @@      @@@@@  ')
        print(' @@         @@   @      @       @        @      @      @@ @ @ @@     @ ')
        print('  @@   @   @@    @@@    @       @        @      @     @@   @   @@    @@@  ')
        print('   @@ @ @ @@     @      @       @        @      @    @@         @@   @  ')
        print('    @@   @@      @@@@@  @@@@@@   @@@@@    @@@@@@    @@           @@  @@@@@   ')
        print('\n')
        name=input("Enter your name")
        print('Hey',name,'! Welcome to the "Riddle Game!"')
        time.sleep(2)
        print('\n')
        print('                             00000000000000000000000000')
        print('                        000000000000000000000000000000000000')
        print('                    00000000000000000000000000000000000000000000')
        print('                 00000000000000000000000000000000000000000000000000')
        print('               000000000000000000000000000000000000000000000000000000')
        print('             0000000000000000000000000000000000000000000000000000000000')
        print('           00000000000000000000000000000000000000000000000000000000000000')
        print('         000000000000000000000000000000000000000000000000000000000000000000')
        print('        00000000000000000000000000000000000000000000000000000000000000000000')
        print('      000000000000000000000000000000000000000000000000000000000000000000000000')
        print('     00000000000000000000000000000000000000000000000000000000000000000000000000')
        print('    0000000000000000000000000000000000000000000000000000000000000000000000000000')
        print('   000000000000000    0000000000000000000000000000000000000000    000000000000000')
        print('  000000000000000      00000000000000000000000000000000000000      000000000000000')
        print('  00000000000000        000000000000000000000000000000000000        00000000000000')
        print(' 000000000000000        000000000000000000000000000000000000        000000000000000')
        print(' 000000000000000        000000000000000000000000000000000000        000000000000000')
        print('0000000000000000        000000000000000000000000000000000000        0000000000000000')
        print('0000000000000000        000000000000000000000000000000000000        0000000000000000')
        print('00000000000000000      00000000000000000000000000000000000000      00000000000000000')
        print('000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        print('000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        print('000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        print('000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        print(' 0000000000000000000000000000000000000000000000000000000000000000000000000000000000')
        print(' 0000000000000000                                                  0000000000000000')
        print('  0000000000000000                                                0000000000000000')
        print('  00000000000000000                                              00000000000000000')
        print('   00000000000000000                                            00000000000000000')
        print('    000000000000000000                                        000000000000000000')
        print('     0000000000000000000                                    0000000000000000000')
        print('      00000000000000000000                                00000000000000000000')
        print('       000000000000000000000                            000000000000000000000')
        print('         00000000000000000000000                    00000000000000000000000')
        print('          0000000000000000000000000000000000000000000000000000000000000000')
        print('            000000000000000000000000000000000000000000000000000000000000')
        print('             0000000000000000000000000000000000000000000000000000000000')
        print('              00000000000000000000000000000000000000000000000000000000')
        print('                 00000000000000000000000000000000000000000000000000')
        print('                     000000000000000000000000000000000000000000')
        print('                          00000000000000000000000000000000')
        print('Hi! I am Suzy')
        print('I will ask you some riddles...')
        request=input('Would you like to continue? Type "yes" or "no"')
        if request == 'yes':
            time.sleep(1)
            print('\n')
            print("ALL THE BEST")
            time.sleep(1)
            print('Let\'s begin........')
            time.sleep(1)
            print('\n')
            print('Here is your first riddle.')
            time.sleep(1)
            print('\n')
            ans1=input("1) What kind of a key opens a banana?")
            time.sleep(1)
            print('\n')
            if ans1=='monkey' or ans1=='Monkey':
                print('MONKEY.....Yippee! You got it right')
                print('            .-"""-.')
                print('          _/-=-.   \ ')
                print('         (_|a a/   |_')
                print('          / "  \   ,_)')
                print("     _    \`=' /__/")
                print("    / \_  .;--'  `-.")
                print('    \___)//      ,  \ ')
                print('     \ \/;        \  \ ')
                print('      \_.|         | | ')
                print("       .-\ '     _/_/ ")
                print("      .'  _;.    (_  \ ")
                print("     /  .'   `\   \\_/")
                print('    |_ /       |  |\\ ')
                print('   /  _)       /  / ||')
                print('  /  /       _/  /  //')
                print('  \_/       ( `-/  ||')
                print('            /  /   \\ .-.')
                print("            \_/     \'-'/")
            else:    
                print('Sorry! Wrong answer')
                print('The answer is "MONKEY"')
                print('            .-"""-.')
                print('          _/-=-.   \ ')
                print('         (_|a a/   |_')
                print('          / "  \   ,_)')
                print("     _    \`=' /__/")
                print("    / \_  .;--'  `-.")
                print('    \___)//      ,  \ ')
                print('     \ \/;        \  \ ')
                print('      \_.|         | | ')
                print("       .-\ '     _/_/ ")
                print("      .'  _;.    (_  \ ")
                print("     /  .'   `\   \\_/")
                print('    |_ /       |  |\\ ')
                print('   /  _)       /  / ||')
                print('  /  /       _/  /  //')
                print('  \_/       ( `-/  ||')
                print('            /  /   \\ .-.')
                print("            \_/     \'-'/")
            print('\n')
            enter=input('Press enter for next riddle.....')
            print('\n')
            ans2=input('2) Why was six afraid of seven?')
            time.sleep(1)
            print('\n')
            if ans2=='seven ate nine' or ans2=='7 8 9' or ans2=='789':
                print('Yahoo!! Right answer')
                print('SEVEN ATE NINE')
                print('|""""""|  ("""""")  9999999 ')
                print('       |  |      |  9     9')
                print('       |  \______/  9999999')
                print('       |  /      \        9')
                print('       |  |      |        9')
                print('       |  (______)  9999999')
            else:
                print('Oho! Wrong answer')
                print('The Answer is "SEVEN ATE NINE(7 8 9)"')
                print('|""""""|  ("""""")  9999999 ')
                print('       |  |      |  9     9')
                print('       |  \______/  9999999')
                print('       |  /      \        9')
                print('       |  |      |        9')
                print('       |  (______)  9999999')
            print('\n')
            enter=input('Press enter for next riddle....')
            print('\n')
            ans3=input('3) What has one eye but cannot see?')
            time.sleep(1)
            print('\n')
            if ans3=='needle' or ans3=='Needle':
                print('NEEDLE')
                print('Great! Right answer.')
                print('             \ ')
                print('              \ ')
                print('  ___          \ ')
                print(":` o `:         \ ")
                print("|`---`|          \ ")
                print('|MmmmM|  .--.    ()')
                print('|MMMMM| /    \   /\ ')
                print("|mMMMm|/      `.'  '.__.")
                print(' `---` ')
            else:
                print('Ofo!! Wrong answer')
                print('The Answer is "NEEDLE"')
                print('             \ ')
                print('              \ ')
                print('  ___          \ ')
                print(":` o `:         \ ")
                print("|`---`|          \ ")
                print('|MmmmM|  .--.    ()')
                print('|MMMMM| /    \   /\ ')
                print("|mMMMm|/      `.'  '.__.")
                print(' `---` ')
            print('\n')
            enter=input('Press enter for next riddle....')
            print('\n')
            ans4=input('4) What makes music on your hair?')
            time.sleep(1)
            print('\n')
            if ans4=='hair band' or ans4=='Hair band' or ans4=='band' or ans4=='Band':
                print('HAIR BAND')
                print('Yay!! Correct')
                print('                $$$$$              $$$$$')
                print('               $     $            $     $')
                print('               $      $          $      $')
                print('               $       $        $       $')
                print('               $        $_$$$$_$        $')
                print('                $        $    $        $')
                print('               $         $    $         $')
                print('             $$ $        $    $        $ $$')
                print('            $  $         $$$$$$         $  $')
                print('            $  $   $$$$$$ $  $ $$$$$$   $  $')
                print('            $   $ $    $ $$  $$ $   $ $   $')
                print('             $  $$    $ $ $  $ $ $    $$  $')
                print('          ____$  $$$$$ $  $  $  $ $$$$$  $____')
                print('         / ____$      $   $  $   $      $____ \ ')
                print('        / /    $     $    $  $    $     $    \ \ ')
                print('       / /      $   $     $  $     $   $      \ \ ')
                print('      | |        $$$      $$$$      $$         | |')
                print('      | |                                      | |')
                print('      | |                                      | |')
                print('      | |                                      | |')
                print('      | |                                      | |')
                print('      | |                                      | |')
                print('      | |                                      | |')
                print('      | |                                      | |')
                print('      | |                                      | |')
                print('      | |                                      | |')
                print('      | |                                      | |')
                print('       \ \                                    / /')
                print('        \ \                                  / /')
                print('         \ \                                / /')

            else:
                print('Wrong answer')
                print('The Answer is "HAIR BAND"')
                print('                $$$$$              $$$$$')
                print('               $     $            $     $')
                print('               $      $          $      $')
                print('               $       $        $       $')
                print('               $        $_$$$$_$        $')
                print('                $        $    $        $')
                print('               $         $    $         $')
                print('             $$ $        $    $        $ $$')
                print('            $  $         $$$$$$         $  $')
                print('            $  $   $$$$$$ $  $ $$$$$$   $  $')
                print('            $   $ $    $ $$  $$ $   $ $   $')
                print('             $  $$    $ $ $  $ $ $    $$  $')
                print('          ____$  $$$$$ $  $  $  $ $$$$$  $____')
                print('         / ____$      $   $  $   $      $____ \ ')
                print('        / /    $     $    $  $    $     $    \ \ ')
                print('       / /      $   $     $  $     $   $      \ \ ')
                print('      | |        $$$      $$$$      $$         | |')
                print('      | |                                      | |')
                print('      | |                                      | |')
                print('      | |                                      | |')
                print('      | |                                      | |')
                print('      | |                                      | |')
                print('      | |                                      | |')
                print('      | |                                      | |')
                print('      | |                                      | |')
                print('      | |                                      | |')
                print('      | |                                      | |')
                print('       \ \                                    / /')
                print('        \ \                                  / /')
                print('         \ \                                / /')
            print('\n')
            enter=input('Press enter for next riddle....')
            print('\n')
            print('5) A donkey behind another donkey')
            time.sleep(1)
            print('                         /\        /\\                             /\         /\\')
            print('                        ( \\        // )                          ( \\        // )')
            print('                         \ \\      // /                            \ \\      // /')
            print('                          \_\\||||//_/                              \_\\||||//_/')
            print('                           \/ _  _ \\                                \/ _  _ \\')
            print('                          \/|(O)(O)|                               \/|(O)(O)|')
            print('                         \/ |      |                              \/ |      |')
            print('     ___________________\/  \      /          ___________________\/  \      /')
            print('     //                //     |____|          //                //     |____|')
            print('    //                ||     /      \        //                ||     /      \\')
            print('   //|                \|     \ 0  0 /       //|                \|     \ 0  0 /')
            print('  // \       )         V    / \____/       // \       )         V    / \____/')
            print(' //   \     /        (     /              //   \     /        (     /')
            print('""     \   /_________|  |_/              ""     \   /_________|  |_/')
            print('       /  /\   /     |  ||                      /  /\   /     |  ||')
            print('      /  / /  /      \  ||                     /  / /  /      \  ||')
            print('      | |  | |        | ||                     | |  | |        | ||')
            print('      | |  | |        | ||                     | |  | |        | ||')
            print('      |_|  |_|        |_||                     |_|  |_|        |_||')
            print('      \_\  \_\         \_\                     \_\  \_\         \_\\')
            time.sleep(1)
            print('I’m behind that second donkey')
            print('But there is a whole nation behind me')
            print('It is a killing you can describe in a word.')
            ans5=input('Guess the Word')
            time.sleep(1)
            print('\n')
            if ans5=='assassination'or ans5=='Assassination':
                print('Yuhoo!! Right Answer')
            else:
                print('Oops!! Wrong answer')
                print('The Answer is "ASSASSINATION (ass-ass-i-nation)"')
            print('\n')
            time.sleep(2)
            print('Here we complete our riddles')
            print('\n')
            time.sleep(1)
            print('Thank you!!')
            print('\n')
            print('  *  *     *  *')
            print(' *     * *      *')
            print(' *      *       *')
            print('  *            *')
            print('   *         *')
            print('    *       *')
            print('      *   *')
            print('        *')

            enter=input('Press enter to exit....')
        elif request=='no':
            print('\n')
            print('OK! Thank You')
            print('\n')
            input('Press Enter to leave the program')
        else:
            print("ERROR")
        print("Try again next time!!")

              

    if number==3:
        os.system("cls")
        os.system("color F")
        print("The dice is showing:")
        print("[------------]")
        print("[   O   O    ]")
        print("[     O      ]")
        print("[            ]")
        print("[------------]")
        print('\n')
        time.sleep(1)
        def joint_rolling():
            score=randint(1,6)
            if score==1:
                print("You got slot 1")
                input("Press enter to continue.")
                animal=input("Enter an Animal's name.")
                verb=input("Enter a Verb ending in -ing.")
                noun=input("Enter a Plural Noun.")
                verb1=input("Enter a Verb- Present Tense.")
                adjective=input("Enter an adjective.")
                noun1=input("Enter a Plural Noun .")
                noun2=input("Enter the same Plural Noun.")
                verb1=input("Enter a Verb- Present Tense.")
                number=input("Enter a Number.")
                print("JINGLE BELLS")
                print("Dashing through the snow")
                print("in a one",animal,"open sleigh.")
                print("O'er the fields we go")
                print(verb,"all the way.")
                print("Bells on bobtail ring,")
                print("making",noun,"bright.")
                print("What fun it is to",verb1,)
                print("and sing a/an",adjective,"song tonight!")
                print("Jingle",noun1,", jingle",noun2,".")
                print("Jingle all the way!")
                print("Oh what fun it is to",verb1,)
                print("in a one-horse open sleigh.")
                print("Jingle bells, jingle bells.")
                print("Jingle all the way! Oh")
                print("what fun it is to ride")
                print("in a",number,"horse open sleigh.")
                
            elif score==2:
                print("You got slot 2")
                input("Press enter to continue.")
                body_part=input("Enter a Body Part.")
                noun=input("Enter a Noun")
                vegetable=("Enter a Vegetable's name")
                adjective=("Enter an Adjective")
                verb=input("Enter a Verb")
                nouns=input("Enter Nouns")
                adjective1=input("Enter an Adjective")
                number=input("Enter a Number")
                verb1=input("Enter a verb")
                print("RECESS!")
                print("Here are some things to do at recess.")
                print("1. Start a game of touch",body_part,"-ball.")
                print("2. Put a",noun,"in someone's lunch bag.")
                print("3. Start a",vegetable,"fight in the school",adjective,"room.")
                print("4. Choose sides and have a",verb,"ball tournament.")
                print("5. Demand more",nouns,"and shorter",adjective1,"classes.")
                print("6. Choose",number,"kids to be it at",verb1,".")

            elif score==3:
                print("You got slot 3")
                input("Press enter to continue.")
                name=input("Enter a Silly name.")
                profession=input("Enter an Unrealistic profession Name.")
                country=input("Enter a Country's name.")
                name1=input("Enter another silly name.")
                color=input("Enter a Color.")
                adjective=input("Enter an Adjective.")
                adverb=input("Enter an Adverb.")
                name2=input("Enter the Third silly name.")
                name3=input("Enter the Fourth silly name.")
                feature=input("Enter a Facial feature.")
                name4=input("Enter the Second silly name.")
                city=input("Enter the name of an US City.")
                name5=input("Enter One more silly name.")
                verb=input("Enter a Verb.")
                noun=input("Enter a Noun.")
                actor=input("Enter the name of a formerly badass actor now selling out.")
                noun1=input("Enter a Noun.")
                print("GENERIC COMIC SUPERHERO MOVIE")
                print("Meet our hero",name,"a super-intelligent",profession,".")
                print("A run-in with the",country,"military leads him to create his alter-ego",name1,",")
                print(",a",color,adjective,"gaint capable of great destruction.")
                print("He",adverb,"battles the militry with his girlfriend",name2,".")
                print("Eventually it is discovered that our hero's long-time collegue",name3,",")
                print("distinguished by his",feature,"is trying turn",name4,"into a weapon,")
                print("leading to a climactic (if pointless) battle in downtown",city,)
                print("with an evil version of the same gaint alter-ego called",name5,".")
                print("Eventually the enemy is subdued by",verb,"ing him with a",noun,".")
                print("In the final reel,",actor,"appears to propose joining him in a",noun1,".")

            elif score==4:
                print("You got slot 4")
                input("Press enter to continue.")
                number=input("Enter a Number.")
                number1=input("Enter another Number.")
                number2=input("Enter another Number.")
                verb=input("Enter a Verb.")
                noun=input("Enter a Noun.")
                verb1=input("Enter a verb")
                lyrics=input("Enter a Lyrics to a Song.")
                noun1=input("Enter a Noun.")
                verb2=input("Enter a verb")
                lyrics1=input("Enter a Lyrics to a Song.")
                sound=input("Enter an American-Sounding First Name.")
                noun2=input("Enter a Noun.")
                adjective=input("Enter an Adjective.")
                print("CALLING CUSTOMER SERVICE SUPPORT")
                print("[Press",number,"] [Press",number1,"] [Press",number2,"] Hi, I'm",verb,"about the",noun,".")
                print("Sure, I'll",verb1,".",lyrics,". Hello, I'm calling about the",noun1,".")
                print("Yes, I can",verb,".",lyrics1,".")
                print("Sorry,",sound,", I didn't realize the music had stopped playing.")
                print("No, I haven't tried turning the",noun2,"off and turning it back on again.")
                print("I'll give it a try, but- well, that was",adjective,".")

            elif score==5:
                print("You got slot 5")
                input("Press enter to continue.")
                adjective=input("Enter a Adjective.")
                plural_noun=input("Enter a Plural Noun.")
                noun=input("Enter another Noun.")
                adjective1=input("Enter an Adjective.")
                body_part=input("Enter a Part of the Body.")
                adjective2=input("Enter an Adjective")
                plural_noun1=input("Enter a Plural Noun.")
                body_part1=input("Enter a Part of the Body.")
                adjective2=input("Enter an Adjective.")
                adverb=input("Enter an Adverb.")
                noun1=input("Enter an Noun.")
                print("THE POWER OF THE FORCE")
                print("The Force is a mystical,",adjective,"power. As Jedi Master Obi-Wan Kenobi once said,")
                print('"The Force is an energy field, created by all living',plural_noun,'that surrounds us,')
                print('penetrates us, and binds the',noun,'together." Using the power of the Force,')
                print("a Jedi can do many",adjective1,"things, like using the Force to Exercise",body_part)
                print("control over",adjective2,"-minded",plural_noun1,". A Jedi can also use the Force")
                print("to move objects with his or her",body_part1,". It doesn't matter how",adjective2,)
                print("these objects are; it only matters how",adverb,"the Jedi believes in the Force.")
                print("Most importantly, the Force teaches a Jedi to rely on his or her feelings.")
                print("As Obi-Wan Kenobi told his student, Luke",noun1,".")


            else:
                print("You got slot 6")
                input("Press enter to continue.")
                container=input("Enter a Type of Container.")
                adjective=input("Enter an Adjective.")
                adjective1=input("Enter another Adjective.")
                noun=input("Enter a Noun.")
                animal=input("Enter the name of an Animal.")
                vegetable=input("Enter a Vegetable.")
                vegetable1=input("Enter another Vegether.")
                color=input("Enter a Color.")
                adjective2=input("Enter an Adjective.")
                print("LUNCH ROOM")
                print("Make sure your lunc",container,"is filled with nutritious",adjective,"food.")
                print("Do not go the",adjective1,"food stand across the street from the school.")
                print("The hamburgers they serve are fried in",noun,"and are made of",animal,"meat.")
                print("So take a sandwich made of",vegetable,"or",vegetable1,"it's much healthier!")
                print("Drink",color,"milk instead of",adjective2,"colas.")

                
        print("Hey! This is 'MAD LIBS'")
        input("Press enter to play.")
        print("Lets see what slot u get....")
        time.sleep(2)
        joint_rolling()
        input('Press Enter to continue......')
      
    if number==4:
        os.system("cls")
        os.system("color F")
        print("The dice is showing:")
        print("[------------]")
        print("[   O   O    ]")
        print("[   O   O    ]")
        print("[            ]")
        print("[------------]")
        print('\n')
        time.sleep(1)
        computer_guess = randint(1,10)
        def check():
            #Get the value from txt_guess
            user_guess = int(txt_guess.get())

            #Determine higher, lower, or just right
            if user_guess < computer_guess:
                msg = "Lower!"
            elif user_guess > computer_guess:
                msg = "Higher!"
            elif user_guess == computer_guess:   
                msg = "Correct!"
            elif user_guess >10:
                msg = "Guess a number between 1-10"
            else:
                msg = "Something went wrong..."
                    
            #Show the result
            lbl_result["text"] = msg
            
            #Clear txt_guess
            txt_guess.delete(0, 5)

        def reset():
            #Declare the global variable
            global computer_guess
            #Get a random number
            computer_guess = randint(1,10)
            #Change the lbl_result text
            lbl_result["text"] = "Game reset. Guess again!"

        class quitButton(Button):
            def __init__(self, parent):
                Button.__init__(self, parent)
                self['text'] = 'GOOD BYE'
                # Command to close the window
                self['command'] = parent.destroy
                self['height'] = 4
                self['width'] = 25
                self['font'] = 'helvetica',15
                self['bg'] = "green"
                self['fg'] = "black"
                self.pack(side=BOTTOM)

        #Create root window
        root = Tk()

        #Change root window background color
        root.configure(bg="navy")

        #Change the title
        root.title("Guess the number!")

        #Change the window size
        root.geometry("1000x1000")

        #Create Widgets
        lbl_title = Label(root, text="Welcome to the Guessing Game!", bg="white", height = 4, width = 30, font = ('helvetica',45) ) 
        lbl_title.pack()

        lbl_result = Label(root, text="Good Luck! \n Guess a number between 1-10", bg="white" , height = 4, width = 25, font = ('helvetica',15)) 
        lbl_result.pack()

        btn_check = Button(root, text="Check", fg="green", bg="white", command=check, height = 4, width = 25, font = ('helvetica',15))
        btn_check.pack(side="left")

        btn_reset = Button(root, text="Reset", fg="red", bg="white", command=reset, height = 4, width = 25, font = ('helvetica',15))
        btn_reset.pack(side="right")

        txt_guess = Entry(root, width=40)
        txt_guess.pack()

        quitButton(root)
        #Start the main events loop
        root.mainloop()
        input("Press enter to continue......")
        
    if number==5:
        os.system("cls")
        os.system("color B")
        print("The dice is showing:")
        print("[------------]")
        print("[   O   O    ]")
        print("[     O      ]")
        print("[   O   O    ]")
        print("[------------]")
        print('\n')
        time.sleep(1)
        answer_A = ["A", "a"]
        answer_B = ["B", "b"]
        answer_C = ["C", "c"]
        yes = ["Y", "y", "yes"]
        no = ["N", "n", "no"]

        sword = 0
        flower = 0

        required = ("\nUse only A, B, or C\n") #Cutting down on duplication

        #This is a function, we use it to do lots of things and then call it by it's name later on
        #To create a function we use "def name():" where name can be anything.

        def clear_screen():  #Simple function that clears the screen
            os.system('cls' if os.name=='nt' else 'clear')
        def title():
             print ("   ░█▀▀█ ▒█▀▀▄ ▒█░░▒█ ▒█▀▀▀ ▒█▄░▒█ ▀▀█▀▀ ▒█░▒█ ▒█▀▀█ ▒█▀▀▀  ")
             print ("   ▒█▄▄█ ▒█░▒█ ░▒█▒█░ ▒█▀▀▀ ▒█▒█▒█ ░▒█░░ ▒█░▒█ ▒█▄▄▀ ▒█▀▀▀  ")
             print ("   ▒█░▒█ ▒█▄▄▀ ░░▀▄▀░ ▒█▄▄▄ ▒█░░▀█ ░▒█░░ ░▀▄▄▀ ▒█░▒█ ▒█▄▄▄ ")
             print ("\n")
             print ("                  ▒█▀▀█ ░█▀▀█ ▒█▀▄▀█ ▒█▀▀▀ ")
             print ("                  ▒█░▄▄ ▒█▄▄█ ▒█▒█▒█ ▒█▀▀▀ ")
             print ("                  ▒█▄▄█ ▒█░▒█ ▒█░░▒█ ▒█▄▄▄ ")

        def castle():
            print ("\n")
            print ("*                                 |>>>                    +        ")
            print ("+          *                      |                   *       +")
            print ("                    |>>>      _  _|_  _   *     |>>>		   ")
            print ("           *        |        |;| |;| |;|        |                 *")
            print ("     +          _  _|_  _    \\.    .  /    _  _|_  _       +")
            print (" *             |;|_|;|_|;|    \\: +   /    |;|_|;|_|;|")
            print ("               \\..      /    ||:+++. |    \\.    .  /           *")
            print ("      +         \\.  ,  /     ||:+++  |     \\:  .  /")
            print ("                 ||:+  |_   _ ||_ . _ | _   _||:+  |       *")
            print ("          *      ||+++.|||_|;|_|;|_|;|_|;|_|;||+++ |          +")
            print ("                 ||+++ ||.    .     .      . ||+++.|   *")
            print ("+   *            ||: . ||:.     . .   .  ,   ||:   |               *")
            print ("         *       ||:   ||:  ,     +       .  ||: , |      +")
            print ("  *              ||:   ||:.     +++++      . ||:   |         *")
            print ("     +           ||:   ||.     +++++++  .    ||: . |    +")
            print ("           +     ||: . ||: ,   +++++++ .  .  ||:   |             +")
            print ("                 ||: . ||: ,   +++++++ .  .  ||:   |        *")
            print ("                 ||: . ||: ,   +++++++ .  .  ||:   |")


        def north():
            print ("To go north press n then enter")

        def east():
            print ("To go east press e then enter")

        def south():
            print ("to go south press s then enter")

        def west():
            print ("To go west press w then enter")


        def setup():
            #global is used to create variables that can be used throughout our game
            global name
            global HP
            global MP
             
            #Our variable "name" is used to store our name, captured by keyboard input.
            name = input("What is your name player? ")
            print("welcome to adventure game")
            #randint is a great way of adding some variety to your players statistics.
            HP = randint(5,20)
            MP = randint(5,20)

        def villager():
            #This will create a randomly named Villager to interact with
            global npcname
            global response
            #Below is a list, we can store lots of things in a list and then retrieve them later.
            responses = ["Hi", "Are you a hero?", "Are you from this village?", "There has been a dark shadow cast across the village"]
            npcnamechoice = ["Roger", "Dexter", "Sarah", "Susan"]
            #Shuffle will shuffle the list contents into a random order.
            shuffle(npcnamechoice)
            npcname = npcnamechoice[0]
            print ("\n["+npcname+":] Hello, my name is "+npcname+", Would you like to talk to me?\n")
            shuffle(responses)
            print ("Press y to talk to the villager")
            time.sleep(1)
            if input() == "y":
                print ("["+npcname+":] " +responses[0])
            else:
                print("["+npcname+":] Goodbye")

        def enemy():
            global enemyHP
            global enemyMP
            global enemyname
            enemyHP = randint(5,20)
            enemyMP = randint(5,20)
            #Below is the enemy's name, perhaps you could change this to a list and then shuffle the list, such as we did for the villager above.
            enemyname = "monster"
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print ("                 SUDDENLY...                    ")
            print ("   YOU HEAR A ROAR, AND FROM THE SHADOW YOU     ")
            print ("  SEE AN "+enemyname+" COMING STRAIGHT AT YOU   ")
            time.sleep(3)
            print (" ")
            print("                                              ,--,  ,.-.")
            print("                ,                   \,       '-,-`,'-.' | ._")
            print("               /|           \    ,   |\         }  )/  / `-,',")
            print("               [ '          |\  /|   | |        /  \|  |/`  ,`")
            print("               | |       ,.`  `,` `, | |  _,...(   (      _',")
            print("               \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\ ")
            print("                    _\,``,   ` , ,  /  |         )         _,/ ")
            print("                 \  '  `  ,_ _`_,-,<._.<        /         /")
            print("                  ', `>.,`  `  `   ,., |_      |         /")
            print("                    \/`  `,   `   ,`  | /__,.-`    _,   `\ ")
            print("                -,-..\  _  \  `  /  ,  / `._) _,-\`       \ ")
            print("                 \_,,.) /\    ` /  / ) (-,, ``    ,        |")
            print("                ,` )  | \_\       '-`  |  `(               \ ")
            print("               /  /```(   , --, ,' \   |`<`    ,            |")
            print("              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)")
            print("        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`")
            print("       (-, \           ) \ ('_.-._)/ /,`    /")
            print("       | /  `          `/ \\ V   V, /`     /")
            print("    ,--\(        ,     <_/`\\     ||      /")
            print("   (   ,``-     \/|         \-A.A-`|     /")
            print("  ,>,_ )_,..(    )\          -,,_-`  _--`")
            print(" (_ \|`   _,/_  /  \_            ,--`")
            print("  \( `   <.,../`     `-.._   _,-`")
            print("   `                      ```")

            
            print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

            #print enemyname
            print ("Your enemy has " + " " + str(enemyHP) + " " + "Health Points")
            print ("Your enemy has " + " " + str(enemyMP) + " " + "Magic Points")
            print ("""  A. Grab a nearby rock and throw it at the monster
                        B. Lie down and wait to be mauled
                        C. Run""")
            choice = input(">>> ") #Here is your first choice.
            if choice in answer_A:
              option_rock()
            elif choice in answer_B:
              print ("\nWelp, that was quick. ")
              time.sleep(1)
              print ("                  _______$___________$_______")
              print ("                  _____$$_____________$$_____")
              print ("                  ____$____$$$___$$$____$____")
              print ("                  ________$$$$$_$$$$$________")
              print ("                  ________$$$$$_$$$$$________")
              print ("                  ________$$$$$_$$$$$________")
              print ("                  _________$$$___$$$_________")
              print ("                  ___$__________________$____")
              print ("                  ____$________________$_____")
              print ("                  _____$$$$$$$$$$$$$$$$______")
              print ("                  ___________$$$$$$$_________")
              print ("                  ____________$$$$$$$________")
              print ("                  _____________$$$$$$________")
              print ("                  ______________$$$$_________")
              time.sleep(1)
              print ("             YOU DIED!             ")
            elif choice in answer_C:
              option_run()
            else:
              print (required)
          
        def option_rock():
          print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          print ("  The monster is stunned, but regains control.  ")
          print ("             He begins                          ")
          print ("  running towards you again. Will you:          ")
          print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          time.sleep(1)
          print ("""  A. Run
          B. Throw another rock
          C. Run towards a nearby cave""")
          choice = input(">>> ")
          if choice in answer_A:
            option_run()
          elif choice in answer_B:
           print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
           print ("      You decided to throw another rock,        ")
           print ("                 as if the first                ") 
           print ("      rock thrown did much damage.              ")
           print ("          The rock flew well over the ,         ")
           print ("         monster head. You missed.     ")
           time.sleep(1)
           print ("                  _______$___________$_______")
           print ("                  _____$$_____________$$_____")
           print ("                  ____$____$$$___$$$____$____")
           print ("                  ________$$$$$_$$$$$________")
           print ("                  ________$$$$$_$$$$$________")
           print ("                  ________$$$$$_$$$$$________")
           print ("                  _________$$$___$$$_________")
           print ("                  ___$__________________$____")
           print ("                  ____$________________$_____")
           print ("                  _____$$$$$$$$$$$$$$$$______")
           print ("                  ___________$$$$$$$_________")
           print ("                  ____________$$$$$$$________")
           print ("                  _____________$$$$$$________")
           print ("                  ______________$$$$_________")
           print ("             YOU DIED!             ")
           print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          elif choice in answer_C:
            option_cave()
          else:
            print (required)
            option_rock()

        def option_cave():
          print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")  
          print ("\nYou were hesitant, since the cave was dark and ")
          print  (      "ominous. Before you fully enter,"          )
          print  (     "you notice a shiny sword on "               )
          print(      "the ground. Do you pick up a sword. Y/N?"    )
          print  ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          choice = input(">>> ")
          if choice in yes:
            sword = 1 #adds a sword
          else:
            sword = 0
          print ("\nWhat do you do next?")
          time.sleep(1)
          print ("""  A. Hide in silence
          B. Fight
          C. Run""")
          choice = input(">>> ")
          if choice in answer_A:
            print  ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print (  "\nReally? You're going to hide in the dark? I think  ")
            print ( "moster can see very well in the dark, right? Not sure,")
            print (       "but,I'm going with YES, so...\n     ")
            print ("                  _______$___________$_______")
            print ("                  _____$$_____________$$_____")
            print ("                  ____$____$$$___$$$____$____")
            print ("                  ________$$$$$_$$$$$________")
            print ("                  ________$$$$$_$$$$$________")
            print ("                  ________$$$$$_$$$$$________")
            print ("                  _________$$$___$$$_________")
            print ("                  ___$__________________$____")
            print ("                  ____$________________$_____")
            print ("                  _____$$$$$$$$$$$$$$$$______")
            print ("                  ___________$$$$$$$_________")
            print ("                  ____________$$$$$$$________")
            print ("                  _____________$$$$$$________")
            print ("                  ______________$$$$_________")
            print("                 \nYOU DIED! ")
            print ( "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          elif choice in answer_B:
           if sword > 0:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print ("\nYou laid in wait. The shimmering sword attracted ")
            print("the monster, which thought you were no match. As he walked ")
            print("closer and closer, your heart beat rapidly. As the orc ")
            print("reached out to grab the sword, you pierced the blade into ")
            print(                          "its chest"                      )
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            global name
            global HP
            global MP
            global move
            global enemyHP

            while HP > 0:
        #This loop will only work while our characters HP is greater than 0.
                  hit = randint(0,5)
                  print ("You swing your sword and cause " + str(hit) + " of damage")
                  enemyHP = enemyHP - hit
                  print (enemyHP)
                  enemyhit = randint(0,5)
                  print ("The moster swings a club at you and causes " + str(enemyhit) + " of damage")
                  HP = HP - enemyhit
                  print (HP)
                  print("you win")
           else: #If the user didn't grab the sword
             print ("\nYou should have picked up that sword. You're "
                    "defenseless. ")
             time.sleep(1)
             print ("")
             print("▒ █ ░ ░ ▒ █ 　▒ █ ▀ ▀ ▀ █ 　▒ █ ░ ▒ █ 　　 　▒ █ ▀ ▀ ▄ 　▀ █ ▀ 　▒ █ ▀ ▀ ▀ 　░ 　░ 　░ 　░ 　█ 　█ 　█ ")
             print("▒ █ ▄ ▄ ▄ █ 　▒ █ ░ ░ ▒ █ 　▒ █ ░ ▒ █ 　　 　▒ █ ░ ▒ █ 　▒ █ ░ 　▒ █ ▀ ▀ ▀ 　▄ 　▄ 　▄ 　▄ 　▀ 　▀ 　▀ ")
             print("░ ░ ▒ █ ░ ░ 　▒ █ ▄ ▄ ▄ █ 　░ ▀ ▄ ▄ ▀ 　　 　▒ █ ▄ ▄ ▀ 　▄ █ ▄ 　▒ █ ▄ ▄ ▄ 　█ 　█ 　█ 　█ 　▄ 　▄ 　▄ ")
          elif choice in answer_C:
            print ("As the monster enters the dark cave, you sliently "
                   "sneak out. You're several feet away, but the monster turns "
                   "around and sees you running.")
            option_run()
          else:
            print (required)
            option_cave()

        def option_run():
          print ("\nYou run as quickly as possible, but the moster's "
          "speed is too great. You will:")
          time.sleep(1)
          print ("""  A. Hide behind boulder
          B. Trapped, so you fight
          C. Run towards an abandoned town""")
          choice = input(">>> ")
          if choice in answer_A:
            print ("You're easily spotted. "
            "\n\nYou died!")
          elif choice in answer_B:
            print ("\nYou're no match for an moster. ")
            time.sleep(1)
            print ("")
            print("▒ █ ░ ░ ▒ █ 　▒ █ ▀ ▀ ▀ █ 　▒ █ ░ ▒ █ 　　 　▒ █ ▀ ▀ ▄ 　▀ █ ▀ 　▒ █ ▀ ▀ ▀ 　░ 　░ 　░ 　░ 　█ 　█ 　█ ")
            print("▒ █ ▄ ▄ ▄ █ 　▒ █ ░ ░ ▒ █ 　▒ █ ░ ▒ █ 　　 　▒ █ ░ ▒ █ 　▒ █ ░ 　▒ █ ▀ ▀ ▀ 　▄ 　▄ 　▄ 　▄ 　▀ 　▀ 　▀ ")
            print("░ ░ ▒ █ ░ ░ 　▒ █ ▄ ▄ ▄ █ 　░ ▀ ▄ ▄ ▀ 　　 　▒ █ ▄ ▄ ▀ 　▄ █ ▄ 　▒ █ ▄ ▄ ▄ 　█ 　█ 　█ 　█ 　▄ 　▄ 　▄ ")
          elif choice in answer_C:
            option_town()
          else:
            print (required)
            option_run()
        
        def option_town():
          print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          print("      \nWhile frantically running, you notice a rusted ")
          print("    sword lying in the mud. You quickly reach down and grab it, ")
          print("  but miss. You try to calm your heavy breathing as you hide ")
          print("   behind a delapitated building, waiting for the monster to come ")
          print("     charging around the corner. You notice a purple flower ")
          print("          near your foot. Do you pick it up? Y/N")
          print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          choice = input(">>> ")
          if choice in yes:
            flower = 1 #adds a flower
          else:
            flower = 0
          print ("You hear its heavy footsteps and ready yourself for "
          "the impending moster.")
          time.sleep(1)
          if flower > 0:
            print ("\nYou quickly hold out the purple flower, somehow "
            "hoping it will stop the orc. It does! The moster was looking "
            "for love. "
            "\n\nThis got weird,")
            print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
            print("█░░░░░░░░▀█▄▀▄▀██████░▀█▄▀▄▀██████   ")                                 
            print("░░░░ ░░░░░░░▀█▄█▄███▀░░░ ▀█▄█▄███")
            
            print("      but YOU SURVIVED!!!")
          else: #If the user didn't grab the sword
             print ("\nMaybe you should have picked up the flower. ")
             print ("")
             print("▒ █ ░ ░ ▒ █ 　▒ █ ▀ ▀ ▀ █ 　▒ █ ░ ▒ █ 　　 　▒ █ ▀ ▀ ▄ 　▀ █ ▀ 　▒ █ ▀ ▀ ▀ 　░ 　░ 　░ 　░ 　█ 　█ 　█ ")
             print("▒ █ ▄ ▄ ▄ █ 　▒ █ ░ ░ ▒ █ 　▒ █ ░ ▒ █ 　　 　▒ █ ░ ▒ █ 　▒ █ ░ 　▒ █ ▀ ▀ ▀ 　▄ 　▄ 　▄ 　▄ 　▀ 　▀ 　▀ ")
             print("░ ░ ▒ █ ░ ░ 　▒ █ ▄ ▄ ▄ █ 　░ ▀ ▄ ▄ ▀ 　　 　▒ █ ▄ ▄ ▀ 　▄ █ ▄ 　▒ █ ▄ ▄ ▄ 　█ 　█ 　█ 　█ 　▄ 　▄ 　▄ ")
         
        def intro():
          print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
          print ("     After a drunken night out with friends,    ")
          print ("               you awaken the                   ")
          print ("        next morning in a thick, dank forest.   ")             
          print ("               Head spinning and                ")
          print ("          fighting the urge to vomit,           ")  
          print ("         you stand and marvel at your new,      ")
          print ("               unfamiliar land......            ")
          print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        clear_screen()
        title()
        castle()
        setup()
        time.sleep(1)
        intro()

        #Below we are using the helper functions to join a string of text to an integer via the str() helper.
        print ("\nYour health is" + " " + str(HP))
        print ("Your magic skill is" + " " + str(MP))

        print ("Would you like to venture out into the land? Press y then enter to continue")
        if input() == "y":
            print ("In the distance to the north you can see a small village, to the east you can see a river and to the west a field of wild flowers.")
        print ("\n")
        north()
        east()
        west()
        move = input("Where would you like to go? ")
        if move == 'n':
            print ("\nYou move to the north, walking in the sunshine.")
            print ("A villager is in your path and greets you")
        #elif is short for Else If and it means that if the previous condition is false, to check this condition to see if that is true.
        elif move == 'e':
            print ("\nYou walk to the river which lies to the east of your home.")
            print ("A villager is in your path and greets you")
        elif move == 'w':
            print ("\nYou walk to the field of wild flowers, stopping to take in the beauty")
            print ("A villager is in your path and greets you\n")
        villager()
        enemy()
        input('Press Enter to continue.....')
        
    if number==6:
        os.system("cls")
        os.system("color A")
        print("The dice is showing:")
        print("[------------]")
        print("[   O   O    ]")
        print("[   O   O    ]")
        print("[   O   O    ]")
        print("[------------]")
        time.sleep(1)
        print("░█▀▀█ ░█▀▀▀█ ░█─── ░█─── 　 ─█▀▀█ ░█▀▀█ ─█▀▀█ ▀█▀ ░█▄─░█ ─ ─ ─ █ █ █ ")
        print("░█▄▄▀ ░█──░█ ░█─── ░█─── 　 ░█▄▄█ ░█─▄▄ ░█▄▄█ ░█─ ░█░█░█ ▄ ▄ ▄ ▀ ▀ ▀ ")
        print("░█─░█ ░█▄▄▄█ ░█▄▄█ ░█▄▄█ 　 ░█─░█ ░█▄▄█ ░█─░█ ▄█▄ ░█──▀█ █ █ █ ▄ ▄ ▄ ")
        input('Press Enter to continue.....')
print("\n")
print("\n")
print("▒█▀▀▀ ░█▀▀█ ▒█▄░▒█ ▀▀█▀▀ ░█▀▀█ ▒█▀▀▀█ ▀▀█▀▀ ▀█▀ ▒█▀▀█ 　 ▒█▀▀▀ ▀█▀ ▒█░░▒█ ▒█▀▀▀ ")
print("▒█▀▀▀ ▒█▄▄█ ▒█▒█▒█ ░▒█░░ ▒█▄▄█ ░▀▀▀▄▄ ░▒█░░ ▒█░ ▒█░░░ 　 ▒█▀▀▀ ▒█░ ░▒█▒█░ ▒█▀▀▀ ")
print("▒█░░░ ▒█░▒█ ▒█░░▀█ ░▒█░░ ▒█░▒█ ▒█▄▄▄█ ░▒█░░ ▄█▄ ▒█▄▄█ 　 ▒█░░░ ▄█▄ ░░▀▄▀░ ▒█▄▄▄ ")
print("\n")
print("\n")
print("This is a dice rolling program")
num=int(input("How many times you want to roll the dice?"))
time.sleep(1)
for num1 in range(1,num+1):
    print("ROLLING THE DICE.........")
    time.sleep(2)
    print(dice_rolling())
print("▒█░▒█ █▀▀█ █▀▀█ █▀▀ 　 █░░█ 　 █░░█ █▀▀█ █▀▀▄ 　 ▒█▀▀▀ █░░█ ▒█▄░▒█ ░ ░ █ █ █ ")
print("▒█▀▀█ █░░█ █░░█ █▀▀ 　 █░░█ 　 █▀▀█ █▄▄█ █░░█ 　 ▒█▀▀▀ █░░█ ▒█▒█▒█ ▄ ▄ ▀ ▀ ▀ ")
print("▒█░▒█ ▀▀▀▀ █▀▀▀ ▀▀▀ 　 ░▀▀▀ 　 ▀░░▀ ▀░░▀ ▀▀▀░ 　 ▒█░░░ ░▀▀▀ ▒█░░▀█ █ █ ▄ ▄ ▄ ")
print("\n")
input("Press enter to exit")    

