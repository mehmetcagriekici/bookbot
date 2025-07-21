def sort_on(items):
    return items["num"]

def get_number_of_words(text):
    return len(text.split())


def get_char_count(text):
    #dict to store counts
    count_memo = {}

    #convert text to lowercase
    text = text.lower()

    #loop over the text
    for i in range(0, len(text)):
        #check if char exist
        if text[i] in count_memo:
            count_memo[text[i]]["num"] += 1
        else:
            if text[i] != " ":
                count_memo[text[i]] = {"chr": text[i], "num": 1}

    chr_list = list(count_memo.values())

    chr_list.sort(reverse=True, key=sort_on)

    count_str = ""
    for i in range(0, len(chr_list)):
        count_str += f"{chr_list[i]["chr"]}: {chr_list[i]["num"]}"
        if i < len(chr_list) - 1:
            count_str += "\n"
        

    return count_str
        
    
    
    
