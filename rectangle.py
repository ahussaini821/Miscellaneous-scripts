# Small function which takes a list of coordinates and returns the number of 
# rectangles that can be formed from those coordinates 

x = [(2,2),(2,10),(7,10),(7,2),(15,2),(15,10), (20,2), (20,10)]


def rectangle(coord):
     count=0
     
     # Where to record the final answer
     answer = 0
     coord2 = coord
     if len(coord) < 4:
          return 0
     ymatch = []
     for index,xy in enumerate(coord):
          
          # Check to see if any y matches are here and record their index
          for i in range(count,len(coord)):
               # To make sure we don't match a coordinate against itself
               if index == i:
                    continue
               # If the Ys match, this means we have a vertical line for
               # our rectangle, so these are recorded
               if xy[1] == coord[i][1]:
                    ymatch.append((index, i)) 
               
          
          count +=1
     count = 0
     #print ymatch
     # Now we want to see if these vertical lines have corresponding matching
     # X coordinates to create our rectangle
     for index,xy in enumerate(ymatch):
          
          for i in range(count, len(ymatch)):
               # AGain checking to see if we don't match against ourselves
               if index == i:
                    continue
               
               # Over here we're checking to see if there aren't matches for the
               # x coord of the current line against any of the Xs of another 
               # line. If there aren't, then that makes a rectangle impossible
               if coord[xy[0]][0] != coord[ymatch[i][0]][0] and coord[xy[0]][0] != coord[ymatch[i][1]][0]:
                    continue
                    
               elif coord[xy[1]][0] != coord[ymatch[i][0]][0] and coord[xy[1]][0] != coord[ymatch[i][1]][0]:
                    continue
               # If it passes both conditions, menas at least one X match for 
               # both points of the vertical line meaning rectangle is possible
               # thus we increment answer
               else:
                    answer+=1
          count += 1
          
          
     return answer
                    
          
          
          

          
print(rectangle(x))