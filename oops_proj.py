class chatbook:

    # Static variable accessed using class name
    __user_id = 1

    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.username = ""
        self.password = ""
        self.loggedin = False

        # self.menu()

    def menu(self):
        user_input = input("Welcome to Chatbook!\n1.Press 1 to Sign Up\n2.Press 2 to Sign In\n3.Press 3 to write a post\n4.Press 4 to message a friend\n5.Press Any other key to Exit\n\n>")

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.message_friend()
        else:
            print("Thank you for visiting Chatbook. Goodbye!")
            exit()

    def signup(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        self.username = email
        self.password = password
        print("Sign Up Successful!\n\n")
        self.menu()

    def signin(self):
        if self.username == "" and self.password == "":
            print("No user found. Please sign up first.\n\n")
            self.menu()
        else:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if email == self.username and password == self.password:
                self.loggedin = True
                print("Sign In Successful!\n\n")
            else:
                print("Incorrect credentials. Please try again.\n\n")
            self.menu()

    def my_post(self):
        if self.loggedin:
            post_content = input("Write your post: ")
            print(f"Post Successful! -> {post_content}\n\n")
        else:
            print("Please sign in to write a post.\n\n")
        
        self.menu()

    def message_friend(self):
        if self.loggedin:
            friend_name = input("Enter your friend's name: ")
            message_content = input("Enter your message: ")
            print(f"Message sent to {friend_name}! -> {message_content}\n\n")
        else:
            print("Please sign in to message a friend.\n\n")
        
        self.menu()

    def get_name(self):
        return self.username
    def set_name(self, name):
        self.username = name

obj = chatbook()