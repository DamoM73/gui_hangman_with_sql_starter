import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QPixmap
from ui_hangman import Ui_MainWindow
from datastore import Datastore


class MainWindow:
    def __init__(self):
        """
        Initialise game window
        """
        # ----- setup UI elements ----- #
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        
        # ----- initialise game variables ----- #
        self.db = Datastore()
        self.word = ""
        self.guessed_word = []
        self.misses = 0
        
        # ----- initialise the UI with starting values ----- #
        self.choose_word()
        self.display_guesses()
        self.display_gallows()
        self.signals()
        

    def show(self):
        """
        Displays main window
        """
        self.main_win.show()


    def choose_word(self):
        """
        Gets word from datastore, and creates corresponding 
        list for guessed letters
        """
        self.word = self.db.get_word()
        self.guessed_word = ["_"] * len(self.word)
        print(self.word)


    def display_guesses(self):
        """
        Display the guessed letters to the UI
        """
        display_word = ""
        for character in self.guessed_word:
            display_word = display_word + character + " "
            
        self.ui.word_lb.setText(display_word)

    def display_gallows(self):
        """
        Displays the gallow progression to the UI
        """
        file_name = (f"./assets/{self.misses}.png")
        gallow = QPixmap(file_name)
        self.ui.gallow_lb.setPixmap(gallow)

    def set_button_enabled(self,val):
        """
        Changes the enabled status of the letter buttons to passed value
        val: bool
        """
        self.ui.a_btn.setEnabled(val)
        self.ui.b_btn.setEnabled(val)
        self.ui.c_btn.setEnabled(val)
        self.ui.d_btn.setEnabled(val)
        self.ui.e_btn.setEnabled(val)
        self.ui.f_btn.setEnabled(val)
        self.ui.g_btn.setEnabled(val)
        self.ui.h_btn.setEnabled(val)
        self.ui.i_btn.setEnabled(val)
        self.ui.j_btn.setEnabled(val)
        self.ui.k_btn.setEnabled(val)
        self.ui.l_btn.setEnabled(val)
        self.ui.m_btn.setEnabled(val)
        self.ui.n_btn.setEnabled(val)
        self.ui.o_btn.setEnabled(val)
        self.ui.p_btn.setEnabled(val)
        self.ui.q_btn.setEnabled(val)
        self.ui.r_btn.setEnabled(val)
        self.ui.s_btn.setEnabled(val)
        self.ui.t_btn.setEnabled(val)
        self.ui.u_btn.setEnabled(val)
        self.ui.v_btn.setEnabled(val)
        self.ui.w_btn.setEnabled(val)
        self.ui.x_btn.setEnabled(val)
        self.ui.y_btn.setEnabled(val)
        self.ui.z_btn.setEnabled(val)

    def signals(self):
        """
        Connects the UI buttons to the corresponding functions (see slots)
        """
        
        # control buttons
        self.ui.quit_btn.clicked.connect(QCoreApplication.instance().quit)
        self.ui.new_word_btn.clicked.connect(self.new_word_btn)

        # letter buttons
        self.ui.a_btn.clicked.connect(lambda: self.letter_btn(self.ui.a_btn))
        self.ui.b_btn.clicked.connect(lambda: self.letter_btn(self.ui.b_btn))
        self.ui.c_btn.clicked.connect(lambda: self.letter_btn(self.ui.c_btn))
        self.ui.d_btn.clicked.connect(lambda: self.letter_btn(self.ui.d_btn))
        self.ui.e_btn.clicked.connect(lambda: self.letter_btn(self.ui.e_btn))
        self.ui.f_btn.clicked.connect(lambda: self.letter_btn(self.ui.f_btn))
        self.ui.g_btn.clicked.connect(lambda: self.letter_btn(self.ui.g_btn))
        self.ui.h_btn.clicked.connect(lambda: self.letter_btn(self.ui.h_btn))
        self.ui.i_btn.clicked.connect(lambda: self.letter_btn(self.ui.i_btn))
        self.ui.j_btn.clicked.connect(lambda: self.letter_btn(self.ui.j_btn))
        self.ui.k_btn.clicked.connect(lambda: self.letter_btn(self.ui.k_btn))
        self.ui.l_btn.clicked.connect(lambda: self.letter_btn(self.ui.l_btn))
        self.ui.m_btn.clicked.connect(lambda: self.letter_btn(self.ui.m_btn))
        self.ui.n_btn.clicked.connect(lambda: self.letter_btn(self.ui.n_btn))
        self.ui.o_btn.clicked.connect(lambda: self.letter_btn(self.ui.o_btn))
        self.ui.p_btn.clicked.connect(lambda: self.letter_btn(self.ui.p_btn))
        self.ui.q_btn.clicked.connect(lambda: self.letter_btn(self.ui.q_btn))
        self.ui.r_btn.clicked.connect(lambda: self.letter_btn(self.ui.r_btn))
        self.ui.s_btn.clicked.connect(lambda: self.letter_btn(self.ui.s_btn))
        self.ui.t_btn.clicked.connect(lambda: self.letter_btn(self.ui.t_btn))
        self.ui.u_btn.clicked.connect(lambda: self.letter_btn(self.ui.u_btn))
        self.ui.v_btn.clicked.connect(lambda: self.letter_btn(self.ui.v_btn))
        self.ui.w_btn.clicked.connect(lambda: self.letter_btn(self.ui.w_btn))
        self.ui.x_btn.clicked.connect(lambda: self.letter_btn(self.ui.x_btn))
        self.ui.y_btn.clicked.connect(lambda: self.letter_btn(self.ui.y_btn))
        self.ui.z_btn.clicked.connect(lambda: self.letter_btn(self.ui.z_btn))
        
        
    # ----- slots ----- #
    def new_word_btn(self):
        """
        Chooses a new word and resets the UI
        """
        # get new word
        self.choose_word()
        self.display_guesses()
        # reset GUI
        self.misses = 0
        self.display_gallows()
        self.set_button_enabled(True)
        self.ui.result_lb.setText("")
        
    def letter_btn(self,button):
        """
        Disables the clicked button, checks if letter is in the word, 
        checks for state of the game. 
        """
        # get letter 
        guess = button.text().lower()
        
        # disable letter
        button.setEnabled(False)
        
        # check if letter is in word
        if guess in self.word:
            # add guess to guessed_word
            for index, letter in enumerate(self.word):
                if guess == letter:
                    self.guessed_word[index] = guess.upper()
            # disiplay guessed_word
            self.display_guesses()
            # check for win
            if "_" not in self.guessed_word:
                self.ui.result_lb.setText("Winner!")
        else:
            # add to the misses count, update GUI and check if game over
            self.misses += 1
            self.display_gallows()
            # check for loss
            if self.misses == 11:
                self.ui.result_lb.setText(f"The word was {self.word.upper()}")
                self.set_button_enabled(False)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())