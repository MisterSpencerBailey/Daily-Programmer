# Source: https://www.reddit.com/r/dailyprogrammer/comments/4ybbcz/20160818_challenge_279_intermediate_text_reflow/


def reflowed(file):
    
    lines = open(file).read().split()

    line_length = 0
    reflowed = ''


    for word in lines:
        if len(word) + line_length <= 40:
            reflowed += word
            line_length += len(word)
            if line_length + len(word) + 1 <= 40:
                line_length += 1
                reflowed += ' '
        else:
            reflowed += '\n'+ word +' '
            line_length = len(word)+2
            
    return reflowed

print(reflowed('text reflow.txt'))
