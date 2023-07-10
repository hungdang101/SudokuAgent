import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QSizePolicy,QHeaderView
from PyQt5.QtCore import Qt
from GUI.menu_ui import Ui_Menu
from GUI.solver_ui import Ui_Solver
from GUI.play_ui import Ui_Play
import cv2
import numpy
from keras.models import load_model
import imutils
import random
from solver import *

class Menu(QDialog, Ui_Menu):
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        self.setupUi(self)
        self.play = Play(self)
        self.play_btn.clicked.connect(self.openPlay)
        self.solver = Solver(self)
        self.solve_btn.clicked.connect(self.openSolver)

    def openPlay(self):
        self.play.show()

    def openSolver(self):
        self.solver.show()

class Play(QDialog, Ui_Play):
    def __init__(self, parent=None):
        super(Play, self).__init__(parent)
        self.setupUi(self)
        self.squares = [[self.topleft, self.topmiddle, self.topright],
                        [self.middleleft, self.middlemiddle, self.middleright],
                        [self.bottomleft, self.bottommiddle, self.bottomright]]
        self.newClick()
        self.cancel_btn.clicked.connect(self.close)
        self.new_btn.clicked.connect(self.newClick)

    def newClick(self):
        # puzzle = self.genPuzzle()
        # for r, row in enumerate(self.squares):
        #     for c, square in enumerate(row):
        #         for i in range(3):
        #             for j in range(3):
        #                 val = puzzle[i + r * 3][j + c * 3]
        #                 if val != 0:
        #                     item = QTableWidgetItem(str(val))
        #                     item.setFlags(Qt.ItemIsSelectable or Qt.ItemIsEnabled)
        #                 else:
        #                     item = QTableWidgetItem("")
        #                 square.setItem(i, j, item)
        #                 square.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #                 square.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #         square.clearSelection()
        puzzle = [[0] * 9 for _ in range(9)]

        # Find sudoku image in the directory
        sudoku_img = cv2.imread('sudoku1.jpg')
        board, position = self.find_board(sudoku_img)
        # cv2.imshow("Board", board)
        gray_out = cv2.cvtColor(board, cv2.COLOR_BGR2GRAY)
        rois = self.split_board(gray_out)
        rois = numpy.array(rois).reshape(-1,48,48,1)
    
    # Input image and locate sudoku board on the image
    def find_board(self, sudoku_img):
        # Convert img to gray color
        gray_img = cv2.cvtColor(sudoku_img, cv2.COLOR_BGR2GRAY)

        #Remove noise from the image
        img_bfiler = cv2.bilateralFilter(gray_img, 13, 20, 20)

        # Detecting edge of picture
        # Canny Edge detection is an Algorithm consisting of 4 major steps:
        # Reduce Noise using Gaussian Smoothing.
        # Compute image gradient using Sobel filter.
        # Apply Non-Max Suppression or NMS to just jeep the local maxima
        # Apply Hysteresis thresholding which that 2 threshold values T_upper and T_lower 
        # which is used in the Canny() function.
        img_edge = cv2.Canny(img_bfiler,30, 180)

        # Decting all the continous point within the edges using findContours 
        contour_pts = cv2.findContours(img_edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        img_contours = imutils.grab_contours(contour_pts)
        new_img = cv2.drawContours(sudoku_img.copy(), img_contours, -1, (0,255,0), 3) # type: ignore

        img_contours = sorted(img_contours, key = cv2.contourArea, reverse=True)[:15]
        position = None

        # Finding rectangular
        for cont in img_contours:
            aprx = cv2.approxPolyDP(cont, 15, True)
            if (len(aprx) == 4):
                position = aprx
                break

        ressult = self.perspective_trans(sudoku_img, position)
        return ressult, position

    # Perspective transformation is bird_eyes view
    # Selected region from an image is projected into another plane   
    def perspective_trans(self,img, position, height=900, width=900):
        # Take img and location position of region
        # Return the only selected region with a perspective transformation
        point1 = numpy.float32([position[0], position[3], position[1], position[2]]) # type: ignore
        point2 = numpy.float32([[0,0], [width,0], [0, height], [width, height]]) # type: ignore

        # Apply perspective transformation algorithm
        matrix = cv2.getPerspectiveTransform(point1, point2)
        result = cv2.warpPerspective(img, matrix, (width, height))

        return result

    # Split the board into 81 individual image
    # Input: board image
    # Return: lists of 81 individual
    def split_board(self, board):
        rows = numpy.vsplit(board, 9)
        square_list = []
        for r in rows:
            columns = numpy.hsplit(r, 9)
            for c in columns:
                c = cv2.resize(c, (48, 48))/255.0
                cv2.imshow("Splitted block", c)
                cv2.waitKey(50)
                square_list.append(c)
        #cv2.destroyAllWindows()
        return square_list
    
    def genPuzzle(self):
        '''Generates a valid sudoku board with random num of hints btwn 17 and 27'''
        board = [[0] * 9 for _ in range(9)]
        clues = random.randint(17,27)
        for _ in range(clues):
            i = random.randint(0,8)
            j = random.randint(0,8)
            while board[i][j] != 0:
                i = random.randint(0,8)
                j = random.randint(0,8)
            num = random.randint(1,9)
            board[i][j] = num
        return board
    
class Solver(QDialog, Ui_Solver):
    def __init__(self, parent=None):
        super(Solver, self).__init__(parent)
        self.setupUi(self)
        self.solve_btn.clicked.connect(self.solveClick)
        self.reset_btn.clicked.connect(self.tableWidget.clear)
        self.cancel_btn.clicked.connect(self.close)

    def solveClick(self):
        # Add your solve logic here
        pass

def main():
    app = QApplication(sys.argv)
    form = Menu()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
