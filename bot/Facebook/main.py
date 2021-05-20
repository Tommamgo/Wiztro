import facebook
import os
import sys
import io
from PIL import Image

def main():
    token = 'get_your_user_token_or_from_Graph_API_Explorer'
    graph = fb.GraphAPI(token)

    file = open('test.jpg', 'rb')

    graph.put_photo(file, "this is a test photo")





if __name__ == "__main__":
    main()