#!/usr/bin/env python3


class SocialNetwork:

    def __init__(self):
        '''Constructor; initialize an empty social network
        '''
        self.users = {}

    def list_users(self):
        '''List all users in the network

        Returns:
            [str]: A list of usernames
        '''
        return list(self.users.keys())
        # result = []
        # for key in self.users:
        #    result.append(key)
        # return result

        pass # FIXME

    def add_user(self, user):

        '''Add a user to the network

        This user will have no friends initially.

        Arguments:
            user (str): The username of the new user

        Returns:
            None
        '''
        self.users[user] = []
        pass # FIXME

    def add_friend(self, user, friend):
        '''Adds a friend to a user

        Note that "friends" are one-directional - this is the equivalent of
        "following" someone.

        If either the user or the friend is not a user in the network, they
        should be added to the network.

        Arguments:
            user (str): The username of the follower
            friend (str): The username of the user being followed

        Returns:
            None
        '''
        if user not in self.users.keys():
            self.add_user(user)
        if friend not in self.users.keys():
            self.add_user(friend)
        self.users[user].append(friend)
        pass # FIXME

    def get_friends(self, user):

        '''Get the friends of a user

        Arguments:
            user (str): The username of the user whose friends to return

        Returns:
            [str]: The list of usernames of the user's friends

        '''
        return self.users[user]

    def suggest_friend(self, user):
        argument_user_list = list(self.users[user])
        # self.users.pop(user)
        # print(list(self.users.keys()))
        _A_ = len(self.users[user])
        # print(_A_)
        max_value = -1
        for friends in (list(self.users)):
            if friends == user:
                continue
            # print(self.users[friends])
            _B_ = len(list(self.users[friends]))
            intersction_A_B_ = len(set(argument_user_list) & set(list(self.users[friends])))
            # print(intersction_A_B_)
            Jacaard_index = ( abs(intersction_A_B_) / ( abs(_A_) + abs(_B_) - abs(intersction_A_B_)) )
            print(Jacaard_index)
            if Jacaard_index > max_value:
                max_value = Jacaard_index
                most_similar_user = friends
        # Double check the Jacaard Index, and see the intersection list etc.
        print(list(set(argument_user_list) & set(self.users[friends])))
        print(most_similar_user)
        print(max_value)
        most_similar_user_list = self.users[most_similar_user]
        for potential_friend in most_similar_user_list:
            if potential_friend == user:
                self.users[most_similar_user].remove(user)
        print(most_similar_user_list)
        # print(set(argument_user_list) ^ set(list(self.users[most_similar_user])))
        new_non_friends_list = set(argument_user_list) ^ set(list(self.users[most_similar_user]))
        #print(new_non_friends_list)
        most_followers = -1
        for not_yet_friend in new_non_friends_list:
            most_followers_list = self.users[not_yet_friend]
            if len(most_followers_list) > most_followers:
                most_followers = len(most_followers_list)
                recommended_friend = not_yet_friend
        return recommended_friend

        # print(max_value)
        # print(most_similar_user)


            # print(len(self.users[friends]))
        '''Suggest a friend to the user

        See project specifications for details on this algorithm.

        Arguments:
            user (str): The username of the user to find a friend for

        Returns:
            str: The username of a new candidate friend for the user
        '''
        # return list(self.users[user])
        pass # FIXME

    def to_dot(self):
        result = []
        result.append('digraph {')
        result.append('    layout=neato')
        result.append('    overlap=scalexy')
        for user in self.list_users():
            for friend in self.get_friends(user):
                result.append('    "{}" -> "{}"'.format(user, friend))
        result.append('}')
        return '\n'.join(result)


def create_network_from_file(filename):
    '''Create a SocialNetwork from a saved file

    Arguments:
        filename (str): The name of the network file

    Returns:
        SocialNetwork: The SocialNetwork described by the file
    '''
    network = SocialNetwork()
    with open(filename) as fd:
        for line in fd.readlines():
            line = line.strip()
            users = line.split()
            network.add_user(users[0])
            for friend in users[1:]:
                network.add_friend(users[0], friend)
    return network


def main():
    network = create_network_from_file('twitter.network')
    print(network.to_dot())
    print(network.suggest_friend('jasonpontius'))


if __name__ == '__main__':
    main()
