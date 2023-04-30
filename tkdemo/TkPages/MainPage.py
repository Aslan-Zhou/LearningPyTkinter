from TkPages.HomePageFrame import *
from TkPages.AboutPageFrame import *
from TkPages.SwitchPages import *
from TkPages.Algorithm24PageFrame import *
from TkPages.AlgorithmExpressionPageFrame import *
from TkPages.FractionExpressionPageFrame import *
from TkPages.JosephRingPageFrame import *
from TkPages.PalindromeConfirmationPageFrame import *


class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.title("我的Tk练习册")
        self.root.geometry("680x480+600+480")
        self.createMenu()
        self.createAllPages()
        self.showHomePage()

    def createMenu(self):
        self.menubar = Menu(self.root)
        self.createStartMenu()
        self.createAlgorithmMenu()
        self.createHelpMenu()
        self.root.config(menu=self.menubar)

    def createStartMenu(self):
        self.homePageMenu = Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="开始", menu=self.homePageMenu)
        self.homePageMenu.add_command(label="主页", command=lambda: switchPage(self, "HomePage"))
        self.homePageMenu.add_command(label="退出", command=self.root.destroy)

    def createAlgorithmMenu(self):
        self.algorithmMenu = Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="算法", menu=self.algorithmMenu)
        self.createExpressionMenu()
        self.createData_structureMenu()
        self.createGameMenu()
        self.algorithmMenu.add_cascade(label="小游戏", menu=self.gameMenu)
        self.algorithmMenu.add_cascade(label="计算器", menu=self.expressionMenu)
        self.algorithmMenu.add_cascade(label="数据结构", menu=self.data_structureMenu)

    def createGameMenu(self):
        self.gameMenu = Menu(self.algorithmMenu, tearoff=False)
        self.gameMenu.add_command(label="24点", command=lambda: switchPage(self, "Algorithm24Page"))

    def createExpressionMenu(self):
        self.expressionMenu = Menu(self.algorithmMenu, tearoff=False)
        self.expressionMenu.add_command(label="四则运算", command=lambda: switchPage(self, "AlgorithmExpPage"))
        self.expressionMenu.add_command(label="分数计算", command=lambda: switchPage(self, "FractionExpPage"))

    def createData_structureMenu(self):
        self.data_structureMenu = Menu(self.algorithmMenu, tearoff=False)
        self.data_structureMenu.add_command(label="约瑟夫环", command=lambda: switchPage(self, "JosephRingPage"))
        self.data_structureMenu.add_command(label="回文确认", command=lambda: switchPage(self, "PalConPage"))

    def createHelpMenu(self):
        self.helpMenu = Menu(self.menubar, tearoff=False)
        self.menubar.add_cascade(label="帮助", menu=self.helpMenu)
        self.helpMenu.add_command(label="关于", command=lambda: switchPage(self, "AboutPage"))

    def createAllPages(self):
        self.homePage = HomePageFrame(self.root)
        self.aboutPage = AboutPageFrame(self.root)
        self.algorithm24Page = Algorithm24PageFrame(self.root)
        self.algorithmExpressionPage = AlgorithmExpressionPageFrame(self.root)
        self.fractionExpressionPage = FractionExpressionPageFrame(self.root)
        self.josephRingPage = JosephRingPageFrame(self.root)
        self.palindConfirmationPage = PalindromeConfirmationPageFrame(self.root)

    def showHomePage(self):
        switchPage(self, "HomePage")
