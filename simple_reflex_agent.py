import random


class Environment(object):
    def __init__(self):
        self.location = {'A': rand(), 'B': rand()}


class SimpleReflexAgent(Environment):

    def __init__(self, Environment):
        print("Environment Condition:" + str(Environment.location))

        cleaner_location = rand()

        if cleaner_location == 0:
            print("Cleaner is at A")
            if Environment.location['A'] == 1:
                print("Room A is dirty")
                Environment.location['A'] = 0

                print("Room A Has Been Cleaned")

                print("Moving Cleaner To Room B....")

                if Environment.location['B'] == 1:
                    print("Room B Is Dirty")
                    Environment.location['B'] = 0
                    print("Room B Has Been Cleaned")
            else:
                print("Moving Cleaner To Room B")

                if Environment.location['B'] == 1:
                    print("Room B Is Dirty")
                    Environment.location['B'] = 0
                    print("Room B Has Been Cleaned")

        elif cleaner_location == 1:

            print("Cleaner Has Benn Randomly Place At Room B")

            if Environment.location['B'] == 1:
                print("Room B Is Dirty")
                Environment.location['B'] = 0
                print("Room B Has Been Cleaned")

                print("Moving Cleaner To Room A")

                if Environment.location['A'] == 1:
                    print("Room A Is Dirty")
                    Environment.location['A'] = 0
                    print("Room A Has Been Cleaned")

        print("Final Location Status:" + str(Environment.location))


def rand():
    return random.randint(0, 1)


env = Environment()
cleaner = SimpleReflexAgent(env)
