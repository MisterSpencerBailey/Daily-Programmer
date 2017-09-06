#  Source: https://www.reddit.com/r/dailyprogrammer/comments/6y19v2/20170904_challenge_330_easy_surround_the_circles/


#  Circle = xPos, yPos, radius
coords =   [[1,1,2],
           [2,2,0.5],
           [-1,-3,2],
           [5,2,1]]

#  Starting X/Y coords to find the edges of the rectangle. 


#  Functions to find the outmost edges by taking the X or Y position and adding/subtracting the radius

def right_side(circles):
    
    edge = 0
    
    for circle in range(len(circles)):
        if circles[circle][0] + circles[circle][2] > edge:
            edge = circles[circle][0] + circles[circle][2]
    return edge

def left_side(circles):
    
    edge = 0
    
    for circle in range(len(circles)):
        if circles[circle][0] - circles[circle][2] < edge:
            edge = circles[circle][0] - circles[circle][2]
    return edge

def top_side(circles):
    
    edge = 0
    
    for circle in range(len(circles)):
        if circles[circle][1] + circles[circle][2] > edge:
            edge = circles[circle][1] + circles[circle][2]
    return edge

def bottom_side(circles):
    
    edge = 0
    
    for circle in range(len(circles)):
        if circles[circle][1] - circles[circle][2] < edge:
            edge = circles[circle][1] - circles[circle][2]
    return edge

def box(coords):
    
    top = top_side(coords)
    right = right_side(coords)
    bottom = bottom_side(coords)
    left = left_side(coords)
        
    corners = [[left, bottom], [right, top]]

    return corners
