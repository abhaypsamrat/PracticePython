class RailwayForm:
    formType = "Railwayform"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"train is {self.train}")

abhayApplication = RailwayForm()
abhayApplication.name = "Abhay"
abhayApplication.train = "Shiva Ganga"
abhayApplication.printData()