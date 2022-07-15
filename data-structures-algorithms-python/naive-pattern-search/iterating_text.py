
def pattern_search(text, pattern):
    print("\nInput Text:", text, "\nInput Pattern:", pattern)
    print(text)
    print(pattern)
    for i in range(len(text)):
        print("Text Index: {}".format(i))
        for j in range(len(pattern)):
            print(" Pattern Index: {}".format(j))
            if pattern[char] == text[index + char]:
                match_count += 1
            else:
                break
        if match_count == len(pattern):
            print(pattern, "found at index", index, "\n")


text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"
# Invoke pattern_search
pattern_search(text, pattern)

text2 = "SOMEMORERANDOMWORDSTOpatternSEARCHTHROUGH"
pattern2 = "pattern"
pattern_search(text2, pattern2)

text3 = "This   still      works with    spaces"
pattern3 = "works"
pattern_search(text3, pattern3)

text4 = "722615457824612704202682179992552072047396"
pattern4 = "42"
pattern_search(text4, pattern4)
