def switchPage(tkapp, page_name):
    tkapp.algorithm24Page.pack_forget()
    tkapp.algorithmExpressionPage.pack_forget()
    tkapp.fractionExpressionPage.pack_forget()
    tkapp.josephRingPage.pack_forget()
    tkapp.palindConfirmationPage.pack_forget()
    tkapp.aboutPage.pack_forget()
    tkapp.homePage.pack_forget()

    if page_name == "HomePage":
        tkapp.homePage.pack()
    elif page_name == "AboutPage":
        tkapp.aboutPage.pack()
    elif page_name == "Algorithm24Page":
        tkapp.algorithm24Page.pack()
    elif page_name == "AlgorithmExpPage":
        tkapp.algorithmExpressionPage.pack()
    elif page_name == "FractionExpPage":
        tkapp.fractionExpressionPage.pack()
    elif page_name == "JosephRingPage":
        tkapp.josephRingPage.pack()
    elif page_name == "PalConPage":
        tkapp.palindConfirmationPage.pack()
    else:
        print("页面名称不合法! 程序退出.")
        tkapp.root.destroy()
