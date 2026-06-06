class AuctionSystem(object):

#     def __init__(self):
        

#     def addBid(self, userId, itemId, bidAmount):
#         """
#         :type userId: int
#         :type itemId: int
#         :type bidAmount: int
#         :rtype: None
#         """
        

#     def updateBid(self, userId, itemId, newAmount):
#         """
#         :type userId: int
#         :type itemId: int
#         :type newAmount: int
#         :rtype: None
#         """
        

#     def removeBid(self, userId, itemId):
#         """
#         :type userId: int
#         :type itemId: int
#         :rtype: None
#         """
        

#     def getHighestBidder(self, itemId):
#         """
#         :type itemId: int
#         :rtype: int
#         """
        


# # Your AuctionSystem object will be instantiated and called as such:
# # obj = AuctionSystem()
# # obj.addBid(userId,itemId,bidAmount)
# # obj.updateBid(userId,itemId,newAmount)
# # obj.removeBid(userId,itemId)
# # param_4 = obj.getHighestBidder(itemId)
    def __init__(self):
        self.bids=defaultdict(dict)
        self.heaps=defaultdict(list)

    def addBid(self,userId,itemId,bidAmount):
        self.bids[itemId][userId]=bidAmount
        heapq.heappush(self.heaps[itemId],(-bidAmount,-userId))
        
    def updateBid(self,userId,itemId,newAmount):
        self.bids[itemId][userId]=newAmount
        heapq.heappush(self.heaps[itemId],(-newAmount,-userId))

    def removeBid(self,userId,itemId):
        del self.bids[itemId][userId]
        
    def getHighestBidder(self,itemId):
        if itemId not in self.bids or not self.bids[itemId]:
            return -1

        heap=self.heaps[itemId]
        bids=self.bids[itemId]

        while heap:
            bid,user=heap[0]
            bid=-bid
            user=-user
            if user in bids and bids[user]==bid:
                return user
            heapq.heappop(heap)
        return -1