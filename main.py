import turtle

def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    while(n != 1):
        count += 1
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    return count                  # the last print is 1

def graphData(upper_limit=0):
  turtle_graph = turtle.Turtle()
  turtle_writer = turtle.Turtle()
  myscreen = turtle.Screen()

  myscreen.setworldcoordinates(0,0,10,10)
  
  max_so_far = 0
  start = 1
  for i in range(upper_limit):
    result = seq3np1(start)
    if result > max_so_far:
        max_so_far = result
        turtle_writer.clear()
    
    myscreen.setworldcoordinates(0,0,start+10, max_so_far+10)

    turtle_writer.up()
    turtle_writer.goto(0,max_so_far)
    turtle_writer.down()
    turtle_writer.write("Maximum so far:<{}>, <{}>".format(start, max_so_far))
    
    
    turtle_graph.goto(start, result)
    turtle_graph.dot(5,'blue')
    print(start, result)

    start += 1
  

  myscreen.exitonclick()
    
    
    


def main():
  upperbound = int(input("What is your upperbound for your range?:"))
  if upperbound <= 0:
    return
    
  #part A    
  # start = 1
  # for i in range(upperbound):
  #   number_of_iterations = seq3np1(start)
  #   print(start, number_of_iterations)
  #   start += 1
  # return number_of_iterations
  


  graphData(upperbound)
 
main()
