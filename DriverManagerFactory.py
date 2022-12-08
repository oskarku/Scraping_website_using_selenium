from ChromeDriverManager import ChromeDriverManagerLoc


class DriverManagerFactory():
    def __init__(self, info=""):
        self.info = "this is info "

    def getInfo(self):
        return self.info


    def getManager(self, typeManager):
        driveManager=None
        if ( typeManager == "CHROME" ):
            print("driver chrome")
            driveManager=ChromeDriverManagerLoc()
        return driveManager
    def printDupa(self):
        print("dupa")