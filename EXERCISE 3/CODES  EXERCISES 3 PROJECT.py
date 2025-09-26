# PROJECT 75 : STACK & QUEUE PRACTICE QUETIONS
 # === stack  quetion 1 ===
stack = []
print(" === stack operation ====")
stack.append("dial") 
stack.append("pin")
stack.append("confirm")
print("stack before undo:",stack)
stack.pop() # undo last
print("stack after undo",stack)
print("top element left",stack[-1]) # "PIN"
 
 # === stack question 2 ===
 # ur pushes ["exercisesA","exercisesB","exercisesC"] then pop two

stack = []
stack.append("ExercisesA")
stack.append("ExercisesB")
stack.append("ExercisesC")
print("\nstack before popping",stack)
stack.pop() # remove exercisesC
stack.pop() # remove exercisesB
print("stack after popping two:",stack)
print("top element left:",stack[-1])  # exercisesA
# === stack quetion3 ===
# reverse "QUEUESTACK" using stack
s = "QUEUESTACK"
stack = []
# push each character
for ch in s:
    stack.append(ch)
    # pop to reverse
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
        print("\nOrginal string:",s)
        print("reverseds string:",
              reversed_string)
        # === stack quetion 4 ===
        print("\nReflection: A stack (LIFO")
             
        (" reverses sequences because the last pushed item is the first popped out")

from collections import deque # FIX: import deque first
#  === queue quetion 1 ===
# nyabugogo: 9 buses, after 5 depart
queue = deque(["bus1","bus2","bus3","bus4","bus5","bus6","bus7","bus8","bus9"])
print("\nQueue before departure:",
      list(queue))
for i in range(5): # first 5 depart
      queue.popleft()
      print("bus now in front:", queue[0]) # bus6

# === Queue Quetion 2 ===
# Aitel: 6 clients
queue = deque(["client1","client2","client3","client4","client5","client6"])
print("\nQueue:",list(queue))
print("last client in queue:",
      queue[-1]) # client 6
# === Queue Quetion 3 ===
print("\nchalleng: for voting lines, a queue(FIFO) is correct, because people\
are served in order allival,")
# Queue Quetion 4 ===
print("Reflection: FIFO ensures fairness since the first preson to allive is the first tobe served.")
