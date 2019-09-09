import datetime
from random import Random

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import praw

reddit = praw.Reddit(client_id='XZEqL7TQgebI0g',
                     client_secret='4F1bJPYnomLkhciLD1Ao_9X9WkI',
                     user_agent='alexavila2000'
                     )

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

#Global Variables, comment types arrays
positive_comments = []
negative_comments = []
neutral_comments = []
oldest_comment_index = -1
oldest_positive_comment_index = -1
oldest_negative_comment_index = -1

def get_text_negative_proba(text):
    return sid.polarity_scores(text)['neg']


def get_text_neutral_proba(text):
    return sid.polarity_scores(text)['neu']


def get_text_positive_proba(text) -> str:
    return sid.polarity_scores(text)['pos']


def get_submission_comments(url):
    submission = reddit.submission(url=url)
    submission.comments.replace_more()

    return submission.comments


# Traversing the tree using pre order traversal
def process_comments(comments, index):
    # if the array of comments is less than the list then return
    if len(comments) <= index:
        return

    # assign a number for the probability of each comment
    curr_comment = comments[index].body
    pos = get_text_positive_proba(curr_comment)
    neg = get_text_negative_proba(curr_comment)
    neu = get_text_neutral_proba(curr_comment)

    # Add comment to list depending on its category
    global positive_comments
    global negative_comments
    global positive_comments

    if pos >= neg and pos >= neu:
        positive_comments.append(comments[index])
    elif neg >= neu and neg >= pos:
        negative_comments.append(comments[index])
    else:
        neutral_comments.append(comments[index])

    # Go to the next comment until there no more
    process_comments(comments, index + 1)

    # Go to the first reply of the comment
    process_comments(comments[index].replies, 0)


def get_oldest_comment_any():
    # Get global variables
    global oldest_comment_index
    global positive_comments
    global negative_comments
    global positive_comments

    # all comments contains all the comments on the post
    all_comments = []
    all_comments.extend(positive_comments)
    all_comments.extend(negative_comments)
    all_comments.extend(neutral_comments)

    #sort the comments by date: unix time
    all_comments = sort_comments_by_date(all_comments)

    # if there are no comments return nothing
    if all_comments is None or len(all_comments) is 0:
        return None

    #increment the index of the oldest comment until it gets to the end
    oldest_comment_index += 1
    if oldest_comment_index is len(all_comments):
        oldest_comment_index -= 1
    return all_comments[oldest_comment_index]

def get_oldest_positive_comment():
    # Get global variables
    global oldest_positive_comment_index
    global positive_comments

    # Sort comments
    positive_comments = sort_comments_by_date(positive_comments)

    # if there are no comments return nothing
    if positive_comments is None or len(positive_comments) is 0:
        return None

    # increment the index of the oldest comment until it gets to the end
    oldest_positive_comment_index += 1
    if oldest_positive_comment_index is len(positive_comments):
        oldest_positive_comment_index -= 1
    return positive_comments[oldest_positive_comment_index]


def get_oldest_negative_comment():
    # Get global variables
    global oldest_negative_comment_index
    global negative_comments

    # Sort comments
    negative_comments = sort_comments_by_date(negative_comments)

    # if there are no comments return nothing
    if negative_comments is None or len(negative_comments) is 0:
        return None

    # increment the index of the oldest comment until it gets to the end
    oldest_negative_comment_index += 1
    if oldest_negative_comment_index is len(negative_comments):
        oldest_negative_comment_index -= 1
    return negative_comments[oldest_negative_comment_index]


def sort_comments_by_date(comments):
    #Create dictionary key = date and value = commment
    date_comment_dictionary = {}

    #List for date of the comments
    date_list = []
    for i in range(0, len(comments)):
        date_comment_dictionary[comments[i].created] = comments[i]
        date_list.append(comments[i].created)

    #sort list of the dates and use it to sort the comments
    date_list.sort()
    comment_list = []
    for date in date_list:
        comment_list.append(date_comment_dictionary[date])

    #return new sorted comment list
    return comment_list


def main():
    comments = get_submission_comments(
        'https://www.reddit.com/r/learnprogramming/comments/5w50g5/eli5_what_is_recursion/')

    #Test Case: post with no comments
    comments2 = get_submission_comments('https://www.reddit.com/r/learnprogramming/comments/d1fbfy/google_summer_of_code_2019_turned_out_to_be_a/')


    #print(comments[0].body)
    #print(comments[0].replies[0].body)

    #neg = get_text_negative_proba(comments[0].replies[0].body)

    #print(neg)

    #separates pos neg and neu comments into the global variables'
    process_comments(comments, 0)

    print("Number of positive comments:", len(positive_comments))
    print("Number of negative comments:", len(negative_comments))
    print("Number of neutral comments:", len(neutral_comments))

    #Print oldest comments if they are not empty
    print("")
    print("Extra Credit:")
    oldest_comment = get_oldest_comment_any()
    if oldest_comment is not None:
        print("Oldest comment:", oldest_comment.body)

    oldest_positive_comment = get_oldest_positive_comment()
    if oldest_positive_comment is not None:
        print("Oldest positive comment:", oldest_positive_comment.body)

    oldest_negative_comment = get_oldest_negative_comment()
    if oldest_negative_comment is not None:
        print("Oldest negative comment:", oldest_negative_comment.body)

    oldest_comment = get_oldest_comment_any()
    if oldest_comment is not None:
        print("Second oldest comment:", oldest_comment.body)

main()

