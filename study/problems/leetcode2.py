"""
You are given two non-empty linked lists representing two non-negative integers. 

The digits are stored in reverse order, and each of their nodes contains a single digit. 

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    def has_value(self, val):
        "method to compare the value with the node data"
        if self.val == val:
            return True
        else:
            return False
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return
    #add item 
    def add_list_item(self, item):
        "add an item at the end of the list"
        if not isinstance(item, ListNode):
            item = ListNode(item)
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item   
        return
    #return length
    def list_length(self):
        "returns the number of list items"
        count = 0
        current_node = self.head
        while current_node is not None:
            # increase counter by one
            count = count + 1
            
            # jump to the linked node
            current_node = current_node.next   
        return count
    #return outputs
    def output_list(self):
        "outputs the list (the value of the node, actually)"
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            # jump to the linked node
            current_node = current_node.next 
        return
    #search nodes 
    def unordered_search (self, value):
        "search the linked list for the node that has this value"
        # define current_node
        current_node = self.head
        # define position
        node_id = 1
        # define list of results
        results = []
        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)  
            # jump to the linked node
            current_node = current_node.next
            node_id = node_id + 1
        return results
    #remove nodes
    def remove_list_item_by_id(self, item_id):
        "remove the list item with the item id"
        current_id = 1
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_id == item_id:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    # we don't have to look any further
                    return
            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next
            current_id = current_id + 1
        return
class Solution:
    def __init__(self, l1, l2):
        self.l1 = l1 
        self.l2 = l2
    def addTwoNumbers(self):
        #first node
        added = ListNode(val = (self.l1.val + self.l2.val) % 10)
        carry_over = (self.l1.val + self.l2.val) // 10 #0 or 1 is added to next digit
        current_node = added
        #while nodes are injective
        while self.l1.next and self.l2.next:
            self.l1 = self.l1.next
            self.l2 = self.l2.next
            current_node.next = ListNode(val = (carry_over + self.l1.val + self.l2.val) % 10)
            #0 or 1 is added to next digit
            carry_over = (carry_over + self.l1.val + self.l2.val) // 10 
            current_node = current_node.next
        #only l1 nodes left
        while(self.l1.next):
            self.l1 = self.l1.next     
            current_node.next = ListNode(val = (carry_over + self.l1.val) % 10)
            carry_over = (carry_over + self.l1.val) // 10 #0 or 1 is added to next digit
            current_node = current_node.next
        #only l2 nodes left
        while(self.l2.next):
            self.l2 = self.l2.next
            current_node.next = ListNode(val = (carry_over + self.l2.val) % 10)
            carry_over = (carry_over + self.l2.val) // 10 #0 or 1 is added to next digit
            current_node = current_node.next
        #for the last digit
        if (carry_over) > 0: 
            current_node.next = ListNode(val = 1)
        return added.val, added.next.val, added.next.next.val #first node represents rest of them for a linked list
        
if __name__ == '__main__':
    a = [2,4,3]
    b = [5,6,4]
    c = []
    d = []
    for i in range(len(a)):
        c.append(ListNode(a[i]))
    for i in range(len(b)):
        d.append(ListNode(b[i]))
    list1 = SingleLinkedList()
    list2 = SingleLinkedList()
    for i in range(len(c)):
        list1.add_list_item(a[i])
    for i in range(len(d)):
        list2.add_list_item(b[i])
    case1 = Solution(list1.head, list2.head)
    print(case1.addTwoNumbers())