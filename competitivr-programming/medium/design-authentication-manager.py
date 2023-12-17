from collections import defaultdict
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.generatedTokens = defaultdict(int)
        self.expire = timeToLive
        self.rv = set()
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.generatedTokens[tokenId] = self.expire + currentTime
        self.rv.add(tokenId)
    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.generatedTokens and self.generatedTokens[tokenId] > currentTime:
            self.generatedTokens[tokenId] = currentTime + self.expire
        else:
            self.rv.discard(tokenId)
    def countUnexpiredTokens(self, currentTime: int) -> int:
        ct = 0
        for x in self.rv:
            if self.generatedTokens[x] > currentTime:
                ct += 1
        return ct

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)