import yake

def extract_keywords(sentence):
    # Create a YAKE object
    keyword_extractor = yake.KeywordExtractor()

    # Extract keywords
    keywords = keyword_extractor.extract_keywords(sentence)

    # Get the top-ranked keywords
    top_keywords = [keyword for keyword, _ in keywords]
    fin_list=[]
    for i in top_keywords:
        print(i,type(i))
        if " " not in i:
            fin_list.append(i)

    return fin_list
