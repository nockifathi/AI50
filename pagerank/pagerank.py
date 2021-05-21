import os
import random
import re
import sys
from numpy.random import choice

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    transition = dict()

    # check if page has link
    if corpus[page]:
        for link in corpus:
            # set the base prob for every page to (1-d)/numLinks
            transition[link] = (1 - damping_factor) / len(corpus)
            # update the prob value for every linked page
            if link in corpus[page]:
                transition[link] += damping_factor / len(corpus[page])

    # in case page has no link, every page has equal prob which is 1/numLinks
    else:
        for link in corpus:
            transition[link] = 1 / len(corpus)

    return transition


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # create a list of every page
    page_list = list(corpus.keys())

    # define a page rank dict and set initial prob to zero
    page_rank = dict()
    for page in page_list:
        page_rank[page] = 0

    # randomly select the first page and update the clicked page counter
    first_page = random.choice(page_list)
    page_rank[first_page] += 1

    # iterate through n samples, first sample has been made, so iterate until n-1
    for i in range(n-1):
        # get the transition model of the current page
        transition = transition_model(corpus, first_page, damping_factor)
        # get the probability distribution to randomly get the next page
        prob_distribution = list(transition.values())
        next_page = choice(page_list, 1, p=prob_distribution)[0]
        # print(next_page)
        # update the clicked page counter for the next page
        page_rank[next_page] += 1
        # update the next page as the first page for the next iteration
        first_page = next_page

    # update the page rank, divide by the number of samples to get the prob value
    for page in page_rank:
        page_rank[page] /= n

    return page_rank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # define a list of all pages
    page_list = list(corpus.keys())

    # create dicts of page count and page prob rank and set initial value to zero
    page_count = dict()
    page_rank = dict()
    for page in page_list:
        page_count[page] = 0
        page_rank[page] = 0

    # randomly select first page and update the counter and clicked page count dict
    first_page = random.choice(page_list)
    page_count[first_page] += 1
    counter = 1

    # repeat until result difference is less than 0.001
    while True:
        # update the counter
        counter += 1
        # get the transition model and probability distribution of the current page to the next page
        transition = transition_model(corpus, first_page, damping_factor)
        prob_distribution = list(transition.values())
        # randomly select the next page given the probability distribution
        next_page = choice(page_list, 1, p=prob_distribution)[0]
        # capture the list of the page rank for the previous iteration
        first_page_rank_list = list(page_rank.values())
        # update the click count for the next page clicked
        page_count[next_page] += 1
        # get the page rank prob value by dividing the click count by sample counter
        for page in page_count:
            page_rank[page] = page_count[page] / counter

        # print(f"page rank: {page_count}")
        # capture the list of the page rank for the next iteration
        next_page_rank_list = list(page_rank.values())
        diffs = [abs(n1 - n2) for n1, n2 in zip(first_page_rank_list, next_page_rank_list)]
        # print(page_rank)
        # make sure no page has zero probability
        if all(pr != 0 for pr in next_page_rank_list):
            # check if all page rank has less than 0.001 difference with the previous iteration
            if all(diff <= 0.001 for diff in diffs):
                # print(counter)
                return page_rank
        # update the next page as the new first page
        first_page = next_page


if __name__ == "__main__":
    main()
