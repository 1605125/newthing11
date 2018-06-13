class Profile:
    # def __init__(self, name, email, address):
    def setProfile(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def displayProfile(self):
        return "Name : {0} \nEmail : {1} \nAddress : {2} ".format(self.name, self.email, self.address)


class UserProfile(Profile):
    def __init__(self, name, email, address, pincode):
        # super(UserProfile, self).__init__(name, email, address)
        super(UserProfile, self).setProfile(name, email, address)
        self.pincode = pincode

    def setCity(self, city):
        self.city = city

    def getEmail(self):
        return self.email

    def displayProfile(self):
        return "Name : {0} \nEmail : {1} \nAddress : {2} \nCity : {3} \nPincode : {4}".format(self.name, self.email,
                                                                                              self.address,
                                                                                              self.city, self.pincode)

    # def __del__(self):
    #     super(UserProfile, self).__del__()


userProfile = UserProfile("Raj", "RAj@gmail.com", "btm", 8120002)  # object of base class
userProfile.setCity("Bangalore")
temp = userProfile.displayProfile()  # as we are declaring obj of child class this will call or give preference
# child class method
print(temp)
