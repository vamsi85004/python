class ListNode:
    def _init_(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates(head):
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            # Skip the next node since it's a duplicate
            current.next = current.next.next
        else:
            # Move to the next node
            current = current.next
            
    return head
