# AUTOGENERATED! DO NOT EDIT! File to edit: 03_submissionshandler.ipynb (unless otherwise specified).

__all__ = ['SubmissionsHandler']

# Cell
import praw
import pickle
from collections import Counter
from pprint import pprint
from .firsttry import PrawClient

# Cell
class SubmissionsHandler():
    def __init__(self, path, remove_irrelevant=True):
        self.path = path
        self.submissions = []

        self._unpickle(path, remove_irrelevant)

    def unlabeled_data(self):
        unlabeled = []
        for submission in self.submissions:
            pass

    def common_domains(self):
        '''
            Show the number of posts that link to each domain
        '''
        pprint(Counter([post['domain'] for post in self.submissions]).most_common())

    def make_sqllite_database(self):
        pass

    def _unpickle(self, path, remove_irrelevant):
        self.submissions = []
        with open(path, "rb") as file:
            while 1:
                try:
                    self.submissions += pickle.load(file)
                except EOFError:
                    break

        print(f'Unpickled {len(self.submissions)} objects.')

        if remove_irrelevant:
            self._select_mostly_useful()

    def _select_mostly_useful(self):
        '''
        Remove mostly invalid posts, stuff like:
        few comments (so no label),
        no selftext are often not useful
        post was deleted or removed

        It's not a complete solution, as the pushshift data
        doesn't get updated when the post changes, so there
        are many posts which were deleted after fact.
        '''
        mostly_useful = []
        for post in self.submissions:
            if (post['num_comments'] >= 2 and
                    'selftext' in post and
                    post['selftext'] != '[deleted]' and
                    post['selftext'] != '[removed]' and
                    post.get('removed_by_category') == None and
                    post.get('link_flair_text') != 'Meme' and
                    post.get('domain') == 'i.redd.it'):
                mostly_useful.append(post)

        self.submissions = mostly_useful

        print(f'{len(self.submissions)} are mostly useful.\n')

        # Show that no posts were deleted when pushshift downloaded them
        selftext = [post['selftext'] for post in self.submissions]
        print('This should show no [deleted] or [removed] entries:')
        print(Counter(selftext).most_common())