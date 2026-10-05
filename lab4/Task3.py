
class PriorityQueue:
    
    
    def __init__(self):
        
        self.queue = [] 
        
    def is_empty(self):
        
        return len(self.queue) == 0 
    
    def enqueue(self, item, priority):
      
        self.queue.append((priority, item)) 
        
        self.queue.sort(reverse=True) 
        print(f"Enqueued: '{item}' with priority {priority}") 
        
    def dequeue(self):
        
        if self.is_empty(): 
            print("Priority Queue is empty!") 
            return None 
        
        
        
        removed_element = self.queue.pop(0) 
        
        
        priority = removed_element[0] 
        item = removed_element[1] 
        
        print(f"Dequeued: '{item}' (Priority: {priority})") 
        return item 
    
    def display(self):
        
        print("Current Priority Queue (Priority, Item):", self.queue) 


if __name__ == "__main__":
    pq = PriorityQueue() 
    
    
    pq.enqueue("Do homework", 2)
    pq.enqueue("Watch TV", 1) 
    pq.enqueue("Put out fire", 5) 
    pq.enqueue("Eat dinner", 3)
    
    print("\n--- After Enqueuing ---")
    pq.display() 
    
    print("\n--- Dequeuing Items ---")
    
    pq.dequeue() 
    pq.dequeue() 
    
    print("\n--- Final State ---")
    pq.display() 