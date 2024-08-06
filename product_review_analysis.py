'''
Task 1: Keyword Highlighter

Write a program that searches through reviews list and looks for keywords such as "good", 
"excellent", "bad", "poor", and "average". We want you to capitalize those keywords then 
print out each review. Print out each review with the keywords in uppercase so they stand out.

So for the first string in the reviews list, we want it to say: 
"This product is really GOOD. I'm impressed with its quality."

'''

def keyword_highlighter(reviews_list):
    # search through review list (iterate with for loop
    for review in reviews_list:
        reviews_list[reviews_list.index(review)] = reviews_list[reviews_list.index(review)].replace("good", "GOOD").replace("excellent", "EXCELLENT").replace("bad", "BAD").replace("poor", "POOR").replace("average", "AVERAGE")
    return reviews_list


provided_reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",        
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
    ]

# print(keyword_highlighter(provided_reviews))


'''
Task 2: Sentiment Tally

Develop a function that tallies the number of positive and negative words in each review.  
The function should return the total count of positive and negative words.

    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
'''
# create function that tallies and returns total count of positive and negative words in each reviews
def sentiment_tally(reviews_list):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    negative_tally = 0
    positive_tally = 0
    reviews_list = str(reviews_list)
    # go through the string and look for all occurances of positive words
    for word in positive_words:
        positive_tally += reviews_list.count(word)
    # go through the string and look for all occurances of negative words
    for word in negative_words:
        negative_tally += reviews_list.count(word)

    return f"POSITIVE TALLY: {positive_tally}\nNEGATIVE TALLY: {negative_tally}"

provided_reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",        
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
    ]

# print(sentiment_tally(provided_reviews))

'''    
Task 3: Review Summary

Implement a script that takes the first 30 characters of a review and appends "…" to create a 
summary. Ensure that the summary does not cut off in the middle of a word.

Example: "This product is really good. I'm...",
'''
review = input("POST REVIEW TO BE SUMMARIZED: ")
length = 30
first_30_rough = review[:length].strip()
if review[length - 1:].startswith(" "):
    print(first_30_rough + "...")
else:
    first_30_clean = first_30_rough.split()
    if len(first_30_clean) > 1:
        first_30_clean.pop()
print(" ".join(first_30_clean) + "...")

